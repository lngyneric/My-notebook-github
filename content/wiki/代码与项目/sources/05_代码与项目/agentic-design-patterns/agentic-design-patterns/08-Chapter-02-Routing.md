---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/08-Chapter-02-Routing.md
raw_sha256: 444ae6285ed8748bc6d695d69289393f9112f3ea786d516e404f0db73822b323
compiled_at: 2026-04-14T03:58:07.347Z
---
# 智能体设计模式 - 路由（Routing）

> 来源路径：`raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/08-Chapter-02-Routing.md`

[[上一章：提示链|07-Chapter-01-Prompt-Chaining]] | [[首页|000-Home]] | [[下一章：并行化|09-Chapter-03-Parallelization]]

---

## TL;DR
路由（Routing）是智能体系统中实现动态决策的核心设计模式，它通过引入条件分支逻辑，让智能体不再沿固定线性流程执行，而是根据输入意图、环境状态等信息动态将请求分发到最合适的专业工具、子智能体或子流程。路由可通过基于大语言模型、向量嵌入、预定义规则、微调分类器四种方式实现，广泛应用于意图分类、任务调度、数据处理流水线等场景，是构建自适应、上下文感知智能体系统的基础能力。

---

## 路由模式概述
提示链虽然是执行确定性线性工作流的基础方法，但在需要自适应响应的场景下适用性有限。现实场景中，智能体系统往往需要根据环境状态、用户输入或上一步执行结果等情境信息，从多个可选方案中选择合适的行动路径，路由机制正是实现这种控制流分发的关键技术。

路由为智能体引入了条件分支能力，让系统从固定执行路径转变为动态评估选择后续动作的模式，可实现更灵活、更具上下文感知的系统行为。

### 举例：客户咨询智能体
具备路由能力的客户咨询智能体工作流程：
1. 分析用户的请求
2. 基于查询意图将其路由到相应处理路径：
   - 意图为「查订单」→ 调用订单查询子智能体/工具链
   - 意图为「问产品」→ 调用产品目录检索子智能体/工具链
   - 意图为「求技术支持」→ 查阅故障排除手册或转人工
   - 意图不明 → 转到澄清子智能体追问细节

### 常见路由实现方式
| 实现方式 | 原理 | 特点 |
|---------|------|------|
| **基于大语言模型的路由** | 通过提示词引导大模型分析输入，输出分类标识/下一步指令，系统根据输出导向对应路径 | 实现简单，可处理语义复杂的输入，依赖大模型推理 |
| **向量（嵌入）路由** | 将输入转换为向量嵌入，与不同路由的嵌入向量计算相似度，路由到相似度最高的路径 | 基于语义做决策，优于关键词匹配，适合语义路由场景 |
| **规则路由** | 基于关键词、模式或提取的结构化数据，通过预定义if-else/switch规则决策 | 速度快、结果确定，处理复杂语境/新颖输入时灵活性低 |
| **机器学习路由** | 使用标注数据训练专门的判别分类器，将路由逻辑编码在模型权重中 | 决策不依赖实时大模型推理，需要标注数据训练 |

路由可应用在智能体运行周期的多个节点：任务初始阶段分类、处理链中间点决策、子程序中工具选择等。LangChain、LangGraph、Google ADK 等框架都提供了实现路由的原生支持，其中 LangGraph 基于状态的图架构特别适合依赖系统累积状态的复杂路由场景。

---

## 实际应用场景
路由模式是自适应智能体系统的核心控制机制，应用覆盖多个领域：
1. **人机交互**：虚拟助手、AI家教中用于识别用户意图，选择对应工具/模块/人工，打破线性对话流程，实现上下文响应
2. **自动化数据/文档处理流水线**：对邮件、支持工单、API负载等输入按内容/元数据/格式分类，分发到对应工作流（如销售线索录入、不同格式数据转换、紧急问题升级）
3. **多智能体协作**：在包含多个专业智能体/工具的复杂系统中充当高级调度器，根据当前目标将任务分配给最合适的智能体（如AI编码助手先识别编程语言和用户意图，再分发到对应专业工具）

