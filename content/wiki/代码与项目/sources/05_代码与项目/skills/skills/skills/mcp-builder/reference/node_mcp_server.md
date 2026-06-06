---
source: raw/05_代码与项目/skills/skills/skills/mcp-builder/reference/node_mcp_server.md
raw_sha256: c3ba35a4f599dd53be9c6555ae72c19a7bf412cd5426576c2c08d42755482c66
compiled_at: 2026-04-14T05:18:55.237Z
---
# Node/TypeScript MCP Server 实现指南
> 来源路径：`raw/05_代码与项目/skills/skills/skills/mcp-builder/reference/node_mcp_server.md`

## TL;DR
本文是基于官方 MCP TypeScript SDK 的 Node/TypeScript MCP 服务开发规范指南，涵盖项目结构、服务初始化、工具/资源注册、参数校验、错误处理、工程配置等全流程最佳实践，要求仅使用现代 `register*` 系列 API，遵循统一的命名和项目结构规范，使用 Zod 做运行时参数校验，保证类型安全与代码可维护性。

## 目录
- [快速参考](#快速参考)
- [SDK 规范要求](#mcp-typescript-sdk)
- [命名与项目结构规范](#命名与项目结构规范)
- [工具开发规范](#工具实现)
- [核心开发实践](#核心开发实践)
- [工程配置](#包配置)
- [高级功能](#高级mcp功能)
- [代码质量与检查清单](#代码最佳实践与质量检查清单)

## 快速参考
### 关键导入
```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import express from "express";
import { z } from "zod";
```

### 服务初始化
```typescript
const server = new McpServer({
  name: "service-mcp-server",
  version: "1.0.0"
});
```

### 工具注册基础模式
```typescript
server.registerTool(
  "tool_name",
  {
    title: "Tool Display Name",
    description: "What the tool does",
    inputSchema: { param: z.string() },
    outputSchema: { result: z.string() }
  },
  async ({ param }) => {
    const output = { result: `Processed: ${param}` };
    return {
      content: [{ type: "text", text: JSON.stringify(output) }],
      structuredContent: output // Modern pattern for structured data
    };
  }
);
```

## MCP TypeScript SDK
官方 MCP TypeScript SDK 提供：
- `McpServer` 类用于服务初始化
- `registerTool` 方法用于工具注册
- Zod 集成支持运行时输入校验
- 类型安全的工具处理器实现

> [!IMPORTANT] 仅允许使用现代 API
> - ✅ 必须使用：`server.registerTool()`、`server.registerResource()`、`server.registerPrompt()`
> - ❌ 禁止使用：已废弃的旧 API，例如 `server.tool()`、`server.setRequestHandler(ListToolsRequestSchema, ...)` 或手动处理器注册
> - `register*` 系列 API 提供更好的类型安全、自动 schema 处理，是官方推荐方式

## 命名与项目结构规范
### 服务命名规范
Node/TypeScript MCP 服务必须遵循以下命名规则：
- 格式：`{service}-mcp-server`（全小写，连字符分隔）
- 示例：`github-mcp-server`、`jira-mcp-server`、`stripe-mcp-server`
- 命名要求：
  - 保持通用，不绑定特定功能
  - 清晰描述集成的服务/API
  - 可以从任务描述中轻松推断
  - 不包含版本号或日期

### 推荐项目结构
```
{service}-mcp-server/
├── package.json
├── tsconfig.json
├── README.md
├── src/
│   ├── index.ts          # 主入口，包含 McpServer 初始化
│   ├── types.ts          # TypeScript 类型定义与接口
│   ├── tools/            # 工具实现（按领域分文件）
│   ├── services/         # API 客户端与共享工具
│   ├── schemas/          # Zod 校验 schema
│   └── constants.ts      # 共享常量（API_URL、CHARACTER_LIMIT 等）
└── dist/                 # 构建输出的 JavaScript 文件（入口：dist/index.js）
```

## 工具实现
### 工具命名规范
- 使用蛇形命名法（snake_case），例如 `search_users`、`create_project`、`get_channel_info`，使用清晰的面向动作的命名
- 为避免命名冲突，需要加上服务上下文前缀：
  - 用 `slack_send_message` 代替仅 `send_message`
  - 用 `github_create_issue` 代替仅 `create_issue`
  - 用 `asana_list_tasks` 代替仅 `list_tasks`

### 工具结构要求
必须使用 `registerTool` 方法注册工具，满足以下要求：
- 使用 Zod schema 做运行时输入校验和类型安全
- 必须显式提供 `description` 字段，JSDoc 注释不会被自动提取
- 必须显式提供 `title`、`description`、`inputSchema` 和 `annotations`
- `inputSchema` 必须是 Zod schema 对象（不能是 JSON schema）
- 所有参数和返回值必须显式标注类型

完整示例：
```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";

const server = new McpServer({
  name: "example-mcp",
  version: "1.0.0"
});

// Zod schema 用于输入校验
const UserSearchInputSchema = z.object({
  query: z.string()
    .min(2, "Query must be at least 2 characters")
    .max(200, "Query must not exceed 200 characters")
    .describe("Search string to match against names/emails"),
  limit: z.number()
    .int()
    .min(1)
    .max(100)
    .default(20)
    .describe("Maximum results to return"),
  offset: z.number()
    .int()
    .min(0)
    .default(0)
    .describe("Number of results to skip for pagination"),
  response_format: z.nativeEnum(ResponseFormat)
    .default(ResponseFormat.MARKDOWN)
    .describe("Output format: 'markdown' for human-readable or 'json' for machine-readable")
}).strict();

// 从 Zod schema 生成类型定义
type UserSearchInput = z.infer<typeof UserSearchInputSchema>;

server.registerTool(
  "example_search_users",
  {
    title: "Search Example Users",
    description: `Search for users in the Example system by name, email, or team.

This tool searches across all user profiles in the Example platform, supporting partial matches and various search filters. It does NOT create or modify users, only searches existing ones.

Args:
  - query (string): Search string to match against names/emails
  - limit (number): Maximum results to return, between 1-100 (default: 20)
  - offset (number): Number of results to skip for pagination (default: 0)
  - response_format ('markdown' | 'json'): Output format (default: 'markdown')

Returns:
  For JSON format: Structured data with schema:
  {
    "total": number,           // Total number of matches found
    "count": number,           // Number of results in this response
    "offset": number,          // Current pagination offset
    "users": [
      {
        "id": string,          // User ID (e.g., "U123456789")
        "name": string,        // Full name (e.g., "John Doe")
        "email": string,       // Email address
        "team": string,        // Team name (optional)
        "active": boolean      // Whether user is active
      }
    ],
    "has_more": boolean,       // Whether more results are available
    "next_offset": number      // Offset for next page (if has_more is true)
  }

Examples:
  - Use when: "Find all marketing team members" -> params with query="team:marketing"
  - Use when: "Search for John's account" -> params with query="john"
  - Don't use when: You need to create a user (use example_create_user instead)

Error Handling:
  - Returns "Error: Rate limit exceeded" if too many requests (429 status)
  - Returns "No users found matching '<query>'" if search returns empty`,
    inputSchema: UserSearchInputSchema,
    annotations: {
      readOnlyHint: true,
