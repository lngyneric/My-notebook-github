---
source: raw/04_文档与参考/Markdown文档/pydanticai-101.md
raw_sha256: 79a9d8d81eb8af16f624c0054d1d9a4c70178030391516c2cc4ee41b95796448
compiled_at: 2026-04-14T03:52:24.427Z
---
> 来源路径：`raw/04_文档与参考/Markdown文档/pydanticai-101.md`

# Build Your First AI Agent with PydanticAI: Customer Chat Support

预计完成时间：**45** 分钟

---

## TL;DR
这是一份PydanticAI入门实践教程，带你基于PydanticAI框架构建结构化分类的客户支持聊天机器人，使用 Kaggle 客户支持工单数据集训练，实现用户查询分类、优先级分配、 escalation 判断和标准化响应生成，帮助开发者理解PydanticAI**模式优先、类型安全**的AI Agent开发思路。

---

## 要点
- PydanticAI是Pydantic团队开发的Python原生GenAI框架，核心思路是把AI Agent视为强类型函数，保证LLM输出可预测、可验证
- 核心优势：面向Agent设计、类型安全与数据校验、多LLM模型兼容、与Pydantic Logfire原生集成、Python原生开发体验
- 本实践最终产出：可运行的结构化客户支持聊天机器人，支持对话分类、优先级判定、人工 escalation 推荐
- 配套有练习任务：基于PydanticAI实现情绪+饮食偏好适配的食谱推荐AI助手

---

## 正文内容

<p style="text-align:center">
    <a href="https://skills.network" target="_blank">
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
    </a>
</p>

PydanticAI is an innovative, Python-based framework developed by the creators of Pydantic, designed to build reliable, structured, and type-safe AI agents powered by Large Language Models (LLMs). Unlike traditional prompt-centric AI development, PydanticAI introduces a schema-first, developer-centric approach that ensures LLM responses are predictable, validated, and aligned with strongly typed Python models.

At the heart of PydanticAI is the idea of treating AI agents as strongly typed functions. Developers define the inputs and outputs of their agents using standard Pydantic models, and the framework ensures that all AI responses conform to these constraints. This tight integration between LLM reasoning and Python typing empowers developers to build robust agents without the uncertainty and fragility commonly associated with free-form LLM outputs.
 
Here in this guided project, we are building a customer support chatbot using PydanticAI, trained on Kaggle's customer support ticket dataset. The chatbot uses structured schemas to classify user queries into categories, assign priority levels, escalate where necessary, and generate consistent, professional responses.

It’s a practical, real-world application that highlights how to turn raw AI potential into operational excellence—all using type-safe models and modular agent design.

Whether you’re building support bots, legal agents, data annotators, or AI workflow chains, PydanticAI empowers you to build with confidence, clarity, and control—without compromising on the power of LLMs.


## __Table of Contents__

<ol>
    <li><a href="#Objectives">Objectives</a></li>
    <li>
        <a href="#Setup">Setup</a>
        <ol>
            <li><a href="#Installing-Required-Libraries">Installing Required Libraries</a></li>
            <li><a href="#Importing-Required-Libraries">Importing Required Libraries</a></li>
            <li><a href="#Defining-Helper-Functions">Defining Helper Functions</a></li>
        </ol>
    </li>
    <li>
        <a href="#What-is-PydanticAI?">What is PydanticAI?</a>
         <li><a href="#Why-was-PydanticAI-created?"> Why was PydanticAI created?</a></li>
        <li><a href="#Key-Features-of-PydanticAI:">Key Features of PydanticAI:</a></li>
         <li><a href="#About-Dataset">About Dataset</a></li>
    <li><a href="#Load-Dataset">Load Dataset</a></li>
    </li>
    <li><a href="#What-is-an-Agent?">What is an Agent?</a></li>
    <li><a href="#What-is-nest_asyncio?">What is nest_asyncio?</a></li>
</ol>

<a href="#Exercises">Exercises</a>


## Objectives

After completing this lab you will be able to:

- Understand the core concepts of AI agentic systems and their applications.
- Learn how to use Pydantic for data modeling, validation, and serialization within agent frameworks.
- Define and implement modular, structured AI agents using the Pydantic Agentic Framework.
- Orchestrate multi-step reasoning and decision-making processes in agents.
- Integrate external tools and APIs to enhance agent capabilities.
- Design agents that are scalable, interpretable, and maintainable for real-world use cases.


----


## Setup


For this lab, we will be using the following libraries:

*   [`pandas`](https://pandas.pydata.org/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMML0187ENSkillsNetwork31430127-2021-01-01) for managing the data.
*   [`numpy`](https://numpy.org/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMML0187ENSkillsNetwork31430127-2021-01-01) for mathematical operations.
*   [`sklearn`](https://scikit-learn.org/stable/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMML0187ENSkillsNetwork31430127-2021-01-01) for machine learning and machine-learning-pipeline related functions.
*   [`seaborn`](https://seaborn.pydata.org/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMML0187ENSkillsNetwork31430127-2021-01-01) for visualizing the data.
*   [`pydentic-ai`](https://ai.pydantic.dev/) is a Python agent framework designed to build production grade applications with Generative AI.


### Installing Required Libraries

```python
!pip install pydantic-ai==0.1.3 pandas==2.2.3 | tail -n1
```

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/nQn6NwuUQcQ7E90e29UJbw/Restarting-the-Kernel.png" width="70%" alt="Restart kernel">

**Note:** After completing the library installation, the next step is to restart the kernel.


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

# What is PydanticAI?
PydanticAI is a powerful open-source Python framework built to simplify the process of developing production-ready applications using Generative AI (GenAI), such as Large Language Models (LLMs). 

It’s designed for developers who want to create smart AI agents and applications that are structured, maintainable, and scalable.

# Why was PydanticAI created?
In the world of Python, Pydantic is widely used for data validation and settings management, and FastAPI made web development faster and cleaner by building on top of Pydantic.

When the team behind Pydantic started using LLMs in their own tool called Logfire, they noticed a gap — there wasn’t any agent framework that provided the same smooth experience that FastAPI offered for APIs. Most existing LLM tools were either too complex, too loosely structured, or hard to manage at scale.

So they built PydanticAI with one goal:

“Bring the developer-friendly experience of FastAPI to the world of GenAI apps.”

# Key Features of PydanticAI:
