import os
import json
import httpx
import urllib.parse
import uuid
import google.generativeai as genai
from datetime import datetime, timedelta
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Body, Request, Depends, status
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session as DBSession

# Import Database
from database import init_db, get_db, User, Session

# ==========================================
# 配置区
# ==========================================
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# WeCom Config
WECOM_CORP_ID = os.getenv("WECOM_CORP_ID")
WECOM_CORP_SECRET = os.getenv("WECOM_CORP_SECRET")
WECOM_AGENT_ID = os.getenv("WECOM_AGENT_ID")

SKILL_FILE = "academic_tutor_skill.md"
# 优先使用环境变量中的 KB_PATH，如果没有则使用默认的本地路径
KB_PATH = os.getenv("KB_PATH", r"C:\Users\lingyun\Documents\BaiduSyncdisk\xcxnotes\content")

# ==========================================
# 工具函数
# ==========================================

def list_notes():
    """List all markdown files in the knowledge base."""
    files = []
    if not os.path.exists(KB_PATH):
        return ["Error: Knowledge base directory not found."]
        
    for root, _, filenames in os.walk(KB_PATH):
        for filename in filenames:
            if filename.endswith(".md"):
                # Make relative path for cleaner output
                rel_path = os.path.relpath(os.path.join(root, filename), KB_PATH)
                files.append(rel_path)
    return files

def read_note(filename):
    """Read the content of a specific note file."""
    # Security check to prevent reading outside KB_PATH
    full_path = os.path.join(KB_PATH, filename)
    
    # Simple path normalization check
    try:
        full_path = os.path.abspath(full_path)
        base_path = os.path.abspath(KB_PATH)
        if not full_path.startswith(base_path):
             return "Error: Access denied. File is outside knowledge base."
    except Exception:
        return "Error: Invalid path."
    
    if not os.path.exists(full_path):
        return "Error: File not found."
        
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

def load_system_instruction():
    """读取 SKILL.md 作为 AI 的灵魂"""
    if not os.path.exists(SKILL_FILE):
        return "Error: System instruction file not found."
    with open(SKILL_FILE, "r", encoding="utf-8") as f:
        return f.read()

# ==========================================
# WeCom SSO Utilities
# ==========================================

async def get_wecom_access_token():
    """Get WeCom Access Token"""
    if not WECOM_CORP_ID or not WECOM_CORP_SECRET:
        raise HTTPException(status_code=500, detail="WeCom credentials not configured")
        
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={WECOM_CORP_ID}&corpsecret={WECOM_CORP_SECRET}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        if data.get("errcode") != 0:
            raise HTTPException(status_code=400, detail=f"Failed to get access token: {data.get('errmsg')}")
        return data.get("access_token")

async def get_wecom_user_info(code: str):
    """Get User Info from WeCom Code"""
    access_token = await get_wecom_access_token()
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token={access_token}&code={code}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        if data.get("errcode") != 0:
            raise HTTPException(status_code=400, detail=f"Failed to get user info: {data.get('errmsg')}")
        return data

# ==========================================
# FastAPI 应用
# ==========================================

app = FastAPI(
    title="Academic Tutor API", 
    description="API for Academic Tutor Chatbot with Local Knowledge Base",
    root_path=os.getenv("ROOT_PATH", "")
)

# ==========================================
# SSO Endpoints
# ==========================================

@app.get("/auth/wecom/login")
async def wecom_login(redirect_uri: str):
    """
    Generate WeCom OAuth URL
    User should be redirected to this URL to start login
    """
    if not WECOM_CORP_ID:
        raise HTTPException(status_code=500, detail="WeCom Corp ID not configured")
        
    # URL Encode the redirect URI
    encoded_redirect_uri = urllib.parse.quote(redirect_uri)
    
    # Construct OAuth URL
    # Scope: snsapi_base (silent) or snsapi_privateinfo (manual confirm)
    oauth_url = f"https://open.weixin.qq.com/connect/oauth2/authorize?appid={WECOM_CORP_ID}&redirect_uri={encoded_redirect_uri}&response_type=code&scope=snsapi_base&state=STATE#wechat_redirect"
    
    return {"url": oauth_url}

