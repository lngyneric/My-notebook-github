---
tags:
  - Agentic-Patterns
  - Prompt-Chaining
  - AI
  - LLM
created: 2024-05-21
---

[[06-What-Makes-Agent|< Previous Chapter]] | [[000-Home|Home]] | [[08-Chapter-02-Routing|Next Chapter >]]

# Chapter 1: Prompt Chaining | ==第一章：提示链==

## Prompt Chaining Pattern Overview | ==提示链模式概述==

Prompt chaining, sometimes referred to as Pipeline pattern, represents a powerful paradigm for handling intricate tasks when leveraging large language models (LLMs). Rather than expecting an LLM to solve a complex problem in a single, monolithic step, prompt chaining advocates for a divide-and-conquer strategy. The core idea is to break down the original, daunting problem into a sequence of smaller, more manageable sub-problems. Each sub-problem is addressed individually through a specifically designed prompt, and the output generated from one prompt is strategically fed as input into the subsequent prompt in the chain.

==提示链模式，也称为「管道模式」，是利用大语言模型处理复杂任务的一种强大范式。它不期望用单一步骤解决复杂问题，而是采用「分而治之」策略。其核心思想是将难题拆解为一系列更小、更易管理的子问题。每个子问题通过专门设计的提示独立解决，前一步的输出传递给下一步作为输入。==

This sequential processing technique inherently introduces modularity and clarity into the interaction with LLMs. By decomposing a complex task, it becomes easier to understand and debug each individual step, making the overall process more robust and interpretable. Each step in the chain can be meticulously crafted and optimized to focus on a specific aspect of the larger problem, leading to more accurate and focused outputs.

==这种顺序处理技术天然具备模块化和清晰性特点。通过分解复杂任务，每个独立步骤都变得更易于理解和调试，从而使整个流程更加稳健、更具可解释性。链条中的每一步都可以被精心设计和优化，专注于解决整体问题中的某个特定方面，最终带来更精准、更聚焦的输出。==

The output of one step acting as the input for the next is crucial. This passing of information establishes a dependency chain, hence the name, where the context and results of previous operations guide the subsequent processing. This allows the LLM to build on its previous work, refine its understanding, and progressively move closer to the desired solution.

==上一步的输出成为下一步的输入，这一点至关重要。这种信息传递建立起一个依赖链（链式结构由此得名），前序操作的上下文和结果引导后续处理。这使得模型能够在先前工作的基础上不断深化理解，逐步接近最终期望的解决方案。==

Furthermore, prompt chaining is not just about breaking down problems; it also enables the integration of external knowledge and tools. At each step, the LLM can be instructed to interact with external systems, APIs, or databases, enriching its knowledge and abilities beyond its internal training data. This capability dramatically expands the potential of LLMs, allowing them to function not just as isolated models but as integral components of broader, more intelligent systems.

==提示链不仅能分解问题，还能整合外部知识与工具。每一步都可以指示模型调用外部系统、API 或数据库，极大丰富其知识和能力，突破训练数据的局限。这让模型从孤立的个体，演变为更广阔智能系统中的关键组件。==

> [!WARNING] Limitations of single prompts
> For multifaceted tasks, using a single, complex prompt for an LLM can be inefficient, causing the model to struggle with constraints and instructions, potentially leading to instruction neglect where parts of the prompt are overlooked, contextual drift where the model loses track of the initial context, error propagation where early errors amplify, prompts which require a longer context window where the model gets insufficient information to respond back and hallucination where the cognitive load increases the chance of incorrect information. For example, a query asking to analyze a market research report, summarize findings, identify trends with data points, and draft an email risks failure as the model might summarize well but fail to extract data or draft an email properly.

==**单一提示的局限性：**对于包含多个子任务的复杂任务，使用单一复杂提示往往效率不高。模型可能难以同时满足多项约束和指示，从而出现以下问题：忽视部分指令、上下文漂移（Contextual Drift）、早期错误被放大、上下文超出窗口限制导致信息不足，以及因认知负担加重而产生幻觉。==

