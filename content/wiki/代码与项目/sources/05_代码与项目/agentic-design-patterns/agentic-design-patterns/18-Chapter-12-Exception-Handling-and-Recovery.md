---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/18-Chapter-12-Exception-Handling-and-Recovery.md
raw_sha256: d9464dd4cf9f453cb9258725b8c7997bcbe4fd1e4618635bda5d5d2bf9332496
compiled_at: 2026-04-14T04:01:26.354Z
---
# 异常处理与恢复（Exception Handling and Recovery）
> 来源路径：`raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/18-Chapter-12-Exception-Handling-and-Recovery.md`

---

## TL;DR
异常处理与恢复是AI智能体的核心设计模式，用于帮助智能体在不可预测的现实环境中处理突发故障、错误，通过主动检测、分级处理、状态恢复机制，保障智能体持续稳定运行，避免整体失效，是构建可靠、有韧性AI智能体的基础能力，可结合反思模式提升故障修复效果。

---

## 模式基础
为使AI智能体能够在多样化的现实环境中可靠运行，它们必须具备管理突发状况、错误和故障的能力。正如人类能适应意外的障碍，智能体也需要强大的系统来检测问题、启动恢复程序，或者至少确保可控的失败。这项基本要求构成了「异常处理与恢复」模式的基础。

该模式专注于开发具有出色的耐用性和韧性的智能体，使其在面对各种困难和异常时仍能保持不间断的功能和操作完整性，它同时强调主动准备和被动响应策略，确保即使在面临挑战时也能持续运行。这种适应能力对于智能体在复杂且不可预测的环境中成功运行至关重要，最终能提升它们的整体效能和可信赖度。

此模式可以和**反思模式**结合使用：如果初次尝试失败并引发异常，反思过程可以分析该失败，并采用更完善的方法（如改进提示词）重新尝试任务，以解决错误。

---

## 核心组件
下图为AI智能体异常处理与恢复的关键组件：
![关键组件](images/chapter12_fig1.png "Key Components")
*图1：AI智能体异常处理与恢复的关键组件*

### 1. 错误检测（Error Detection）
细致识别运行中出现的问题，常见的检测场景包括：
- 工具输出无效或格式错误
- 特定API错误（如404 Not Found、500 Internal Server Error状态码）
- 服务/API响应时间异常延长
- 偏离预期格式的混乱无意义响应
- 可通过其他智能体或专用监控系统实现主动异常检测，在问题升级前捕捉风险

### 2. 错误处理（Error Handling）
检测到错误后执行预设响应策略，常用策略包括：
| 策略 | 说明 |
|------|------|
| 日志记录 | 详细记录错误详情，用于后续调试分析 |
| 重试 | 对瞬时错误，调整参数后重新发起请求/操作 |
| 回退机制 | 切换到替代策略/方法，保障部分功能可用 |
| 优雅降级 | 无法完全恢复时，维持部分功能提供基础服务 |
| 通知机制 | 对需要人工干预的问题，向操作人员/相关方发出警报 |

### 3. 恢复（Recovery）
将智能体/系统恢复到稳定可运行状态，常用机制包括：
- **状态回滚**：撤销最近的更改/事务，消除错误影响
- **诊断与自我纠正**：调查错误原因，调整智能体的计划、逻辑或参数，避免重复出错
- **升级处理**：复杂/严重故障下，将问题上报给人工操作员或更高级系统

---

## 适用场景
任何部署在真实世界场景、无法保证运行条件完美的智能体都需要该模式，典型应用场景：
| 场景 | 具体说明 |
|------|----------|
| 客户服务聊天机器人 | 访问客户数据库宕机时，不会崩溃，可告知用户临时问题、建议重试或转接人工 |
| 自动化金融交易 | 遇到资金不足、市场休市等错误时，记录错误、停止重复无效尝试、通知用户或调整策略 |
| 智能家居自动化 | 控制灯具因网络/设备故障无法点亮时，检测失败后重试，仍失败则通知用户建议手动干预 |
| 数据处理智能体 | 遇到损坏文件时，跳过该文件、记录错误、继续处理其他文件，结束后汇总报告，不中止整个流程 |
| 网页抓取智能体 | 遇到验证码、网站结构变更、服务器错误（404/503等）时，可暂停、切换代理或上报失败URL，实现优雅处理 |
| 机器人与制造 | 机械臂抓取组件因错位失败时，通过传感器检测故障，重新调整重试，持续失败则提醒人工或切换组件 |

