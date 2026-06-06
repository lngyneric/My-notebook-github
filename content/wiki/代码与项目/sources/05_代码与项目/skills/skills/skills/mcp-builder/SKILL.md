---
source: raw/05_代码与项目/skills/skills/skills/mcp-builder/SKILL.md
raw_sha256: 0f4592dcb53cf2b5d6b7febee6b4152018b565551a1c29e3c612f57b218ab295
compiled_at: 2026-04-14T05:06:25.993Z
---
> [!INFO]
> 来源路径：`raw/05_代码与项目/skills/skills/skills/mcp-builder/SKILL.md`

# mcp-builder

---

## 元信息
| 字段 | 值 |
|------|-----|
| 名称 | mcp-builder |
| 描述 | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK). |
| 协议 | Complete terms in LICENSE.txt |

---

## TL;DR
mcp-builder 是高质量MCP（模型上下文协议）服务器开发指南，提供了从规划、实现到测试评估的完整工作流，覆盖TypeScript和Python两种技术栈，帮助开发者构建能让大模型有效调用外部服务的MCP工具服务。

---

## 开发总览
创建MCP服务器的核心目标是让大语言模型能够通过设计良好的工具与外部服务交互，MCP服务器的质量由其支持大模型完成真实任务的能力衡量。

---

## 开发流程
### 🚀 高层工作流
高质量MCP服务器开发分为四个核心阶段：

---

#### 阶段一：深度调研与规划
##### 1.1 理解现代MCP设计原则
| 设计维度 | 核心要点 |
|----------|----------|
| API覆盖 vs 工作流工具 | 需要平衡全面的API端点覆盖和专用工作流工具；不确定时优先选择全面API覆盖 |
| 工具命名与可发现性 | 使用清晰描述性命名，统一前缀（如`github_create_issue`），面向动作命名 |
| 上下文管理 | 工具返回聚焦的相关数据，支持结果过滤/分页，配合客户端代码处理能力 |
| 可操作错误信息 | 错误信息需要包含具体解决方案建议和后续步骤指引 |

##### 1.2 学习MCP协议文档
访问步骤：
1. 从站点地图开始查找相关页面：`https://modelcontextprotocol.io/sitemap.xml`
2. 添加`.md`后缀获取markdown格式的具体页面（例如`https://modelcontextprotocol.io/specification/draft.md`）

需要重点学习的内容：
- 规范概述与架构
- 传输机制（可流式HTTP、stdio）
- 工具、资源和提示词定义

##### 1.3 学习框架文档
推荐技术栈：
- **语言**：TypeScript（拥有高质量SDK支持，在多种执行环境兼容性好，大模型更擅长生成TypeScript代码，受益于静态类型和完善的lint工具）
- **传输**：远程服务器使用可流式HTTP（无状态JSON，相比有状态会话和流式响应更易扩展维护），本地服务器使用stdio

参考文档：
- 核心最佳实践：[📋 MCP 最佳实践](./reference/mcp_best_practices.md)
- TypeScript（推荐）：
  - SDK文档：从 `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md` 获取
  - 实现指南：[⚡ TypeScript 开发指南](./reference/node_mcp_server.md)
- Python：
  - SDK文档：从 `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md` 获取
  - 实现指南：[🐍 Python 开发指南](./reference/python_mcp_server.md)

##### 1.4 规划实现
1. 理解目标服务API： review服务API文档，识别关键端点、鉴权要求和数据模型，可按需使用网页搜索和网页获取工具
2. 工具选型：优先全面API覆盖，列出需要实现的端点，从最常用操作开始

---

#### 阶段二：实现
##### 2.1 初始化项目结构
参考语言特定指南：
- [⚡ TypeScript 实现指南](./reference/node_mcp_server.md)：包含项目结构、package.json、tsconfig.json配置
- [🐍 Python 实现指南](./reference/python_mcp_server.md)：包含模块组织、依赖管理

##### 2.2 实现核心基础设施
需要创建的公共工具：
- 带鉴权的API客户端
- 错误处理辅助函数
- 响应格式化（JSON/Markdown）
- 分页支持