==例如，要求模型在单次调用中同时完成分析市场报告、总结要点、识别趋势和草拟邮件等多项任务，失败概率极高。模型或许能给出不错的总结，但在提取精确数据或撰写得体邮件这类更细致的环节上，就很容易出错。==

> [!TIP] Enhanced Reliability Through Sequential Decomposition
> Prompt chaining addresses these challenges by breaking the complex task into a focused, sequential workflow, which significantly improves reliability and control. Given the example above, a pipeline or chained approach can be described as follows:

==**通过顺序分解提升可靠性：**提示链通过将复杂任务分解成一个聚焦的、顺序性的工作流，显著提升了可靠性与可控性。以上述例子来说，一个流水线或链式方法可以描述如下：==

1. Initial Prompt (Summarization): "Summarize the key findings of the following market research report: [text]." The model's sole focus is summarization, increasing the accuracy of this initial step.

   ==初始提示（总结）："请总结以下市场研究报告的核心发现：[报告文本]。" 模型的唯一焦点是总结，这大大提高了第一步的准确性。==

2. Second Prompt (Trend Identification): "Using the summary, identify the top three emerging trends and extract the specific data points that support each trend: [output from step 1]." This prompt is now more constrained and builds directly upon a validated output.

   ==第二个提示（识别趋势）：“基于以上总结，请识别出三大新兴趋势，并提取支持每个趋势的具体数据：[第一步的输出]。”这个提示的约束性更强，并且直接建立在一个经过验证的输出之上。==

3. Third Prompt (Email Composition): "Draft a concise email to the marketing team that outlines the following trends and their supporting data: [output from step 2]."

   ==第三个提示（撰写邮件）：“请起草一封简洁的邮件给市场团队，概述以下趋势及其支持数据：[第二步的输出]。”==

This decomposition allows for more granular control over the process. Each step is simpler and less ambiguous, which reduces the cognitive load on the model and leads to a more accurate and reliable final output. This modularity is analogous to a computational pipeline where each function performs a specific operation before passing its result to the next. To ensure an accurate response for each specific task, the model can be assigned a distinct role at every stage. For example, in the given scenario, the initial prompt could be designated as "Market Analyst," the subsequent prompt as "Trade Analyst," and the third prompt as "Expert Documentation Writer," and so forth.

==这种分解让我们可以对过程进行更精细的控制。每一步都更简单、更明确，从而降低了模型的认知负荷，带来更准确、更可靠的最终输出。==

==这种模块化类似于计算流水线：每个函数执行特定操作后，将结果传递给下一步。为了确保每个任务的响应都精确无误，我们还可以在每个阶段为模型赋予不同角色。例如，在上述场景中，初始提示可指定模型扮演「市场分析师」，后续提示指定为「行业分析师」，第三个提示则指定为「专业文档撰写人」。==

**The Role of Structured Output:** The reliability of a prompt chain is highly dependent on the integrity of the data passed between steps. If the output of one prompt is ambiguous or poorly formatted, the subsequent prompt may fail due to faulty input. To mitigate this, specifying a structured output format, such as JSON or XML, is crucial.

==**结构化输出的作用：**提示链的可靠性高度依赖于步骤间传递数据的完整性。如果一个提示的输出模棱两可或格式不佳，后续的提示可能会因错误的输入而失败。为了缓解这一问题，指定一个结构化的输出格式至关重要，例如 JSON 或 XML。==

For example, the output from the trend identification step could be formatted as a JSON object:

==例如，趋势识别步骤的输出可以格式化为 JSON 对象：==

```json
{
  "trends": [
    {
      "trend_name": "AI-Powered Personalization",
      "supporting_data": "73% of consumers prefer to do business with brands that use personal information to make their shopping experiences more relevant."
    },
    {
      "trend_name": "Sustainable and Ethical Brands",
      "supporting_data": "Sales of products with ESG-related claims grew 28% over the last five years, compared to 20% for products without."
    }
  ]
}
```

