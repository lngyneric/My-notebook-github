# Astrill VPN 配置 Antigravity/Gemini CLI/Claude Code 分离规则教程

# 一、核心目标与合规提示

## 1.1 核心目标

仅让 **Antigravity、Gemini CLI、Claude Code** 走美国VPN节点（满足地域限制与API合规），同时保持豆包及其他本地应用直连网络，与此前配置的NotebookLM规则共存无冲突。

## 1.2 合规提示

- 在中国内地使用VPN须仅限 **企业跨境办公等合法场景**，遵守《中华人民共和国网络安全法》及相关规定。

- Google Antigravity、Gemini、Claude Code 目前仅限美国地区访问，需使用合规美国IP及对应DNS配置。

# 二、基础准备（必做）

## 2.1 Astrill 基础配置

1. 登录Astrill客户端，选择协议：优先 **OpenWeb**（浏览器+域名分流友好）或 **WireGuard**（速度与稳定性佳），避免使用StealthVPN（域名分流兼容性差）。

2. 选择服务器：筛选并连接 **美国低延迟节点**（优先非黑名单IP，降低Google风控概率）。

3. 确认连接成功（客户端显示Connected，IP为美国地域）。

## 2.2 工具进程与路径确认

以下为工具默认进程名与路径，用于后续添加分流规则（可根据实际安装位置调整）：

|工具名称|Windows进程名|macOS进程名|默认安装路径|
|---|---|---|---|
|Antigravity|antigravity.exe、language_server_windows_x64.exe|antigravity、language_server_macos_arm/x64|Windows：C:\Users\<用户名>\AppData\Local\antigravity\macOS：/Applications/Antigravity.app/Contents/MacOS/|
|Gemini CLI|gemini.exe|gemini|Windows：C:\Users\<用户名>\.gemini\macOS：/usr/local/bin/gemini 或 ~/bin/gemini|
|Claude Code|claude.exe|claude|Windows：C:\Users\<用户名>\AppData\Local\claude\macOS：/usr/local/bin/claude 或 ~/bin/claude|
## 2.3 API与环境变量配置

确保工具可正常调用API，提前完成以下配置：

- Gemini CLI：配置 ~/.gemini/settings.json 文件，设置 GOOGLE_GEMINI_API_KEY 环境变量。

- Claude Code：配置 ANTHROPIC_API_KEY；若与Antigravity集成，额外设置 ANTHROPIC_BASE_URL=http://127.0.0.1:8045（Antigravity默认代理端口）。

- Antigravity：完成Google账号OAuth登录，启动API代理（默认自动启动，端口8045）。

# 三、Windows系统配置步骤

## 3.1 分离规则核心设置（关键）

1. 打开Astrill客户端，进入**Settings（设置）→ Split Tunneling/Application & Website Filter（分流/应用与网站过滤器）**。

2. 启用功能（开关置为ON），选择 **Tunnel only selected apps/websites（仅隧道选定应用/网站）** 模式（核心逻辑：仅指定工具走VPN，其余直连）。

3. 添加进程级规则（精准匹配工具进程）：
       

    - 点击 **Add Application（添加应用）**，分别找到并添加以下进程：
                

        - Antigravity：同时添加 antigravity.exe 和 language_server_windows_x64.exe（遗漏后台语言服务会导致裸连失败）。

        - Gemini CLI：添加 gemini.exe。

        - Claude Code：添加 claude.exe。

        - 浏览器（可选）：若通过浏览器登录工具/使用NotebookLM，添加 chrome.exe/msedge.exe。

    - ⚠️ 重要：确保豆包客户端/浏览器 **未被添加** 到隧道列表，保持直连。

4. 添加域名级规则（补充进程规则，防止API端点遗漏）：
        

    - OpenWeb协议下，找到 **Website Filter（网站过滤器）**，添加以下域名（每行一个）：
    `# Antigravity相关
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
    *.notebooklm.google.com`

    - 所有域名均选择 **Route through VPN（通过VPN路由）**，保存设置。

## 3.2 DNS优化与Override配置

1. 配置Astrill DNS：
        

    - 进入 **Settings → DNS**，**启用DNS Override（DNS覆盖）**，设置为Google DNS：
                

        - 首选DNS：8.8.8.8

        - 备选DNS：8.8.4.4

    - 目的：确保美国IP与DNS地域一致，避免Google风控。

2. 配置本地网络DNS（非VPN流量使用）：
        

    - 按下 `Win+R`，输入 `ncpa.cpl`，打开网络连接面板。

    - 右键当前网络（以太网/Wi-Fi）→ 属性 → 选中 **Internet 协议版本4（TCP/IPv4）** → 属性。

    - 选择 **使用下面的DNS服务器地址**，输入：
                

        - 首选DNS：114.114.114.114 或 223.5.5.5（阿里云）

        - 备选DNS：114.114.115.115 或 223.6.6.6

    - 点击确定保存，关闭所有网络属性窗口。

