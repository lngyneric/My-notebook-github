---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/25-Chapter-19-Evaluation-and-Monitoring.md
raw_sha256: 17ceff76d6b61079d935dfaef5fe7e00c1bcac9b70b1ac37599e8af282db51d0
compiled_at: 2026-04-14T04:03:32.916Z
---
# 评估与监控（Evaluation and Monitoring）

> 本文整理自 *Agentic Design Patterns* 第19章

---

## TL;DR
评估与监控是智能体系统在生产环境中保障性能、合规性与可靠性的核心设计模式。不同于传统确定性软件测试，智能体的概率性、动态性特征要求对最终输出**和**智能体执行轨迹（决策步骤序列）进行持续多维度评估，涵盖响应质量、延迟、资源消耗、行为合规性等多种指标，支持漂移检测、异常发现、A/B测试与合规审计。面向高风险复杂任务，领域正在从简单提示驱动的智能体向基于正式合约的"高级承包商"范式演进，通过明确规范、协商反馈、迭代自验证、分层分解决构保障结果可验证、可问责。

---

## 目录
- [实际应用与用例](#实际应用与用例)
- [常用评估方法对比](#常用评估方法对比)
- [智能体轨迹评估](#智能体轨迹评估)
- [从智能体到高级承包商范式](#从智能体到高级承包商范式)
- [Google ADK 评估支持](#google-adk-评估支持)
- [要点速览](#要点速览)
- [关键要点](#关键要点)
- [参考文献](#参考文献)

---

## 实际应用与用例
评估与监控最常见的应用场景包括：
| 场景 | 说明 |
|------|------|
| 实时系统性能跟踪 | 持续监控生产环境智能体的准确率、延迟、资源消耗（例如客服聊天机器人的问题解决率、响应时间） |
| 智能体改进A/B测试 | 并行对比不同智能体版本/策略的性能，识别最优方案（例如为物流智能体测试两种不同规划算法） |
| 合规性与安全审计 | 自动生成审计报告跟踪智能体对伦理准则、监管要求、安全协议的遵守情况，支持人工/其他智能体验证，异常时生成KPI或触发警报 |
| 企业系统智能体治理 | 需要新型控制工具`AI合约`，对AI委托任务的目标、规则、控制进行编码，实现企业级Agentic AI治理 |
| 漂移检测 | 随时间监控智能体输出的相关性/准确性，检测因输入数据分布变化（概念漂移）或环境变化导致的性能下降 |
| 智能体行为异常检测 | 识别智能体的异常/非预期行为，指示错误、恶意攻击或涌现的非预期行为 |
| 学习进展评估 | 针对可学习智能体，跟踪其学习曲线、特定技能改进、跨任务/数据集的泛化能力 |

---

## 实战代码示例
### 1. 智能体响应准确性基础评估
基础的精确匹配评估仅适用于非常简单的场景，无法处理语义等价的同义改写：
```py
def evaluate_response_accuracy(agent_output: str, expected_output: str) -> float:
    """Calculates a simple accuracy score for agent responses."""
    # This is a very basic exact match; real-world would use more sophisticated metrics
    return 1.0 if agent_output.strip().lower() == expected_output.strip().lower() else 0.0

# Example usage
agent_response = "The capital of France is Paris."
ground_truth = "Paris is the capital of France."
score = evaluate_response_accuracy(agent_response, ground_truth)
print(f"Response accuracy: {score}")
```
> 上述示例中两个句子语义完全一致，但因为逐字符不匹配，会错误返回0分。实际场景需要更复杂的指标，包括：字符串相似性（莱文斯坦距离、Jaccard相似性）、关键词分析、基于嵌入的语义相似性、LLM-as-a-Judge评估、RAG专属指标（忠实度、相关性）等。

### 2. LLM交互Token使用跟踪
基于LLM的智能体需要跟踪Token用量用于成本管理与资源优化，以下是概念实现（实际场景需要使用LLM官方分词器获得精确计数）：
```py
# This is conceptual as actual token counting depends on the LLM API
class LLMInteractionMonitor:
    def __init__(self):
        self.total_input_tokens = 0
        self.total_output_tokens = 0

    def record_interaction(self, prompt: str, response: str):
        # In a real scenario, use LLM API's token counter or a tokenizer
        input_tokens = len(prompt.split())  # Placeholder
        output_tokens = len(response.split())  # Placeholder
        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens
        print(f"Recorded interaction: Input tokens={input_tokens}, Output tokens={output_tokens}")

    def get_total_tokens(self):
        return self.total_input_tokens, self.total_output_tokens

# Example usage
monitor = LLMInteractionMonitor()
monitor.record_interaction("What is the capital of France?", "The capital of France is Paris.")
monitor.record_interaction("Tell me a joke.", "Why don't scientists trust atoms? Because they make up everything!")
input_t, output_t = monitor.get_total_tokens()
print(f"Total input tokens: {input_t}, Total output tokens: {output_t}")
```

### 3. LLM-as-a-Judge 自定义"有用性"评估
针对主观质量评估（例如法律调查问题质量），可以使用LLM作为评判者基于预设评分标准进行评估：
```py
import google.generativeai as genai
import os
import json
import logging
from typing import Optional

# --- Configuration ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set your API key as an environment variable to run this script
# For example, in your terminal: export GOOGLE_API_KEY='your_key_here'
try:
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
except KeyError:
    logging.error("Error: GOOGLE_API_KEY environment variable not set.")
    exit(1)

# --- LLM-as-a-Judge Rubric for Legal Survey Quality ---
LEGAL_SURVEY_RUBRIC = """
You are an expert legal survey methodologist and a critical legal reviewer. Your task is to evaluate the quality of a given legal survey question.

Provide a score from 1 to 5 for overall quality, along with a detailed rationale and specific feedback.

Focus on the following criteria:

1. **Clarity & Precision (Score 1-5):**
   * 1: Extremely vague, highly ambiguous, or confusing.
   * 3: Moderately clear, but could be more precise.
   * 5: Perfectly clear, unambiguous, and precise in its legal terminology (if applicable) and intent.

2. **Neutrality & Bias (Score 1-5):**
   * 1: Highly leading or biased, clearly influencing the respondent towards a specific answer.
   * 3: Slightly suggestive or could be interpreted as leading.
   * 5: Completely neutral, objective, and free from any leading language or loaded terms.

3. **Relevance & Focus (Score 1-5):**
   * 1: Irrelevant to the stated survey topic or out of scope.
   * 3: Loosely related but could be more focused.
   * 5: Directly relevant to the survey's objectives and well-focused on a single concept.

4. **Completeness (Score 1-5):**
   * 1: Omits critical information needed to answer accurately or provides insufficient context.
   * 3: Mostly complete, but minor details are missing.
   * 5: Provides all necessary context and information for the respondent to answer thoroughly.

5. **Appropriateness for Audience (Score 1-5):**
   * 1: Uses jargon inaccessible to the target audience or is overly simplistic for experts.
   * 3: Generally appropriate, but some terms might be challenging or oversimplified.
   * 5: Perfectly tailored to the assumed legal knowledge and background of the target survey audience.

**Output Format:**
Your response MUST be a JSON object with the following keys:
* `overall_score`: An integer from 1 to 5 (average of criterion scores, or your holistic judgment).
* `rationale`: A concise summary of why this score was given, highlighting major strengths and weaknesses.
* `detailed_feedback`: A bullet-point list detailing feedback for each criterion (Clarity, Neutrality, Relevance, Completeness, Audience Appropriateness). Suggest specific improvements.
* `concerns`: A list of any specific legal, ethical, or methodological concerns.
* `recommended_action`: A brief recommendation (e.g., "Revise for neutrality", "Approve as is", "Clarify scope").
"""

class LLMJudgeForLegalSurvey:
    """A class to evaluate legal survey questions using a generative AI model."""

    def __init__(self, model_name: str = 'gemini-
