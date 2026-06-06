---
source: raw/04_文档与参考/Markdown文档/pydanticai-101.md
raw_sha256: 79a9d8d81eb8af16f624c0054d1d9a4c70178030391516c2cc4ee41b95796448
compiled_at: 2026-04-24T06:10:22.294Z
---
<wiki>
<p style="text-align:center">
    <a href="https://skills.network" target="_blank">
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
    </a>
</p>

# Build Your First AI Agent with PydanticAI: Customer Chat Support

Estimated time needed: **45** minutes

---

## Abstract
PydanticAI is a Python-based AI agent framework developed by the creators of Pydantic, designed to build reliable, structured, and type-safe LLM-powered applications via a schema-first, developer-centric approach. This guided project walks through building a customer support chatbot trained on Kaggle's customer support ticket dataset, with capabilities to classify queries, assign priorities, flag issues for escalation, and generate consistent responses. It demonstrates how to eliminate the uncertainty of free-form LLM outputs using strongly typed Python models.

---

## Learning Objectives
After completing this lab, you will be able to:
- Understand core concepts of AI agentic systems and their real-world applications
- Use Pydantic for data modeling, validation, and serialization within agent frameworks
- Define and implement modular, structured AI agents using the Pydantic Agentic Framework
- Orchestrate multi-step reasoning and decision-making processes in agents
- Integrate external tools and APIs to enhance agent capabilities
- Design scalable, interpretable, and maintainable agents for production use cases

---

## Setup
### Required Libraries
The following libraries are used in this project:
* `pandas` for tabular data management
* `numpy` for mathematical operations
* `scikit-learn` for machine learning pipeline functions
* `seaborn` for data visualization
* `pydantic-ai` for building production-grade GenAI agent applications

### Installing Required Libraries
```python
!pip install pydantic-ai==0.1.3 pandas==2.2.3 | tail -n1
```

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/nQn6NwuUQcQ7E90e29UJbw/Restarting-the-Kernel.png" width="70%" alt="Restart kernel">
**Note:** Restart the Jupyter kernel after completing library installation.

### Importing Required Libraries
```python
import os
import json
import pandas as pd
from pydantic import BaseModel, validator, Field, field_validator
from openai import OpenAI
from pydantic_ai import Agent, RunContext
import nest_asyncio
from dataclasses import dataclass  
```

---

## Core Framework Concepts
### What is PydanticAI?
PydanticAI is an open-source Python framework built to simplify development of production-ready Generative AI (GenAI) applications. It is designed for developers creating structured, maintainable, and scalable AI agents that use LLMs.

### Motivation for PydanticAI
The Pydantic team built PydanticAI to address gaps in existing LLM tools, which were often too complex, loosely structured, or difficult to scale. Its core goal is to bring the developer-friendly experience of FastAPI (built on Pydantic) to the GenAI application ecosystem.

### Key Features of PydanticAI
1. **Agent-Oriented Design**: Agents act as centralized containers managing prompts, tools, and structured outputs, enabling complex workflows and multi-agent interactions.
2. **Type Safety and Validation**: Leverages Pydantic's robust type system to ensure data integrity and predictable agent behaviors, reducing runtime errors.
3. **Model-Agnostic Compatibility**: Supports all major LLMs including OpenAI, Anthropic, Gemini, Ollama, Groq, Cohere, and Mistral, with a simple interface for integrating additional models.
4. **Pydantic Logfire Integration**: Provides native debugging, performance monitoring, and behavior tracking for full observability of LLM-powered applications.
5. **Python-Centric Approach**: Uses familiar Python control flows and best practices, lowering the barrier to entry for developers building AI projects.

Official documentation: https://ai.pydantic.dev/

---

## Project Resources
### Customer Support Ticket Dataset
This project uses the Kaggle *Customer Support Ticket Dataset* (owner: suraj520), which contains customer support tickets for various tech products. It includes the following fields:
| Field | Description |
|-------|-------------|
| Ticket ID | Unique identifier for each ticket |
| Customer Name | Name of the customer who raised the ticket |
| Customer Email | Anonymized email of the customer |
| Customer Age | Age of the customer |
| Customer Gender | Gender of the customer |
| Product Purchased | Tech product associated with the ticket |
| Date of Purchase | Date the product was purchased |
| Ticket Type | Category of the ticket (technical, billing, product inquiry, etc.) |
| Ticket Subject | Topic of the ticket |
| Ticket Description | Full text of the customer's inquiry |
| Ticket Status | Current status of the ticket (open, closed, pending) |
| Resolution | Solution provided for closed tickets |
| Ticket Priority | Urgency level (low, medium, high, critical) |
| Ticket Channel | Channel used to submit the ticket (email, phone, chat, social media) |
| First Response Time | Time to initial customer response |
| Time to Resolution | Total time to resolve the ticket |
| Customer Satisfaction Rating | 1-5 satisfaction score for closed tickets |

### Load Dataset
```python
path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IJIikY8I-Q79KdIA5WtYIw/customer-support-tickets.csv"
df = pd.read_csv(path)
df.head(5)
```

---

## Agent Implementation
### Step 1: Initialize LLM Client
```python
# Initialize OpenAI client (uses internal authentication in Skills Network environment)
client = OpenAI()
```

### Step 2: Define Structured Response Schema
A Pydantic `BaseModel` is used to enforce the structure, type, and validation rules for all LLM outputs:
```python
from pydantic import BaseModel, Field, field_validator

class SupportResponse(BaseModel):
    category: str = Field(..., description="The issue category")
    priority: str = Field(default="low", description="Issue priority (low, medium, high)")
    escalate: bool = Field(..., description="Should this be escalated to a human?")
    suggested_response: str = Field(..., description="A helpful support reply")

    @field_validator("priority", mode="before")
    @classmethod
    def validate_priority(cls, v):
        valid_priorities = {"low", "medium", "high"}
        if isinstance(v, str) and v.lower() in valid_priorities:
            return v.lower()
        return "low"  # fallback if invalid

    def priority_as_int(self) -> int:
        priority_map = {"low": 1, "medium": 2, "high": 3}
        return priority_map.get(self.priority, 1)
```

### Step 3: Configure System Prompt with Few-Shot Examples
Sample input-output pairs are provided to guide the LLM to generate responses that match the required schema format:
```python
prompt = """
User: I forgot my password and can’t login.
Response:
{
  "category": "Authentication",
  "priority": "High",
  "escalate": true,
  "suggested_response": "You can reset your password from the login page. If that doesn’t work, we'll escalate this issue for manual support."
}

User: Please cancel my account.
Response:
{
  "category": "Subscription",
  "priority": "Medium",
  "escalate": false,
  "suggested_response": "To cancel your subscription, go to Settings > Billing > Cancel Plan. Contact us if you need help."
}
"""
```

### Step 4: What is a PydanticAI Agent?
An Agent is the core component that structures LLM-user interactions. It allows developers to define:
- Input dependencies (`AgentDepsT`: custom context data passed to the agent)
- Expected output type (`OutputDataT`: enforced via Pydantic schemas)
- System prompts and few-shot examples to guide LLM behavior

### Step 5: Initialize the Customer Support Agent
```python
agent = Agent[SupportResponse](
    instructions=f"""
You are a helpful customer support assistant.
You can use this CSV file: {df}

Your task is to:
- Match user input to any ticket using ticket_id, email, or customer_name.
- Respond ONLY using the data in the CSV.
- If no match is found, respond politely asking the user to check their input.
- Output MUST be a valid JSON object in this exact format (no markdown, no prose):

{{
  "category": "Connectivity",
  "priority":
