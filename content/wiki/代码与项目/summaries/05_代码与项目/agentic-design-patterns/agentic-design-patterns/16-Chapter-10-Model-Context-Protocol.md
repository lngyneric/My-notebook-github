---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/16-Chapter-10-Model-Context-Protocol.md
raw_sha256: b3d6b67a2211016200a74fc6bce39db7a39cba7b9db0cb7ddbb71300a4240ec2
compiled_at: 2026-04-24T07:39:45.469Z
---
<wiki>
# Chapter 10: Model Context Protocol | 第 10 章：模型上下文协议
[[15-Chapter-09-Learning-and-Adaptation|< Previous Chapter]] | [[000-Home|Home]] | [[17-Chapter-11-Goal-Setting-And-Monitoring|Next Chapter >]]

## Abstract | 摘要
To enable LLMs to function effectively as agents, their capabilities must extend beyond multimodal generation to support interaction with the external environment (e.g., accessing real-time data, utilizing external software, executing operational tasks). The Model Context Protocol (MCP) addresses this requirement by providing a standardized interface for LLMs to interface with external resources, serving as a core mechanism for consistent, predictable integration of external capabilities.
> 要让大语言模型成为高效的智能体，仅具备多模态生成能力是不够的，还需要支持与外部环境交互（如获取实时数据、调用外部软件、执行操作任务）。模型上下文协议（MCP）通过为大语言模型提供对接外部资源的标准化接口，实现一致、可预测的外部能力集成，是智能体系统的核心机制。

---

## 1. MCP Pattern Overview | MCP 模式概览
### Core Definition | 核心定义
MCP is an open standard that acts as a "universal adapter" for LLMs (e.g., Gemini, GPT, Mixtral, Claude) to connect with external systems, databases, and tools without custom per-integration development. It standardizes communication between LLMs and external applications, data sources, and tools, simplifying the process for LLMs to obtain context, execute actions, and interact with diverse systems.
> MCP 是一个开放标准，相当于大语言模型的「通用适配器」，无需为每个集成单独开发定制方案即可让各类大语言模型（如Gemini、GPT、Mixtral、Claude）接入外部系统、数据库和工具。它统一规范了大语言模型与外部应用、数据源、工具的通信方式，简化了大语言模型获取上下文、执行操作、与各类系统交互的过程。

### Architecture | 架构
MCP adopts a **client-server architecture** with three core elements exposed by MCP servers and consumed by MCP clients:
- **Resources**: Static data (e.g., PDF files, database records)
- **Prompts**: Interactive templates (essentially prompt engineering guides for LLM interaction)
- **Tools**: Executable functions for performing actions (e.g., sending emails, querying APIs)
MCP clients can be LLM host applications or AI agents themselves. This standardized approach drastically reduces the complexity of integrating LLMs into heterogeneous operational environments.
> MCP 采用**客户端-服务器架构**，MCP服务器对外提供三类核心元素供MCP客户端使用：
> - **资源**：静态数据（如PDF文件、数据库记录）
> - **提示词**：交互模板（本质上是指导LLM交互的提示工程规范）
> - **工具**：用于执行操作的可执行功能（如发送邮件、调用API）
> MCP客户端可以是LLM宿主应用或AI智能体本身，这种标准化架构极大降低了将LLM集成到异构运行环境的复杂度。

### Key Caveats | 关键注意事项
1. **Underlying API Optimization**: MCP is only a contract for agentic interfaces; its effectiveness depends heavily on the quality of underlying APIs. Wrapping unmodified legacy APIs may lead to suboptimal agent performance (e.g., slow, inaccurate ticket summarization from APIs that only support single-record queries). Underlying APIs should be enhanced with deterministic features (filtering, sorting) to support efficient operation of non-deterministic agents.
> 1. **底层API优化**：MCP只是智能体接口的协议规范，其实际效果很大程度上取决于底层API的设计质量。直接封装未修改的老旧API可能导致智能体性能不佳（例如，仅支持单条查询的API会导致工单汇总任务缓慢、不准确）。底层API应增加过滤、排序等确定性功能，以支持非确定性智能体的高效运行。

2. **Agent-Friendly Data Formats**: MCP does not guarantee that wrapped APIs have input/output formats understandable by agents. For example, a document store MCP server returning raw PDFs is useless if the agent cannot parse PDFs. Developers must prioritize agent-compatible data formats (e.g., Markdown text) alongside connection logic.
> 2. **智能体友好的数据格式**：MCP不保证封装的API的输入输出格式是智能体可理解的。例如，如果智能体无法解析PDF，返回原始PDF的文档存储MCP服务器就没有实用价值。开发者必须在连接逻辑之外，优先考虑智能体兼容的数据格式（如Markdown文本）。