This structured format ensures that the data is machine-readable and can be precisely parsed and inserted into the next prompt without ambiguity. This practice minimizes errors that can arise from interpreting natural language and is a key component in building robust, multi-step LLM-based systems.

==这种结构化格式确保数据可被机器读取，能够被精确解析并无歧义地插入到下一个提示中。这样可以减少因解析自然语言而产生的错误，是构建稳健多步骤大语言模型应用的重要环节。==

---

## Practical Applications & Use Cases | ==实际应用场景==

Prompt chaining is a versatile pattern applicable in a wide range of scenarios when building agentic systems. Its core utility lies in breaking down complex problems into sequential, manageable steps. Here are several practical applications:

==提示链是一种通用模式，可应用于构建智能体系统的多种场景。其核心效用在于将复杂问题分解为顺序的、可管理的步骤。以下是一些实际应用和用例：==

> [!example] 1. Information Processing Workflows
> Many tasks involve processing raw information through multiple transformations. For instance, summarizing a document, extracting key entities, and then using those entities to query a database or generate a report. A prompt chain could look like:

==**信息处理工作流：**许多任务涉及对原始信息进行多重转换。例如，总结一份文档，提取关键实体，然后用这些实体查询数据库或生成报告。一个提示链可能如下所示：==

- Prompt 1: Extract text content from a given URL or document.
   ==提示 1: 从给定的 URL 或文档中提取文本内容。==
- Prompt 2: Summarize the cleaned text.
   ==提示 2: 总结清洗后的文本。==
- Prompt 3: Extract specific entities (e.g., names, dates, locations) from the summary or original text.
   ==提示 3: 从总结或原文中提取特定实体（如姓名、日期、地点）。==
- Prompt 4: Use the entities to search an internal knowledge base.
   ==提示 4: 使用这些实体搜索内部知识库。==
- Prompt 5: Generate a final report incorporating the summary, entities, and search results.
   ==提示 5: 结合总结、实体和搜索结果，生成最终报告。==

This methodology is applied in domains such as automated content analysis, the development of AI-driven research assistants, and complex report generation.

==此方法被广泛应用于自动化内容分析、AI 驱动的研究助手开发以及复杂报告生成等领域。==

> [!example] 2. Complex Query Answering
> Answering complex questions that require multiple steps of reasoning or information retrieval is a prime use case. For example, "What were the main causes of the stock market crash in 1929, and how did government policy respond?"

==**复杂问答：**回答需要多步推理或信息检索的复杂问题是提示链的典型应用场景。例如，"1929 年股市崩盘的主要原因是什么？政府的应对政策又是什么？"==

- Prompt 1: Identify the core sub-questions in the user's query (causes of crash, government response).
  ==提示 1: 识别用户查询中的核心子问题（崩盘原因、政府对策）。==
- Prompt 2: Research or retrieve information specifically about the causes of the 1929 crash.
  ==提示 2: 研究或检索关于 1929 年崩盘原因的信息。==
- Prompt 3: Research or retrieve information specifically about the government's policy response to the 1929 stock market crash.
  ==提示 3: 研究或检索关于 1929 年股市崩盘的政府对策信息。==
- Prompt 4: Synthesize the information from steps 2 and 3 into a coherent answer to the original query.
  ==提示 4: 将步骤 2 和 3 的信息整合成一个连贯的答案，回答原始问题。==

This sequential processing methodology is integral to developing AI systems capable of multi-step inference and information synthesis. Such systems are required when a query cannot be answered from a single data point but instead necessitates a series of logical steps or the integration of information from diverse sources.

==这种顺序处理的方法是构建具备多步推理和信息整合能力的 AI 系统的关键。当一个问题无法仅凭单一信息解决，而必须经过一系列逻辑步骤或整合多个信息源才能作答时，这种模式就显得尤为重要。==

For example, an automated research agent designed to generate a comprehensive report on a specific topic executes a hybrid computational workflow. Initially, the system retrieves numerous relevant articles. The subsequent task of extracting key information from each article can be performed concurrently for each source. This stage is well-suited for parallel processing, where independent sub-tasks are run simultaneously to maximize efficiency.

