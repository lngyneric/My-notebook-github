---
source: raw/05_代码与项目/skills/skills/skills/mcp-builder/reference/mcp_best_practices.md
raw_sha256: 80fb4369a349447cf18ecdd7494fe7938b6065377e9f08c077cec411093a3007
compiled_at: 2026-04-14T05:18:40.095Z
---
# MCP Server 最佳实践
> 来源路径：`raw/05_代码与项目/skills/skills/skills/mcp-builder/reference/mcp_best_practices.md`

---

## TL;DR
MCP Server 开发遵循统一的命名规范、工具设计、响应格式、分页、传输、安全、测试和文档标准，核心是保证服务可互操作、安全可靠、易于使用。

---

## 目录
- [命名规范](#命名规范)
  - [服务端命名](#服务端命名)
  - [工具命名与设计](#工具命名与设计)
- [响应格式](#响应格式)
- [分页规范](#分页规范)
- [传输选择](#传输选择)
- [安全最佳实践](#安全最佳实践)
- [工具注解](#工具注解)
- [错误处理](#错误处理)
- [测试要求](#测试要求)
- [文档要求](#文档要求)

---

## 命名规范

### 服务端命名
| 语言/生态 | 命名格式 | 示例 |
|-----------|----------|------|
| Python | `{service}_mcp`（小写下划线） | `slack_mcp`, `github_mcp` |
| Node/TypeScript | `{service}-mcp-server`（小写连字符） | `slack-mcp-server`, `github-mcp-server` |

**通用规则**：名称需通用、描述集成的服务、可从任务描述轻松推断，不包含版本号。

### 工具命名与设计
#### 命名规则
1. 使用 `snake_case` 格式
2. 必须包含服务前缀（避免和其他 MCP 服务器工具冲突）
3. 以动词开头（get/list/search/create 等），面向动作
4. 名称具体，避免泛称

> [!EXAMPLE] 正确示例
> `slack_send_message`（而非 `send_message`），`github_create_issue`（而非 `create_issue`）

#### 工具设计规则
- 工具描述必须精准无歧义，和实际功能严格一致
- 保持工具操作聚焦、原子化
- 必须提供工具注解（见[工具注解](#工具注解)）

---

## 响应格式
所有返回数据的工具必须同时支持 JSON 和 Markdown 两种格式：

| 格式 | 适用场景 | 要求 |
|------|----------|------|
| JSON（`response_format="json"`） | 程序处理 | 机器可读结构化数据，包含所有可用字段和元数据，字段名/类型一致 |
| Markdown（`response_format="markdown"`，默认） | 人类阅读 | 易读格式化文本，时间戳转可读格式，显示名后带ID括号，省略冗余元数据 |

---

## 分页规范
针对列出资源的工具：
1. 始终遵守 `limit` 参数
2. 必须实现分页（offset 或 游标模式）
3. 返回分页元数据：`has_more`、`next_offset`/`next_cursor`、`total_count`
4. 禁止将所有结果加载到内存（对大数据集尤其重要）
5. 默认条数建议 20~50 条

> [!EXAMPLE] 分页响应示例
> ```json
> {
>   "total": 150,
>   "count": 20,
>   "offset": 0,
>   "items": [...],
>   "has_more": true,
>   "next_offset": 20
> }
> ```

---

## 传输选择
### 传输对比
| 传输方式 | 最佳适用场景 | 核心特点 | 注意事项 |
|----------|--------------|----------|----------|
| **Streamable HTTP** | 远程服务、多客户端场景 | 基于HTTP的双向通信，支持多并发客户端，可部署为web服务，支持服务端推送通知 | 推荐替代已废弃的SSE |
| **stdio** | 本地集成、命令行工具 | 通过标准输入输出通信，无需网络配置，作为客户端子进程运行 | 禁止向stdout打日志，日志请输出到stderr |

### 选择对照表
| 评判维度 | stdio | Streamable HTTP |
|-----------|-------|-----------------|
| 部署场景 | 本地 | 远程 |
| 支持客户端数 | 单客户端 | 多客户端 |
| 复杂度 | 低 | 中等 |
| 实时能力 | 不支持 | 支持 |

---

## 安全最佳实践
### 身份认证与授权
- **OAuth 2.1**：使用权威机构证书的安全OAuth 2.1，处理请求前验证访问令牌，仅接受专门发给本服务器的令牌
- **API Key**：密钥存储在环境变量，禁止硬编码到代码，服务启动时验证密钥，认证失败提供清晰错误信息

### 输入验证
- 清理文件路径，防止目录遍历攻击
- 验证URL和外部标识符
- 检查参数大小和范围
- 系统调用中防止命令注入
- 对所有输入使用模式验证（Python用Pydantic，TS用Zod）

### 错误处理
- 禁止向客户端暴露内部错误
- 服务端记录安全相关错误
- 提供有帮助但不泄露敏感信息的错误信息
- 错误后清理资源

### DNS重绑定防护（本地运行的Streamable HTTP服务器）
- 开启DNS重绑定防护
- 验证所有入站连接的`Origin`头
- 绑定到`127.0.0.1`而非`0.0.0.0`

---

## 工具注解
需要提供注解帮助客户端理解工具行为，注解仅为提示，不是安全保证，禁止客户端仅基于注解做安全关键决策：

| 注解 | 类型 | 默认值 | 说明 |
|-----------|------|---------|-------------|
| `readOnlyHint` | boolean | false | 工具不会修改运行环境 |
| `destructiveHint` | boolean | true | 工具可能执行破坏性更新 |
| `idempotentHint` | boolean | false | 相同参数重复调用不会产生额外效果 |
| `openWorldHint` | boolean | true | 工具会和外部实体交互 |

---

## 错误处理
- 使用标准JSON-RPC错误码
- 工具错误在结果对象中返回（而非协议层面错误）
- 提供有帮助、具体的错误信息，并给出下一步建议
- 禁止暴露内部实现细节
- 错误后正确清理资源

> [!EXAMPLE] TypeScript错误处理示例
> ```typescript
> try {
>   const result = performOperation();
>   return { content: [{ type: "text", text: result }] };
> } catch (error) {
>   return {
>     isError: true,
>     content: [{
>       type: "text",
>       text: `Error: ${error.message}. Try using filter='active_only' to reduce results.`
>     }]
>   };
> }
> ```

---

## 测试要求
完整测试需要覆盖以下维度：
- 功能测试：验证合法/非法输入的执行正确性
- 集成测试：测试和外部系统的交互
- 安全测试：验证认证、输入清理、限流能力
- 性能测试：检查负载、超时行为
- 错误处理测试：确保错误报告和清理正确

---

## 文档要求
- 提供所有工具和能力的清晰文档
- 包含可运行示例（每个主要功能至少3个）
- 文档记录安全注意事项
- 明确说明所需权限和访问级别
- 文档记录限流和性能特征

---

## 引用原始证据片段
<details>
<summary>点击展开原始内容</summary>

```markdown
# MCP Server Best Practices

## Quick Reference

### Server Naming
- **Python**: `{service}_mcp` (e.g., `slack_mcp`)
- **Node/TypeScript**: `{service}-mcp-server` (e.g., `slack-mcp-server`)

### Tool Naming
- Use snake_case with service prefix
- Format: `{service}_{action}_{resource}`
- Example: `slack_send_message`, `github_create_issue`

### Response Formats
- Support both JSON and Markdown formats
- JSON for programmatic processing
- Markdown for human readability

### Pagination
- Always respect `limit` parameter
- Return `has_more`, `next_offset`, `total_count`
- Default to 20-50 items

### Transport
- **Streamable HTTP**: For remote servers, multi-client scenarios
- **stdio**: For local integrations, command-line tools
- Avoid SSE (deprecated in favor of streamable HTTP)

---

## Server Naming Conventions

Follow these standardized naming patterns:

**Python**: Use format `{service}_mcp` (lowercase with