---

## 代码示例（Google ADK）
以下示例实现了一个带回退机制的健壮位置检索智能体：
```python
from google.adk.agents import Agent, SequentialAgent
from google.adk.tools import get_general_area_info, get_precise_location_info

# Agent 1: Tries the primary tool. Its focus is narrow and clear.
primary_handler = Agent(
    name="primary_handler",
    model="gemini-2.0-flash-exp",
    instruction="""
Your job is to get precise location information.
Use the get_precise_location_info tool with the user's provided address.
""",
    tools=[get_precise_location_info],
)

# Agent 2: Acts as the fallback handler, checking state to decide its action.
fallback_handler = Agent(
    name="fallback_handler",
    model="gemini-2.0-flash-exp",
    instruction="""
Check if the primary location lookup failed by looking at state["primary_location_failed"].
- If it is True, extract the city from the user's original query and use
  the get_general_area_info tool.
- If it is False, do nothing.
""",
    tools=[get_general_area_info],
)

# Agent 3: Presents the final result from the state.
response_agent = Agent(
    name="response_agent",
    model="gemini-2.0-flash-exp",
    instruction="""
Review the location information stored in state["location_result"].
Present this information clearly and concisely to the user.
If state["location_result"] does not exist or is empty, apologize that you
could not retrieve the location.
""",
)

# The SequentialAgent ensures the handlers run in a guaranteed order.
robust_location_agent = SequentialAgent(
    name="robust_location_agent",
    sub_agents=[primary_handler, fallback_handler, response_agent],
)
```
逻辑说明：通过`SequentialAgent`按预设顺序执行三个子智能体，主智能体尝试获取精确位置，失败后备用智能体通过状态变量感知故障，切换为获取城市级别的泛用位置信息，最终由结果智能体整理结果返回给用户，实现分层异常处理。

---

## 要点速览
| 分类 | 说明 |
|------|------|
| 问题所在 | 在现实环境中运行的AI智能体不可避免会遇到不可预见的故障（工具故障、网络问题、无效数据等），没有结构化异常管理的智能体脆弱不可靠，无法部署在对稳定性要求高的关键场景 |
| 解决之道 | 异常处理与恢复模式提供了标准化方案，赋予智能体预测、管理、从故障中恢复的能力：通过主动检测发现问题，通过日志、重试、回退等策略处理故障，通过状态回滚、自我纠正、升级处理实现恢复，保障智能体在不可预测环境中可靠运行 |
| 经验法则 | 任何部署在动态真实环境、可能遭遇系统/工具/网络故障或不可预测输入、且对运行可靠性有要求的AI智能体，都需要使用该模式 |

---

## 核心要点
1. 「异常处理与恢复」对于构建强大且可靠的智能体至关重要
2. 此模式的核心流程为：检测错误 → 优雅处理错误 → 实施恢复策略
3. 错误检测可通过验证工具输出、检查API错误码、设置超时机制实现
4. 常用错误处理策略包括：日志记录、重试、回退、优雅降级、通知
5. 恢复阶段聚焦于通过诊断、自我纠正或上报，恢复智能体的稳定运行
6. 该模式确保智能体即使在不可预测的现实世界环境中也能有效运行

---

## 可视化总结
![异常处理模式](images/chapter12_fig2.png "Exception handling pattern")
*图2：异常处理模式*

---

## 参考文献
1. McConnell, S. (2004). Code Complete (2nd ed.). Microsoft Press.
2. Shi, Y., Pei, H., Feng, L., Zhang, Y., & Yao, D. (2024). Towards Fault Tolerance in Multi-Agent Reinforcement Learning. arXiv preprint arXiv:2412.00534.
3. O'Neill, V. (2022). Improving Fault Tolerance and Reliability of Heterogeneous Multi-Agent IoT Systems Using Intelligence Transfer. Electronics, 11
