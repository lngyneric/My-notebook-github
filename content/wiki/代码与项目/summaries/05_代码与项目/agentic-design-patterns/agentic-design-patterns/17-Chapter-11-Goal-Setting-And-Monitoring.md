---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/17-Chapter-11-Goal-Setting-And-Monitoring.md
raw_sha256: 53cd742344cc4e34ce5606022aefcdd8beafde70f7b298877625b2b7f98147de
compiled_at: 2026-04-24T07:43:05.925Z
---
<wiki>
# Chapter 11: Goal Setting and Monitoring
[[16-Chapter-10-Model-Context-Protocol|< Previous Chapter]] | [[000-Home|Home]] | [[18-Chapter-12-Exception-Handling-and-Recovery|Next Chapter >]]

## Summary
For AI agents to be truly effective and purposeful, they need more than just the ability to process information or use tools; they need a clear sense of direction and a way to know if they're actually succeeding. This is where the Goal Setting and Monitoring pattern comes into play. It's about giving agents specific objectives to work towards and equipping them with the means to track their progress and determine if those objectives have been met.
<mark>要让 AI 智能体真正有效且有目的性，它们不仅仅需要处理信息或使用工具的能力，更需要明确的方向感，并能够知道自己是否真的在取得成功。这就是目标设定与监控模式发挥作用的地方。该模式旨在为智能体提供要努力实现的具体目标，并配备跟踪进度和判断这些目标是否实现的手段。</mark>

## Goal Setting and Monitoring Pattern Overview
Think about planning a trip. You don't just spontaneously appear at your destination. You decide where you want to go (the goal state), figure out where you are starting from (the initial state), consider available options (transportation, routes, budget), and then map out a sequence of steps: book tickets, pack bags, travel to the airport/station, board the transport, arrive, find accommodation, etc. This step-by-step process, often considering dependencies and constraints, is fundamentally what we mean by planning in agentic systems.
<mark>想想计划一次旅行。你不会凭空就出现在目的地。你需要决定想去哪里（目标状态），弄清楚从哪里出发（初始状态），考虑可用的选项（交通、路线、预算），然后规划出一系列步骤：订票、打包行李、前往机场/车站、登上交通工具、到达、找到住宿地等。这个逐步进行的过程，通常考虑依赖关系和约束条件，基本上就是我们在智能体系统中所说的规划。</mark>

In the context of AI agents, planning typically involves an agent taking a high-level objective and autonomously, or semi-autonomously, generating a series of intermediate steps or sub-goals. These steps can then be executed sequentially or in a more complex flow, potentially involving other patterns like tool use, routing, or multi-agent collaboration. The planning mechanism might involve sophisticated search algorithms, logical reasoning, or increasingly, leveraging the capabilities of large language models (LLMs) to generate plausible and effective plans based on their training data and understanding of tasks.
<mark>在 AI 智能体的背景下，规划通常涉及智能体接受一个高层目标，自主或半自主地生成一系列中间步骤或子目标。这些步骤可以顺序执行，或以更复杂的流程执行，可能涉及其它模式，如工具使用、路由或多智能体协作。规划机制可能涉及复杂的搜索算法、逻辑推理，或者越来越多地利用大语言模型 (LLMs) 的能力，基于它们的训练数据和任务理解来生成合理且有效的计划。</mark>

A good planning capability allows agents to tackle problems that aren't simple, single-step queries. It enables them to handle multi-faceted requests, adapt to changing circumstances by replanning, and orchestrate complex workflows. It's a foundational pattern that underpins many advanced agentic behaviors, turning a simple reactive system into one that can proactively work towards a defined objective.
<mark>良好的规划能力，使智能体不止能够处理简单的单步查询问题。规划还使得智能体能够处理多个面向的请求，通过重新规划来适应变化，并编排复杂的工作流程。这是一个基础模式，支撑着许多高级智能体行为，将简单的反应式系统，转变为能够主动努力实现既定目标的系统。</mark>

## Practical Applications & Use Cases
The Goal Setting and Monitoring pattern is essential for building agents that can operate autonomously and reliably in complex, real-world scenarios. Here are some practical applications:
<mark>目标设定与监控模式，对于构建能够在复杂现实场景中自主可靠运行的智能体至关重要。以下是一些实际应用：</mark>

