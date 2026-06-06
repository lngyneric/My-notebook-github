---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/30-Appendix-C.md
raw_sha256: b1b410ef04020fb1292606f422a1eba53f1e334d746f501bef049b1bf936de59
compiled_at: 2026-04-24T08:09:53.567Z
---
<wiki>
# Appendix C: Quick Overview of Agentic Frameworks | <mark>附录 C：智能体框架快速概览</mark>

## Navigation
[[29-Appendix-B|< Previous Chapter]] | [[000-Home|Home]] | [[31-Appendix-D|Next Chapter >]]

## Summary
This appendix provides a comprehensive, comparative overview of popular agentic development frameworks, outlining their core architectures, primary use cases, relative strengths, tradeoffs, and practical code examples. It covers tools spanning the full abstraction spectrum, from low-level libraries for defining agent internal logic to high-level platforms for orchestrating collaborative multi-agent systems, to help developers select the optimal tool for their project requirements.

## Key Takeaways
- Agentic frameworks exist on a continuum of abstraction, with low-level libraries offering granular control over agent logic and high-level platforms streamlining multi-agent orchestration via opinionated patterns.
- LangChain is designed for simple, predictable linear workflows modeled as Directed Acyclic Graphs (DAGs), using its LangChain Expression Language (LCEL) to chain components together.
- LangGraph extends LangChain to support stateful, cyclical workflows, enabling advanced agent capabilities such as reasoning, planning, retries, and multi-agent coordination.
- High-level frameworks such as Google ADK and CrewAI abstract low-level control flow management, instead focusing on structured team-based agent collaboration patterns.
- Specialized frameworks cater to niche use cases, including data retrieval for RAG (LlamaIndex), enterprise-grade search (Haystack), SOP-driven task execution (MetaGPT), and enterprise codebase integration (Semantic Kernel).
- Framework selection depends on core workflow requirements: use LangChain for linear sequences, LangGraph for dynamic reasoning loops, and high-level orchestration platforms for structured multi-agent teams.

## Framework Deep Dives
### LangChain
LangChain is a framework for developing applications powered by LLMs. Its core strength lies in its LangChain Expression Language (LCEL), which allows you to "pipe" components together into a chain. This creates a clear, linear sequence where the output of one step becomes the input for the next. It's built for workflows that are Directed Acyclic Graphs (DAGs), meaning the process flows in one direction without loops.
<mark>LangChain是用于开发基于大语言模型(LLM)的应用程序框架。它的核心优势在于其LangChain表达式语言(LCEL)，该语言允许您将组件“串联”成链。这创建了清晰的线性序列，其中上一步的输出成为下一步的输入。它专为有向无环图(DAG)工作流而设计，这意味着流程沿一个方向流动，没有循环。</mark>

#### Use Cases <mark>用途：</mark>
-  **Simple RAG**: Retrieve a document, create a prompt, get an answer from an LLM.
<mark>简单 RAG：检索文档，创建提示，从LLM获取答案。</mark>
-  **Summarization**: Take user text, feed it to a summarization prompt, and return the output.
<mark>摘要：获取用户文本，将其输入摘要提示，并返回输出结果。</mark>
-  **Extraction**: Extract structured data (like JSON) from a block of text.
<mark>提取：从文本块中提取结构化数据（例如JSON）。</mark>

#### Code Example
```python
# A simple LCEL chain conceptually
# (This is not runnable code, just illustrates the flow)
chain = prompt | model | output_parse
```

---

### LangGraph
LangGraph is a library built on top of LangChain to handle more advanced agentic systems. It allows you to define your workflow as a graph with nodes (functions or LCEL chains) and edges (conditional logic). Its main advantage is the ability to create cycles, allowing the application to loop, retry, or call tools in a flexible order until a task is complete. It explicitly manages the application state, which is passed between nodes and updated throughout the process.
<mark>LangGraph是基于LangChain构建的库，用于处理更高级的智能体系统。它允许您将工作流定义为图，该图由节点（函数或LCEL链）和边（条件逻辑）组成。其主要优势在于能够创建循环，从而允许应用程序以灵活的顺序循环、重试或调用工具，直到任务完成。它显式地管理应用程序状态，该状态在节点之间传递并在整个过程中更新。</mark>

#### Use Cases <mark>用途：</mark>
-  **Multi-agent Systems**: A supervisor agent routes tasks to specialized worker agents, potentially looping until the goal is met.
<mark>多智能体系统：主管智能体将任务分配给专门的工作智能体，可能会循环执行，直到达到目标。</mark>
-  **Plan-and-Execute Agents**: An agent creates a plan, executes a step, and then loops back to update the plan based on the result.
<mark>计划执行智能体：智能体创建计划，执行步骤，然后循环返回并根据结果更新计划。</mark>
-  **Human-in-the-Loop**: The graph can wait for human input before deciding which node to go to next.
<mark>人机交互：该图可以等待人工输入，然后再决定下一步要访问哪个节点。</mark>

#### LangChain vs LangGraph Comparison
| Feature | LangChain | LangGraph |
|---------|------|------|
| Core Abstraction | Chain (using LCEL) | Graph of Nodes |
| Workflow Type | Linear (Directed Acyclic Graph) | Cyclical (Graphs with loops) |
| State Management | Generally stateless per run | Explicit and persistent state object |
| Primary Use | Simple, predictable sequences | Complex, dynamic, stateful agents |

#### Selection Guidance <mark>你应该使用哪一个？</mark>
-  Choose LangChain when your application has a clear, predictable, and linear flow of steps. If you can define the process from A to B to C without needing to loop back, LangChain with LCEL is the perfect tool.
<mark>如果您的应用流程清晰、可预测且呈线性发展，那么LangChain是您的理想之选。如果您可以定义从A到B、再到C的完整流程而无需循环，那么LangChain与LCEL结合使用将是您的完美选择。</mark>
-  Choose LangGraph when you need your application to reason, plan, or operate in a loop. If your agent needs to use tools, reflect on the results, and potentially try again with a different approach, you need the cyclical and stateful nature of LangGraph.
<mark>当您的应用程序需要进行推理、规划或循环操作时，请选择LangGraph。如果您的智能体需要使用工具、反思结果，并可能尝试不同的方法，那么您就需要LangGraph的循环性和有状态特性。</mark>

#### Code Example
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
parallel_builder.add_edge("call_llm_1", "aggregator
