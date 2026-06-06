---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/14-Chapter-08-Memory-Management.md
raw_sha256: ca45097dd643ef2165f4ae292f1ead8d1e6f4ae569f0be8a60ca2046846f8194
compiled_at: 2026-04-14T03:59:53.894Z
---
# 记忆管理（Memory Management）智能体设计模式

> 来源路径：`raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/14-Chapter-08-Memory-Management.md`

---

## TL;DR

记忆管理是智能体实现持续智能行为的核心基础机制，通常采用**短期记忆（上下文记忆）+ 长期记忆（持久记忆）**的双组件架构：短期记忆负责存储单次交互的即时上下文，受大语言模型上下文窗口容量限制；长期记忆借助外部存储（通常为向量数据库）实现跨会话的持久知识存储与语义检索。主流智能体框架都提供了标准化的记忆管理组件，支持开发者快速实现智能体的上下文维护、个性化交互、经验学习能力。

---

## 目录
- [核心概念](#核心概念)
- [记忆分类](#记忆分类)
  - [短期记忆（上下文记忆）](#短期记忆上下文记忆)
  - [长期记忆（持久记忆）](#长期记忆持久记忆)
- [实际应用场景](#实际应用场景)
- [框架实现：Google ADK](#框架实现google-adk)
  - [核心概念](#adk核心概念)
  - [Session 会话管理](#session-会话管理)
  - [State 状态管理](#state-状态管理)
  - [Memory 长期记忆管理](#memory-长期记忆管理)
- [框架实现：LangChain & LangGraph](#框架实现langchain--langgraph)
  - [短期记忆实现](#短期记忆实现-1)
  - [长期记忆实现](#长期记忆实现-1)
- [托管服务：Vertex Memory Bank](#托管服务vertex-memory-bank)
- [经验法则](#经验法则)
- [核心要点](#核心要点)
- [参考文献](#参考文献)

---

## 核心概念

在智能体系统中，**记忆**指智能体从过往交互、观察和学习经验中保留并利用信息的能力。这一能力使智能体能够做出明智决策、维持对话上下文，并持续改进，是智能体超越简单单次问答、实现复杂任务处理的必要基础。

智能体记忆通常分为两大主要类型：短期记忆（上下文记忆）和长期记忆（持久记忆）。

---

## 记忆分类

### 短期记忆（上下文记忆）
类似于人类的工作记忆，存储当前正在处理或近期访问的信息：
- 对于基于大语言模型（LLM）的智能体，短期记忆主要存在于上下文窗口内，包含最近的对话消息、智能体回复、工具调用结果、当前交互反思内容，为后续响应和决策提供上下文支撑
- 上下文窗口容量有限，会限制智能体可直接访问的近期信息范围，需要通过总结旧对话、突出关键信息等方式优化管理
- 长上下文模型仅扩大了短期记忆容量，本质仍然是临时存储，会话结束后即丢失，且全量处理的成本高、效率低

### 长期记忆（持久记忆）
充当长期知识库，用于存储智能体在各种交互、任务或长时间跨度内需要保留的信息：
- 数据通常存储在智能体运行时环境之外，常见载体包括数据库、知识图谱、向量数据库
- 向量数据库中，信息会被转换为数值向量存储，支持基于语义相似性而非精确关键词匹配的语义搜索
- 需要使用时，智能体会查询外部存储，检索相关数据并整合到短期上下文中，结合先验知识与当前交互完成决策

---

## 实际应用场景

| 应用场景 | 短期记忆作用 | 长期记忆作用 |
|---------|-------------|-------------|
| 聊天机器人和对话式AI | 维持对话流程，连贯响应用户输入 | 记忆用户偏好、历史问题，提供个性化连续交互 |
| 任务导向型智能体 | 跟踪已完成步骤、当前进度、总体目标 | 访问非当前上下文的用户特定数据 |
| 个性化体验服务 | 维护当前交互流程 | 存储调用用户偏好、历史行为、个人信息，动态调整响应策略 |
| 学习与性能优化 | 处理当前学习任务 | 存储成功策略、错误经验、新知识，支撑未来自适应优化 |
| 信息检索（RAG） | 整合检索结果生成响应 | 作为外部知识库，提供检索来源 |
| 自主控制系统（机器人/自动驾驶） | 处理实时周边环境信息 | 存储地图、路线、通用环境知识、习得行为模式 |

---

## 框架实现：Google ADK

Google ADK 提供了结构化的记忆管理组件，通过三个核心概念分层实现短期和长期记忆管理：

### ADK核心概念
| 组件 | 作用 |
|-----|------|
| `Session`（会话） | 独立的聊天线程，记录特定交互的消息、动作（事件），同时存储该对话相关的临时数据 |
| `State`（状态，`session.state`） | 存储在会话内部的数据，仅包含当前活跃聊天会话相关的上下文信息 |
| `Memory`（记忆） | 可检索的信息知识库，数据来源包括历史聊天和外部数据源，支撑当前对话之外的信息检索 |

ADK 提供两个专用服务管理核心组件：
- `SessionService`：管理聊天会话（`Session` 对象）的生命周期，包括创建、记录、终止
- `MemoryService`：负责长期知识（`Memory`）的存储与检索

两种服务都支持多种存储配置：内存存储适用于测试（重启后数据不保留），也支持数据库、云服务实现生产级持久化与可扩展性。

---

### Session 会话管理
ADK 的 `Session` 对象（`google.adk.sessions.Session`）用于跟踪管理独立聊天线程，对话开始时由 `SessionService` 生成，封装了对话的全量相关数据：唯一标识符、按时间排序的事件列表、状态存储区、最后更新时间戳。

ADK 内置多种 `SessionService` 实现：
#### 1. InMemorySessionService（测试用）
```python
# 示例：使用 InMemorySessionService
# 注意：数据不会持久化，应用重启后会丢失，仅适用于本地开发和测试环境。
from google.adk.sessions import InMemorySessionService
session_service = InMemorySessionService()
```

#### 2. DatabaseSessionService（自托管持久化）
```python
# 示例：使用 DatabaseSessionService
# 这适用于需要持久存储的生产环境或开发环境。
# 你需要配置数据库 URL（例如，用于 SQLite、PostgreSQL 等）。
# 安装依赖：pip install google-adk[sqlalchemy] 和数据库驱动（例如，PostgreSQL 的 psycopg2）
from google.adk.sessions import DatabaseSessionService
# 使用本地 SQLite 文件的示例：
db_url = "sqlite:///./my_agent_data.db"
session_service = DatabaseSessionService(db_url=db_url)
```

#### 3. VertexAiSessionService（GCP 生产可扩展部署）
```python
# 示例：使用 VertexAiSessionService
# 这适用于 Google Cloud Platform 上需要可扩展性的生产环境，利用 Vertex AI 基础设施进行会话管理。
# 安装依赖：pip install google-adk[vertexai] 以及 GCP 设置/身份验证
from google.adk.sessions import VertexAiSessionService

PROJECT_ID = "your-gcp-project-id" # 替换为你的 GCP 项目 ID
LOCATION = "us-central1" # 替换为你所需的 GCP 位置
# 与此服务一起使用的 app_name 应对应于 Reasoning Engine ID 或名称
REASONING_ENGINE_APP_NAME = "projects/your-gcp-project-id/locations/us-central1/reasoningEngines/your-engine-id" # 替换为你的 Reasoning Engine 资源名称

session_service = VertexAiSessionService(project=PROJECT_ID, location=LOCATION)
# 使用此服务时，将 REASONING_ENGINE_APP_NAME 传递给以下方法：
# session_service.create_session(app_name=REASONING_ENGINE_APP_NAME, ...)
# session_service.get_session(app_name=REASONING_ENGINE_APP_NAME, ...)
# session_service.append_event(session, event, app_name=REASONING_ENGINE_APP_NAME)
# session_service.delete_session(app_name=REASONING_ENGINE_APP_NAME, ...)
```

消息交互的标准生命周期流程：
1. 接收用户消息
2. `Runner` 通过 `SessionService` 检索或创建对应 `Session`
3. 智能体利用 `Session` 的上下文（状态+历史交互）处理消息
4. 智能体生成响应并更新状态
5. `Runner` 封装为 `Event`，调用 `session_service.append_event()` 记录事件并更新存储中的状态
6. `Session` 等待下一条消息，交互结束后调用 `delete_session` 终止会话

---

### State 状态管理
每个 `Session` 都包含 `state` 组件，是智能体在当前对话期间的临时
