---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/08-Chapter-02-Routing.md
raw_sha256: 444ae6285ed8748bc6d695d69289393f9112f3ea786d516e404f0db73822b323
compiled_at: 2026-04-24T07:20:28.916Z
---
<wiki>
# Chapter 2: Routing | <mark>第二章：路由</mark>

[[07-Chapter-01-Prompt-Chaining|< Previous Chapter]] | [[000-Home|Home]] | [[09-Chapter-03-Parallelization|Next Chapter >]]

---

## Routing Pattern Overview | <mark>路由模式概述</mark>

While sequential processing via prompt chaining is a foundational technique for executing deterministic, linear workflows with language models, its applicability is limited in scenarios requiring adaptive responses. Real-world agentic systems must often arbitrate between multiple potential actions based on contingent factors, such as the state of the environment, user input, or the outcome of a preceding operation. This capacity for dynamic decision-making, which governs the flow of control to different specialized functions, tools, or sub-processes, is achieved through a mechanism known as routing.

<mark>提示链虽然是执行确定性线性工作流的基础方法，但在需要自适应响应的场景下显得力不从心。现实场景中，智能体系统往往要根据环境状态、用户输入或上一步的执行结果等情境信息，从多个可选方案中选择合适的行动路径。路由（Routing）机制就是实现这种控制流分发的关键技术，它决定该将请求交给哪个功能模块、工具或子流程处理。</mark>

Routing introduces conditional logic into an agent's operational framework, enabling a shift from a fixed execution path to a model where the agent dynamically evaluates specific criteria to select from a set of possible subsequent actions. This allows for more flexible and context-aware system behavior.

<mark>路由为智能体引入了条件分支能力，让系统不再沿着固定流程执行，而是能根据实际情况动态选择最优的后续动作，从而实现更灵活、更懂上下文的智能行为。</mark>

For instance, an agent designed for customer inquiries, when equipped with a routing function, can first classify an incoming query to determine the user's intent. Based on this classification, it can then direct the query to a specialized agent for direct question-answering, a database retrieval tool for account information, or an escalation procedure for complex issues, rather than defaulting to a single, predetermined response pathway. Therefore, a more sophisticated agent using routing could:

<mark>以客户咨询智能体为例。集成路由功能后，系统会先识别用户的真实意图，然后将请求分发到对应的处理单元：简单问题交由问答智能体处理，账户查询则调用数据库检索工具，复杂问题则升级到人工处理，而非采用单一的预设响应路径。</mark>

<mark>因此，具有路由功能的智能体可以：</mark>

1. Analyze the user's query.

   <mark>分析用户的请求。</mark>

2. **Route** the query based on its *intent*:

    <mark>基于查询的意图将其<strong>路由</strong>到相应的处理路径：</mark>

   - If the intent is "check order status", route to a sub-agent or tool chain that interacts with the order database.

      <mark>「查订单」→ 调用订单查询子智能体或工具链</mark>

   - If the intent is "product information", route to a sub-agent or chain that searches the product catalog.

      <mark>「问产品」→ 调用产品目录检索子智能体或工具链</mark>

   - If the intent is "technical support", route to a different chain that accesses troubleshooting guides or escalates to a human.

      <mark>「求技术支持」→ 查阅故障排除手册或转人工</mark>

   - If the intent is unclear, route to a clarification sub-agent or prompt chain.

      <mark>「意图不明」→ 转到澄清子智能体追问细节</mark>

### Routing Implementation Methods

The core component of the Routing pattern is a mechanism that performs the evaluation and directs the flow. This mechanism can be implemented in several ways:

<mark>路由模式的核心在于评估与决策机制，即判断请求类型并确定执行路径。常见的实现方式包括：</mark>

#### LLM-based Routing
The language model itself can be prompted to analyze the input and output a specific identifier or instruction that indicates the next step or destination. For example, a prompt might ask the LLM to "Analyze the following user query and output only the category: 'Order Status', 'Product Info', 'Technical Support', or 'Other'." The agentic system then reads this output and directs the workflow accordingly.