##### 2.3 逐个实现工具
每个工具需要包含：
1. **输入Schema**：TypeScript用Zod，Python用Pydantic；添加约束、清晰描述、字段示例
2. **输出Schema**：尽可能定义`outputSchema`结构化数据，使用SDK的`structuredContent`特性，方便客户端处理输出
3. **工具描述**：功能简洁摘要、参数描述、返回类型Schema
4. **实现要求**：使用async/await处理IO、完善的带可操作信息的错误处理、按需支持分页、同时返回文本内容和结构化数据
5. **标注**：设置`readOnlyHint`/`destructiveHint`/`idempotentHint`/`openWorldHint`四个标志

---

#### 阶段三：Review与测试
##### 3.1 代码质量检查
检查点：
- 无重复代码（符合DRY原则）
- 一致的错误处理
- 完整的类型覆盖
- 清晰的工具描述

##### 3.2 构建与测试
- TypeScript：运行`npm run build`验证编译，使用`npx @modelcontextprotocol/inspector`通过MCP Inspector测试
- Python：运行`python -m py_compile your_server.py`验证语法，通过MCP Inspector测试

详细测试方法和质量检查清单参考对应语言指南

---

#### 阶段四：创建评估
实现完成后需要创建综合评估测试MCP服务器的有效性，完整指南参考 [✅ 评估指南](./reference/evaluation.md)

##### 4.1 评估目标
验证大模型能否有效使用你的MCP服务器回答真实复杂问题。

##### 4.2 创建10个评估问题流程
1. 工具检视：列出所有可用工具，明确能力范围
2. 内容探索：使用只读操作探索可用数据
3. 问题生成：创建10个复杂、真实的问题
4. 答案验证：自行解答每个问题验证答案正确性

##### 4.3 评估问题要求
每个问题需要满足：
- **独立**：不依赖其他问题
- **只读**：只需要非破坏性操作
- **复杂**：需要多次工具调用和深度探索
- **真实**：基于人类真实使用场景
- **可验证**：有单一清晰答案，可以通过字符串对比验证
- **稳定**：答案不会随时间变化

##### 4.4 输出格式
使用XML格式保存评估，示例：
```xml
<evaluation>
  <qa_pair>
    <question>Find discussions about AI model launches with animal codenames. One model needed a specific safety designation that uses the format ASL-X. What number X was being determined for the model named after a spotted wild cat?</question>
    <answer>3</answer>
  </qa_pair>
<!-- More qa_pairs... -->
</evaluation>
```

---

## 参考文件库
### 核心MCP文档（开发第一步加载）
- MCP协议：从站点地图 `https://modelcontextprotocol.io/sitemap.xml` 开始，添加`.md`后缀获取指定页面
- [📋 MCP最佳实践](./reference/mcp_best_practices.md)：通用MCP指南，包含：
  - 服务器和工具命名规范
  - 响应格式指南（JSON vs Markdown）
  - 分页最佳实践
  - 传输选择（可流式HTTP vs stdio）
  - 安全和错误处理标准

### SDK文档（阶段一/二加载）
- Python SDK：从 `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md` 获取
- TypeScript SDK：从 `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md` 获取

### 语言特定实现指南（阶段二加载）
- [🐍 Python 实现指南](./reference/python_mcp_server.md)：完整Python/FastMCP指南，包含：
  - 服务器初始化模式
  - Pydantic模型示例
  - `@mcp.tool`工具注册
  - 完整可运行示例
  - 质量检查清单
- [⚡ TypeScript 实现指南](./reference/node_mcp_server.md)：完整TypeScript指南，包含：
  - 项目结构
  - Zod schema模式
  - `server.registerTool`工具注册
  - 完整可运行示例
  - 质量检查清单

### 评估指南（阶段四加载）
- [✅ 评估指南](./reference/evaluation.md)：完整评估创建指南，包含：
  - 问题创建规范
  - 答案验证策略
  - XML格式规范
  - 示例问题与答案
  - 使用提供的脚本运行评估

---

## 冲突记录
