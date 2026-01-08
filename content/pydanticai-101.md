<p style="text-align:center">
    <a href="https://skills.network" target="_blank">
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
    </a>
</p>

# **Build Your First AI Agent with PydanticAI: Customer Chat Support**


Estimated time needed: **45** minutes


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
1. Agent-Oriented Design: Agents are central to PydanticAI, acting as containers that manage prompts, tools, and structured outputs, facilitating complex workflows and multi-agent interactions.

2. Type Safety and Validation: Leveraging Pydantic's robust type system, it ensures data integrity and clarity in agent behaviors, reducing runtime errors.​

3. Model-Agnostic Compatibility: Supports various LLMs, including OpenAI, Anthropic, Gemini, Deepseek, Ollama, Groq, Cohere, and Mistral, with a straightforward interface for integrating additional models.

4. Integration with Pydantic Logfire: Offers seamless debugging, performance monitoring, and behavior tracking, enhancing the observability of LLM-powered applications.

5. Python-Centric Approach: Emphasizes familiar Python control flows and best practices, making it accessible for developers to build and maintain AI-driven projects.

You can learn more about PydanticAI - https://ai.pydantic.dev/


# About Dataset
In this lab we will use the kagglehub library (which is an unofficial utility that simplifies accessing Kaggle datasets programmatically), also downloads the latest version of the Kaggle dataset titled "customer-support-ticket-dataset" owned by the user suraj520 from here - https://www.kaggle.com/datasets/suraj520/customer-support-ticket-dataset

The Customer Support Ticket Dataset is a dataset that includes customer support tickets for various tech products. It consists of customer inquiries related to hardware issues, software bugs, network problems, account access, data loss, and other support topics. The dataset provides information about the customer, the product purchased, the ticket type, the ticket channel, the ticket status, and other relevant details.

The dataset can be used for various analysis and modelling tasks in the customer service domain.

Features Description:
Ticket ID: A unique identifier for each ticket.  
Customer Name: The name of the customer who raised the ticket.  
Customer Email: The email address of the customer (Domain name - @example.com is intentional for user data privacy concern).  
Customer Age: The age of the customer.  
Customer Gender: The gender of the customer.  
Product Purchased: The tech product purchased by the customer.  
Date of Purchase: The date when the product was purchased.  
Ticket Type: The type of ticket (e.g., technical issue, billing inquiry, product inquiry).  
Ticket Subject: The subject/topic of the ticket.  
Ticket Description: The description of the customer's issue or inquiry.  
Ticket Status: The status of the ticket (e.g., open, closed, pending customer response).  
Resolution: The resolution or solution provided for closed tickets.  
Ticket Priority: The priority level assigned to the ticket (e.g., low, medium, high, critical).  
Ticket Channel: The channel through which the ticket was raised (e.g., email, phone, chat, social media).  
First Response Time: The time taken to provide the first response to the customer.  
Time to Resolution: The time taken to resolve the ticket.  
Customer Satisfaction Rating: The customer's satisfaction rating for closed tickets (on a scale of 1 to 5).  


# Load Dataset
The function dataset_download() handles:
- Authentication with Kaggle (if set up properly),
- Checking if the dataset is already downloaded (uses caching),
- Downloading and extracting it if not present.

It returns the path to the folder where the dataset has been saved locally and assigns it to the variable path.


pd.read_csv() is a function that reads the CSV file and loads it into a DataFrame, which is a tabular data structure (like a table in Excel or a database).



```python
path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IJIikY8I-Q79KdIA5WtYIw/customer-support-tickets.csv"
df = pd.read_csv(path)
```


```python
df.head(5)
```

This line creates an instance of the OpenAI client, which is used to make API calls to services like ChatGPT, GPT-4, or DALL·E.

When OpenAI() is called without any parameters, it tries to read the API key from the environment variable OPENAI_API_KEY.

**Note**- However, in the Skills Network environment, an OpenAI API key is not required, as the platform handles authentication internally.



```python
# Initialize OpenAI client (assumes OPENAI_API_KEY is set in env)
client = OpenAI()
```

Now, We're defining a class called SupportResponse, and it inherits from BaseModel, which comes from Pydantic — a Python library that helps validate and structure data.

This class acts as a blueprint for what a valid AI-generated support response should look like. It makes sure that any response the AI gives follows specific rules.

- The ```category``` field only accepts one of these values: ```"billing", "technical", "account", or "other".```
   This helps classify the type of issue the customer is facing.
- The ```priority``` field is limited to ```"low", "medium", or "high"``` indicating how urgent the issue is.
- The ```escalate``` field is a boolean — either ```True or False```. This shows whether the issue needs to be forwarded to a human or higher-level support.
- The ```suggested_response``` is a string containing the ```actual message``` the AI should send back to the customer.



```python
from pydantic import BaseModel, Field, field_validator

# SupportResponse using Pydantic V2

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

Now we’ll write a prompt that will be sent to the AI to guide its behavior during the conversation.

This prompt works like an instruction — it tells the AI how it should act. When using OpenAI’s chat models, we pass this as the very first message with the role set to "system". That way, the AI knows what kind of assistant it should be throughout the interaction.



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

# What is an Agent?

An Agent is a special kind of setup that helps you manage how an AI (like GPT-4) interacts with users in a structured way.

In PydanticAI, agents are defined using a class called Agent, which is built using Python’s @dataclass system. It allows you to:

Set the type of input data or dependencies it needs (AgentDepsT)  
Define the type of output you expect the agent to return (OutputDataT)  
If you don’t customize these, the default setup looks like: Agent[None, str], meaning it doesn’t need extra input and returns a simple string.

We use an instructions field to guide the AI’s behavior — this is also known as the system prompt.

For example, you might tell the model:

“Act like a support assistant. Return a JSON response with four specific fields.”
You can also include few-shot examples, which are sample conversations (like {prompt}) that help the AI understand the format and tone you expect.  


In this project, we’re using the GPT-4 model for better reasoning and output quality.
You can read more about it here: https://openai.com/index/gpt-4/



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
  "priority": "high",
  "escalate": true,
  "suggested_response": "Please update your Wi-Fi drivers and restart your router."
}}

Only return the JSON — no extra text or explanation.
""",
    model="gpt-4.1-nano",
    client=client,
)
```

