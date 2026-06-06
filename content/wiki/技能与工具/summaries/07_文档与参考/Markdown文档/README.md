---
source: raw/07_文档与参考/Markdown文档/README.md
raw_sha256: f4bca39e71252dc9679bd81fccc14a1aedfb4d1071fb96c6fcb195ddb8aee136
compiled_at: 2026-04-24T06:24:03.729Z
---
# WorkAny
## Summary
WorkAny is a desktop AI agent application that executes tasks through natural language. It provides core capabilities including real-time code generation, tool execution, and workspace management.

## Basic Information
- **Official Website**: [workany.ai](https://workany.ai)
- **Homepage Preview**: ![](./public/imgs/home.png)

## Function Previews
The following demonstrates core functional scenarios of WorkAny:
1. File organization ![](./public/imgs/files.png)
2. Website generation ![](./public/imgs/web.png)
3. Document generation ![](./public/imgs/doc.png)
4. Data table generation ![](./public/imgs/excel.png)
5. Slide generation ![](./public/imgs/ppt.png)
6. Custom model provider configuration for agents ![](./public/imgs/settings.png)
7. Sandbox-based code execution ![](./public/imgs/sandbox.png)
8. Agent skills management ![](./public/imgs/skills.png)

## Core Features
| Feature | Description |
|---------|-------------|
| Task Execution | Natural language task input with real-time streaming output |
| Agent Runtime | Powered by [Claude Code](https://github.com/anthropics/claude-code) |
| Agent SDK | Built on [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) |
| Sandbox | Isolated code execution via [Codex CLI](https://github.com/openai/codex) |
| Artifact Preview | Live preview support for HTML/React/code files |
| MCP Support | Model Context Protocol server integration |
| Skills Support | Custom agent skills for extended functional capabilities |
| Multi-provider | Compatible with OpenRouter, Anthropic, OpenAI, and custom model providers |

## Project Structure
The WorkAny codebase is organized into three main directories:
```
workany/
├── src/                # Frontend (React + TypeScript)
├── src-api/            # Backend API (Hono + Claude Agent SDK)
└── src-tauri/          # Desktop app (Tauri + Rust)
```

## Technology Stack
| Layer | Technologies Used |
|-------|-------------------|
| Frontend | React 19, TypeScript, Vite, Tailwind CSS 4 |
| Backend | Hono, Claude Agent SDK, MCP SDK |
| Desktop | Tauri 2, SQLite |

## Development Guide
### Prerequisites
- Node.js >= 20
- pnpm >= 9
- Rust >= 1.70

### Quick Start Commands
```bash
# Install all dependencies
pnpm install

# Start the backend API server
pnpm dev:api

# Start both web and desktop application (recommended)
pnpm dev:app

# Start web application only (optional)
pnpm dev:web
```

## Contributing
Contributions to the WorkAny project are welcome. Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## Acknowledgments
Some components of WorkAny are built with [ShipAny.ai](https://shipany.ai), an AI-powered full-stack development platform.

## License
This project is licensed under the [WorkAny Community License](LICENSE), which is based on Apache License 2.0 with additional conditions.
© 2026 ThinkAny, LLC. All rights reserved.
