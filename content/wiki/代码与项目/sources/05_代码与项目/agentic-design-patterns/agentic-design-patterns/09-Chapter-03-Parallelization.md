---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/09-Chapter-03-Parallelization.md
raw_sha256: f678d2fba68be9e6934cbc8c659d66f919ddf5dffb74d77ff6506cdd58e3d18b
compiled_at: 2026-04-14T03:58:23.707Z
---
# 并行化（Parallelization）智能体设计模式

> [!INFO] 来源路径
> `raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/09-Chapter-03-Parallelization.md`

---

## TL;DR
并行化是智能体设计中的核心优化模式，通过同时执行工作流中**互不依赖的子任务**，大幅减少总体执行延迟，尤其适用于多源信息收集、多API调用、多模态处理等包含I/O等待的场景，主流智能体框架（LangChain、LangGraph、Google ADK）均原生支持并行执行能力。

---

## 目录
- [并行模式概述](#并行模式概述)
- [实际应用场景](#实际应用场景)
- [实战代码示例 LangChain](#实战代码示例-langchain)
- [实战代码示例 Google ADK](#实战代码示例-google-adk)
- [要点速览与核心要点](#要点速览与核心要点)
- [参考文献](#参考文献)

---

## 并行模式概述

在前面的章节中，我们探讨了用于顺序工作流的提示链以及用于智能决策的路由模式。虽然这些模式很重要，但许多复杂的智能体任务需要**同时**执行多个子任务，而非一个接一个地执行。这时**并行模式**就变得至关重要。

并行模式涉及同时执行多个组件，例如大语言模型调用、工具使用，甚至整个子智能体。与等待一个步骤完成后再开始下一个步骤不同，并行执行允许独立任务同时运行，这大大缩短了那些可以分解为相互独立部分的任务的总执行时间。

### 顺序 vs 并行对比示例
针对「研究主题并汇总结论」任务，两种执行流程对比如下：
| 顺序执行 | 并行优化 |
|---------|---------|
| 1. 搜索来源A | 1. **同时**搜索来源A和来源B |
| 2. 总结来源A | 2. 搜索完成后，**同时**总结来源A和来源B |
| 3. 搜索来源B | 3. 等待并行步骤完成后，整合结果生成最终答案 |
| 4. 总结来源B | - |
| 5. 整合结果生成最终答案 | - |

并行模式的核心在于找出工作流中互不依赖的环节，并将它们并行执行。在处理外部服务（如 API 或数据库）时，这种做法特别有效，因为可以同时发起多个请求，从而减少总体等待时间。实现并行化通常需要使用支持异步执行、多线程或多进程的框架，现代智能体框架原生都能支持异步操作。

![并行化子智能体示例](images/chapter03_fig1.png)
*图 1：使用子智能体进行并行化的示例*

主流框架的并行支持：
- **LangChain (LCEL)**：通过组合可运行对象、设计并发分支结构实现并行执行
- **LangGraph**：基于图拓扑结构，允许单次状态转换触发多个无依赖节点，实现工作流并行分支
- **Google ADK**：提供原生的并行执行管理能力，支持多智能体并发运行，提升复杂多智能体系统的效率和可扩展性

---

## 实际应用场景

并行模式可以在各种场景中使用以提升智能体性能，常见用例如下：

### 1. 信息收集和研究
- **用例**：研究某个公司的智能体
- **并行任务**：同时搜索新闻、拉取股票数据、监测社交媒体提及、查询公司数据库
- **好处**：比逐项查找更快获得全面信息

### 2. 数据处理和分析
- **用例**：分析客户反馈的智能体
- **并行任务**：在一批反馈中同时进行情感分析、关键词提取、反馈分类、紧急问题识别
- **好处**：快速提供多角度的分析

### 3. 多API或工具交互
- **用例**：旅行规划智能体
- **并行任务**：同时检查航班价格、搜索酒店可用性、查询当地活动、查找推荐餐厅
- **好处**：更快速地制定出完整的旅行行程

### 4. 多组件内容生成
- **用例**：撰写营销邮件的智能体
- **并行任务**：同时生成邮件主题、撰写正文、查找相关图片、设计号召性按钮文案
- **好处**：更高效地组装出最终邮件

### 5. 验证和核实
- **用例**：验证用户输入的智能体
- **并行任务**：同时检查邮件格式、验证电话号码、在数据库核对地址、检查不当内容
- **好处**：能够更快地反馈输入是否有效

### 6. 多模态处理
- **用例**：分析包含文本和图像的社交媒体帖子的智能体
- **并行任务**：同时分析文本的情感和关键词、分析图像的对象和场景描述
- **好处**：能更快地综合来自不同模态的信息与洞见

### 7. A/B测试或多种方案生成
- **用例**：生成多个创意文案的智能体
- **并行任务**：同时使用稍微不同的提示或模型为同一篇文章生成三条不同标题
- **好处**：可以快速比较各个方案并选出最优者

---

## 实战代码示例：LangChain

在 LangChain 框架中，通过 LangChain 表达式语言（LCEL）可以实现并行执行。常见做法是把多个可运行组件组织成字典或列表，并把这个集合作为输入传给链中的下一个组件，LCEL 执行器会并行执行集合中的各个可运行项。

完整可运行示例代码（已同步维护）：[Chapter-03-Parallelization-LangChain-Example.py](/codes/Chapter-03-Parallelization-LangChain-Example.py)
> 译者注：原Colab链接：https://colab.research.google.com/drive/1uK1r9p-5sdX0ffMjAi_dbIkaMedb1sTj

```python
import os
import asyncio
from typing import Optional

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable, RunnableParallel, RunnablePassthrough

# 安装依赖
# pip install langchain langchain-community langchain-openai langgraph python-dotenv

# 为了更好的安全性，建议从 .env 文件加载环境变量
from dotenv import load_dotenv
load_dotenv()

# --- Configuration ---
# 确保你的 API 密钥环境变量已设置 (如 OPENAI_API_KEY)
try:
    llm: Optional[ChatOpenAI] = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    if llm:
        print(f"Language model initialized: {llm.model_name}")
except Exception as e:
    print(f"Error initializing language model: {e}")
    llm = None


# --- Define Independent Chains ---
# These three chains represent distinct tasks that can be executed in parallel.
# 这三条链代表彼此独立、可同时执行的任务。
summarize_chain: Runnable = (
    ChatPromptTemplate.from_messages([
        ("system", "Summarize the following topic concisely:"),
        ("user", "{topic}")
    ])
    | llm
    | StrOutputParser()
)

questions_chain: Runnable = (
    ChatPromptTemplate.from_messages([
        ("system", "Generate three interesting questions about the following topic:"),
        ("user", "{topic}")
    ])
    | llm
    | StrOutputParser()
)

terms_chain: Runnable = (
    ChatPromptTemplate.from_messages([
        ("system", "Identify 5-10 key terms from the following topic, separated by commas:"),
        ("user", "{topic}")
    ])
    | llm
    | StrOutputParser()
)


# --- Build the Parallel + Synthesis Chain ---
# 1. Define the block of tasks to run in parallel. The results of these,
#    along with the original topic, will be fed into the next step.
# --- 定义要并行执行的任务块。这些结果以及原始内容将作为输入传递给下一步。
map_chain = RunnableParallel(
    {
        "summary": summarize_chain,
        "questions": questions_chain,
        "key_terms": terms_chain,
        "topic": RunnablePassthrough(),  # Pass the original topic through
    }
)

# 2. Define the final synthesis prompt which will combine the parallel results.
# --- 定义最终的综合提示，将并行结果合并。
synthesis_prompt = ChatPromptTemplate.from_messages([
    ("system", """Based on the following information:
     Summary: {summary}
     Related Questions: {questions}
     Key Terms: {key_terms
