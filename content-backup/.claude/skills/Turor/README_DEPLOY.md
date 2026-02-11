# Academic Tutor Chatbot - 部署与开发文档

## 1. 项目简介
本项目是一个集成了 **Google Gemini AI** 的学术辅导机器人，支持企业微信 (WeCom) SSO 单点登录。
项目采用前后端分离架构，部署在同一台服务器上，通过 **Nginx** 进行反向代理和静态资源托管。

### 核心功能
*   **AI 对话**: 基于 Google Gemini 模型，支持上下文对话。
*   **知识库**: 能够读取本地 Markdown 文件作为知识库。
*   **企业微信登录**: 安全的 OAuth 2.0 身份验证。
*   **用户状态管理**: 使用 SQLite 本地数据库持久化用户登录状态和会话。
*   **动态配置**: 前端支持动态调整模型参数（温度、最大Token数）。

---

## 2. 系统架构

| 组件 | 技术栈 | 说明 |
| :--- | :--- | :--- |
| **前端** | HTML5, CSS3, JavaScript | 单页应用 (SPA)，集成 WeCom OAuth 流程。 |
| **后端** | Python FastAPI | 提供 RESTful API，处理业务逻辑和 AI 调用。 |
| **数据库** | SQLite + SQLAlchemy | 存储用户信息 (User) 和会话 Token (Session)。 |
| **Web 服务器** | Nginx | 反向代理 API 请求，托管前端静态文件。 |
| **AI 模型** | Google Gemini-3-flash | 提供智能对话能力。 |

### 交互流程
1.  用户访问 `https://tool.sysmex.com.cn/hr`。
2.  前端检测登录状态，未登录则跳转企业微信授权。
3.  获取 Code 后调用后端 `/auth/wecom/callback`。
4.  后端验证 Code，创建/更新 SQLite 用户记录，返回 Session Token。
5.  前端存储 Token，后续聊天请求携带 Token 访问 `/chat` 接口。

---

## 3. 环境依赖

### 3.1 服务器环境
*   **操作系统**: Windows Server 或 Linux (本文档以 Windows 为例)。
*   **Python**: 3.10 或更高版本。
*   **Nginx**: 最新稳定版。

### 3.2 外部服务凭证
需要配置以下环境变量：
*   `GEMINI_API_KEY`: Google AI Studio API Key。
*   `WECOM_CORP_ID`: 企业微信企业 ID。
*   `WECOM_AGENT_ID`: 企业微信应用 Agent ID。
*   `WECOM_CORP_SECRET`: 企业微信应用 Secret。

---

## 4. 部署步骤

### 步骤 1: 后端部署

1.  **准备代码**: 确保所有 Python 文件 (`tutor_api.py`, `database.py`) 和依赖文件 (`requirements.txt`) 在同一目录。
2.  **安装依赖**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **配置环境变量**:
    复制 `.env.example` 为 `.env`，并填入真实信息：
    ```ini
    GEMINI_API_KEY=your_gemini_key
    WECOM_CORP_ID=wx1c6695d7030171b2
    WECOM_AGENT_ID=1000029
    WECOM_CORP_SECRET=_odoy6JfFw6jFCvmLCo6ta51TWEr923iY8ruSNY9sG0
    KB_PATH=C:\path\to\your\knowledge_base
    ROOT_PATH=/hr/api  # 如果 Nginx 配置了路径重写，这里需要匹配
    ```
4.  **启动服务**:
    运行启动脚本或手动运行：
    ```bash
    python -m uvicorn tutor_api:app --host 127.0.0.1 --port 8000
    ```
    *服务启动后会自动初始化 SQLite 数据库 `tutor_app.db`。*

### 步骤 2: 前端部署

1.  **文件准备**: 确保 `h5_chatbot.html` 位于部署目录。
2.  **域名验证**: 如果企业微信需要域名验证文件 (如 `WW_verify_xxx.txt`)，请将其放入同一目录。

### 3. Nginx 配置

1.  **修改配置**: 编辑 `nginx_tutor.conf` (或添加到主 `nginx.conf`)。
    *   **关键修改**: 确保 `alias` 路径指向实际的文件所在目录。

    ```nginx
    server {
        listen 80;
        server_name tool.sysmex.com.cn;

        # 前端页面托管
        location /hr {
            alias C:/Users/lingyun/Documents/BaiduSyncdisk/xcxnotes/content/.claude/skills/Turor; # 修改为实际路径
            index h5_chatbot.html;
            try_files $uri $uri/ /h5_chatbot.html;
        }

        # API 反向代理
        location /hr/api/ {
            proxy_pass http://127.0.0.1:8000/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }
    ```
2.  **重载 Nginx**: `nginx -s reload`

---

## 5. 开发说明

### 项目结构
```
Turor/
├── tutor_api.py        # [核心] 后端 API 主程序 (FastAPI)
├── database.py         # [数据] SQLite 数据库模型 (SQLAlchemy)
├── h5_chatbot.html     # [前端] 单页应用 (HTML/JS)
├── nginx_tutor.conf    # [部署] Nginx 配置文件
├── requirements.txt    # [依赖] Python 依赖列表
├── start_server.bat    # [工具] Windows 启动脚本
├── .env                # [配置] 环境变量 (不提交到 Git)
└── academic_tutor_skill.md # [AI] 系统提示词 (System Instruction)
```

### 修改前端
*   **UI 调整**: 直接修改 `h5_chatbot.html` 中的 `<style>` 部分。
*   **逻辑调整**: 修改 `<script>` 标签内的 `login()`, `sendMessage()` 等函数。
*   **API 地址**: 默认配置为 `/hr/api/`，如需跨域调试请修改 `API_BASE_URL`。

### 修改后端
*   **添加 API**: 在 `tutor_api.py` 中使用 `@app.get` 或 `@app.post` 添加新路由。
*   **数据库变更**: 修改 `database.py` 中的模型类，注意 SQLite 不支持直接 `ALTER TABLE`，复杂变更建议删除 `tutor_app.db` 重建。
*   **AI 逻辑**: 修改 `chat_endpoint` 函数中的 `generation_config` 或 `tools`。

## 6. 验证与测试
1.  **健康检查**: 访问 `http://localhost:8000/` 应返回 API 运行消息。
2.  **Nginx 检查**: 访问 `http://tool.sysmex.com.cn/hr` 应看到前端页面。
3.  **SSO 测试**: 点击“企业微信登录”，应跳转授权并成功返回，显示用户 ID。
4.  **对话测试**: 发送“你好”，应收到 AI 回复。