==例如，一个针对特定主题生成详尽报告的研究智能体会执行混合计算工作流。首先，系统会检索大量相关文章。然后，需要从每篇文章中提取关键信息，这一任务可以针对所有来源并发执行。由于各个提取任务相互独立，这个阶段非常适合采用并行处理，从而实现效率最大化。==

However, once the individual extractions are complete, the process becomes inherently sequential. The system must first collate the extracted data, then synthesize it into a coherent draft, and finally review and refine this draft to produce a final report. Each of these later stages is logically dependent on the successful completion of the preceding one. This is where prompt chaining is applied: the collated data serves as the input for the synthesis prompt, and the resulting synthesized text becomes the input for the final review prompt. Therefore, complex operations frequently combine parallel processing for independent data gathering with prompt chaining for the dependent steps of synthesis and refinement.

==然而，一旦各自的提取任务完成，整个流程就转变为顺序执行。系统必须先汇集整合所有提取的数据，再将其综合成一份逻辑连贯的初稿，最后对初稿进行审阅和润色，形成最终报告。后续的每一个阶段在逻辑上都依赖于前一阶段的顺利完成，环环相扣。这正是提示链模式发挥作用的时刻：汇集的数据成为后续综合步骤的输入，而综合生成的文本又成为最后审阅步骤的输入。因此，复杂工作流通常采用混合模式：对独立的数据采集任务并行处理，对依赖关系明确的整合与优化步骤使用提示链。==

> [!example] 3. Data Extraction and Transformation
> The conversion of unstructured text into a structured format is typically achieved through an iterative process, requiring sequential modifications to improve the accuracy and completeness of the output.

==**数据提取和转换：**将非结构化文本转换为结构化格式通常需要一个迭代过程，通过多轮迭代可以提升输出的准确性和完整性。==

- Prompt 1: Attempt to extract specific fields (e.g., name, address, amount) from an invoice document.
  ==提示 1: 尝试从发票中提取特定字段（如姓名、地址、金额）。==
- Processing: Check if all required fields were extracted and if they meet format requirements.
  ==处理：检查是否提取了所有必需的字段，以及是否符合格式要求。==
- Prompt 2 (Conditional): If fields are missing or malformed, craft a new prompt asking the model to specifically find the missing/malformed information, perhaps providing context from the failed attempt.
  ==提示 2（条件判断）：如果字段缺失或格式不正确，构建一个新提示，要求模型专门查找缺失或处理格式不正确的信息，并可提供上一次失败的上下文。==
- Processing: Validate the results again. Repeat if necessary.
  ==处理：再次验证结果。如有必要，重复此过程。==
- Output: Provide the extracted, validated structured data.
  ==输出：提供经过验证的结构化数据。==

This sequential processing methodology is particularly applicable to data extraction and analysis from unstructured sources like forms, invoices, or emails. For example, solving complex Optical Character Recognition (OCR) problems, such as processing a PDF form, is more effectively handled through a decomposed, multi-step approach.

==这种顺序处理的方法论，尤其适用于从表单、发票或邮件等非结构化来源中进行数据提取与分析。例如，在对 PDF 进行 OCR 识别时，采用分解式的多步方法会远比单次请求更为有效。==

Initially, a large language model is employed to perform the primary text extraction from the document image. Following this, the model processes the raw output to normalize the data, a step where it might convert numeric text, such as "one thousand and fifty," into its numerical equivalent, 1050. A significant challenge for LLMs is performing precise mathematical calculations. Therefore, in a subsequent step, the system can delegate any required arithmetic operations to an external calculator tool. The LLM identifies the necessary calculation, feeds the normalized numbers to the tool, and then incorporates the precise result. This chained sequence of text extraction, data normalization, and external tool use achieves a final, accurate result that is often difficult to obtain reliably from a single LLM query.

