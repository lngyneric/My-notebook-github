---
source: raw/07_文档与参考/Markdown文档/README.md
raw_sha256: f4bca39e71252dc9679bd81fccc14a1aedfb4d1071fb96c6fcb195ddb8aee136
compiled_at: 2026-04-14T16:48:01.495Z
---
# WorkAny
## 摘要
WorkAny 是一款通过自然语言执行任务的桌面 AI 智能体应用，提供实时代码生成、工具执行与工作空间管理能力，支持多模型服务商、自定义技能、隔离代码执行等功能，是一款基于前后端分离架构的开源桌面应用。

## 功能特性
| 功能模块 | 说明 |
|---------|------|
| 任务执行 | 支持自然语言任务输入，带实时流式输出 |
| 智能体运行时 | 基于 Claude Code 驱动 |
| 智能体 SDK | 构建于 Claude Agent SDK 之上 |
| 代码沙箱 | 通过 Codex CLI 实现代码隔离执行 |
| 产物预览 | 支持 HTML/React/代码文件的实时预览 |
| MCP 支持 | 集成 Model Context Protocol 服务端 |
| 技能扩展 | 支持自定义智能体技能扩展能力 |
| 多模型服务商 | 支持 OpenRouter、Anthropic、OpenAI 以及自定义服务商 |

## 支持能力预览
- 文件整理
- 静态网站生成
- 文档生成
- 数据表生成
- 演示幻灯片生成
- 自定义智能体模型服务商配置
- 沙箱代码执行
- 自定义智能体技能管理

## 项目结构
```
workany/
├── src/                # 前端（React + TypeScript）
├── src-api/            # 后端API（Hono + Claude Agent SDK）
└── src-tauri/          # 桌面应用主体（Tauri + Rust）
```

## 技术栈
| 层级 | 技术选型 |
|-------|--------------|
| 前端 | React 19, TypeScript, Vite, Tailwind CSS 4 |
| 后端 | Hono, Claude Agent SDK, MCP SDK |
| 桌面端 | Tauri 2, SQLite |

## 开发说明
### 环境要求
- Node.js >= 20
- pnpm >= 9
- Rust >= 1.70

### 快速启动
```bash
# 安装依赖
pnpm install

# 启动API服务
pnpm dev:api

# 启动网页与桌面应用（推荐）
pnpm dev:app

# 仅启动网页端（可选）
pnpm dev:web
```

## 相关信息
- 官方网站：[workany.ai](https://workany.ai)
- 贡献指南：详见 [CONTRIBUTING.md](CONTRIBUTING.md)，欢迎贡献代码
- 致谢：部分组件基于 AI 全栈开发平台 [ShipAny.ai](https://shipany.ai) 构建
- 许可证：基于 Apache License 2.0 附加额外条件的 WorkAny 社区许可证
- 版权：© 2026 ThinkAny, LLC. All rights reserved.
