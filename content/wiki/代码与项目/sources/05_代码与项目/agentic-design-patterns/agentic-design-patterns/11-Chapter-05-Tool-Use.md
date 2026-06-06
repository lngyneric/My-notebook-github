---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/11-Chapter-05-Tool-Use.md
raw_sha256: 24b9f78e871eb8147780c89b4550ca8f053dcd5c1dcf6a85979793d142647fd9
compiled_at: 2026-04-14T03:58:56.820Z
---
# 工具使用（函数调用） | Tool Use (Function Calling)
> 来源路径：`raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/11-Chapter-05-Tool-Use.md`

[[上一章：第四章 反思|< 10-Chapter-04-Reflection]] | [[返回首页|000-Home]] | [[下一章：第六章 规划|12-Chapter-06-Planning >]]

---

## TL;DR
工具使用（通常通过函数调用机制实现）是智能体的核心基础模式，它突破了大语言模型的训练数据限制，让大语言模型能够与外部世界交互：通过向大语言模型描述可用工具，让大语言模型自主判断是否需要调用工具、生成结构化调用请求，再由智能体框架执行工具、将结果返回给大语言模型生成最终响应，最终让智能体能够获取实时信息、执行计算、操作外部系统，完成真实世界任务。

---

## 工具使用模式概述
到目前为止，我们讨论的智能体模式侧重于在大语言模型之间协调交互和管理智能体内部的信息流（如提示链、路由、并行化和反思模式）。但如果要让智能体真正有用、能与现实世界或外部系统交互，就必须赋予它们使用工具的能力。

工具使用模式通常通过函数调用（Function Calling）机制实现，使智能体能够与外部 API、数据库、服务交互，甚至直接执行代码。它允许作为智能体核心的大语言模型根据用户请求或当前任务状态，来决定何时以及如何使用特定的外部函数。

工具调用的典型流程分为6步：
1. **工具定义**：向大语言模型描述外部函数或功能，包括函数的用途、名称，以及所接受参数的类型和说明。
2. **大语言模型决策**：大语言模型接收用户的请求和可用的工具定义，并根据对两者的理解判断是否需要调用一个或多个工具来完成请求。
3. **生成函数调用**：如果大语言模型决定使用工具，它会生成结构化输出（通常是 JSON 对象），指明要调用的工具名称以及从用户请求中提取的参数。
4. **工具执行**：智能体框架或编排层捕获这个结构化输出，识别要调用的工具，并根据给定参数执行相应的外部函数。
5. **观察/结果**：工具执行的输出或结果返回给智能体。
6. **大语言模型处理（可选，但很常见）**：大语言模型接收工具的输出作为上下文，并用它来生成对用户的最终回复，或决定工作流的下一步（可能涉及调用另一个工具、进行反思或提供最终答案）。

这种模式是智能体能力的基础，因为它突破了大语言模型训练数据的局限，使其能够获取最新信息、执行内部无法处理的计算、访问用户特定的数据，或触发现实世界的动作。函数调用是连接大语言模型推理能力与外部功能的技术桥梁。

> [!NOTE]
> 虽然「函数调用」这个说法确实能准确描述调用预定义代码函数的过程，但从更广阔的视角理解「工具调用」这一概念更为有益：工具可以是传统函数、复杂的 API 接口、数据库请求，甚至是发给另一个专用智能体的指令，这种视角能更好地体现智能体作为编排者，在多样化数字资源和智能生态中调度能力的潜力。

LangChain、LangGraph 和 Google ADK 等框架可以很方便地定义工具并将它们集成到智能体工作流中，通常会利用 Gemini 或 OpenAI 等现代大语言模型的原生函数调用功能。在这些框架中，你只需要定义工具，再配置让智能体识别和使用这些工具即可。

工具使用是构建强大、可交互且能感知和利用外部资源的智能体的关键模式。

---

## 实际应用场景
当智能体需要的不只是文本生成，而是执行操作或检索动态信息的时候，工具使用模式几乎都能派上用场，典型场景包括：

