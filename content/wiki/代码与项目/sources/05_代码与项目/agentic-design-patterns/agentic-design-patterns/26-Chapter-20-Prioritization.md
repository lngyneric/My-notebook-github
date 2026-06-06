---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/26-Chapter-20-Prioritization.md
raw_sha256: 849bc0c3075ea9518ad0ed2022a91d6396b67cd62ff4b9d49dfc92472bd804f1
compiled_at: 2026-04-14T04:03:48.756Z
---
# 优先级排序模式（Prioritization Pattern）
> 本文整理自 [Agentic Design Patterns 第二十章](raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/26-Chapter-20-Prioritization.md)

---

## TL;DR
优先级排序模式是智能体设计的核心模式之一，用于解决复杂动态环境下智能体面对大量潜在行动、冲突目标和有限资源时的决策问题：智能体通过**定义评估标准→任务评估→选择调度→动态重排**的流程，对任务/目标/行动按重要性、紧迫性、依赖关系等标准排序，保证智能体聚焦最高优先级的任务，提升效能和目标对齐能力。该模式可应用在高层目标排序、子任务排序、即时行动选择多个层级，是构建稳健智能体的基础能力。

---

## 模式概述
### 问题背景
在复杂多变的环境中，智能体常常面临大量潜在行动、相互冲突的目标以及有限的资源。如果缺乏明确的流程来决定下一步行动，智能体可能会出现效率降低、运行延迟，甚至无法实现关键目标等问题。

### 核心要素
智能体优先级排序通常包含四个核心步骤：
| 要素 | 说明 |
|------|------|
| 1. 标准定义 | 建立任务评估的规则/指标，常见维度包括：<br>- 紧迫性：任务的时间敏感度<br>- 重要性：对核心目标的影响程度<br>- 依赖关系：任务是否是其他任务的前置条件<br>- 资源可用性：所需工具/信息的就绪状态<br>- 成本收益：投入与预期产出的对比<br>- 用户偏好：针对个性化智能体的用户自定义偏好 |
| 2. 任务评估 | 根据定义好的标准评估每个潜在任务，方法可从简单规则到LLM复杂评分/推理 |
| 3. 调度/选择逻辑 | 基于评估结果选择最优下一步行动或任务序列，可使用基础队列或高级规划组件实现 |
| 4. 动态重新排序 | 环境变化时（新关键事件出现、截止日期临近等）调整优先级，保证智能体的适应性和响应能力 |

### 适用层级
优先级排序可应用在多个决策层级：
1. 高层目标优先级排序：选择总体核心目标
2. 子任务优先级排序：安排计划内的步骤顺序
3. 即时行动选择：从可用选项中选择下一个立即执行的行动

---

## 实际应用场景
| 领域 | 应用说明 |
|------|----------|
| 自动化客户支持 | 优先处理系统故障这类紧急请求，高价值客户可获得优先级倾斜，非紧急请求（如密码重置）后置 |
| 云计算资源调度 | 高峰时段优先为关键应用分配资源，非紧急批处理任务安排到非高峰时段优化成本 |
| 自动驾驶系统 | 持续对行动排序保证安全效率，例如制动避撞的优先级高于保持车道/优化燃油效率 |
| 金融交易 | 交易机器人结合市场状况、风险承受、利润率、实时新闻确定交易优先级，保证高优先级交易快速执行 |
| 项目管理 | AI智能体结合截止日期、依赖关系、团队可用情况、战略重要性对项目看板任务排序 |
| 网络安全 | 网络监控智能体结合威胁严重程度、潜在影响、资产关键性对告警排序，优先响应最高危威胁 |
| 个人助理AI | 结合用户定义优先级、截止日期、当前上下文整理日历、提醒、通知，管理用户日常生活 |

---