---

## 2. MCP vs. Tool Function Calling | MCP 与工具函数调用
MCP and tool function calling are distinct mechanisms for extending LLM capabilities beyond text generation, with core differences outlined below:
> MCP和工具函数调用是两种扩展LLM能力、使其超越文本生成的不同机制，核心区别如下：

| Feature | Tool Function Calling | Model Context Protocol (MCP) |
|---------|------------------------|-------------------------------|
| Standardization | Proprietary, vendor-specific implementation with no cross-provider compatibility | Open, standardized protocol enabling interoperability across different LLMs and tools |
| Scope | Direct execution of specific, predefined functions | Broad framework for LLM-tool discovery and communication |
| Architecture | One-to-one interaction between LLM and application tool-handling logic | Client-server architecture supporting connections to multiple heterogeneous MCP servers |
| Discovery | Static tool list configured in conversation context | Dynamic, on-demand discovery of available tools/resources |
| Reusability | Tightly coupled to specific applications and LLM platforms | Supports standalone, reusable MCP servers accessible across platforms |

> | 特性 | 工具函数调用 | 模型上下文协议（MCP） |
> |------|--------------|------------------------|
> | 标准化程度 | 厂商专有实现，不同提供商之间无兼容性 | 开放的标准化协议，支持不同LLM与工具之间的互操作 |
> | 功能范围 | 直接执行特定预定义功能 | 覆盖LLM与工具发现、通信的完整框架 |
> | 架构 | LLM与应用工具处理逻辑之间的一对一交互 | 支持连接多个异构MCP服务器的客户端-服务器架构 |
> | 发现机制 | 会话上下文中静态配置的工具列表 | 动态、按需发现可用的工具/资源 |
> | 可复用性 | 与特定应用、LLM平台深度绑定 | 支持跨平台访问的独立、可复用MCP服务器 |

### Analogy | 类比
Tool function calling is equivalent to giving an AI a fixed set of custom tools (e.g., a specific wrench, screwdriver) efficient for simple, fixed-task scenarios. MCP is equivalent to a universal, standardized power outlet system that does not provide tools directly, but enables any compliant tool from any manufacturer to plug in and operate, supporting dynamic, scalable agent ecosystems.
> 工具函数调用相当于给AI一套固定的定制工具（如特定的扳手、螺丝刀），适合简单、固定任务的场景；MCP相当于一套通用、标准化的电源接口系统，本身不提供工具，但允许任何厂商生产的兼容工具接入运行，支持动态、可扩展的智能体生态。

### Usage Guideline | 使用指引
Tool function calling is sufficient for simple applications with a small, fixed set of predefined functions. MCP is essential for complex, interconnected AI systems that require adaptability, cross-platform interoperability, and dynamic capability discovery without redeployment.
> 对于功能简单、仅需少量固定预定义功能的应用，工具函数调用已足够；对于需要适应性、跨平台互操作、无需重新部署即可动态发现新能力的复杂互联AI系统，MCP是不可或缺的。

---

## 3. Additional Considerations for MCP | MCP 其他注意事项
### Core Component Differentiation | 核心组件区分
- **Resource**: Static data (e.g., files, database records)
- **Tool**: Executable function for performing actions
- **Prompt**: Template guiding structured, effective LLM interaction with resources/tools
> - **资源**：静态数据（如文件、数据库记录）
> - **工具**：用于执行操作的可执行功能
> - **提示词**：指导LLM与资源/工具进行结构化、高效交互的模板

### Key Non-Functional Requirements | 核心非功能需求
1. **Discoverability**: MCP clients can dynamically query servers to obtain available tool/resource lists at runtime, enabling agents to adapt to new capabilities without redeployment.
> 1. **可发现性**：MCP客户端可在运行时动态查询服务器获取可用的工具/资源列表，使智能体无需重新部署即可适配新能力。
2. **Security**: MCP implementations must include authentication and authorization controls to restrict client access to specific servers and actions.
> 2. **安全性**：MCP实现必须包含身份验证和权限控制，限制客户端对特定服务器和操作的访问。
3. **Implementation Complexity**: While MCP is an open standard, implementation can be complex.
