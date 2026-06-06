---
source: raw/04_文档与参考/Markdown文档/Astrill VPN 配置 Antigravity_Gemini CLI_Claude Code 分离规则教程.md
raw_sha256: 27b271bd80d412f37ad630c8e9d017fa51e4b9539b7f4328040fd97afe06bdb6
compiled_at: 2026-04-14T03:50:19.048Z
---
# Astrill VPN 配置 Antigravity/Gemini CLI/Claude Code 分离规则教程

> [!NOTE] 来源路径
> `raw/04_文档与参考/Markdown文档/Astrill VPN 配置 Antigravity_Gemini CLI_Claude Code 分离规则教程.md`

---

## TL;DR
本教程提供了 Astrill VPN 分流配置方案，实现**仅 Antigravity、Gemini CLI、Claude Code 走美国VPN节点，其他应用（如豆包）保持本地直连，同时可与现有NotebookLM分流规则共存**，覆盖Windows和macOS系统配置步骤，包含DNS优化、验证排错与进阶优化内容。

---

## 合规提示
> [!IMPORTANT] 合规要求
> - 在中国内地使用VPN须仅限 **企业跨境办公等合法场景**，遵守《中华人民共和国网络安全法》及相关规定。
> - Google Antigravity、Gemini、Claude Code 目前仅限美国地区访问，需使用合规美国IP及对应DNS配置。

---

## 一、核心目标
仅让 **Antigravity、Gemini CLI、Claude Code** 走美国VPN节点（满足地域限制与API合规），同时保持豆包及其他本地应用直连网络，与此前配置的NotebookLM规则共存无冲突。

---

## 二、基础准备（必做）

### 2.1 Astrill 基础配置
1. 登录Astrill客户端，选择协议：优先 **OpenWeb**（浏览器+域名分流友好）或 **WireGuard**（速度与稳定性佳），避免使用StealthVPN（域名分流兼容性差）。
2. 选择服务器：筛选并连接 **美国低延迟节点**（优先非黑名单IP，降低Google风控概率）。
3. 确认连接成功（客户端显示Connected，IP为美国地域）。

### 2.2 工具进程与路径确认
以下为工具默认进程名与路径，用于后续添加分流规则（可根据实际安装位置调整）：

|工具名称|Windows进程名|macOS进程名|默认安装路径|
|---|---|---|---|
|Antigravity|`antigravity.exe`、`language_server_windows_x64.exe`|`antigravity`、`language_server_macos_arm/x64`|Windows：`C:\Users\<用户名>\AppData\Local\antigravity\`<br>macOS：`/Applications/Antigravity.app/Contents/MacOS/`|
|Gemini CLI|`gemini.exe`|`gemini`|Windows：`C:\Users\<用户名>\.gemini\`<br>macOS：`/usr/local/bin/gemini` 或 `~/bin/gemini`|
|Claude Code|`claude.exe`|`claude`|Windows：`C:\Users\<用户名>\AppData\Local\claude\`<br>macOS：`/usr/local/bin/claude` 或 `~/bin/claude`|

### 2.3 API与环境变量配置
确保工具可正常调用API，提前完成以下配置：
- Gemini CLI：配置 `~/.gemini/settings.json` 文件，设置 `GOOGLE_GEMINI_API_KEY` 环境变量。
- Claude Code：配置 `ANTHROPIC_API_KEY`；若与Antigravity集成，额外设置 `ANTHROPIC_BASE_URL=http://127.0.0.1:8045`（Antigravity默认代理端口）。
- Antigravity：完成Google账号OAuth登录，启动API代理（默认自动启动，端口8045）。

---

## 三、Windows系统配置步骤