3. 刷新DNS缓存：
        

    - 以管理员身份打开命令提示符，执行以下命令：
    `ipconfig /flushdns`

    - 提示“Successfully flushed the DNS Resolver Cache”即刷新成功。

## 3.3 验证与排错

### 3.3.1 功能验证

1. 测试AI工具：
       

    - Gemini CLI：在终端执行 `gemini chat "hello"`，确认正常返回响应。

    - Claude Code：执行 `claude code "print('hello world')"`，确认功能正常。

    - Antigravity：在IDE中测试模型调用（Gemini 3 Pro/Claude Sonnet 4.5），确保模型加载成功。

2. 验证网络路由：
        

    - 用添加到隧道的浏览器访问 [https://www.ipleak.net/](https://www.ipleak.net/)，确认IP为美国IP、DNS为8.8.8.8/8.8.4.4。

    - 打开豆包客户端，确认IP为本地IP，语音/图片生成等功能正常。

### 3.3.2 常见问题排错

- Antigravity模型无法加载：检查 language_server 进程是否添加到隧道；更换美国节点；清除浏览器缓存/Cookie。

- Gemini/Claude API调用失败：确认API密钥与环境变量配置正确；检查域名规则是否包含对应API端点。

- 豆包走VPN：排查分流列表，确保豆包未被误添加到隧道规则，必要时重启Astrill。

# 四、macOS系统配置步骤

## 4.1 分离规则核心设置（关键）

1. 打开Astrill客户端，点击左上角菜单 → **Settings → Split Tunneling/Application & Website Filter**。

2. 启用功能，选择 **Tunnel only selected apps/websites** 模式。

3. 添加进程级规则：
        

    - 点击 **Add Application**，从 **Applications（应用程序）** 中添加：
                

        - Antigravity：添加 Antigravity.app，同时找到其Contents/MacOS目录下的 language_server 进程并添加。

        - Gemini CLI：在终端执行 `which gemini` 找到路径，添加该可执行文件。

        - Claude Code：在终端执行 `which claude` 找到路径，添加该可执行文件。

        - 浏览器：添加Chrome/Edge（若需访问NotebookLM或工具网页端）。

4. 添加域名级规则：与Windows系统一致，复制3.1.4中的域名列表添加到 Website Filter，选择 Route through VPN。

## 4.2 DNS优化与系统设置

1. 配置Astrill DNS：启用DNS Override，设置为8.8.8.8（首选）、8.8.4.4（备选）。

2. 配置系统本地DNS（非VPN流量）：
        

    - 打开 **系统设置 → 网络**，选中当前网络（Wi-Fi/以太网）→ 高级 → DNS。

    - 添加本地公共DNS：114.114.114.114、223.5.5.5、223.6.6.6，移除所有VPN相关DNS条目。

    - 点击OK，应用设置。

3. 刷新DNS缓存：
        

    - 打开终端，执行以下命令（输入系统密码确认）：
    `sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder`

## 4.3 验证与排错

1. 功能验证：与Windows步骤一致，测试AI工具调用、IP/DNS归属、豆包直连功能。

2. 额外排错要点：
        

    - 进程添加失败：用终端命令 `ps aux | grep antigravity`/`ps aux | grep gemini`/`ps aux | grep claude` 查找进程ID，手动定位路径添加。

    - 网络拦截：检查系统防火墙/安全软件，临时关闭以排除流量拦截问题。

# 五、通用进阶优化

## 5.1 协议与节点切换策略

|协议|优势|适用场景|
|---|---|---|
|OpenWeb|域名分流友好，配置简单|浏览器访问NotebookLM + 多AI工具同时使用|
|WireGuard|速度快、稳定性高|频繁API调用、多工具长时间运行|
|StealthVPN|抗干扰性强|网络环境复杂时（域名分流兼容性差，不推荐）|
## 5.2 全隧道模式备选方案（临时使用）

仅临时需要全局VPN时使用，用完立即切换回分流模式：

1. 在Astrill中切换为 **Tunnel all apps（全隧道）**。

2. 单独添加豆包客户端/浏览器到 **Bypass VPN（绕过VPN）** 列表，避免豆包走VPN。

## 5.3 Antigravity与Claude Code集成（可选）

通过Antigravity代理Claude Code请求，优化访问稳定性：

1. 确保Antigravity已启动，API代理默认端口8045正常运行。

2. 配置环境变量：
        

    - Linux/macOS终端：
    `export ANTHROPIC_API_KEY="sk-antigravity"
    export ANTHROPIC_BASE_URL="http://127.0.0.1:8045"`

    - Windows PowerShell：
    `$env:ANTHROPIC_API_KEY="sk-antigravity"
    $env:ANTHROPIC_BASE_URL="http://127.0.0.1:8045"`

3. 执行Claude命令，确认集成成功。

# 六、附录：完整域名规则列表（可直接复制）

```Plain Text

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

# NotebookLM相关
notebooklm.google.com
*.notebooklm.google.com
```
> （注：文档部分内容可能由 AI 生成）