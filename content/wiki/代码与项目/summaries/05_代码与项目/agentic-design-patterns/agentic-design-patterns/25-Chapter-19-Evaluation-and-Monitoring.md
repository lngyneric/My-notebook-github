---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/25-Chapter-19-Evaluation-and-Monitoring.md
raw_sha256: 17ceff76d6b61079d935dfaef5fe7e00c1bcac9b70b1ac37599e8af282db51d0
compiled_at: 2026-04-24T07:59:33.598Z
---
<wiki>
# Chapter 19: Evaluation and Monitoring
[[24-Chapter-18-Guardrails-Safety-Patterns|< Previous Chapter]] | [[000-Home|Home]] | [[26-Chapter-20-Prioritization|Next Chapter >]]

## Overview
This chapter examines methodologies enabling intelligent agents to systematically assess performance, monitor goal progress, and detect operational anomalies. Unlike Chapter 11 (goal setting/monitoring) and Chapter 17 (Reasoning mechanisms), it focuses on **continuous, external measurement** of agent effectiveness, efficiency, and compliance with requirements. This includes defining metrics, establishing feedback loops, and implementing reporting systems to align agent performance with operational expectations (see Fig.1).

![Best practices for evaluation and monitoring](images/chapter19_fig1.png)
*Fig.1: Best practices for evaluation and monitoring*

---

## Practical Applications & Use Cases
Common applications for agent evaluation and monitoring include:
- **Performance Tracking in Live Systems**: Continuous monitoring of accuracy, latency, and resource consumption for production-deployed agents (e.g., customer service chatbot resolution rate, response time).
- **A/B Testing for Agent Improvements**: Systematic parallel comparison of agent versions/strategies to identify optimal approaches (e.g., two planning algorithms for logistics agents).
- **Compliance and Safety Audits**: Automated audit reports tracking agent adherence to ethical guidelines, regulatory requirements, and safety protocols, with human-in-the-loop/agent verification and KPI/alert triggers.
- **Enterprise Systems**: Governance of Agentic AI via the AI "Contract"—a dynamic agreement codifying objectives, rules, and controls for AI-delegated tasks.
- **Drift Detection**: Monitoring agent output relevance/accuracy over time to detect performance degradation from input data distribution shifts (concept drift) or environmental changes.
- **Anomaly Detection in Agent Behavior**: Identification of unusual agent actions indicating errors, malicious attacks, or emergent undesired behavior.
- **Learning Progress Assessment**: Tracking learning curves, skill improvements, and generalization capabilities for learning-enabled agents.

---

## Hands-On Code Examples
Developing a comprehensive agent evaluation framework is highly complex, but practical implementations focus on critical use cases:

### Agent Response Assessment
Core process for evaluating output quality/accuracy, checking for pertinence, correctness, logic, bias-free content, and alignment with user intent. Basic implementations use exact matching, but real-world use requires advanced metrics:
```py
def evaluate_response_accuracy(agent_output: str, expected_output: str) -> float:
    """Calculates a simple accuracy score for agent responses."""
    # Basic exact match; real-world uses sophisticated metrics
    return 1.0 if agent_output.strip().lower() == expected_output.strip().lower() else 0.0

# Example usage
agent_response = "The capital of France is Paris."
ground_truth = "Paris is the capital of France."
score = evaluate_response_accuracy(agent_response, ground_truth)
print(f"Response accuracy: {score}")
```
*Note: This binary exact-match method fails to account for paraphrasing or semantic equivalence. Advanced metrics include string similarity (Levenshtein, Jaccard), keyword analysis, semantic similarity (embedding cosine similarity), LLM-as-a-Judge, and RAG-specific metrics (faithfulness, relevance).*

### Latency Monitoring
Critical for real-time/interactive applications, measuring agent request processing/output generation duration. Latency data should be logged to persistent storage (e.g., JSON logs, time-series databases, data warehouses, observability platforms).

