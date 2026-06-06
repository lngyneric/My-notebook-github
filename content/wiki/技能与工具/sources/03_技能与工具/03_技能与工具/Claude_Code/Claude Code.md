---
source: raw/03_技能与工具/Claude_Code/Claude Code.md
raw_sha256: 244387f6ee086abe2e950d20854544a8c401a8d0239e4fcc256337426c93e4cd
compiled_at: 2026-04-14T03:54:19.846Z
---
# Claude Code 配置 GLM Coding Plan 使用指南

> 来源路径：`raw/03_技能与工具/Claude_Code/Claude Code.md`

---

## TL;DR
Claude Code 是运行在终端的智能编码工具，搭配智谱 GLM Coding Plan 使用后，可以更低价格获得3倍用量，提升编码工作效率。本文档整理了完整的安装、配置、使用与问题排查流程。

---

## 要点
- Claude Code 支持终端自然语言交互，可完成代码生成、调试、重构等开发任务
- 搭配 GLM Coding Plan：以更低价格获得 **3 倍用量**，能力比原生 Claude Code 进一步增强
- 默认服务端模型映射，配置后界面显示 Claude 模型，实际调用 GLM 模型，2025年12月后默认模型已升级到 GLM-4.7
- 提供自动化/手动多种配置方式，支持全平台，配置完成后重启终端即可使用

---

## 功能与说明
> [!NOTE]
> 原始引用
> Claude Code 是一个智能编码工具，可以在终端中运行，通过自然语言命令交互帮助开发者快速完成代码生成、调试、重构等任务。