==首先，系统调用大语言模型从图像中提取文本。随后，模型处理这些原始输出进行数据规范化，比如将「一千零五十」这样的文本转换为数值 1050。由于精确数学计算对大语言模型来说是一项挑战，在后续步骤中，系统会将需要的算术运算交给外部计算器执行。模型负责识别需要的运算，将规范化后的数字传递给计算工具，然后将精确结果整合回来。通过文本提取、数据规范化、外部工具调用的链式流程，系统可获得精确结果，这是单次模型调用难以实现的。==

> [!example] 4. Content Generation Workflows
> The composition of complex content is a procedural task that is typically decomposed into distinct phases, including initial ideation, structural outlining, drafting, and subsequent revision.

==**内容生成工作流：**复杂内容的创作通常被分解为不同阶段，包括初步构思、搭建大纲、起草和修订等。==

- Prompt 1: Generate 5 topic ideas based on a user's general interest.
  ==提示 1: 基于用户的兴趣爱好，生成 5 个主题。==
- Processing: Allow the user to select one idea or automatically choose the best one.
  ==处理：允许用户选择一个主题或自动选择最好的一个。==
- Prompt 2: Based on the selected topic, generate a detailed outline.
  ==提示 2: 基于选定的主题，生成详细的大纲。==
- Prompt 3: Write a draft section based on the first point in the outline.
  ==提示 3: 基于大纲的第一点，撰写初稿。==
- Prompt 4: Write a draft section based on the second point in the outline, providing the previous section for context. Continue this for all outline points.
  ==提示 4: 在提供前一部分上下文的情况下，根据大纲的第二点撰写草稿，并以此类推完成所有要点。==
- Prompt 5: Review and refine the complete draft for coherence, tone, and grammar.
  ==提示 5: 审阅和润色完整的初稿，确保连贯性、语气和语法。==

This methodology is employed for a range of natural language generation tasks, including the automated composition of creative narratives, technical documentation, and other forms of structured textual content.

==这种方法适用于多种自然语言生成任务，比如自动撰写创意故事、编写技术文档以及生成其他结构化文本内容。==

> [!example] 5. Conversational Agents with State
> Although comprehensive state management architectures employ methods more complex than sequential linking, prompt chaining provides a foundational mechanism for preserving conversational continuity. This technique maintains context by constructing each conversational turn as a new prompt that systematically incorporates information or extracted entities from preceding interactions in the dialogue sequence.

==**有状态的对话智能体：**虽然完善的状态管理架构需要比顺序链接更复杂的方法，但提示链为维持对话连续性提供了基础机制。核心思想是将每轮对话构建为新提示，系统性地融入先前交互产生的信息或提取的实体。==

- Prompt 1: Process User Utterance 1, identify intent and key entities.
  ==提示 1: 处理用户的第一轮发言，识别意图和关键实体。==
- Processing: Update conversation state with intent and entities.
  ==处理：更新对话状态，包含意图和实体。==
- Prompt 2: Based on current state, generate a response and/or identify the next required piece of information.
  ==提示 2: 基于当前状态，生成响应或识别下一个所需的信息。==
- Repeat for subsequent turns, with each new user utterance initiating a chain that leverages the accumulating conversation history (state).
  ==在后续的对话中重复此过程，用户的每一句新话语都会启动一个新的处理链，并充分利用不断积累的对话历史（即状态）。==

This principle is fundamental to the development of conversational agents, enabling them to maintain context and coherence across extended, multi-turn dialogues. By preserving the conversational history, the system can understand and appropriately respond to user inputs that depend on previously exchanged information.

==这一原则对于开发对话智能体至关重要，使智能体在多轮对话中保持上下文理解和逻辑连贯性。通过保留对话历史，系统就能够理解并恰当地回应那些依赖于先前交换信息的后续输入。==

> [!example] 6. Code Generation and Refinement
> The generation of functional code is typically a multi-stage process, requiring a problem to be decomposed into a sequence of discrete logical operations that are executed progressively

==**代码生成和优化：**可用代码的生成通常是一个多阶段的过程，它要求将问题分解为一系列可有序执行的逻辑操作。==