路由将智能体从预定义序列的静态执行者，转变为可在变化条件下选择最优任务完成方式的动态系统。

---

## 实战代码示例

### LangChain 实现
本示例使用 LangChain + Google Gemini 构建简单路由系统，协调器根据意图将请求分发到不同模拟子智能体处理器。

#### 依赖安装
```bash
pip install langchain langgraph google-cloud-aiplatform langchain-google-genai google-adk deprecated pydantic
```

需要提前配置对应大模型的 API 密钥环境变量。

```python
# Copyright (c) 2025 Marco Fago
#
# This code is licensed under the MIT License.
# See the LICENSE file in the repository for the full license text.

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableBranch

# --- Configuration ---
# Ensure your API key environment variable is set (e.g., GOOGLE_API_KEY)
# 确保你的 API 密钥环境变量已设置 (如 GOOGLE_API_KEY)
try:
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    print(f"Language model initialized: {llm.model}")
except Exception as e:
    print(f"Error initializing language model: {e}")
    llm = None

# --- Define Simulated Sub-Agent Handlers (equivalent to ADK sub_agents) ---
# --- 定义模拟的子智能体处理器 (等同于 ADK 中的 sub_agents) ---

def booking_handler(request: str) -> str:
    """Simulates the Booking Agent handling a request."""
    print("\n--- DELEGATING TO BOOKING HANDLER ---")
    return f"Booking Handler processed request: '{request}'. Result: Simulated booking action."

def info_handler(request: str) -> str:
    """Simulates the Info Agent handling a request."""
    print("\n--- DELEGATING TO INFO HANDLER ---")
    return f"Info Handler processed request: '{request}'. Result: Simulated information retrieval."

def unclear_handler(request: str) -> str:
    """Handles requests that couldn't be delegated."""
    print("\n--- HANDLING UNCLEAR REQUEST ---")
    return f"Coordinator could not delegate request: '{request}'. Please clarify."

# --- Define Coordinator Router Chain (equivalent to ADK coordinator's instruction) ---
# This chain decides which handler to delegate to.
# --- 定义协调员的路由链 (等同于 ADK 协调员的指令) ---
# 这个链负责决定将任务委派给哪个处理器。
coordinator_router_prompt = ChatPromptTemplate.from_messages([
    ("system", """Analyze the user's request and determine which specialist handler should process it.
     - If the request is related to booking flights or hotels, output 'booker'.
     - For all other general information questions, output 'info'.
     - If the request is unclear or doesn't fit either category, output 'unclear'.
     ONLY output one word: 'booker', 'info', or 'unclear'."""),
    ("user", "{request}")
])

if llm:
    coordinator_router_chain = coordinator_router_prompt | llm | StrOutputParser()

# --- Define the Delegation Logic (equivalent to ADK's Auto-Flow based on sub_agents) ---
# Use RunnableBranch to route based on the router chain's output.
# --- 定义委派逻辑 (等同于 ADK 基于 sub_agents 的自动流) ---
# 使用 RunnableBranch 根据路由链的输出进行路由。

# Define the branches for the RunnableBranch
# 为 RunnableBranch 定义分支
branches = {
    "booker": RunnablePassthrough.assign(output=lambda x: booking_handler(x['request']['request'])),
    "info": RunnablePassthrough.assign(output=lambda x: info_handler(x['request']['request'])),
    "unclear": RunnablePassthrough.assign(output=lambda x: unclear_handler(x['request']['request'])),
}

# Create the RunnableBranch. It takes the output of the router chain
# and routes the original input ('request') to the corresponding handler.
# 创建 RunnableBranch。它会接收路由链的输出，
# 并将原始输入 ('request') 路由到相应的处理器。
delegation_branch = RunnableBranch(
    (lambda x: x['decision'].strip() == 'booker', branches["booker"]), # Added .strip()
    (lambda x: x['decision'].strip() == 'info', branches["info"]),     # Added .strip()
    branches["unclear"] # Default branch for 'unclear' or any other output
)

# Combine the
