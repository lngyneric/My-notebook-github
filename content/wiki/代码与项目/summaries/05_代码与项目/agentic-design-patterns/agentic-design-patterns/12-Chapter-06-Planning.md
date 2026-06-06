---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/12-Chapter-06-Planning.md
raw_sha256: 736f366322f72a9ef27851d6aed9220331c42a9db7e4b3fda20613c920699463
compiled_at: 2026-04-24T07:28:34.556Z
---
<wiki>
# Chapter 6: Planning | 第六章：规划
[[11-Chapter-05-Tool-Use|< Previous Chapter]] | [[000-Home|Home]] | [[13-Chapter-07-Multi-Agent-Collaboration|Next Chapter >]]

## Summary | 摘要
Intelligent behavior often involves more than just reacting to the immediate input. It requires foresight, breaking down complex tasks into smaller, manageable steps, and strategizing how to achieve a desired outcome. This is where the Planning pattern comes into play. At its core, planning is the ability for an agent or a system of agents to formulate a sequence of actions to move from an initial state towards a goal state.
<mark>智能行为远不止对眼前输入作出反应。它需要前瞻性，需要把复杂任务拆解为更小且可管理的步骤，并制定实现预期结果的策略。这正是规划模式发挥作用之处。其核心在于：智能体（或智能体系统）能够制定一系列行动，使系统从初始状态迈向目标状态。</mark>

---

## Planning Pattern Overview | 规划模式概览
In the context of AI, it's helpful to think of a planning agent as a specialist to whom you delegate a complex goal. When you ask it to "organize a team offsite," you are defining the what—the objective and its constraints—but not the how. The agent's core task is to autonomously chart a course to that goal. It must first understand the initial state (e.g., budget, number of participants, desired dates) and the goal state (a successfully booked offsite), and then discover the optimal sequence of actions to connect them. The plan is not known in advance; it is created in response to the request.
<mark>在 AI 的语境下，把规划智能体看作可以委派复杂目标的专家会更容易理解。当你请它「组织团队外出活动」时，你声明了需要它「做什么」——目标及其约束条件——而不是定义「如何做」。智能体的核心任务是自主规划通往该目标的路径：首先是要弄清楚当前状况（如预算、人数、日期）和目标状态（如已经成功预订的外出活动），然后找出将两者衔接起来的最佳行动步骤。而且这个计划并非预先存在的，而是根据请求即时生成的。</mark>

A hallmark of this process is adaptability. An initial plan is merely a starting point, not a rigid script. The agent's real power is its ability to incorporate new information and steer the project around obstacles. For instance, if the preferred venue becomes unavailable or a chosen caterer is fully booked, a capable agent doesn't simply fail. It adapts. It registers the new constraint, re-evaluates its options, and formulates a new plan, perhaps by suggesting alternative venues or dates.
<mark>这一过程的关键是灵活应变。初步计划只是出发点，而非僵硬的指令。智能体的真正能力在于接纳新信息，并在遇到阻碍时调整路线。比如，当首选场地临时无法使用或选定的餐饮服务已约满时，有能力的智能体不会就此终止，而是会根据新的约束重新评估可选方案，制定替代计划，如建议更换场地或调整日期。</mark>

However, it is crucial to recognize the trade-off between flexibility and predictability. Dynamic planning is a specific tool, not a universal solution. When a problem's solution is already well-understood and repeatable, constraining the agent to a predetermined, fixed workflow is more effective. This approach limits the agent's autonomy to reduce uncertainty and the risk of unpredictable behavior, guaranteeing a reliable and consistent outcome. Therefore, the decision to use a planning agent versus a simple task-execution agent hinges on a single question: does the "how" need to be discovered, or is it already known?
<mark>然而，我们必须认识到灵活性与可预测性之间的权衡。动态规划是一个专用工具，而非万能解。当问题的解决方法已经清楚且可以重复时，让智能体遵循预先设定的固定流程通常更有效。通过限制智能体的自主性，可以降低不确定性和不可预测行为的风险，从而确保结果更加可靠一致。因此，是否采用规划型智能体还是简单的任务处理型智能体，关键点在于：「如何做」的方案是否需要探索，还是已经明确了？</mark>

---