- Prompt 1: Understand the user's request for a code function. Generate pseudocode or an outline.
  ==提示 1: 理解用户的需求，生成伪代码或大纲。==
- Prompt 2: Write the initial code draft based on the outline.
  ==提示 2: 基于大纲，编写初始版本的代码。==
- Prompt 3: Identify potential errors or areas for improvement in the code (perhaps using a static analysis tool or another LLM call).
  ==提示 3: 识别代码中可能存在的错误或需要改进的地方（使用静态分析工具或另外调用一次模型）。==
- Prompt 4: Rewrite or refine the code based on the identified issues.
  ==提示 4: 基于识别出的问题，重写或优化代码。==
- Prompt 5: Add documentation or test cases.
  ==提示 5: 添加文档或测试用例。==

In applications such as AI-assisted software development, the utility of prompt chaining stems from its capacity to decompose complex coding tasks into a series of manageable sub-problems. This modular structure reduces the operational complexity for the large language model at each step. Critically, this approach also allows for the insertion of deterministic logic between model calls, enabling intermediate data processing, output validation, and conditional branching within the workflow. By this method, a single, multifaceted request that could otherwise lead to unreliable or incomplete results is converted into a structured sequence of operations managed by an underlying execution framework.

==在 AI 辅助软件开发等应用中，提示链的价值在于将复杂编码任务分解为一系列可管理的子问题，这种模块化结构降低了模型在每一步的复杂度。更重要的是，这种方法允许我们在两次模型调用之间插入确定性逻辑，从而在工作流中实现中间数据处理、输出验证和条件分支等功能。通过这种方式，一个原本可能导致不可靠或不完整结果的单一复杂请求，被转化为由底层执行框架管理的结构化操作序列。==

> [!example] 7. Multimodal and multi-step reasoning
> Analyzing datasets with diverse modalities necessitates breaking down the problem into smaller, prompt-based tasks. For example, interpreting an image that contains a picture with embedded text, labels highlighting specific text segments, and tabular data explaining each label, requires such an approach.

==**多模态和多步推理：**分析包含多种模态（如图像、文本、表格）的数据时，必须将问题分解为更小的、基于提示的任务。例如，要解读一张复杂的图像，其中不仅有图片和文本，还有对特定文本段的高亮标注，以及采用表格来解释每个标签的情况，就需要采用这样的方法。==

- Prompt 1: Extract and comprehend the text from the user's image request.
  ==提示 1: 从用户的图像请求中提取并理解文本内容。==
- Prompt 2: Link the extracted image text with its corresponding labels.
  ==提示 2: 将提取出的图像文本与其对应的标签进行关联。==
- Prompt 3: Interpret the gathered information using a table to determine the required output.
  ==提示 3: 利用表格来解读已收集到的信息，以确定最终需要输出的内容。==

---

## Hands-On Code Example | ==实践示例==

Implementing prompt chaining ranges from direct, sequential function calls within a script to the utilization of specialized frameworks designed to manage control flow, state, and component integration. Frameworks such as LangChain, LangGraph, Crew AI, and the Google Agent Development Kit (ADK) offer structured environments for constructing and executing these multi-step processes, which is particularly advantageous for complex architectures.

==实现提示链的方法有很多，从直接在脚本中依次调用函数，到利用专门的框架来管理控制流、状态和组件集成，形式不一。像 LangChain、LangGraph、Crew AI 以及谷歌智能体开发套件（ADK）这类框架，能为构建和执行多步流程提供结构化的环境，这对于复杂的系统架构尤其有益。==

For the purpose of demonstration, LangChain and LangGraph are suitable choices as their core APIs are explicitly designed for composing chains and graphs of operations. LangChain provides foundational abstractions for linear sequences, while LangGraph extends these capabilities to support stateful and cyclical computations, which are necessary for implementing more sophisticated agentic behaviors. This example will focus on a fundamental linear sequence.