> [!TIP]
> 搭配 [**GLM Coding Plan**](https://zhipuaishengchan.datasink.sensorsdata.cn/t/Nd)，Claude Code 的能力能进一步增强 —— 以更低价格获得 **3 倍用量**，让你在编码、调试和工作流管理中更高效、更稳定。

> [!WARNING]
> 在 2025-12-22 日期前已使用的用户请注意：
> GLM Coding Plan 的默认模型已升级至 GLM-4.7，使用最新配置方式的用户无感知升级。
> 但若您之前在 `settings.json` 中配置过 GLM-4.5 的固定模型映射，请参考下方「常见问题」章节中的「如何切换使用模型」进行调整，以确保使用最新的 GLM-4.7 模型。

> [!TIP]
> 在成功配置套餐后，默认为服务端模型映射，即您界面上看到的是 Claude 模型但实际是 GLM 模型。
> 您可以手动调整模型映射(不推荐)，详见「常见问题」章节中的「如何切换使用模型」。

---

## 步骤一：安装 Claude Code

| 安装方式 | 说明 |
|---------|------|
| 推荐安装（命令行） | 需要 Node.js 18+ 环境，Windows 额外需要 Git for Windows |
| Cursor 引导安装 | 适合不熟悉 Node.js 且已安装 Cursor 的用户 |

### 推荐安装命令
```bash
# 全局安装 Claude Code
npm install -g @anthropic-ai/claude-code

# 验证安装，输出版本号则安装成功
claude --version
```

### Cursor 引导安装命令
```bash
https://docs.anthropic.com/zh-CN/docs/claude-code/overview Help me install Claude Code
```

> [!NOTE]
> **注意**：如果您在安装过程中遇到权限问题，请尝试使用 `sudo`（MacOS/Linux）或以管理员身份运行命令提示符（Windows）重新执行安装命令。
> 安装成功后，还需后续配置步骤，若您直接使用 `claude` 命令启动，可能由于网络或地区限制无法使用。

---

## 步骤二：配置 GLM Coding Plan

### 1. 注册账号
访问 [智谱开放平台](https://open.bigmodel.cn)，点击右上角的「注册/登录」按钮，按照提示完成账号注册流程。

### 2. 获取API Key
登录后，在个人中心页面，点击 [API Keys](https://bigmodel.cn/usercenter/proj-mgmt/apikeys)，创建一个新的 API Key。

> [!WARNING]
> 请妥善保管您的 API Key，不要泄露给他人，也不要直接硬编码在代码中。

### 3. 配置环境变量
选择以下对应系统的一种方式配置即可：

#### 方式一：自动化助手（全平台推荐）
Coding Tool Helper 是智谱提供的编码工具助手，可快速完成 GLM 编码套餐加载、工具配置，执行以下命令后按界面提示操作即可：
```bash
npx @z_ai/coding-helper
```
详细说明：[Coding Tool Helper 文档](/cn/coding-plan/extension/coding-tool-helper)

#### 方式二：自动化脚本（仅支持 MacOS/Linux）
```bash
curl -O "https://cdn.bigmodel.cn/install/claude_code_env.sh" && bash ./claude_code_env.sh
```
脚本会自动完成配置，生成的配置内容如下（无需手动修改）：
`~/.claude/settings.json` 自动添加：
```json
{
    "env": {
        "ANTHROPIC_AUTH_TOKEN": "your_zhipu_api_key",
        "ANTHROPIC_BASE_URL": "https://open.bigmodel.cn/api/anthropic",
        "API_TIMEOUT_MS": "3000000",
        "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": 1
    }
}
```
`~/.claude.json` 自动添加：
```json
{
    "hasCompletedOnboarding": true
}
```

#### 方式三：手动配置（支持全平台）
配置文件路径说明：
- MacOS & Linux：`~/.claude/settings.json`、`~/.claude.json`
- Windows：`用户目录/.claude/settings.json`、`用户目录/.claude.json`

编辑 `settings.json`，新增/修改 `env` 字段，替换 `your_zhipu_api_key` 为你自己获取的 API Key：
```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "your_zhipu_api_key",
    "ANTHROPIC_BASE_URL": "https://open.bigmodel.cn/api/anthropic",
    "API_TIMEOUT_MS": "3000000",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": 1
  }
}
```

编辑 `.claude.json`，新增 `hasCompletedOnboarding` 参数：
```json
{
  "hasCompletedOnboarding": true
}
```

> [!NOTE]
> 配置成功后，请确保重新打开一个新的终端窗口，以便环境配置生效。

---

## 步骤三：开始使用 Claude Code
配置完成后，进入你的代码工作目录，在终端执行 `claude` 命令即可启动：
- 遇到「Do you want to use this API key」提示，选择 `Yes` 即可
- 启动后选择信任 Claude Code 访问当前文件夹的文件

完成后即可正常使用 Claude Code 进行开发。

---

## 常见问题

### 如何切换使用模型
默认模型映射关系：
| 环境变量 | 默认对应 GLM 模型 |
|---------|------------------|
| `ANTHROPIC_DEFAULT_OPUS_MODEL` | `GLM-4.7` |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` | `GLM-4.7` |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | `GLM-4.5-Air` |

> [!NOTE]
> 一般不建议您手动调整模型映射，因为硬编码模型映射后，当 GLM Coding Plan 的模型更新升级时，不方便您自动更新到最新模型。
> 若您想使用最新默认映射（针对老用户已配置旧模型映射的情况），删除 `settings.json` 中的模型映射配置即可，Claude Code 会自动使用最新的默认模型。

手动切换步骤：
1. 修改 `~/.claude/settings.json`，添加/替换环境变量：
```json
{
  "env": {
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm-4.5-air",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-4.7",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-4.7"
  }
}
```
2. 重启终端启动 Claude Code，输入 `/status` 即可确认当前模型状态。

### 视觉和搜索 MCP 服务器
参考对应文档配置后即可在 Claude Code 中使用：
- [视觉MCP服务器](/cn/coding-plan/mcp/vision-mcp-server)
- [搜索MCP服务器](/cn/coding-plan/mcp/search-mcp-server)
- [网页读取MCP服务器](/cn/coding-plan/mcp/reader-mcp-server)

### 手工修改配置不生效
可按以下步骤排查：
1. 关闭所有 Claude Code 窗口，重新打开新的命令行窗口，再次运行
