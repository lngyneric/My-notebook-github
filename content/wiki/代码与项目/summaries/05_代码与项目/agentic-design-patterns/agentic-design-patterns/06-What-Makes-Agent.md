---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/06-What-Makes-Agent.md
raw_sha256: 0e5388b5b07e911b956b71073ab9ad5b3d95dac8b285ea1330b2b5f2a3dbd4f4
compiled_at: 2026-04-24T07:14:46.542Z
---
<wiki>
# What Makes an AI System an Agent? | 是什么让 AI 系统成为「智能体」？

[[05-Introduction|< Previous Chapter]] | [[000-Home|Home]] | [[07-Chapter-01-Prompt-Chaining|Next Chapter >]]

---

## Core Definition of AI Agent
In simple terms, an **AI agent** is a system designed to perceive its environment and take actions to achieve a specific goal. It is an evolution from the standard Large Language Model (LLM), enhanced with the abilities to plan, use tools, and interact with its surroundings. It operates via a 5-step iterative loop to complete tasks:
<mark>简单来说，<strong>AI 智能体</strong>是一个能够感知环境并采取行动以实现特定目标的系统。它从标准大语言模型演进而来，被赋予了规划、使用工具以及与周围环境交互的能力。它遵循一个简单的五步循环来完成任务：</mark>

1. **Get the Mission**: Receive a user-specified goal (e.g., "organize my schedule")
   <mark><strong>获取任务：</strong>接收用户给定的目标（如「帮我安排日程」）</mark>
2. **Scan the Scene**: Gather necessary environmental information (e.g., emails, calendar data, contacts)
   <mark><strong>分析环境：</strong>收集所有必要的环境信息（如邮件、日历数据、联系人）</mark>
3. **Think It Through**: Devise an optimal action plan to achieve the goal
   <mark><strong>思考对策：</strong>制定达成目标的最佳行动计划</mark>
4. **Take Action**: Execute the plan via tool calls (e.g., send invitations, update calendars)
   <mark><strong>采取行动：</strong>通过调用工具执行计划（如发送邀请、更新日历）</mark>
5. **Learn and Get Better**: Observe outcomes and adapt behavior to improve future performance
   <mark><strong>学习并改进：</strong>观察结果并调整行为，以提升未来表现</mark>

![AI Agent Five-Step Loop](images/fig1.png)
**Fig.1**: Agentic AI functions as an intelligent assistant, continuously learning through experience via the five-step loop.
<mark>图 1：AI 智能体如同一位智能助手，通过经验持续学习，依托五步循环完成任务。</mark>

---

## Market & Industry Adoption
AI agents are growing in popularity at an unprecedented rate:
- Majority of large IT companies actively use AI agents, with 20% adopting the technology within the past year (as of 2025)
- AI agent startups raised over $2 billion by the end of 2024, with a total market valuation of $5.2 billion
- Market size is projected to reach nearly $200 billion by 2034
<mark>智能体的普及速度惊人：
- 大多数大型 IT 公司已积极使用智能体，其中20%在过去一年内完成部署（截至2025年）
- 截至2024年底，AI智能体初创公司融资超20亿美元，总市场估值达52亿美元
- 预计2034年市场规模将增长至近2000亿美元
</mark>

---

## AI Paradigm Evolution Timeline
Over 2 years, AI systems have evolved across 4 key stages (see Fig.2):
1. Basic LLM workflows: Reliant on simple prompts and triggers for data processing
2. Retrieval-Augmented Generation (RAG): Improved reliability by grounding model outputs on factual external data
3. Individual AI Agents: Standalone systems capable of using diverse external tools
4. Agentic AI: Collaborative teams of specialized agents working together to complete complex goals
<mark>两年内AI范式历经4个关键阶段的演进（见图2）：
1. 基础LLM工作流：依托简单提示与触发器完成数据处理
2. 检索增强生成（RAG）：通过将模型输出锚定在外部事实数据上提升可靠性
3. 独立AI智能体：可使用多种外部工具的独立系统
4. 智能体AI：由专业化智能体组成的团队协同完成复杂目标
</mark>

![AI Evolution Timeline](images/fig2.png)
**Fig.2**: Transitioning from LLMs to RAG, then to Agentic RAG, and finally to Agentic AI.
<mark>图 2：从 LLM 到 RAG，再到智能体 RAG，最终走向 AI 智能体的演进路径。</mark>