# What is nest_asyncio?
nest_asyncio is a small Python library that lets you run asynchronous code (like async functions) multiple times in the same environment — even if an event loop is already running.

### Why do we need it?
Jupyter notebooks already have their own event loop running in the background (to support things like live outputs and widgets).
Normally, Python doesn’t allow you to start a new event loop when one is already active — and that’s where nest_asyncio helps.

It "patches" the existing loop so you can safely run async code inside your notebook without errors.



```python
nest_asyncio.apply()
```

The run_chatbot() function is an async loop that simulates a real-time conversation with an AI-powered customer support chatbot.

Let's see how this function ```run_chatbot``` works step by step:

It keeps asking the user for input (like a message or question).
If the user types anything other than "exit", the input is sent to the AI agent using await agent.run(user_input).
The AI's response is expected to follow a predefined format called SupportResponse — which includes things like category, priority, escalation, and a suggested reply.
The function checks if the AI actually returned something that matches this format.
- If it does, the chatbot prints a clean, readable reply with all the details.
-  If not, it shows a warning that the AI gave an unexpected output.
The loop continues until the user types "exit", and any errors during the conversation are caught and displayed nicely.



```python
import json
from pydantic import ValidationError

async def run_chatbot():
    print(" Customer Support Chatbot — type 'exit' to quit\n")

    while True:
        user_input = input("🧑 You: ").strip()
        if user_input.lower() == "exit":
            print(" Exiting chatbot.")
            break

        try:
            result = await agent.run(user_input)
            output = result.output

            # Try parsing the result into SupportResponse
            if isinstance(output, SupportResponse):
                response = output
            elif isinstance(output, dict):
                response = SupportResponse(**output)
            elif isinstance(output, str):
                response = SupportResponse(**json.loads(output))
            else:
                raise ValueError("Unsupported output format from agent.")

            # ✅ Print structured response
            print("\nAI Response:")
            print(f"Category        : {response.category}")
            print(f"Priority        : {response.priority}")
            print(f"Escalate        : {'Yes' if response.escalate else 'No'}")
            print(f"Suggested Reply : {response.suggested_response}\n")

        except (ValidationError, ValueError, json.JSONDecodeError) as e:
            print("\n❌ Could not parse structured output from agent:")
            print(output)

# Run this to launch chatbot
await run_chatbot()
```

## Sample Input Questions for above propmt
#### Q1: Christopher Robbins purchased a Dell XPS. If you need more details, please let us know.
#### Q2: My Dell XPS keeps dropping from Wi-Fi every few minutes, which is really frustrating. I’d appreciate some help troubleshooting this issue.


# Exercise
Design a mood-based AI assistant that suggests recipes personalized to both the user's emotional state and their dietary preferences using pydantic_ai's Agent?



```python
# TODO
```

<details>
    <summary>Click here for Solution</summary>

```python

from dataclasses import dataclass

# Simulated database for user preferences
class UserProfile:
    @classmethod
    async def get_diet_type(cls, id: int) -> str:
        return "vegetarian" if id == 7 else "no restrictions"


# Define dependencies passed to the agent
@dataclass
class MoodDeps:
    user_id: int
    mood: str  # e.g. 'happy', 'sad', 'tired'
    db: UserProfile


# Define the expected structured output
class RecipeSuggestion(BaseModel):
    dish_name: str
    description: str
    ingredients: list[str]
    cooking_time_minutes: int


# Create the agent with schema guidance
mood_chef_agent = Agent(
    "openai:gpt-4o",
    deps_type=MoodDeps,
    result_type=RecipeSuggestion,
    system_prompt=(
        "You are EmoChef – a thoughtful and mood-sensitive recipe assistant. "
        "Based on the user's mood and diet type, suggest a comforting or energizing recipe."
    ),
)


# Inject additional context using system_prompt decorator
@mood_chef_agent.system_prompt
async def add_diet_info(ctx: RunContext[MoodDeps]) -> str:
    diet = await ctx.deps.db.get_diet_type(ctx.deps.user_id)
    return f"The user is feeling {ctx.deps.mood} and follows a {diet} diet."


# Run the agent using await (for Jupyter / Colab environments)
async def main():
    deps = MoodDeps(user_id=7, mood="tired", db=UserProfile())
    result = await mood_chef_agent.run("What should I cook tonight?", deps=deps)
    print(result.data)


# Await the main function
await main()
```

</details>


## Authors


[Jigisha Barbhaya](https://www.linkedin.com/in/jigisha-barbhaya/)
> <i> As a data scientist in IBM, I have always been passionate about sharing my knowledge and helping others learn about the field. I believe that everyone should have the opportunity to learn about data science, regardless of their background or experience level. This belief has inspired me to become a learning content provider, creating and sharing educational materials that are accessible and engaging for everyone.


[Faranak Heidari](https://www.linkedin.com/in/faranakhdr/)  
> <i> a datascientist and GenAI developer in IBM


### Other Contributors


[Karan Goswami](https://www.linkedin.com/in/karan-25au2000/) is a dedicated Data Scientist and an AI enthusiast, currently working at IBM's SkillsBuild Network.


Copyright © 2025 IBM Corporation. All rights reserved.

