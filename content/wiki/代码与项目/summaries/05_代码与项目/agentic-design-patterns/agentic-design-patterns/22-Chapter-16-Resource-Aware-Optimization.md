---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/22-Chapter-16-Resource-Aware-Optimization.md
raw_sha256: bf5585039eecb0e46ef73d2ab29705e5eb3fd3958cf050bf5620154b772fae6a
compiled_at: 2026-04-24T07:54:26.265Z
---
<wiki>
# Chapter 16: Resource-Aware Optimization
**Navigation**: [[21-Chapter-15-Inter-Agent-Communication|< Previous Chapter]] | [[000-Home|Home]] | [[23-Chapter-17-Reasoning-Techniques|Next Chapter >]]

## Overview
Resource-Aware Optimization enables intelligent agents to dynamically monitor and manage computational, temporal, and financial resources during operation. This differs from simple planning, which primarily focuses on action sequencing. Resource-Aware Optimization requires agents to make decisions regarding action execution to achieve goals within specified resource budgets or to optimize efficiency, including tradeoffs between accurate but expensive models and fast, low-cost models, or between additional compute for refined outputs and faster, less detailed responses.

*Illustrative Example*: An agent tasked with financial dataset analysis will use a fast, low-cost model to generate immediate preliminary reports for time-sensitive requests, and allocate additional resources to a powerful, high-precision predictive model for high-stakes investment forecasts with larger budget and time allowances.

A core strategy in this pattern is the **fallback mechanism**: when a preferred model is unavailable (due to overload, throttling, or service failure), the system automatically switches to a default or lower-cost alternative to ensure graceful degradation and service continuity, rather than complete system failure.

## Practical Applications & Use Cases
Common real-world use cases include:
- **Cost-Optimized LLM Usage**: Agents select between large, expensive LLMs for complex tasks and smaller, affordable LLMs for simple queries based on predefined budget constraints.
- **Latency-Sensitive Operations**: In real-time systems, agents choose faster, less comprehensive reasoning paths to meet strict response time requirements.
- **Energy Efficiency**: Agents deployed on edge or power-constrained devices optimize processing workflows to conserve battery life.
- **Fallback for Service Reliability**: Agents automatically switch to backup models when primary models are unavailable, ensuring service continuity and graceful degradation.
- **Data Usage Management**: Agents use summarized data retrieval instead of full dataset downloads to reduce bandwidth and storage consumption.
- **Adaptive Task Allocation**: In multi-agent systems, agents self-assign tasks based on their current computational load and available time resources.

## Hands-On Code Examples
### Google ADK Implementation
Google's Agent Development Kit (ADK) supports resource-aware optimization via a multi-agent architecture, enabling modular, scalable applications with:
- Native support for Gemini models and third-party model integration via LiteLLM
- LLM-driven dynamic routing for adaptive behavior
- Built-in performance evaluation capabilities for system refinement

#### Example: Hierarchical Travel Planner Agent
- High-level planning (complex request parsing, itinerary breakdown, logical reasoning) is handled by a high-capacity LLM (Gemini Pro)
- Low-level repetitive tool calls (flight price lookup, hotel availability checks, restaurant review searches) are handled by a fast, low-cost LLM (Gemini Flash)

##### Dual Agent Definition
```python
# Conceptual Python-like structure, not runnable code
from google.adk.agents import Agent

# Agent using the more expensive Gemini Pro 2.5
gemini_pro_agent = Agent(
   name="GeminiProAgent",
   model="gemini-2.5-pro",
   description="A highly capable agent for complex queries.",
   instruction="You are an expert assistant for complex problem-solving."
)

# Agent using the less expensive Gemini Flash 2.5
gemini_flash_agent = Agent(
   name="GeminiFlashAgent",
   model="gemini-2.5-flash",
   description="A fast and efficient agent for simple queries.",
   instruction="You are a quick assistant for straightforward questions."
)
```

#### Router Agent
A Router Agent directs queries to the appropriate downstream agent/model based on task complexity. Simple implementations use heuristic metrics (e.g., query word count), while sophisticated versions use LLMs or ML models to analyze query nuance. Optimization techniques for router agents include prompt tuning and fine-tuning on labeled query/model datasets to improve routing accuracy.