* **Customer Support Automation:** An agent's goal might be to "resolve customer's billing inquiry." It monitors the conversation, checks database entries, and uses tools to adjust billing. Success is monitored by confirming the billing change and receiving positive customer feedback. If the issue isn't resolved, it escalates.
   <mark>* **自动化客户支持：** 智能体的目标可能是“解决客户的账单查询”。它监控对话，检查数据库条目，并使用工具调整账单。通过确认账单变更和收到积极的客户反馈来监控是否成功。如果问题未解决，它会升级处理。</mark>
* **Personalized Learning Systems:** A learning agent might have the goal to "improve students' understanding of algebra." It monitors the student's progress on exercises, adapts teaching materials, and tracks performance metrics like accuracy and completion time, adjusting its approach if the student struggles.
   <mark>* **个性化学习系统：** 学习智能体的目标可能是“提高学生对代数的理解”。它监控学生在练习上的进度，调整教学材料，并跟踪准确性和完成时间等性能指标，如果学生遇到困难则调整其方法。</mark>
* **Project Management Assistants:** An agent could be tasked with "ensuring project milestone X is completed by Y date." It monitors task statuses, team communications, and resource availability, flagging delays and suggesting corrective actions if the goal is at risk.
   <mark>* **项目管理助手：** 智能体可以被赋予“确保项目里程碑 X 在 Y 日期前完成”的任务。它监控任务状态、团队沟通和资源可用性，如果目标存在风险，则标记延迟并建议纠正措施。</mark>
* **Automated Trading Bots:** A trading agent's goal might be to "maximize portfolio gains while staying within risk tolerance." It continuously monitors market data, its current portfolio value, and risk indicators, executing trades when conditions align with its goals and adjusting strategy if risk thresholds are breached.
   <mark>* **自动交易机器人：** 交易智能体的目标可能是“在风险容忍范围内最大化投资组合收益”。它持续监控市场数据、当前投资组合价值和风险指标，在条件符合目标时执行交易，如果违反风险阈值则调整策略。</mark>
* **Robotics and Autonomous Vehicles:** An autonomous vehicle's primary goal is "safely transport passengers from A to B." It constantly monitors its environment (other vehicles, pedestrians, traffic signals), its own state (speed, fuel), and its progress along the planned route, adapting its driving behavior to achieve the goal safely and efficiently.
   <mark>* **机器人和自动驾驶车辆：** 自动驾驶车辆的主要目标是“安全地将乘客从 A 点运送到 B 点”。它不断监控环境（其它车辆、行人、交通信号）、自身状态（速度、燃料）以及沿计划路线的进度，调整驾驶行为以安全高效地到达目的地。</mark>
* **Content Moderation:** An agent's goal could be to "identify and remove harmful content from platform X." It monitors incoming content, applies classification models, and tracks metrics like false positives/negatives, adjusting its filtering criteria or escalating ambiguous cases to human reviewers.
   <mark>* **内容审核：** 智能体的目标可能是“识别并删除平台 X 上的有害内容”。它监控输入内容，应用分类模型，并跟踪误报/漏报等指标，调整过滤标准或将不确定的情况升级到人工审核。</mark>

This pattern is fundamental for agents that need to operate reliably, achieve specific outcomes, and adapt to dynamic conditions, providing the necessary framework for intelligent self-management.
<mark>对于需要可靠运行、实现特定结果并适应动态条件的智能体来说，这种模式是基础，它为智能化的自我管理提供了必要的框架。</mark>

## Hands-On Code Example
To illustrate the Goal Setting and Monitoring pattern, we have an example using LangChain and OpenAI APIs. This Python script outlines an autonomous AI agent engineered to generate and refine Python code. Its core function is to produce solutions for specified problems, ensuring adherence to user-defined quality benchmarks.
<mark>为了说明目标设定与监控模式，我们有一个使用 LangChain 和 OpenAI API 的示例。这个 Python 脚本概述了一个自主 AI 智能体，专门用于生成和优化 Python 代码。其核心功能，是为特定问题生成解决方案，并确保符合用户定义的质量基准。</mark>

It employs a "goal-setting and monitoring" pattern where it doesn't just generate code once, but enters into an iterative cycle of creation, self-evaluation, and improvement. The agent's success is measured by its own AI-driven judgment on whether the generated code successfully meets the initial objectives. The ultimate output is a polished, commented, and ready-to-use Python file that represents the culmination of this refinement process.
<mark>它采用“目标设定和监控”模式，不只是生成一次代码，而是进入创建、自我评估和改进的迭代循环。智能体的成功，通过其自身的 AI 驱动判断来衡量，即生成的代码是否满足初始目标
