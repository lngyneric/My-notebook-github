---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/23-Chapter-17-Reasoning-Techniques.md
raw_sha256: b25c3b10a4b59dc6a134a7ebece87b1c8dc2be5eb2296cc522f2f0476b38c0f9
compiled_at: 2026-04-14T04:03:11.712Z
---
# 第 17 章：推理技术 | Reasoning Techniques

> 导航：[[22-Chapter-16-Resource-Aware-Optimization|< 上一章]] | [[000-Home|首页]] | [[24-Chapter-18-Guardrails-Safety-Patterns|下一章 >]]

---

## TL;DR
本章介绍了智能体的各类先进推理技术，核心是为推理分配更多计算资源，将智能体的内部思考过程显式化，从而分解复杂问题、提升结论的准确性与稳健性。核心技术包括思维链（CoT）、思维树（ToT）、自我修正、程序辅助语言模型（PALM）、ReAct、辩论链（CoD）、推理缩放定律等，最终目标是构建真正自主、可靠、透明的智能体，能够在无直接监督的情况下完成复杂多步任务。

---

## 目录
- [核心思想](#核心思想)
- [实际应用场景](#实际应用场景)
- [核心推理技术](#核心推理技术)
  - [思维链（Chain-of-Thought, CoT）](#思维链chain-of-thought-cot)
  - [思维树（Tree-of-Thought, ToT）](#思维树tree-of-thought-tot)
  - [自我修正（Self-correction）](#自我修正self-correction)
  - [程序辅助语言模型（PALMs）](#程序辅助语言模型palms)
  - [可验证奖励的强化学习（RLVR）](#可验证奖励的强化学习rlvr)
  - [ReAct（推理与行动）](#react推理与行动)
  - [辩论链（CoD）与辩论图（GoD）](#辩论链cod与辩论图god)
  - [多智能体系统搜索（MASS）](#多智能体系统搜索mass)
- [深度研究（Deep Research）](#深度研究deep-research)
- [推理缩放定律（Scaling Inference Law）](#推理缩放定律scaling-inference-law)
- [实践代码示例](#实践代码示例)
- [智能体思考过程总结](#智能体思考过程总结)
- [要点速览](#要点速览)
- [结语](#结语)
- [参考文献](#参考文献)

---

## 核心思想
本章深入探讨了智能体的先进推理方法，重点介绍多步逻辑推理和问题解决技术。这些技术超越了简单的顺序操作，使智能体的内部推理过程更加明确。这使得智能体能够分解问题、考虑中间步骤，并得出更加稳健和准确的结论。

在这些先进方法中，一个核心原则是**在推理过程中分配更多的计算资源**：这意味着给予智能体或底层大语言模型（LLM）更多的处理时间或步骤来处理查询并生成响应，智能体可以进行迭代优化、探索多种解决方案路径或利用外部工具，而非快速的单次处理。这种延长的推理处理时间通常能显著提高响应的准确性、连贯性和稳健性，尤其对于需要深入分析和思考的复杂问题效果显著。

---

## 实际应用场景
| 应用领域 | 具体价值 |
|---------|---------|
| 复杂问答 | 支持多跳查询，整合多来源数据、执行逻辑推理，检查多条推理路径，借助更长推理时间综合信息 |
| 数学问题解决 | 将问题分解为更小的可解子问题，展示逐步过程，使用代码执行精确计算，支持更复杂的代码生成与验证 |
| 代码调试与生成 | 支持智能体解释生成/修正代码的推理依据，顺序定位潜在问题，根据测试结果迭代优化代码（自我修正） |
| 战略规划 | 通过推理多种选项、结果和前置条件制定全面计划，根据实时反馈调整计划（ReAct），深入思考带来更有效可靠的计划 |
| 医疗诊断 | 帮助智能体系统评估症状、检查结果和患者病史做出诊断，阐述每个阶段的推理过程，可利用外部工具检索数据，更长推理时间支持更全面的鉴别诊断 |
| 法律分析 | 支持分析法律文件和判例以构建论点或提供指导，详细记录逻辑步骤，通过自我修正确保逻辑一致性，更长推理时间支持更深入的法律研究和论点构建 |

---

## 核心推理技术

### 思维链（Chain-of-Thought, CoT）
思维链提示通过模仿逐步思考的过程，显著增强了LLM的复杂推理能力。CoT提示并非直接给出答案，而是引导模型生成一系列中间推理步骤。这种清晰的拆解使LLM能够将复杂问题分解为更小、更易处理的子问题，从而攻克难题，显著提升模型在多步推理任务（例如算术、常识推理、符号操作）上的表现。

CoT的核心优势：
1. 将困难的单步问题转化为一系列简单步骤，提高LLM推理过程的透明度
2. 不仅提升准确性，还能为模型决策提供可洞察的依据，便于调试和理解
3. 实现方式灵活：既可以提供展示逐步推理的少样本示例，也可以直接指示模型"逐步思考"

这种增强的透明度，以及将复杂问题拆解为可管理子问题的做法，对于自主智能体尤为重要，它使智能体能够在复杂环境中执行更可靠、更可审计的行动。

<details>
<summary>CoT 完整示例（英中对照）</summary>

#### 英文示例
```python
You are an Information Retrieval Agent. Your goal is to answer the user's question comprehensively and accurately by thinking step-by-step.
Here's the process you must follow:

1. **Analyze the Query:** Understand the core subject and specific requirements of the user's question. Identify key entities, keywords, and the type of information being sought.
2. **Formulate Search Queries (for Knowledge Base):** Based on your analysis, generate a list of precise search queries that you would use to retrieve relevant information from a knowledge base or external tools.
3. **Simulate Information Retrieval (Self-Correction/Reasoning):**For each search query, mentally consider what kind of information you expect to find. If you were to retrieve the content, what would be the most relevant snippets? Think about potential ambiguities or
missing pieces.
4. **Synthesize Information:** Based on the simulated retrieval and your understanding of the user's original query, synthesize the gathered information into a coherent and complete answer. Ensure all aspects of the query are addressed.
5. **Review and Refine:** Before finalizing, critically evaluate your answer. Is it accurate? Is it comprehensive? Is it easy to understand? Is it concise? If not, identify what needs to be improved and how.

**User Query:** "Explain the main differences between classical computers and quantum computers, and briefly describe a potential application of quantum computing."

**Agent's Thought Process (Internal CoT Output - encouraged by the prompt):**

**Thought 1 (Analyze Query):**
The user wants two things:
1. Main differences between classical and quantum computers.
2. One potential application of quantum computing.
Keywords: classical computers, quantum computers, differences, potential application.

**Thought 2 (Formulate Search Queries):**
- "differences classical vs quantum computers"
- "how quantum computers work"
- "how classical computers work"
- "applications of quantum computing"

**Thought 3 (Simulate Information Retrieval & Identify Key Concepts):**
- From "differences": Expect concepts like bits vs. qubits, superposition, entanglement, probabilistic nature, computational power for specific problems.
- From "how they work": Classical uses transistors/binary. Quantum uses quantum mechanics.
- From "applications": Expect drug discovery, material science, cryptography, optimization.

**Thought 4 (Synthesize Information):**
Classical computers use bits (0 or 1), processing information sequentially. Quantum computers use qubits, which can be 0, 1, or both simultaneously (superposition), and can be entangled, allowing for vastly different computational approaches. This enables them to
solve certain problems (like factoring large numbers or simulating complex molecules) far more efficiently than classical computers. A potential application is in drug discovery, where quantum computers could simulate molecular interactions with unprecedented accuracy,
accelerating the development of new medicines.

**Thought 5 (Review and Refine):**
- Differences are covered (bits vs qubits, superposition, entanglement, processing).
- Application is given (drug discovery).
- Is it brief? Yes.
- Is it clear? Yes.
- Looks good.

**Agent's Final Answer (Output to User):**
Classical computers process information using bits, which can be either a 0 or a 1 at any given time, performing operations sequentially. In contrast, quantum computers utilize qubits, which can exist in multiple states simultaneously through superposition and can be linked through entanglement, allowing for exponentially more complex computations. This fundamental difference enables quantum machines to tackle certain problems, such as simulating molecular structures or breaking complex encryption, that are intractable for even the most powerful classical supercomputers. A significant potential application of quantum computing lies in drug discovery, where its ability to precisely model molecular behavior could revolutionize