```python
# Conceptual Python-like structure, not runnable code
from google.adk.agents import Agent, BaseAgent
from google.adk.events import Event
from google.adk.agents.invocation_context import InvocationContext
import asyncio

class QueryRouterAgent(BaseAgent):
   name: str = "QueryRouter"
   description: str = "Routes user queries to the appropriate LLM agent based on complexity."

   async def _run_async_impl(self, context: InvocationContext) -> AsyncGenerator[Event, None]:
       user_query = context.current_message.text
       query_length = len(user_query.split()) # Simple complexity metric: word count

       if query_length < 20:
           print(f"Routing to Gemini Flash Agent for short query (length: {query_length})")
           response = await gemini_flash_agent.run_async(context.current_message)
           yield Event(author=self.name, content=f"Flash Agent processed: {response}")
       else:
           print(f"Routing to Gemini Pro Agent for long query (length: {query_length})")
           response = await gemini_pro_agent.run_async(context.current_message)
           yield Event(author=self.name, content=f"Pro Agent processed: {response}")
```

#### Critique Agent
A Critique Agent evaluates LLM responses to enable self-correction, performance monitoring, and routing logic refinement. It identifies errors or inconsistencies, tracks accuracy and relevance metrics, and provides feedback to improve router agent decision-making, indirectly optimizing resource allocation and cost efficiency.

Critique Agent system prompt template:
```python
CRITIC_SYSTEM_PROMPT = """
You are the **Critic Agent**, serving as the quality assurance arm of our collaborative research assistant system. Your primary function is to **meticulously review and challenge** information from the Researcher Agent, guaranteeing **accuracy, completeness, and unbiased presentation**.
Your duties encompass:
* **Assessing research findings** for factual correctness, thoroughness, and potential leanings.
* **Identifying any missing data** or inconsistencies in reasoning.
* **Raising critical questions** that could refine or expand the current understanding.
* **Offering constructive suggestions** for enhancement or exploring different angles.
* **Validating that the final output is comprehensive** and balanced.
All criticism must be constructive. Your goal is to fortify the research, not invalidate it. Structure your feedback clearly, drawing attention to specific points for revision. Your overarching aim is to ensure the final research product meets the highest possible quality standards.
"""
```

### OpenAI Implementation
This implementation uses a 3-way query classification system to route requests to optimized processing paths:
1. `simple`: Direct factual questions, routed to low-cost `gpt-4o-mini`
2. `reasoning`: Multi-step logic/math queries, routed to high-performance `o4-mini`
3. `internet_search`: Current/up-to-date information queries, routed to `gpt-4o` with Google Custom Search context

Full code (MIT licensed, available at https://github.com/mahtabsyed/21-Agentic-Patterns/blob/main/16_Resource_Aware_Opt_LLM_Reflection_v2.ipynb):
```python
# MIT License
# Copyright (c) 2025 Mahtab Syed
# https://www.linkedin.com/in/mahtabsyed/

import os
import requests
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_CUSTOM_SEARCH_API_KEY = os.getenv("GOOGLE_CUSTOM_SEARCH_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

if not OPENAI_API_KEY or not GOOGLE_CUSTOM_SEARCH_API_KEY or not GOOGLE_CSE_ID:
    raise ValueError(
        "Please set OPENAI_API_KEY, GOOGLE_CUSTOM_SEARCH_API_KEY, and GOOGLE_CSE_ID in your .env file."
    )

client = OpenAI(api_key=OPENAI_API_KEY)

# --- Step 1: Classify the Prompt ---
def classify_prompt(prompt: str) -> dict:
    system_message = {
        "role": "system",
        "content": (
            "You are a classifier that analyzes user prompts and returns one of three categories ONLY:\n\n"
            "- simple\n"
            "- reasoning\n"
            "- internet_search\n\n"
            "Rules:\n"
            "- Use 'simple' for direct factual questions that need no reasoning or current events.\n"
            "- Use 'reasoning' for logic, math, or multi-step inference questions.\n"
            "- Use 'internet_search' if the prompt refers to current events, recent data, or things not in your training data.\n\n"
            "Respond ONLY with JSON like:\n"
            '{ "classification": "simple" }'
        ),
    }

    user_message = {"role": "user", "content": prompt}

    response = client.chat.completions.create(
        model="gpt-4o", messages=[system_message