### 1. 从外部来源获取信息
获取大语言模型训练数据中未包含的实时数据或信息。
- **用例**：天气信息智能体
- **工具**：天气查询接口，可输入地点并返回该地的实时天气
- **智能体流程**：用户提问「伦敦天气怎么样？」，大语言模型识别出需要使用天气工具，并使用「伦敦」作为参数调用该工具，工具返回数据后，大语言模型将这些信息整理并以易懂的方式输出给用户。

### 2. 与数据库和接口交互
对结构化数据执行查询、更新或其他操作。
- **用例**：电商平台智能体
- **工具**：通过接口来检查产品库存、查询订单状态或处理支付
- **智能体流程**：用户提问「产品 X 有货吗？」，大语言模型先调用库存接口，工具返回库存数量后，大语言模型向用户反馈该产品库存情况。

### 3. 执行计算和数据分析
使用计算器、数据分析库或统计工具。
- **用例**：金融领域智能体
- **工具**：计算器函数、股票行情接口、电子表格工具
- **智能体流程**：用户提问「苹果公司当前股价是多少？如果我以 150 美元买入 100 股，可能会赚多少钱？」，大语言模型会先调用股票行情接口获取最新价格，然后调用计算器工具计算收益，最后把结果整理并返回给用户。

### 4. 发送消息
发送电子邮件、消息或调用外部通信服务的接口。
- **用例**：个人助理智能体
- **工具**：邮件发送接口
- **智能体流程**：用户说「给约翰发一封关于明天会议的邮件」，大语言模型会从请求中提取收件人、主题和正文，并调用邮件接口发送邮件。

### 5. 执行代码
在受控且安全的环境中运行代码片段以完成特定任务。
- **用例**：编程助理智能体
- **工具**：代码解释器
- **智能体流程**：用户提供一段 Python 代码并问「这段代码是做什么的？」，大语言模型会先使用代码解释器运行代码，并据此进行分析和解释。

### 6. 控制其他系统或设备
与智能家居设备、物联网平台或其他联网系统交互。
- **用例**：智能家居智能体
- **工具**：控制智能灯的接口
- **智能体流程**：用户说「关掉客厅的灯」，大语言模型将带有命令和目标设备信息的请求发送给智能家居工具以执行操作。

工具使用模式将语言模型从文本生成器变成能够在数字或现实世界中感知、推理和行动的智能体。

![Tool Use Examples](https://raw.githubusercontent.com/Japan7/agentic-design-patterns-zh/main/images/chapter05_fig1.jpg)
*图1：智能体使用工具的示例*

---

## 实战代码示例

### LangChain 示例
在 LangChain 框架中，使用工具分两个步骤：首先封装定义一个或多个工具，随后将这些工具绑定到语言模型，让模型在需要时生成结构化工具调用请求。

完整可运行代码维护在：[/codes/Chapter-05-Tool-Use-LangChain-Example.py](/codes/Chapter-05-Tool-Use-LangChain-Example.py)，也可打开[在线 Colab 运行](https://colab.research.google.com/drive/1PNsMB2kcCP-iPgpYamG11bGkBiP3QViz#scrollTo=FW3Eh5_OjUea)。

核心代码片段：
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool as langchain_tool
from langchain.agents import create_tool_calling_agent, AgentExecutor

# 1. 初始化带工具调用能力的大语言模型
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

# 2. 用装饰器定义工具
@langchain_tool
def search_information(query: str) -> str:
   """
   Provides factual information on a given topic. Use this tool to find answers to phrases
   like 'capital of France' or 'weather in London?'.
   """
   # 工具逻辑：这里用预定义结果模拟搜索
   simulated_results = {
       "weather in london": "The weather in London is currently cloudy with a temperature of 15°C.",
       "capital of france": "The capital of France is Paris.",
       "population of earth": "The estimated population of Earth is around 8 billion people.",
       "tallest mountain": "Mount Everest is the tallest mountain above sea level.",
       "default": f"Simulated search result for '{query}': No specific information found,
