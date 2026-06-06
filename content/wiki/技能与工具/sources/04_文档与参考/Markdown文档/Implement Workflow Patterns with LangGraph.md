---
source: raw/04_文档与参考/Markdown文档/Implement Workflow Patterns with LangGraph.md
raw_sha256: 207100f9b7bb095fb6bbe0bf8166bb26402b9548b6534bc4a6faa1b4ae0e2f4f
compiled_at: 2026-04-14T03:51:13.982Z
---
# Implement Workflow Patterns with LangGraph

> 来源路径：`raw/04_文档与参考/Markdown文档/Implement Workflow Patterns with LangGraph.md`

## TL;DR
本教程是一个时长约45分钟的实践实验，讲解了如何使用LangGraph实现三类核心AI工作流模式：**提示链（Prompt Chaining）、基于意图的路由（Routing）、并行执行（Parallelization）**。通过求职助手、任务分类器、多语言翻译助手三个示例，以及一个多代理路由系统的练习，演示了如何将单个大模型组装为协调的多代理企业AI系统。

---

## 目录
- [要点概览](#要点概览)
- [环境准备](#环境准备)
- [工作流模式1：提示链（Prompt Chaining）](#工作流模式1提示链-prompt-chaining)
  - [求职助手示例（生成个性化求职信）](#use-case-prompt-chaining--求职助手)
  - [LangGraph实现](#langGraph实现提示链)
- [工作流模式2：路由（Routing）](#工作流模式2路由-routing)
  - [任务分类器示例（摘要/翻译路由）](#use-case-routing--任务分类器)
  - [LangGraph实现](#langGraph实现路由)
- [工作流模式3：并行化（Parallelization）](#工作流模式3并行化-parallelization)
  - [多语言翻译助手示例](#use-case-parallelization--多语言翻译助手)
  - [LangGraph实现](#langGraph实现并行化)
- [练习：构建多代理服务路由系统](#练习-building-a-multi-agent-routing-system)
- [作者与版本信息](#作者与版本信息)

---

## 要点概览
| 工作流模式 | 核心思想 | 典型应用场景 |
| ---- | ---- | ---- |
| **提示链（Prompt Chaining）** | 将复杂任务分解为顺序依赖的LLM调用，每一步基于前一步输出迭代 | 分步生成文案、自动报告生成、教育内容创作 |
| **路由（Routing）** | 由路由器节点对输入分类，转发给对应 specialised 处理节点 | 多意图客服机器人、多技能代理、自适应教育机器人 |
| **并行化（Parallelization）** | 多个独立任务同时执行，完成后聚合结果，提升效率 | 大文档分块同时摘要、批量翻译、多输出变体生成、多代理共识投票 |

> [!NOTE] 引用证据
> 这些经过验证的模式——顺序代理协调、基于意图的路由和并行代理执行——构成了每个企业AI系统的基础。学完后你将获得架构知识，能够创建智能编排多个专用代理解决复杂问题的AI应用。
> <br>—— 原文档引言

---

## 环境准备

```python
%%capture
%pip install langchain-openai==0.3.27
%pip install langgraph==0.6.6
%pip install pygraphviz==1.14
```

```python
from langgraph.graph import StateGraph, END,START
from typing import TypedDict
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph
```

辅助工具函数：
```python
def print_workflow_info(workflow, app=None):
    """Prints comprehensive information about a LangGraph workflow."""
    print("WORKFLOW INFORMATION")
    print("====================")
    print(f"Nodes: {workflow.nodes}")
    print(f"Edges: {workflow.edges}")

    # Use getter method for finish points if available
    try:
        finish_points = workflow.finish_points
        print(f"Finish points: {finish_points}")
    except:
        try:
            # Alternative approaches
            print(f"Finish point: {workflow._finish_point}")
        except:
            print("Finish points attribute not directly accessible")

    if app:
        print("\nWorkflow Visualization:")
        from IPython.display import display
        display(app.get_graph().draw_png())
```

初始化LLM：
```python
llm = ChatOpenAI(model="gpt-4o-mini")
```

---

## 工作流模式1：提示链（Prompt Chaining）

### 核心概念
提示链将复杂任务分解为顺序的LLM调用序列，每一步依赖前一步的输出，符合人类拆解复杂问题的思路，每个节点（步骤）职责明确，支持在步骤间插入外部工具。

#### 典型结构
1. 初始LLM提示（例如生成草稿）
2. 优化提示（例如调整风格语气）
3. 评估或格式化（例如转换为指定格式、评估质量）

> [!NOTE] 引用证据
> 这种方法模仿了人类处理复杂问题的方式——将其分解为可管理的步骤。它利用函数调用、顺序链和/或AI代理，通常使用LangChain、LangGraph甚至自定义脚本实现。关键在于模块化和清晰性——每个节点（或步骤）在整个管道中都有特定的角色。

---

### Use Case: Prompt Chaining — 求职助手
本示例目标：根据给定的职位描述，生成定制化的简历摘要和求职信，任务分为两个顺序步骤：
1. 根据职位描述生成匹配的简历摘要
2. 使用简历摘要生成个性化求职信

首先定义状态结构，在节点间共享数据：
```python
class ChainState(TypedDict):
    job_description: str
    resume_summary: str
    cover_letter: str
```

初始状态示例：
```python
state = {
    "job_description": "We are looking for a data scientist with experience in machine learning, NLP..", 
    "resume_summary": "",
    "cover_letter": ""
}
```

第一步完成后状态演变：
```python
state = {
    "job_description": "We are looking for a data scientist with experience in machine learning, NLP..", 
    "resume_summary": "Results-driven data scientist with expertise in machine learning...",
    "cover_letter": ""
}
```

#### 简历摘要代理
```python
def generate_resume_summary(state: ChainState) -> ChainState:
    prompt = f"""
You're a resume assistant. Read the following job description and summarize the key qualifications and experience the ideal candidate should have, phrased as if from the perspective of a strong applicant's resume summary.

Job Description:
{state['job_description']}
"""

    response = llm.invoke(prompt)

    return {**state, "resume_summary": response.content}
```

#### 生成求职信代理
```python
def generate_cover_letter(state: ChainState) -> ChainState:
    prompt = f"""
You're a cover letter writing assistant. Using the resume summary below, write a professional and personalized cover letter for the following job.

Resume Summary:
{state['resume_summary']}

Job Description:
{state['job_description']}
"""

    response = llm.invoke(prompt)

    return {**state, "cover_letter": response.content}
```

---

### LangGraph实现提示链

```python
# 初始化状态图
workflow = StateGraph(ChainState)

# 添加节点
workflow.add_node("generate_resume_summary", generate_resume_summary)
workflow.add_node("generate_cover_letter", generate_cover_letter)

# 设置入口点
workflow.set_entry_point("generate_resume_summary")

# 添加边连接两个节点
workflow.add_edge("generate_resume_summary", "generate_cover_letter")

# 设置结束点
workflow.set_finish_point("generate_cover_letter")

# 查看工作流信息
print_workflow_info(workflow)

# 编译为可执行应用
app = workflow.compile()
```

可视化工作流（Jupyter环境）：
```python
from IPython.display import Image, display
display(Image(app.get_graph().draw_png()))
```

运行工作流：
```python
input_state = {
        "job_description": "We are looking for a data scientist with experience in machine learning, NLP, and Python. Prior work with large datasets and experience deploying models into production is required."
}
result = app.invoke(input_state)
# 查看结果：result['resume_summary'], result['cover_letter']
```

---

## 工作流模式2：路由（Routing）

### 核心概念
路由模式中，路由器代理（LLM）对输入分类，然后转发给对应的专用处理代理，适合处理多种用户意图/任务类型的场景，比单个大模型处理所有任务更高效专业。

常见路由技术：
1. 硬编码关键词路由（基础方案）
2. 基于LLM分类的路由
3. 基于嵌入的语义匹配路由

> [!NOTE] 引用证据
> 它就像一个总机——一个智能节点（分类器或路由器）分析