@app.get("/auth/wecom/callback")
async def wecom_callback(code: str, db: DBSession = Depends(get_db)):
    """
    Callback for WeCom OAuth
    Frontend sends the code here to exchange for user info
    """
    user_info = await get_wecom_user_info(code)
    wecom_user_id = user_info.get("UserId")
    
    if not wecom_user_id:
        raise HTTPException(status_code=400, detail="Invalid WeCom User Info")

    # 1. Update/Create User
    user = db.query(User).filter(User.id == wecom_user_id).first()
    if not user:
        user = User(
            id=wecom_user_id,
            name=wecom_user_id, # We don't have name from basic info, can fetch detail if needed
            created_at=datetime.utcnow(),
            last_login=datetime.utcnow()
        )
        db.add(user)
    else:
        user.last_login = datetime.utcnow()
    
    db.commit()
    db.refresh(user)
    
    # 2. Create Session
    session_token = str(uuid.uuid4())
    new_session = Session(
        token=session_token,
        user_id=wecom_user_id,
        created_at=datetime.utcnow(),
        expires_at=datetime.utcnow() + timedelta(days=7), # 7 days expiry
        is_active=True
    )
    db.add(new_session)
    db.commit()
    
    return {
        "status": "success",
        "user_id": wecom_user_id,
        "token": session_token,
        "device_id": user_info.get("DeviceId")
    }

@app.get("/users/me")
async def read_users_me(token: str = None, db: DBSession = Depends(get_db)):
    """Get current user info from session token"""
    if not token:
        raise HTTPException(status_code=401, detail="Token required")
        
    session = db.query(Session).filter(
        Session.token == token,
        Session.is_active == True,
        Session.expires_at > datetime.utcnow()
    ).first()
    
    if not session:
        raise HTTPException(status_code=401, detail="Invalid or expired session")
        
    user = db.query(User).filter(User.id == session.user_id).first()
    if not user:
         raise HTTPException(status_code=404, detail="User not found")
         
    return {
        "id": user.id,
        "name": user.name,
        "last_login": user.last_login,
        "session_expires_at": session.expires_at
    }

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000", 
        "http://127.0.0.1:3000",
        "http://localhost:8080",
        "http://127.0.0.1:8080",
        "https://tool.sysmex.com.cn"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 模型与会话管理
model = None
sessions: Dict[str, Any] = {}

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"
    temperature: Optional[float] = 0.7
    max_output_tokens: Optional[int] = 2000
    top_p: Optional[float] = 0.95
    top_k: Optional[int] = 40

class ChatResponse(BaseModel):
    response: str
    session_id: str

@app.on_event("startup")
async def startup_event():
    # Initialize Database
    init_db()
    
    global model
    system_instruction = load_system_instruction()
    tools = [list_notes, read_note]
    model = genai.GenerativeModel(
        model_name="models/gemini-3-flash-preview",
        system_instruction=system_instruction,
        tools=tools
    )
    print("🎓 Academic Tutor API initialized.")

@app.get("/")
async def root():
    return {"message": "Academic Tutor API is running. Visit /docs for Swagger UI."}

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    global model, sessions
    
    session_id = request.session_id
    user_input = request.message
    
    # 获取或创建会话
    if session_id not in sessions:
        # Enable automatic function calling
        sessions[session_id] = model.start_chat(history=[], enable_automatic_function_calling=True)
        print(f"Created new session: {session_id}")
    
    chat_session = sessions[session_id]
    
    try:
        # Configure generation parameters
        generation_config = genai.types.GenerationConfig(
            temperature=request.temperature,
            max_output_tokens=request.max_output_tokens,
            top_p=request.top_p,
            top_k=request.top_k
        )

        # stream=False for API simplicity
        response = chat_session.send_message(
            user_input, 
            stream=False,
            generation_config=generation_config
        )
        return ChatResponse(response=response.text, session_id=session_id)
    except Exception as e:
        # Handle potential empty response due to function calls only (though auto-calling should handle it)
        # or other errors
        print(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/reset/{session_id}")
async def reset_session(session_id: str):
    if session_id in sessions:
        del sessions[session_id]
        return {"message": f"Session {session_id} reset."}
    return {"message": f"Session {session_id} not found."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