## 实战代码示例：基于LangChain的项目经理智能体
以下代码实现了一个可对任务创建、排序、分配的项目经理AI智能体，完整展示优先级排序模式的应用：
```python
import os
import asyncio
from typing import List, Optional, Dict, Type
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain.memory import ConversationBufferMemory

# --- 0. Configuration and Setup ---
# Loads the OPENAI_API_KEY from the .env file.
load_dotenv()

# The ChatOpenAI client automatically picks up the API key from the environment.
llm = ChatOpenAI(temperature=0.5, model="gpt-4o-mini")

# --- 1. Task Management System ---
class Task(BaseModel):
    """Represents a single task in the system."""
    id: str
    description: str
    priority: Optional[str] = None  # P0, P1, P2
    assigned_to: Optional[str] = None # Name of the worker

class SuperSimpleTaskManager:
    """An efficient and robust in-memory task manager."""
    def __init__(self):
        # Use a dictionary for O(1) lookups, updates, and deletions.
        self.tasks: Dict[str, Task] = {}
        self.next_task_id = 1

    def create_task(self, description: str) -> Task:
        """Creates and stores a new task."""
        task_id = f"TASK-{self.next_task_id:03d}"
        new_task = Task(id=task_id, description=description)
        self.tasks[task_id] = new_task
        self.next_task_id += 1
        print(f"DEBUG: Task created - {task_id}: {description}")
        return new_task

    def update_task(self, task_id: str, **kwargs) -> Optional[Task]:
        """Safely updates a task using Pydantic's model_copy."""
        task = self.tasks.get(task_id)
        if task:
            # Use model_copy for type-safe updates.
            update_data = {k: v for k, v in kwargs.items() if v is not None}
            updated_task = task.model_copy(update=update_data)
            self.tasks[task_id] = updated_task
            print(f"DEBUG: Task {task_id} updated with {update_data}")
            return updated_task
        print(f"DEBUG: Task {task_id} not found for update.")
        return None

    def list_all_tasks(self) -> str:
        """Lists all tasks currently in the system."""
        if not self.tasks:
            return "No tasks in the system."

        task_strings = []
        for task in self.tasks.values():
            task_strings.append(
                f"ID: {task.id}, Desc: '{task.description}', "
                f"Priority: {task.priority or 'N/A'}, "
                f"Assigned To: {task.assigned_to or 'N/A'}"
            )
        return "Current Tasks:\n" + "\n".join(task_strings)

task_manager = SuperSimpleTaskManager()

# --- 2. Tools for the Project Manager Agent ---
# Use Pydantic models for tool arguments for better validation and clarity.
class CreateTaskArgs(BaseModel):
    description: str = Field(description="A detailed description of the task.")

class PriorityArgs(BaseModel):
    task_id: str = Field(description="The ID of the task to update, e.g., 'TASK-001'.")
    priority: str = Field(description="The priority to set. Must be one of: 'P0', 'P1', 'P2'.")

class AssignWorkerArgs(BaseModel):
    task_id: str = Field(description="The ID of the task to update, e.g., 'TASK-001'.")
    worker_name: str = Field(description="The name of the worker to assign the task to.")

def create_new_task_tool(description: str) -> str:
    """Creates a new project task with the given description."""
    task = task_manager.create_task(description)
    return f"Created task {task.id}: '{task.description}'."

def assign_priority_to_task_tool(task_id: str, priority: str) -> str:
    """Assigns a priority (P0, P1, P2) to a given task ID."""
    if priority not in ["P0", "P1", "P2"]:
        return "Invalid priority. Must be P0, P1, or P2."
    task = task_manager.update_task(task_id, priority=priority)
    return f"Assigned priority {priority} to task {task.id}." if task else f"Task {task_id} not found."

def assign_task_to_worker_tool(task_id: str, worker_name: str) -> str:
    """Assigns a task to a specific worker."""
    task = task_manager.update_task(task_id, assigned_to=worker_name)
    return f"Assigned task {task.id} to {worker_name}." if task else f"Task {task_id} not found."

# All tools the PM agent can
