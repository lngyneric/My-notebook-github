---
source: raw/Openmaic/README-zh.md
raw_sha256: cff2fe845325564ab62da7e55891cc419e2f55119d62293251f6bd6573edbf88
compiled_at: 2026-04-14T03:48:32.251Z
---
# OpenMAIC

<p align="center">
  <img src="https://raw.githubusercontent.com/THU-MAIC/OpenMAIC/main/assets/banner.png" alt="OpenMAIC Banner" width="680"/>
</p>

<p align="center">
  一键生成沉浸式多智能体互动课堂。
</p>

---

## TL;DR

OpenMAIC（Open Multi-Agent Interactive Classroom）是一个开源 AI 互动课堂平台，可将任意主题/文档转化为由 AI 教师、AI 同学共同参与的多智能体互动学习体验，支持生成幻灯片、测验、交互式模拟、项目制学习等多种课堂场景，支持白板绘图、语音讲解、实时讨论，支持导出PPT和独立网页，并可通过 OpenClaw 集成直接在飞书/Slack 等聊天工具中使用。

---

## 目录

- [项目简介](#项目简介)
- [核心亮点](#核心亮点)
- [快速开始](#快速开始)
  - [环境要求](#环境要求)
  - [本地部署步骤](#本地部署步骤)
  - [一键Vercel部署](#vercel-部署)
  - [Docker部署](#docker-部署)
  - [可选增强：MinerU文档解析](#可选mineru增强文档解析)
- [功能特性](#功能特性)
- [OpenClaw集成](#openclaw-集成)
- [使用场景示例](#使用场景示例)
- [参与贡献](#参与贡献)
- [商业合作](#商业合作)
- [引用](#引用)
- [许可证](#许可证)

---

## 项目简介

**OpenMAIC**（Open Multi-Agent Interactive Classroom）是一个开源的 AI 互动课堂平台，能够将任何主题或文档转化为丰富的互动学习体验。基于多智能体协作引擎，它可以自动生成演示幻灯片、测验、交互式模拟实验和项目制学习活动——由 AI 教师和 AI 同学进行语音讲解、白板绘图，并与你展开实时讨论。内置 [OpenClaw](https://github.com/openclaw/openclaw) 集成，你还可以直接在飞书、Slack、Telegram 等聊天应用中生成课堂。

https://github.com/user-attachments/assets/dbd013f6-9fab-43c5-a788-b47126cff7a8

### 核心亮点
> [!TIP] 核心亮点
> - **一键生成课堂** — 描述一个主题或附上学习材料，AI 几分钟内构建完整课堂
> - **多智能体课堂** — AI 老师和智能体同学实时授课、讨论、互动
> - **丰富的场景类型** — 幻灯片、测验、HTML 交互式模拟、项目制学习（PBL）
> - **白板 & 语音** — 智能体实时绘制图表、书写公式、语音讲解
> - **灵活导出** — 下载可编辑的 `.pptx` 幻灯片或交互式 `.html` 网页
> - **[OpenClaw 集成](#openclaw-集成)** — 通过 AI 助手在飞书、Slack、Telegram 等 20+ 聊天应用中直接生成课堂

> [!TIP] OpenClaw 零配置使用说明
> <img src="https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/png/openclaw.png" height="28" align="top"/> 通过 [OpenClaw](https://github.com/openclaw/openclaw)，你可以直接在飞书、Slack、Discord、Telegram 等 20+ 聊天应用中生成课堂。
> 1. `clawhub install openmaic`，或者直接跟你的 Claw 说 *"安装 OpenMAIC skill"*
> 2. 选一种模式：
>    - **托管模式** — 在 [open.maic.chat](https://open.maic.chat/) 获取访问码，无需本地部署
>    - **本地部署** — Skill 会引导你逐步完成 clone、配置和启动
> 3. 告诉你的助手 *"教我量子物理"* — 搞定！

---

## 🚀 快速开始

### 环境要求
- **Node.js** >= 20
- **pnpm** >= 10

### 本地部署步骤

#### 1. 克隆 & 安装
```bash
git clone https://github.com/THU-MAIC/OpenMAIC.git
cd OpenMAIC
pnpm install
```

#### 2. 配置
```bash
cp .env.example .env.local
```
至少填写一个 LLM 服务商的 API Key：
```env
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=...
```
也可以通过 `server-providers.yml` 配置服务商：
```yaml
providers:
  openai:
    apiKey: sk-...
  anthropic:
    apiKey: sk-ant-...
```
支持的服务商：**OpenAI**、**Anthropic**、**Google Gemini**、**DeepSeek** 以及任何兼容 OpenAI API 的服务。

> **推荐模型：** **Gemini 3 Flash** — 效果与速度的最佳平衡。追求最高质量可选 **Gemini 3.1 Pro**（速度较慢）。
> 如果希望 OpenMAIC 服务端默认走 Gemini，还需要额外设置 `DEFAULT_MODEL=google:gemini-3-flash-preview`。

#### 3. 启动开发服务
```bash
pnpm dev
```
打开 **http://localhost:3000** 开始学习！

#### 4. 生产环境构建
```bash
pnpm build && pnpm start
```

### Vercel 部署
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FTHU-MAIC%2FOpenMAIC&envDescription=Configure%20at%20least%20one%20LLM%20provider%20API%20key%20(e.g.%20OPENAI_API_KEY%2C%20ANTHROPIC_API_KEY).%20All%20providers%20are%20optional.&envLink=https%3A%2F%2Fgithub.com%2FTHU-MAIC%2FOpenMAIC%2Fblob%2Fmain%2F.env.example&project-name=openmaic&framework=nextjs)

手动部署步骤：
1. Fork 本仓库
2. 导入到 [Vercel](https://vercel.com/new)
3. 配置环境变量（至少一个 LLM API Key）
4. 部署完成

### Docker 部署
```bash
cp .env.example .env.local
# 编辑 .env.local 填入你的 API Key，然后执行：
docker compose up --build
```

### 可选：MinerU（增强文档解析）
[MinerU](https://github.com/opendatalab/MinerU) 提供更强的表格、公式和 OCR 解析能力。你可以使用 [MinerU 官方 API](https://mineru.net/) 或[自行部署](https://opendatalab.github.io/MinerU/quick_start/docker_deployment/)。

在 `.env.local` 中设置 `PDF_MINERU_BASE_URL`（如需认证则同时设置 `PDF_MINERU_API_KEY`）。

---

## ✨ 功能特性

### 课堂生成流程
描述你想学习的内容，或附上参考材料。OpenMAIC 的两阶段流水线自动完成剩余工作：

| 阶段 | 说明 |
|------|------|
| **大纲生成** | AI 分析你的输入，生成结构化的课堂大纲 |
| **场景生成** | 每个大纲条目生成为丰富的场景——幻灯片、测验、交互模块或 PBL 活动 |

### 课堂组件

| 🎓 幻灯片（Slides） | 🧪 测验（Quiz） |
| ---- | ---- |
| AI 老师配合聚光灯和激光笔动作进行语音讲解——如同真实课堂 | 交互式测验（单选 / 多选 / 简答），支持 AI 实时判分和反馈 |

| 🔬 交互式模拟（Interactive） | 🏗️ 项目制学习（PBL） |
| ---- | ---- |
| 基于 HTML 的交互实验，用于可视化、动手学习——物理模拟器、流程图等 | 选择一个角色，与 AI 智能体协作完成结构化项目，包含里程碑和交付物 |

### 多智能体互动
- **课堂讨论** — 智能体主动发起讨论话题，你可以随时加入或被点名互动
- **圆桌辩论** — 多个不同人设的智能体围绕话题展开讨论，配合白板讲解
- **自由问答** — 随时提问，AI 老师通过幻灯片、图表或白板进行解答