> The intent of this book is to discuss the design patterns of how specialized agents can work in concert and collaborate to achieve complex goals, with one collaboration and interaction paradigm covered in each chapter.
> <mark>本书旨在讨论专业化智能体如何协同工作以实现复杂目标的设计模式，每章将介绍一种协作与交互范式。</mark>

---

## Agent Complexity Levels
AI agents are categorized into 4 levels based on functional complexity (see Fig.3):
![Agent Complexity Levels](images/fig3.png)
**Fig.3**: Instances demonstrating the spectrum of agent complexity.
<mark>图 3：不同复杂度级别的智能体实例。</mark>

### Level 0: The Core Reasoning Engine | 0 级：核心推理引擎
A standard LLM serving as the reasoning core of a basic agentic system, operating without tools, memory, or environment interaction, only responding based on pretrained knowledge. It lacks awareness of current events outside its training data cutoff.
<mark>作为基础智能体系统推理核心的标准大语言模型，无工具、记忆或环境交互能力，仅基于预训练知识响应，无法获取训练数据截止后的时事信息。</mark>

### Level 1: The Connected Problem-Solver | 1 级：连接外部的问题解决者
A functional agent that connects to and utilizes external tools (e.g., search engines, RAG databases, financial APIs) to gather and process information beyond its pretrained knowledge. Its core capability is multi-step interaction with the external world.
<mark>通过连接并使用外部工具（如搜索引擎、RAG数据库、金融API）获取并处理预训练知识外信息的功能性智能体，核心能力是与外部世界的多步交互。</mark>

### Level 2: The Strategic Problem-Solver | 2 级：战略性问题解决者
An agent with expanded capabilities including strategic planning, proactive assistance, and self-improvement, enabled by core skills of prompt engineering and context engineering. It performs context engineering to avoid cognitive overload and improve performance, and can refine its own processes via feedback loops.
<mark>能力扩展至战略规划、主动协助与自我提升的智能体，依托提示工程与上下文工程为核心赋能技能，可通过上下文工程避免认知过载、提升表现，并通过反馈循环优化自身流程。</mark>

#### Core Enabling Skill: Context Engineering | 核心赋能技能：上下文工程
The discipline of strategically selecting, packaging, and managing the most critical information from all available sources to curate a short, focused context for AI models, effectively managing the model's limited attention to prevent overload and ensure high-quality, efficient task performance.
<mark>从所有可用来源中战略性选择、打包、管理最关键信息，为AI模型构建简短、集中的上下文的学科，可有效管理模型有限的注意力，避免过载，确保任务的高质量、高效率完成。</mark>

### Level 3: Collaborative Multi-Agent Systems | 3 级：协作型多智能体系统
A paradigm shift away from single all-powerful agents to teams of specialized agents working in concert, mirroring human organizational structures with division of labor and coordinated effort. Current limitations include LLM reasoning constraints and immature collective learning capabilities, with the long-term goal of automating entire business workflows end-to-end.
<mark>从单一全能智能体转向专业化智能体团队协同工作的范式转变，映射人类组织结构的劳动分工与协调模式。当前限制包括LLM的推理瓶颈与不成熟的集体学习能力，长期目标是端到端自动化完整业务工作流。</mark>

---

## Future of AI Agents: Top 5 Hypotheses | 智能体的未来：五大假设
The next wave of AI agent innovation will focus on improved reliability, collaboration, and real-world integration, with 5 leading hypotheses for future development (see Fig.4):
![Future Agent Hypotheses](images/fig4.png)
**Fig.4**: Five hypotheses about the future of agents
<mark>图 4：关于智能体未来的五个假设</mark>

### Hypothesis 1: The Emergence of the Generalist Agent | 假设 1：通用智能体的崛起
AI agents will evolve from narrow specialists to highly reliable generalists capable of managing complex, ambiguous, long-term goals. An alternative complementary path is the "Lego-like" composition of systems from small specialized expert agents (Small Language Models, SLMs) for lower cost, faster debugging, and easier deployment.
<mark>AI智能体将从狭隘的专家演进为可高可靠性管理复杂、模糊、长期目标的通用型智能
