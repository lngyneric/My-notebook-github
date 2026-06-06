---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/07-Chapter-01-Prompt-Chaining.md
raw_sha256: 2a0811a51cf4ccf4ded764ff64c5a250756666041f6157fedbb9d7a652d86fdf
compiled_at: 2026-04-24T07:17:13.175Z
---
<wiki>
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

## Summary | ==摘要==
Prompt chaining, sometimes referred to as Pipeline pattern, represents a powerful paradigm for handling intricate tasks when leveraging large language models (LLMs). Rather than expecting an LLM to solve a complex problem in a single, monolithic step, prompt chaining advocates for a divide-and-conquer strategy. The core idea is to break down the original, daunting problem into a sequence of smaller, more manageable sub-problems. Each sub-problem is addressed individually through a specifically designed prompt, and the output generated from one prompt is strategically fed as input into the subsequent prompt in the chain.

==提示链模式，也称为「管道模式」，是利用大语言模型处理复杂任务的一种强大范式。它不期望用单一步骤解决复杂问题，而是采用「分而治之」策略。其核心思想是将难题拆解为一系列更小、更易管理的子问题。每个子问题通过专门设计的提示独立解决，前一步的输出传递给下一步作为输入。==

## Core Principles | ==核心原则==
### 1. Modularity & Interpretability | ==模块化与可解释性==
This sequential processing technique inherently introduces modularity and clarity into the interaction with LLMs. By decomposing a complex task, it becomes easier to understand and debug each individual step, making the overall process more robust and interpretable. Each step in the chain can be meticulously crafted and optimized to focus on a specific aspect of the larger problem, leading to more accurate and focused outputs.

==这种顺序处理技术天然具备模块化和清晰性特点。通过分解复杂任务，每个独立步骤都变得更易于理解和调试，从而使整个流程更加稳健、更具可解释性。链条中的每一步都可以被精心设计和优化，专注于解决整体问题中的某个特定方面，最终带来更精准、更聚焦的输出。==

### 2. Dependency Chaining | ==依赖链式结构==
The output of one step acting as the input for the next is crucial. This passing of information establishes a dependency chain, hence the name, where the context and results of previous operations guide the subsequent processing. This allows the LLM to build on its previous work, refine its understanding, and progressively move closer to the desired solution.

==上一步的输出成为下一步的输入，这一点至关重要。这种信息传递建立起一个依赖链（链式结构由此得名），前序操作的上下文和结果引导后续处理。这使得模型能够在先前工作的基础上不断深化理解，逐步接近最终期望的解决方案。==

### 3. External Tool & Knowledge Integration | ==外部工具与知识整合==
Furthermore, prompt chaining is not just about breaking down problems; it also enables the integration of external knowledge and tools. At each step, the LLM can be instructed to interact with external systems, APIs, or databases, enriching its knowledge and abilities beyond its internal training data. This capability dramatically expands the potential of LLMs, allowing them to function not just as isolated models but as integral components of broader, more intelligent systems.

==提示链不仅能分解问题，还能整合外部知识与工具。每一步都可以指示模型调用外部系统、API 或数据库，极大丰富其知识和能力，突破训练数据的局限。这让模型从孤立的个体，演变为更广阔智能系统中的关键组件。==

## Limitations of Single Prompts | ==单一提示的局限性==
For multifaceted tasks, using a single, complex prompt for an LLM can be inefficient, causing the model to struggle with constraints and instructions, potentially leading to instruction neglect where parts of the prompt are overlooked, contextual drift where the model loses track of the initial context, error propagation where early errors amplify, prompts which require a longer context window where the model gets insufficient information to respond back and hallucination where the cognitive load increases the chance of incorrect information. For example, a query asking to analyze a market research report, summarize findings, identify trends with data points, and draft an email risks failure as the model might summarize well but fail to extract data or draft an email properly.

==对于包含多个子任务的复杂任务，使用单一复杂提示往往效率不高。模型可能难以同时满足多项约束和指示，从而出现以下问题：忽视部分指令、上下文漂移（Contextual Drift）、早期错误被放大、上下文超出窗口限制导致信息不足，以及因认知负担加重而产生幻觉。例如，要求模型在单次调用中同时完成分析市场报告、总结要点、识别趋势和草拟邮件等多项任务，失败概率极高。模型或许能给出不错的总结，但在提取精确数据或撰写得体邮件这类更细致的环节上，就很容易出错。==

## Reliability Improvement via Sequential Decomposition | ==通过顺序分解提升可靠性==
Prompt chaining addresses these challenges by breaking the complex task into a focused, sequential workflow, which significantly improves reliability and control. Given the market report task example above, a chained approach can be described as follows:

==提示链通过将复杂任务分解成一个聚焦的、顺序性的工作流，显著提升了可靠性与可控性。以上述例子来说，一个流水线或链式方法可以描述如下：==

1. Initial Prompt (Summarization): "Summarize the key findings of the following market research report: [text]." The model's sole focus is summarization, increasing the accuracy of this initial step.
   ==初始提示（总结）："请总结以下市场研究报告的核心发现：[报告文本]。" 模型的唯一焦点是总结，这大大提高了第一步的准确性。==

2. Second Prompt (Trend Identification): "Using the summary, identify the top three emerging trends and extract the specific data points that support each trend: [output from step 1]." This prompt is now more constrained and builds directly upon a validated output.
   ==第二个提示（识别趋势）：“基于以上总结，请识别出三大新兴趋势，并提取支持每个趋势的具体数据：[第一步的输出]。”这个提示的约束性更强，并且直接建立在一个经过验证的输出之上。==

3. Third Prompt (Email Composition): "Draft a concise email to the marketing team that outlines the following trends and their supporting data: [output from step 2]."
   ==第三个提示（撰写邮件）：“请起草一封简洁的邮件给市场团队，概述以下趋势及其支持数据：[第二步的输出]。”==

This decomposition allows for more granular control over the process. Each step is simpler and less ambiguous, which reduces the cognitive load on the model and leads to a more accurate and reliable final output. This modularity is analogous to a computational pipeline where each function performs a specific operation before passing its result to the next. To ensure an accurate response for each specific task, the model can be assigned a distinct role at every stage. For example, in the given scenario, the initial prompt could be designated as "Market Analyst," the subsequent prompt as "Trade Analyst," and the third prompt as "Expert Documentation Writer," and so forth.

==这种分解让我们可以对过程进行更精细的控制。每一步都更简单、更明确，从而降低了模型的认知负荷，带来更准确、更可靠的最终输出。这种模块化类似于计算流水线：每个函数执行特定操作后，将结果传递给下一步。为了确保每个任务的响应都精确无误，我们还可以在每个阶段为模型赋予不同角色。例如，在上述场景中，初始提示可指定模型扮演「市场分析师」，后续提示指定为「行业分析师」，第三个提示则指定为「专业文档撰写人」。==

## Key Implementation Requirement: Structured Output | ==关键实现要求：结构化输出==
The reliability of a prompt chain is highly dependent on the integrity of the data passed between steps. If the output of one prompt is ambiguous or poorly formatted, the subsequent prompt may fail due to faulty input. To mitigate this, specifying a structured output format, such as JSON or XML, is crucial.

==提示链的可靠性高度依赖于步骤间传递数据的完整性。如果一个提示的输出模棱两可或格式不佳，后续的提示可能会因错误的输入而失败。为了缓解这一问题，指定一个结构化的输出格式至关重要，例如 JSON 或 XML。==

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
      "supporting_data": "Sales of products with ESG-related claims grew 28% over the last five years, compared
