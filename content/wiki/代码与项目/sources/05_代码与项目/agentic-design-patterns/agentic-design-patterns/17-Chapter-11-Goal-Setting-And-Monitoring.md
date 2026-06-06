---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/17-Chapter-11-Goal-Setting-And-Monitoring.md
raw_sha256: 53cd742344cc4e34ce5606022aefcdd8beafde70f7b298877625b2b7f98147de
compiled_at: 2026-04-14T04:01:00.948Z
---
# 目标设定与监控（Goal Setting and Monitoring）
> 来源路径：`raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/17-Chapter-11-Goal-Setting-And-Monitoring.md`

## TL;DR
目标设定与监控是智能体系统的核心基础模式，它为AI智能体赋予明确目标与自我评估能力，让智能体可以自主跟踪进度、判断目标是否达成，并通过反馈循环调整行动，从而将简单的反应式系统转变为能够主动应对复杂多步骤任务、适应动态环境的目标导向系统。

---

## 目录
- [模式概述](#模式概述)
- [实际应用场景](#实际应用场景)
- [实战代码示例](#实战代码示例)
- [要点速览](#要点速览)
- [核心要点](#核心要点)
- [结语](#结语)
- [参考文献](#参考文献)

---

## 模式概述
要让 AI 智能体真正有效且有目的性，它们不仅仅需要处理信息或使用工具的能力，更需要明确的方向感，并能够知道自己是否真的在取得成功。这就是目标设定与监控模式发挥作用的地方。该模式旨在为智能体提供要努力实现的具体目标，并配备跟踪进度和判断这些目标是否实现的手段。

规划是目标设定与监控模式的核心基础，类比旅行计划：你需要确定目的地（目标状态）、起点（初始状态）、可用选项（交通、路线、预算），再规划出订票、打包、出行等一系列依赖约束下的步骤，这就是智能体系统中规划的本质。

在AI智能体场景中，规划通常是智能体接收高层目标后，自主/半自主生成一系列中间步骤或子目标，这些步骤可顺序执行或按复杂流程执行，可能结合工具使用、路由、多智能体协作等其他模式。规划机制可使用复杂搜索算法、逻辑推理，现在也越来越多地借助大语言模型（LLM）基于训练数据和任务理解生成合理有效的计划。

良好的规划能力让智能体可以处理非简单单步的问题，支持多维度请求，通过重规划适应环境变化，编排复杂工作流，是支撑众多高级智能体行为的基础模式。

---

## 实际应用场景
目标设定与监控模式对于构建能够在复杂现实场景中自主可靠运行的智能体至关重要，典型应用场景包括：

| 场景领域 | 具体目标与监控逻辑 |
|---------|------------------|
| 自动化客户支持 | 目标：解决客户账单查询<br>监控：跟踪对话、检查账单变更、收集客户反馈，未解决则升级处理 |
| 个性化学习系统 | 目标：提高学生对代数的理解<br>监控：跟踪练习进度、准确率、完成时间，学生遇到困难则调整教学方法 |
| 项目管理助手 | 目标：确保项目里程碑X在Y日期前完成<br>监控：跟踪任务状态、团队沟通、资源可用性，目标存在风险则标记延迟并给出纠正建议 |
| 自动交易机器人 | 目标：在风险容忍范围内最大化投资组合收益<br>监控：持续跟踪市场数据、组合价值、风险指标，触发目标条件则执行交易，突破风险阈值则调整策略 |
| 机器人和自动驾驶车辆 | 目标：安全地将乘客从A点运送到B点<br>监控：持续感知环境（其他车辆、行人、信号灯）、自身状态（速度、燃油）、路线进度，调整驾驶行为安全高效完成目标 |
| 内容审核 | 目标：识别并删除平台X上的有害内容<br>监控：跟踪输入内容、跟踪误报/漏报指标，调整过滤规则，不确定内容转人工审核 |

该模式是需要可靠运行、实现特定结果、适应动态环境的智能体的基础，为智能化自我管理提供必要框架。

---

## 实战代码示例
### 示例说明
本示例基于LangChain和OpenAI API实现了一个可自主生成并优化Python代码的AI智能体，核心是采用目标设定与监控的迭代循环：不只生成一次代码，而是进入「创建→自我评估→优化」的迭代过程，通过LLM判断生成代码是否满足初始目标，最终输出润色完善、可直接使用的Python文件。

### 依赖项
`pip install langchain_openai openai python-dotenv`，需要在`.env`文件中配置`OPENAI_API_KEY`

### 完整代码
译者注：可在线运行的[Colab版本](https://colab.research.google.com/drive/1553L0BIxqhPFS6RHiLnF_ELjEkWZpqsC?usp=drive_open)，也可下载本地版本[此处](/codes/17-Chapter-11-Goal-Setting-and-Monitoring-Example.py)。

```python
# MIT License
# Copyright (c) 2025 Mahtab Syed
# https://www.linkedin.com/in/mahtabsyed/

"""
Hands-On Code Example - Iteration 2
- To illustrate the Goal Setting and Monitoring pattern, we have an example using LangChain and OpenAI APIs:

Objective: Build an AI Agent which can write code for a specified use case based on specified goals:
- Accepts a coding problem (use case) in code or can be as input.
- Accepts a list of goals (e.g., "simple", "tested", "handles edge cases")  in code or can be input.
- Uses an LLM (like GPT-4o) to generate and refine Python code until the goals are met. (I am using max 5 iterations, this could be based on a set goal as well)
- To check if we have met our goals I am asking the LLM to judge this and answer just True or False which makes it easier to stop the iterations.
- Saves the final code in a .py file with a clean filename and a header comment.
"""

import os
import random
import re
from pathlib import Path
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv

# 🔐 Load environment variables
# 🔐 加载环境变量
_ = load_dotenv(find_dotenv())
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
   raise EnvironmentError("❌ Please set the OPENAI_API_KEY environment variable.")
   # ❌ 请设置 OPENAI_API_KEY 环境变量

# ✅ Initialize OpenAI model
# ✅ 初始化 OpenAI 模型
print("📡 Initializing OpenAI LLM (gpt-4o)...")
llm = ChatOpenAI(
   model="gpt-4o", # If you dont have access to got-4o use other OpenAI LLMs
                  # 如果你没有 gpt-4o 的访问权限，可以使用其他 OpenAI LLM
   temperature=0.3,
   openai_api_key=OPENAI_API_KEY,
)

# --- Utility Functions ---
# --- 实用工具函数 ---

def generate_prompt(
   use_case: str, goals: list[str], previous_code: str = "", feedback: str = ""
) -> str:
   print("📝 Constructing prompt for code generation...")
   # 📝 正在构建代码生成的提示词...
   base_prompt = f"""
You are an AI coding agent. Your job is to write Python code based on the following use case:

Use Case: {use_case}

Your goals are:
{chr(10).join(f"- {g.strip()}" for g in goals)}
"""
   if previous_code:
       print("🔄 Adding previous code to the prompt for refinement.")
       # 🔄 将之前的代码添加到提示词中进行改进
       base_prompt += f"\nPreviously generated code:\n{previous_code}"
   if feedback:
       print("📋 Including feedback for revision.")
       # 📋 包含反馈信息用于修订
       base_prompt += f"\nFeedback on previous version:\n{feedback}\n"

   base_prompt += "\nPlease return only the revised Python code. Do not include comments or explanations outside the code."
   # 请只返回修订后的 Python 代码。不要包含代码之外的注释或解释
   return base_prompt

def get_code_feedback(code: str, goals: list[str]) -> str:
   print("🔍 Evaluating code against the goals...")
   # 🔍 正在根据目标评估代码...
   feedback_prompt = f"""
You are a Python code reviewer. A code snippet is shown below. Based on the following goals:

{chr(10).join(f"- {g.strip()}" for g in goals)}

Please critique this code and identify if the goals are met. Mention if improvements are needed for clarity, simplicity, correctness, edge case handling, or test coverage.

Code:
{code}
"""
   return llm.invoke(feedback_prompt
