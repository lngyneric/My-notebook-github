---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/30-Appendix-C.md
raw_sha256: b1b410ef04020fb1292606f422a1eba53f1e334d746f501bef049b1bf936de59
compiled_at: 2026-04-14T04:04:34.278Z
---
# 附录 C：智能体框架快速概览
> 来源路径：`raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/30-Appendix-C.md`

---

## TL;DR
智能体开发框架按抽象层级和能力定位形成了清晰的生态分层：底层框架（如LangChain）提供基础组件实现线性DAG工作流，中层扩展框架（如LangGraph）支持带循环的有状态复杂推理，高层编排框架（如Google ADK、CrewAI）专注于多智能体协作调度，还有大量垂直领域专用框架满足不同场景需求。开发者选择框架的核心权衡是：基于图的框架提供细粒度控制，更规范的高层框架提供更流畅的开发体验，需根据项目对流程灵活性、开发效率的要求选择对应抽象层级的工具。

---

## 目录
- [LangChain](#langchain)
- [LangGraph](#langgraph)
- [LangChain vs LangGraph 对比](#langchain-vs-langgraph-对比)
- [Google ADK](#google-adk)
- [CrewAI](#crewai)
- [其他智能体开发框架](#其他智能体开发框架)
- [结语](#结语)
- [参考文献](#参考文献)

---

## LangChain
### 要点
- 定位：开发大语言模型驱动应用的基础框架
- 核心优势：LangChain表达式语言(LCEL)支持将组件串联为链，形成清晰线性流程
- 适配场景：有向无环图(DAG)类型的工作流，流程单向流动无循环

### 适用场景
| 场景 | 说明 |
|------|------|
| 简单RAG | 检索文档 → 构造提示 → LLM生成回答 |
| 文本摘要 | 输入用户文本 → 摘要提示 → 返回输出 |
| 结构化提取 | 从文本块中提取JSON等结构化数据 |

### 代码示例
```python
# A simple LCEL chain conceptually
# (This is not runnable code, just illustrates the flow)
chain = prompt | model | output_parse
```

---

## LangGraph
### 要点
- 定位：基于LangChain构建的高级智能体系统库
- 核心能力：支持将工作流定义为「节点（函数/LCEL链）+ 边（条件逻辑）」组成的图，支持创建循环，可灵活循环、重试、乱序调用工具直到任务完成
- 状态管理：显式管理在节点间传递、全程更新的应用状态

### 适用场景
| 场景 | 说明 |
|------|------|
| 多智能体系统 | 主管智能体向专业工作智能体分发任务，循环执行直到达成目标 |
| 计划执行智能体 | 智能体创建计划 → 执行步骤 → 循环返回根据结果更新计划 |
| 人机交互 | 流程可暂停等待人工输入，再决定下一步走向 |

### 代码示例
```python
# Graph state
class State(TypedDict):
   topic: str
   joke: str
   story: str
   poem: str
   combined_output: str

# Nodes
def call_llm_1(state: State):
   """First LLM call to generate initial joke"""

   msg = llm.invoke(f"Write a joke about {state['topic']}")
   return {"joke": msg.content}

def call_llm_2(state: State):
   """Second LLM call to generate story"""

   msg = llm.invoke(f"Write a story about {state['topic']}")
   return {"story": msg.content}

def call_llm_3(state: State):
   """Third LLM call to generate poem"""

   msg = llm.invoke(f"Write a poem about {state['topic']}")
   return {"poem": msg.content}

def aggregator(state: State):
   """Combine the joke and story into a single output"""

   combined = f"Here's a story, joke, and poem about {state['topic']}!\n\n"
   combined += f"STORY:\n{state['story']}\n\n"
   combined += f"JOKE:\n{state['joke']}\n\n"
   combined += f"POEM:\n{state['poem']}"
   return {"combined_output": combined}

# Build workflow
parallel_builder = StateGraph(State)

# Add nodes
parallel_builder.add_node("call_llm_1", call_llm_1)
parallel_builder.add_node("call_llm_2", call_llm_2)
parallel_builder.add_node("call_llm_3", call_llm_3)
parallel_builder.add_node("aggregator", aggregator)

# Add edges to connect nodes
parallel_builder.add_edge(START, "call_llm_1")
parallel_builder.add_edge(START, "call_llm_2")
parallel_builder.add_edge(START, "call_llm_3")
parallel_builder.add_edge("call_llm_1", "aggregator")
parallel_builder.add_edge("call_llm_2", "aggregator")
parallel_builder.add_edge("call_llm_3", "aggregator")
parallel_builder.add_edge("aggregator", END)
parallel_workflow = parallel_builder.compile()

# Show workflow
display(Image(parallel_workflow.get_graph().draw_mermaid_png()))

# Invoke
state = parallel_workflow.invoke({"topic": "cats"})
print(state["combined_output"])
```

---

## LangChain vs LangGraph 对比
| 特性 | LangChain | LangGraph |
|---------|------|------|
| 核心抽象 | 基于LCEL的链 | 节点组成的图 |
| 工作流类型 | 线性（有向无环图） | 循环（支持循环的图） |
| 状态管理 | 单次运行通常无状态 | 显式持久化状态对象 |
| 主要用途 | 简单可预测的步骤序列 | 复杂动态有状态智能体 |

### 选择标准
- 选LangChain：应用流程清晰可预测，是无需回循环的线性流程（A→B→C）
- 选LangGraph：应用需要推理、规划或循环操作，智能体需要使用工具、反思结果、尝试不同方法

---

## Google ADK
### 要点
- 定位：Google推出的高级结构化框架，用于构建部署多交互AI智能体组成的应用
- 核心特点：相比LangChain/LangGraph更偏向规范性、面向生产，专注于协调智能体协作，而非提供智能体内部逻辑的基础构建块
- 抽象层级：封装了底层图构建工作，提供预构建的多智能体交互架构模式，内置`SequentialAgent`/`ParallelAgent`等智能体类型自动管理控制流；围绕智能体「团队」架构设计，主智能体向子智能体委派任务，状态和会话管理由框架隐式处理，比LangGraph的显式传参更统一但粒度更粗

> 类比：LangGraph提供设计单个机器人/机器团队详细线路的工具，Google ADK提供工厂流水线，可直接构建管理已经会协同的机器人集群

### 代码示例
```python
from google.adk.agents import LlmAgent
from google.adk.tools import google_Search

dice_agent = LlmAgent(
   model="gemini-2.0-flash-exp", 
   name="question_answer_agent",
   description="A helpful assistant agent that can answer questions.",
   instruction="""Respond to the query using google search""",
   tools=[google_search],
)
```
> 代码说明：创建搜索增强型智能体，收到问题后会调用谷歌搜索获取实时网络信息，再基于信息构造回答。

---

## CrewAI
### 要点
- 定位：专注于多智能体系统协作编排的框架，核心围绕协作角色和结构化流程，抽象层级高于基础工具包，用类人类团队的概念模型开发
- 核心组件：
  1. **智能体(Agent)**：除功能外，还通过角色、目标、背景故事定义人设，指导行为和沟通风格
  2. **任务(Task)**：独立工作单元，有清晰描述和预期输出，绑定到特定智能体
  3. **团队(Crew)**：包含所有智能体和任务的整体单元，执行预定义流程：支持顺序式（上一个任务输出作为下一个输入）、层级式（经理类智能体委派任务协调工作流）两种模式
- 定位差异：摒弃LangGraph底层显式状态管理和控制流，开发者不需要连接每个节点和条件边，只需要设计团队规则；Google ADK是覆盖全智能体生命周期的面向生产平台，CrewAI则专注于智能体协作逻辑和专家团队模拟。

### 代码示例
```python