### 3.1 分离规则核心设置（关键）
1. 打开Astrill客户端，进入**Settings（设置）→ Split Tunneling/Application & Website Filter（分流/应用与网站过滤器）**。
2. 启用功能（开关置为ON），选择 **Tunnel only selected apps/websites（仅隧道选定应用/网站）** 模式（核心逻辑：仅指定工具走VPN，其余直连）。
3. 添加进程级规则（精准匹配工具进程）：
   - 点击 **Add Application（添加应用）**，分别找到并添加以下进程：
     - Antigravity：同时添加 `antigravity.exe` 和 `language_server_windows_x64.exe`（遗漏后台语言服务会导致裸连失败）。
     - Gemini CLI：添加 `gemini.exe`。
     - Claude Code：添加 `claude.exe`。
     - 浏览器（可选）：若通过浏览器登录工具/使用NotebookLM，添加 `chrome.exe`/`msedge.exe`。
   - ⚠️ 重要：确保豆包客户端/浏览器 **未被添加** 到隧道列表，保持直连。
4. 添加域名级规则（补充进程规则，防止API端点遗漏）：
   OpenWeb协议下，找到 **Website Filter（网站过滤器）**，添加以下域名（每行一个），所有域名均选择 **Route through VPN（通过VPN路由）**，保存设置：
   ```
   # Antigravity相关
   antigravityide.app
   *.antigravityide.app
   daily-cloudcode-pa.sandbox.googleapis.com
   accounts.google.com
   *.gstatic.com
   
   # Gemini CLI相关
   generativelanguage.googleapis.com
   ai.google.dev
   *.googleapis.com
   
   # Claude Code相关
   api.anthropic.com
   *.anthropic.com
   
   # NotebookLM相关（与原有配置共存）
   notebooklm.google.com
   *.notebooklm.google.com
   ```

### 3.2 DNS优化与Override配置
1. 配置Astrill DNS：
   - 进入 **Settings → DNS**，**启用DNS Override（DNS覆盖）**，设置为Google DNS：
     - 首选DNS：`8.8.8.8`
     - 备选DNS：`8.8.4.4`
   - 目的：确保美国IP与DNS地域一致，避免Google风控。
2. 配置本地网络DNS（非VPN流量使用）：
   - 按下 `Win+R`，输入 `ncpa.cpl`，打开网络连接面板。
   - 右键当前网络（以太网/Wi-Fi）→ 属性 → 选中 **Internet 协议版本4（TCP/IPv4）** → 属性。
   - 选择 **使用下面的DNS服务器地址**，输入：
     - 首选DNS：`114.114.114.114` 或 `223.5.5.5`（阿里云）
     - 备选DNS：`114.114.115.115` 或 `223.6.6.6`
   - 点击确定保存，关闭所有网络属性窗口。
3. 刷新DNS缓存：
   - 以管理员身份打开命令提示符，执行以下命令：
   ```powershell
   ipconfig /flushdns
   ```
   - 提示“Successfully flushed the DNS Resolver Cache”即刷新成功。

### 3.3 验证与排错
#### 3.3.1 功能验证
1. 测试AI工具：
   - Gemini CLI：在终端执行 `gemini chat "hello"`，确认正常返回响应。
   - Claude Code：执行 `claude code "print('hello world')"`，确认功能正常。
   - Antigravity：在IDE中测试模型调用（Gemini 3 Pro/Claude Sonnet 4.5），确保模型加载成功。
2. 验证网络路由：
   - 用添加到隧道的浏览器访问 [https://www.ipleak.net/](https://www.ipleak.net/)，确认IP为美国IP、DNS为`8.8.8.8`/`8.8.4.4`。
   - 打开豆包客户端，确认IP为本地IP，语音/图片生成等功能正常。

#### 3.3.2 常见问题排错
- Antigravity模型无法加载：检查 `language_server` 进程是否添加到隧道；更换美国节点；清除浏览器缓存/Cookie。
- Gemini/Claude API调用失败：确认API密钥与环境变量配置正确；检查域名规则是否包含对应API端点。
- 豆包走VPN：排查分流列表，确保豆包未被误添加到隧道规则，必要时重启Astrill。

---

## 四、macOS系统配置步骤

### 4.1 分离规则核心设置（关键）
1. 打开Astrill客户端，点击左上角菜单 → **Settings → Split Tunneling/Application & Website Filter**。
2. 启用功能，选择 **Tunnel only selected apps/websites** 模式。
3. 添加进程级规则：
   - 点击 **Add Application**，从 **Applications（应用程序）** 中添加
