import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# ==========================================
# 配置区
# ==========================================
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

SKILL_FILE = "academic_tutor_skill.md"
HISTORY_FILE = "tutor_session_history.json"

# ==========================================
# 核心功能逻辑
# ==========================================

def load_system_instruction():
    """读取 SKILL.md 作为 AI 的灵魂"""
    if not os.path.exists(SKILL_FILE):
        print(f"❌ 错误：找不到 {SKILL_FILE} 文件！请确保它在同一目录下。")
        exit()
    with open(SKILL_FILE, "r", encoding="utf-8") as f:
        return f.read()

def save_history(history):
    """持久化保存对话历史"""
    serializable = []
    for content in history:
        serializable.append({
            "role": content.role,
            "parts": [{"text": part.text} for part in content.parts]
        })
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(serializable, f, ensure_ascii=False, indent=4)
    print(f"\n[系统] 进度已自动保存至 {HISTORY_FILE}")

def load_history():
    """加载历史进度"""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            print("📜 正在恢复之前的学习记录...")
            return json.load(f)
    return []

def main():
    # 初始化 AI 模型
    system_instruction = load_system_instruction()
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=system_instruction
    )
    
    # 恢复会话
    initial_history = load_history()
    chat_session = model.start_chat(history=initial_history)
    
    print("\n" + "="*40)
    print("🎓 ACADEMIC TUTOR (本地增强版) 已启动")
    print("输入 'exit' 退出并保存，输入 'clear' 清空进度")
    print("="*40 + "\n")

    try:
        while True:
            user_input = input("🙂 你: ")
            
            if user_input.lower() in ['exit', 'quit', '退出']:
                break
            if user_input.lower() == 'clear':
                if os.path.exists(HISTORY_FILE):
                    os.remove(HISTORY_FILE)
                print("♻️ 进度已清空，请重启程序。")
                break

            # 调用大模型 API
            try:
                response = chat_session.send_message(user_input, stream=True)
                print("\n👨‍🏫 老师: ", end="")
                for chunk in response:
                    print(chunk.text, end="", flush=True)
                print("\n\n" + "-"*30)
            except Exception as e:
                print(f"\n❌ API 调用失败: {e}")

    finally:
        save_history(chat_session.history)

if __name__ == "__main__":
    main()