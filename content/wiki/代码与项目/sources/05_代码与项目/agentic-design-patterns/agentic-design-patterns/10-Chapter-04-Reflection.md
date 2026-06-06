---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/10-Chapter-04-Reflection.md
raw_sha256: 04de0caf51707f4774ee00abbe66102385d8d16eb3f188cf9b239a8194345dcd
compiled_at: 2026-04-14T03:58:40.072Z
---
# 第四章：反思（Reflection）
> 来源路径：`raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/10-Chapter-04-Reflection.md`

[[上一章：并行化 | 09-Chapter-03-Parallelization](09-Chapter-03-Parallelization.md) | [首页 | 000-Home](000-Home.md) | [下一章：工具使用 | 11-Chapter-05-Tool-Use](11-Chapter-05-Tool-Use.md)

---

## TL;DR
反思模式是智能体的核心设计模式，通过引入**反馈循环**让智能体能够评估自身输出、修正错误，最终产出更高质量的结果。典型实现为**生产者-评论者（Producer-Critic）双智能体架构，通过职责分离避免自我审查的认知偏见，通过多轮迭代逐步优化输出。该模式以额外的调用成本和延迟换取输出质量提升，适合对准确性、完整性要求高的非实时场景。

---

## 反思模式概述

在前面的章节中，我们已经探讨了智能体的基础模式：用于顺序执行的提示链（Prompt Chaining）、用于动态路径选择的路由（Routing），以及用于并发任务执行的并行模式（Parallelization）。这些模式使智能体能够更高效、更灵活地执行复杂任务。然而，即使工作流设计再精妙，智能体初始输出或计划也未必最优、准确或完整。这正是**反思（Reflection）模式**发挥作用之处。

反思模式是指智能体评估自己的工作、输出和内部状态，并利用评估结果改进性能和优化响应。这是一种自我纠正或自我改进的形式，智能体可以根据反馈、内部剖析及与期望标准的比较，不断优化输出、调整方法。反思有时也可由独立的智能体承担，其职责是专门分析初始智能体的输出。

和直接传递输出的顺序链、选路模式不同，反思模式引入了反馈循环：智能体产出结果后，会回过头审视输出（或生成过程），识别潜在问题与改进空间，再基于这些洞察生成更优版本，或是修正后续行动策略。

### 反思的典型流程：
1. **执行**：智能体执行任务，生成初始输出
2. **评估/剖析**：智能体（通常通过额外的大模型调用或规则集）基于事实准确性、连贯性、完整性、指令符合度等标准分析上一步结果
3. **反思/优化**：根据评估结果确定改进方向，可能包括生成优化后的输出、调整后续步骤参数、甚至修改整体计划
4. **迭代（可选但常用）**：重复上述流程，直到结果满足要求或达到停止条件

### 生产者-评论者模型
反思模式一个高效的经典实现，是将流程拆分为两个独立逻辑角色，也称为「生成器-评论者」或「生产者-审查者」模型：
1. **生产者智能体**：负责完成任务的初始执行，专注生成内容（编写代码、起草内容、制定计划等），接收初始提示后产出第一版输出。
2. **评论者智能体**：唯一职责是评估生产者的输出，通常会赋予明确的角色设定（如高级工程师、严谨事实核查员），按特定标准分析生产者工作，找出缺陷、提出改进建议、输出结构化反馈。

这种职责分离可以避免智能体自我审查时的认知偏见，评论者以全新视角完全专注于发现问题，反馈回传给生产者后生成更优版本。本文提供的代码示例都实现了这个双智能体模型：LangChain示例使用特定的`reflector_prompt`创建评论者角色，Google ADK示例明确定义了生产者和审查者两个独立智能体。

实现反思通常需要构建包含反馈循环的工作流，可以通过代码迭代循环，或是使用支持状态管理、条件跳转的框架完成。单步评估优化可以在LangChain/LangGraph、ADK或Crew.AI中实现，但完整的迭代反思需要更复杂的编排。

反思模式和其他模块的协同：
- 和**目标设定与监控（见第11章）：目标为自我评估提供基准，监控跟踪进度，反思作为纠偏引擎，基于监控反馈调整策略，让智能体从被动执行者变为主动适应的目标驱动系统。
- 和**对话记忆（见第8章）：记忆为评估提供完整上下文，让智能体结合历史交互、用户反馈和演化目标评估输出，从过去的反馈中学习避免重复错误，让反思成为累积性的优化过程，显著提升有效性。

---

## 实际应用场景
当输出质量、准确性或对复杂约束的遵从性要求较高时，反思模式非常适用，典型场景包括：

| 应用场景 | 用例 | 反思流程 | 收益 |
|---------|------|----------|------|
| 创意写作与内容生成 | 撰写博客文章 | 生成草稿 → 从流畅性、语气、清晰度评估 → 根据反馈重写，重复直到符合质量标准 | 产出更精致有效的内容 |
| 代码生成与调试 | 编写Python函数 | 生成初始代码 → 运行测试/静态分析 → 识别错误/低效点 → 基于发现优化代码 | 生成更健壮、功能完整的代码 |
| 复杂问题解决 | 解决逻辑谜题 | 提出步骤 → 评估是否推进求解、是否引入矛盾 → 需要时回退选择其他步骤 | 提升智能体在复杂问题空间的探索能力 |
| 摘要与信息综合 | 总结长文档 | 生成初始摘要 → 和原文要点对照 → 补充遗漏信息修正错误 | 生成更准确全面的摘要 |
| 规划与策略 | 规划实现目标的行动序列 | 生成计划 → 模拟执行/根据约束评估可行性 → 根据评估结果修订计划 | 制定更有效、更符合实际的计划 |
| 对话智能体 | 客户支持聊天机器人 | 用户回复后，回顾对话历史和上一轮生成内容 → 确认连贯性、准确性，保证正确响应用户最新输入 | 实现更自然高效的对话 |

反思模式为智能体系统增加了元认知能力，使其能从自身处理过程和输出中学习，最终产出更智能、可靠、高质量的结果。

---

## 实战示例：LangChain 实现
完整迭代反思需要状态管理和循环执行机制，本示例通过LangChain + GPT-4o实现迭代反思循环，逐步优化计算阶乘的Python函数，直到满足要求后停止。

### 前置准备
安装依赖：
```bash
pip install langchain langchain-community langchain-openai python-dotenv
```
配置大模型API密钥（本示例使用OpenAI）。

### 完整代码
<details>
<summary>点击展开完整代码</summary>

```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

# Colab 可运行版本：https://colab.research.google.com/drive/1xnL6Rky6nsm4iAhomLnUK3kgwSyyYZfb
# 本地维护版本：/codes/Chapter-04-Reflection-LangChain-Example.py

# --- Configuration ---
# Load environment variables from .env file (for OPENAI_API_KEY)
load_dotenv()

# Check if the API key is set
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found in .env file. Please add it.")

# Initialize the Chat LLM. We use a powerful model like gpt-4o for better reasoning.
# A lower temperature is used for more deterministic and focused outputs.
llm = ChatOpenAI(model="gpt-4o", temperature=0.1)


def run_reflection_loop():
    """
    Demonstrates a multi-step AI reflection loop to progressively improve a Python function.
    展示了通过多步骤反思循环，逐步改进 Python 函数的方法。
    """

    # --- The Core Task ---
    task_prompt = """
    Your task is to create a Python function named `calculate_factorial`.
    This function should do the following:
    1.  Accept a single integer `n` as input.
    2.  Calculate its factorial (n!).
    3.  Include a clear docstring explaining what the function does.
    4.  Handle edge cases: The factorial of 0 is 1.
    5.  Handle invalid input: Raise a ValueError if the input is a negative number.
    """

    # --- The Reflection Loop ---
    max_iterations = 3
    current_code = ""
    # We will build a conversation history to provide context in each step.
    message_history = [HumanMessage(content=task_prompt)]

    for i in range(max_iterations):
        print("\n" + "="*25 + f" REFLECTION