## Practical Applications & Use Cases | 实际应用场景
The Planning pattern is a core computational process in autonomous systems, enabling an agent to synthesize a sequence of actions to achieve a specified goal, particularly within dynamic or complex environments. This process transforms a high-level objective into a structured plan composed of discrete, executable steps.
<mark>规划是自主系统的核心计算过程之一，它使智能体能够在动态或复杂的环境中，设计出一连串动作来实现特定目标。该过程把高层次的目标转化为由若干可执行的具体步骤组成的结构化计划。</mark>

In domains such as procedural task automation, planning is used to orchestrate complex workflows. For example, a business process like onboarding a new employee can be decomposed into a directed sequence of sub-tasks, such as creating system accounts, assigning training modules, and coordinating with different departments. The agent generates a plan to execute these steps in a logical order, invoking necessary tools or interacting with various systems to manage dependencies.
<mark>在流程自动化等领域，规划用于编排复杂工作流。例如，新员工入职这样的业务流程可以分解成一系列有序的子任务，如创建系统账户、分配培训课程、与各部门协调等。智能体会制定计划，并按逻辑顺序执行这些步骤，调用必要的工具或与各类系统交互，以处理各项依赖关系。</mark>

Within robotics and autonomous navigation, planning is fundamental for state-space traversal. A system, whether a physical robot or a virtual entity, must generate a path or sequence of actions to transition from an initial state to a goal state. This involves optimizing for metrics such as time or energy consumption while adhering to environmental constraints, like avoiding obstacles or following traffic regulations.
<mark>在机器人与自主导航中，规划是进行状态空间遍历的核心。无论是实体机器人还是虚拟主体，系统都需要生成路径或动作序列，从起始状态到达目标状态。这个过程要在遵守环境约束（如避障或遵守交通法规）的前提下，优化时间、能耗等指标。</mark>

This pattern is also critical for structured information synthesis. When tasked with generating a complex output like a research report, an agent can formulate a plan that includes distinct phases for information gathering, data summarization, content structuring, and iterative refinement. Similarly, in customer support scenarios involving multi-step problem resolution, an agent can create and follow a systematic plan for diagnosis, solution implementation, and escalation.
<mark>这种模式对结构化的信息整合也至关重要。当任务需要生成研究报告等复杂输出时，智能体可以制定包含信息收集、数据归纳、内容结构化与迭代打磨等阶段的计划。在涉及多步骤问题解决的客户支持场景中，智能体也能制定并执行一套系统化流程来进行诊断、实施解决方案并在必要时升级处理。</mark>

In essence, the Planning pattern allows an agent to move beyond simple, reactive actions to goal-oriented behavior. It provides the logical framework necessary to solve problems that require a coherent sequence of interdependent operations.
<mark>本质上，规划模式使智能体不再局限于简单的被动反应，而是能够以目标为导向地行动。它为解决那些需要一系列相互关联步骤才能完成的问题，提供了必要的逻辑框架。</mark>

---

## Hands-on Implementation: Crew AI | 实战代码：使用 Crew AI
The following section will demonstrate an implementation of the Planner pattern using the Crew AI framework. This pattern involves an agent that first formulates a multi-step plan to address a complex query and then executes that plan sequentially.
<mark>接下来我们将演示如何使用 CrewAI 框架实现规划模式。该模式中，智能体先制定多步骤的计划来解决复杂请求，然后按步骤依次执行该计划。</mark>

```python
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

# Load environment variables from .env file for security
# 从 .env 文件加载环境变量（如 OPENAI_API_KEY）
load_dotenv()

# 1. Explicitly define the language model for clarity
# 明确指定使用的模型
llm = ChatOpenAI(model="gpt-4-turbo")

# 2. Define a clear and focused agent
# 定义一个目标明确且聚焦的智能体
planner_writer_agent = Agent(
    role='Article Planner and Writer',
    goal='Plan and then write a concise, engaging summary on a specified topic.',
    backstory=(
        'You are an expert technical writer and content strategist. '
        'Your strength lies in creating a clear, actionable plan before writing, '
        'ensuring the final summary is both informative and easy to digest.'
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm # Assign the specific LLM to the agent
)

# 3. Define a task with a more structured and