<mark><strong>基于大语言模型的路由（LLM-based Routing）：</strong>通过提示词引导语言模型分析输入并输出特定的分类标识或指令，以指示下一步的执行目标。例如，提示词可以要求模型「分析以下用户查询并仅输出类别：订单状态、产品信息、技术支持或其他」。智能体系统读取该输出后，据此将工作流导向相应的处理路径。</mark>

#### Embedding-based Routing
The input query can be converted into a vector embedding (see RAG, Chapter 14). This embedding is then compared to embeddings representing different routes or capabilities. The query is routed to the route whose embedding is most similar. This is useful for semantic routing, where the decision is based on the meaning of the input rather than just keywords.

<mark><strong>向量路由（Embedding-based Routing）：</strong>将输入查询转换为向量嵌入（详见第 14 章 RAG），然后与代表不同路由或能力的嵌入向量进行比较，将查询路由到嵌入相似度最高的路径。此方法适用于语义路由场景，其决策基于输入的语义含义而非仅仅关键词匹配。例如，「帮我退款」和「订单有问题想取消」虽然措辞不同，但向量距离相近，因此都会被路由到退款处理流程。</mark>

#### Rule-based Routing
This involves using predefined rules or logic (e.g., if-else statements, switch cases) based on keywords, patterns, or structured data extracted from the input. This can be faster and more deterministic than LLM-based routing, but is less flexible for handling nuanced or novel inputs.

<mark><strong>规则路由（Rule-based Routing）：</strong>基于关键词、模式或从输入中提取的结构化数据，使用预定义规则或逻辑（如 if-else 语句、switch 语句）进行决策。此方法比大模型路由更快速且具有确定性，但在处理复杂语境或新颖输入时灵活性较低。</mark>

#### Machine Learning Model-Based Routing
it employs a discriminative model, such as a classifier, that has been specifically trained on a small corpus of labeled data to perform a routing task. While it shares conceptual similarities with embedding-based methods, its key characteristic is the supervised fine-tuning process, which adjusts the model's parameters to create a specialized routing function. This technique is distinct from LLM-based routing because the decision-making component is not a generative model executing a prompt at inference time. Instead, the routing logic is encoded within the fine-tuned model's learned weights. While LLMs may be used in a pre-processing step to generate synthetic data for augmenting the training set, they are not involved in the real-time routing decision itself.

<mark><strong>机器学习路由（Machine Learning Model-Based Routing）：</strong>采用判别式模型（如分类器），该模型在少量标注数据上经过专门训练以执行路由任务。虽然在概念上与向量路由方法有相似之处，但其关键特征在于监督微调过程，通过调整模型参数来创建专门的路由功能。此技术与大模型路由的区别在于，其决策组件并非在推理时执行提示词的生成式模型，而是将路由逻辑编码在微调后模型的学习权重中。虽然在预处理阶段可能使用大语言模型生成合成数据以扩充训练集，但实时路由决策本身并不涉及大模型。</mark>

### Routing Deployment Positions & Supporting Frameworks

Routing mechanisms can be implemented at multiple junctures within an agent's operational cycle. They can be applied at the outset to classify a primary task, at intermediate points within a processing chain to determine a subsequent action, or during a subroutine to select the most appropriate tool from a given set.

<mark>路由机制可在智能体运行周期的多个节点实施：可在初始阶段对主要任务进行分类，可在处理链的中间点确定后续操作，也可在子程序中从给定工具集中选择最合适的工具。</mark>

Computational frameworks such as LangChain, LangGraph, and Google's Agent Developer Kit (ADK) provide explicit constructs for defining and managing such conditional logic. With its state-based graph architecture, LangGraph is particularly well-suited for complex routing scenarios where decisions are contingent upon the accumulated state of the entire system. Similarly, Google's ADK provides foundational components for structuring an agent's capabilities and interaction models, which serve as the basis for implementing routing logic. Within the execution environments provided by these frameworks, developers define the possible operational paths and the functions or model-based evaluations that dictate the transitions between nodes in the computational graph.

<mark>LangChain、LangGraph 和 Google 智能体开发套件（ADK）等计算框架为定义和管理此类条件逻辑提供了明确的构造。凭借基于状态的图架构，LangGraph