==为了演示，LangChain 和 LangGraph 是非常合适的选择，因为它们的核心 API 就是为组合操作链（Chains）和图（Graphs）而设计的。LangChain 为线性序列提供了基础的抽象，而 LangGraph 则在此基础上进一步扩展，支持有状态和循环计算，这对于实现更复杂的智能体行为至关重要。本示例将聚焦于一个基础的线性序列。==

The following code implements a two-step prompt chain that functions as a data processing pipeline. The initial stage is designed to parse unstructured text and extract specific information. The subsequent stage then receives this extracted output and transforms it into a structured data format.

==下面的代码实现了一个两步的提示链，它就像一个数据处理流水线。第一步旨在解析非结构化文本并提取特定信息；第二步则接收上一步的输出，并将其转换为结构化的数据格式。==

To replicate this procedure, the required libraries must first be installed. This can be accomplished using the following command:

==要运行此示例，首先需要安装必要的库：==

```bash
pip install langchain langchain-community langchain-openai langgraph
```

Note that langchain-openai can be substituted with the appropriate package for a different model provider. Subsequently, the execution environment must be configured with the necessary API credentials for the selected language model provider, such as OpenAI, Google Gemini, or Anthropic.

==请注意，langchain-openai 可以替换为其他模型提供商的相应库包。此外，你必须在运行环境中配置好所选语言模型（如 OpenAI、Google Gemini 或 Anthropic）的 API 密钥。==

[Colab 代码](https://colab.research.google.com/drive/15XCzDOvBhIQaZ__xkvruf5sP9OznAbK9) 已维护在 [此处](codes/Chapter-01-Prompt-Chaining-Example.py)。

```python
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# For better security, load environment variables from a .env file
# 为了更好的安全性，建议从 .env 文件加载环境变量
# from dotenv import load_dotenv
# load_dotenv()
# Make sure your OPENAI_API_KEY is set in the .env file
# 确保你的 OPENAI_API_KEY 已在 .env 文件中设置

# Initialize the Language Model (using ChatOpenAI is recommended)
# 初始化语言模型（推荐使用 ChatOpenAI）
llm = ChatOpenAI(temperature=0)

# --- Prompt 1: Extract Information ---
# --- 提示 1: 提取信息 ---
prompt_extract = ChatPromptTemplate.from_template(
    "Extract the technical specifications from the following text:\n\n{text_input}"
)

# --- Prompt 2: Transform to JSON ---
# --- 提示 2: 转换为 JSON ---
prompt_transform = ChatPromptTemplate.from_template(
    "Transform the following specifications into a JSON object with 'cpu', 'memory', and 'storage' as keys:\n\n{specifications}"
)

# --- Build the Chain using LCEL ---
# The StrOutputParser() converts the LLM's message output to a simple string.
# --- 使用 LCEL 构建链 ---
# StrOutputParser() 会将 LLM 的消息输出转换为一个简单的字符串。
extraction_chain = prompt_extract | llm | StrOutputParser()

# The full chain passes the output of the extraction chain into the 'specifications'
# variable for the transformation prompt.
# 完整的链将提取链的输出传递给转换提示中的 'specifications' 变量。
full_chain = (
    {"specifications": extraction_chain}
    | prompt_transform
    | llm
    | StrOutputParser()
)

# --- Run the Chain ---
# --- 运行链 ---
input_text = "The new laptop model features a 3.5 GHz octa-core processor, 16GB of RAM, and a 1TB NVMe SSD."

# Execute the chain with the input text dictionary.
# 接收输入文本并执行链。
final_result = full_chain.invoke({"text_input": input_text})

print("\n--- Final JSON Output ---")
# print("\n--- 打印最终输出的 JSON ---")
print(final_result)
```

**运行输出（译者添加）：**

```json
--- Final JSON Output ---
{
    "cpu": "3.5 GHz octa-core",
    "memory": "16GB",
    "storage": "1TB NVMe SSD"
}
```

[[06-What-Makes-Agent|< Previous Chapter]] | [[000-Home|Home]] | [[08-Chapter-02-Routing|Next Chapter >]]
