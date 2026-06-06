---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/22-Chapter-16-Resource-Aware-Optimization.md
raw_sha256: bf5585039eecb0e46ef73d2ab29705e5eb3fd3958cf050bf5620154b772fae6a
compiled_at: 2026-04-14T04:02:52.777Z
---
# 资源感知优化（Resource-Aware Optimization）

> 本页内容编译自 `raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/22-Chapter-16-Resource-Aware-Optimization.md`

## TL;DR
资源感知优化是智能体的设计模式，让智能体能够在运行过程中动态监控、分配计算、时间、财务等资源，在指定资源约束内实现目标，平衡输出质量与运行成本，核心是根据任务复杂度动态选择合适的模型/工具，常用路由智能体+评论智能体的多智能体架构实现。

---

## 目录
- [定义与核心概念](#定义与核心概念)
- [实际应用场景](#实际应用场景)
- [典型架构实现](#典型架构实现)
  - [Google ADK 示例（Gemini 系列）](#google-adk-示例gemini-系列)
  - [OpenAI 可运行实现示例](#openai-可运行实现示例)
  - [OpenRouter 原生支持](#openrouter-原生支持)
- [更多优化技术](#更多优化技术)
- [要点速览](#要点速览)
- [核心要点](#核心要点)
- [参考资料](#参考资料)

---

## 定义与核心概念

资源感知优化使智能体能够在运行过程中动态监控和管理计算、时间和财务资源。这和仅关注动作序列的简单规划不同，它要求智能体在执行动作时决策，以在指定资源预算内实现目标或优化效率。典型场景包括：在更准确但昂贵的模型与更快速低成本的模型之间做选择，或是决策是否为更精细的响应分配额外计算，还是返回更快但不够详细的答案。

> [!example] 典型示例
> 为金融分析师分析大型数据集的智能体：如果分析师需要立即拿到初步报告，智能体可使用更快更便宜的模型快速总结关键趋势；如果分析师需要为关键投资决策提供高精度预测，且有更大预算和更多时间，智能体就会分配更多资源，使用强大、更慢但更精确的预测模型。
>
> 该模式的核心策略之一是**后备机制**：当首选模型因过载、限流不可用时，系统自动切换到默认或更便宜的模型，维持服务连续性实现优雅降级，不会完全失败。

---

## 实际应用场景

| 应用场景 | 说明 |
|---------|------|
| 成本优化的LLM使用 | 智能体根据预算约束，决定用大型昂贵LLM处理复杂任务，还是小型便宜LLM处理简单查询 |
| 延迟敏感操作 | 在实时系统中，智能体选择更快但可能不够全面的推理路径，保证响应及时性 |
| 能源效率优化 | 部署在边缘设备或电力受限场景的智能体，优化处理过程节省电池寿命 |
| 服务可靠性后备 | 主选项不可用时自动切换到备份模型，保证服务连续性和优雅降级 |
| 数据使用管理 | 选择摘要数据检索而非下载完整数据集，节省带宽和存储空间 |
| 自适应任务分配 | 多智能体系统中，智能体根据当前计算负载、可用时间自行分配任务 |

---

## 典型架构实现

资源感知优化最常用的实现是「路由智能体分类任务+不同能力模型处理+评论智能体优化路由逻辑」的多智能体架构。

### Google ADK 示例（Gemini 系列）

以旅行规划器场景为例：
1. 高层规划需要理解复杂用户请求、拆解为多步骤行程、做逻辑决策，由能力更强的 `Gemini Pro` 处理（规划器智能体）
2. 规划完成后，查找航班价格、检查酒店可用性、搜索餐厅评论这类简单重复的工具调用，由更快更便宜的 `Gemini Flash` 处理

Google ADK 原生支持这种多智能体架构，允许模块化可扩展开发，支持直接使用各类 Gemini 模型，也可通过 LiteLLM 集成第三方模型，其编排能力支持动态LLM路由实现自适应行为，内置评估能力支持系统优化。

#### 定义分级智能体示例代码（概念代码，不可直接运行）
```python
# Conceptual Python-like structure, not runnable code

from google.adk.agents import Agent
# from google.adk.models.lite_llm import LiteLlm # If using models not directly supported by ADK's default Agent

# Agent using the more expensive Gemini Pro 2.5
gemini_pro_agent = Agent(
   name="GeminiProAgent",
   model="gemini-2.5-pro", # Placeholder for actual model name if different
   description="A highly capable agent for complex queries.",
   instruction="You are an expert assistant for complex problem-solving."
)

# Agent using the less expensive Gemini Flash 2.5
gemini_flash_agent = Agent(
   name="GeminiFlashAgent",
   model="gemini-2.5-flash", # Placeholder for actual model name if different
   description="A fast and efficient agent for simple queries.",
   instruction="You are a quick assistant for straightforward questions."
)
```

#### 路由智能体（Router Agent）
路由智能体负责根据查询复杂度将请求转发给合适的下游模型：
- 简单实现可基于查询长度等指标：短查询走便宜模型，长查询走能力更强的模型
- 更复杂的实现可使用LLM/ML模型分析查询的细微差异和复杂度，提升分类准确性，还可通过提示调优、微调进一步提升路由效果

##### 基于长度的路由智能体示例代码（概念代码，不可直接运行）
```python
# Conceptual Python-like structure, not runnable code

from google.adk.agents import Agent, BaseAgent
from google.adk.events import Event
from google.adk.agents.invocation_context import InvocationContext
import asyncio

class QueryRouterAgent(BaseAgent):
   name: str = "QueryRouter"
   description: str = "Routes user queries to the appropriate LLM agent based on complexity."

   async def _run_async_impl(self, context: InvocationContext) -> AsyncGenerator[Event, None]:
       user_query = context.current_message.text # Assuming text input
       query_length = len(user_query.split()) # Simple metric: number of words

       if query_length < 20: # Example threshold for simplicity vs. complexity
           print(f"Routing to Gemini Flash Agent for short query (length: {query_length})")
           # In a real ADK setup, you would 'transfer_to_agent' or directly invoke
           # For demonstration, we'll simulate a call and yield its response
           response = await gemini_flash_agent.run_async(context.current_message)
           yield Event(author=self.name, content=f"Flash Agent processed: {response}")
       else:
           print(f"Routing to Gemini Pro Agent for long query (length: {query_length})")
           response = await gemini_pro_agent.run_async(context.current_message)
           yield Event(author=self.name, content=f"Pro Agent processed: {response}")
```

#### 评论智能体（Critique Agent）
评论智能体负责评估回答智能体的输出质量，提供反馈实现：
1. 自我修正：识别错误和不一致，促使回答智能体优化输出
2. 性能监控：跟踪准确性、相关性等指标，用于系统优化
3. 优化路由逻辑：持续识别次优路由（比如简单查询走了大模型、复杂查询走了小模型），为路由逻辑调整提供信息，间接实现预算管理

可配置为仅审查生成文本，或同时审查原始查询和生成文本，保证响应符合原始问题需求。

##### 评论智能体系统提示示例
```python
CRITIC_SYSTEM_PROMPT = """
You are the **Critic Agent**, serving as the quality assurance arm of our collaborative research assistant system. Your primary function is to **meticulously review and challenge** information from the Researcher Agent, guaranteeing **accuracy, completeness, and unbiased presentation**.
Your duties encompass:
* **Assessing research findings** for factual correctness, thoroughness, and potential leanings.
* **Identifying any missing data** or inconsistencies in reasoning.
* **Raising critical questions** that could refine or expand the current understanding.
* **Offering constructive suggestions** for enhancement or exploring different angles.
* **Validating that the final output is comprehensive** and balanced.
All criticism must be constructive. Your goal is to fortify the research, not invalidate it. Structure your feedback clearly, drawing attention to specific points for revision. Your overarching aim is to ensure the final research product meets the highest possible quality standards.
"""
```

---

### OpenAI 可运行实现示例

该实现将用户查询分为三类，分别匹配不同的处理路径和模型，完整可运行代码见 [GitHub 仓库](https://github.com/mahtabsyed/21-Agentic-Patterns/blob/main/16_Resource_Aware_Opt_LLM_Reflection_v2.ipyn