### Tracking Token Usage for LLM Interactions
Essential for cost management and resource optimization for LLM-powered agents, as billing depends on input/output token counts:
```py
# Conceptual; actual token counting uses LLM API/tokenizer
class LLMInteractionMonitor:
    def __init__(self):
        self.total_input_tokens = 0
        self.total_output_tokens = 0

    def record_interaction(self, prompt: str, response: str):
        # Placeholder: split strings for simulation
        input_tokens = len(prompt.split())
        output_tokens = len(response.split())
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

### Custom Metric for "Helpfulness" using LLM-as-a-Judge
Evaluates subjective qualities (e.g., helpfulness) using an LLM as an evaluator, leveraging advanced linguistic capabilities for nuanced, human-like assessments:
```py
import google.generativeai as genai
import os
import json
import logging
from typing import Optional

# --- Configuration ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set GOOGLE_API_KEY env var to run
try:
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
except KeyError:
    logging.error("Error: GOOGLE_API_KEY environment variable not set.")
    exit(1)

# --- LLM-as-a-Judge Rubric for Legal Survey Quality ---
LEGAL_SURVEY_RUBRIC = """
You are an expert legal survey methodologist and critical legal reviewer. Evaluate the quality of a legal survey question.
Provide a 1-5 score, rationale, and feedback per these criteria:
1. Clarity & Precision (1-5)
2. Neutrality & Bias (1-5)
3. Relevance & Focus (1-5)
4. Completeness (1-5)
5. Appropriateness for Audience (1-5)
Output MUST be a JSON object with keys: overall_score, rationale, detailed_feedback, concerns, recommended_action.
"""

class LLMJudgeForLegalSurvey:
    def __init__(self, model_name: str = 'gemini-1.5-flash-latest', temperature: float = 0.2):
        self.model = genai.GenerativeModel(model_name)
        self.temperature = temperature

    def _generate_prompt(self, survey_question: str) -> str:
        return f"{LEGAL_SURVEY_RUBRIC}\n\n---\n**LEGAL SURVEY QUESTION:**\n{survey_question}\n---"

    def judge_survey_question(self, survey_question: str) -> Optional[dict]:
        full_prompt = self._generate_prompt(survey_question)
        try:
            logging.info(f"Sending request to '{self.model.model_name}'...")
            response = self.model.generate_content(
                full_prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=self.temperature,
                    response_mime_type="application/json"
                )
            )
            if not response.parts:
                logging.error(f"Empty/blocked response. Safety Ratings: {response.prompt_feedback.safety_ratings}")
                return None
            return json.loads(response.text)
        except json.JSONDecodeError:
            logging.error(f"JSON decode failed. Raw response: {response.text}")
            return None
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return None

# --- Example Usage ---
if __name__ == "__main__":
    judge = LLMJudgeForLegalSurvey()
    # Good Example
    good_question = """
    To what extent do you agree/disagree that Swiss IP laws adequately protect AI-generated content (meeting Federal Supreme Court originality criteria)?
    (Select: Strongly Disagree, Disagree, Neutral, Agree, Strongly Agree)
    """
    print("\n--- Evaluating Good Question ---")
    print(json.dumps(judge.judge_survey_question(good_question), indent=2))
    # Biased Example
    biased_question = """
    Don't you agree that restrictive data privacy laws like FADP hinder Swiss tech innovation?
    (Select: Yes, No)
    """
    print("\n--- Evaluating Biased Question ---")
    print(json.dumps(judge.judge_survey_question(biased_question), indent=2))
    # Vague Example
    vague_question = "What are your thoughts on legal tech?"
    print("\n--- Evaluating Vague Question ---")
    print(json.dumps(judge.judge_survey_question(vague_question), indent=2))
```

### Evaluation Methods Comparison
| Evaluation Method | Strengths | Weaknesses |
|-------------------|-----------|------------|
