---
source: raw/04_文档与参考/Markdown文档/Build Multi-Agent Chatbot with AG2 AutoGen for Healthcare.md
raw_sha256: 9057f4a66165014265ae8a5ec78f276964e1057b308281fd4c729d083eeedbcc
compiled_at: 2026-04-24T05:52:59.407Z
---
<wiki>
<p style="text-align:center">
    <a href="https://skills.network" target="_blank">
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
    </a>
</p>

# Build a Multi-Agent Chatbot with AG2 (AutoGen) for Healthcare

## Summary
This 30-minute guided lab demonstrates how to build **AutoMed**, a multi-agent AI medical consultation system powered by Microsoft's AG2 (AutoGen) open-source framework. AutoMed orchestrates specialized AI agents to collaborate on symptom analysis, diagnosis, medication recommendations, and care guidance, delivering context-aware, tailored medical support unlike generic single-agent chatbots.
> 🚨 Disclaimer: This project is for educational purposes only. The medical guidance provided is not a substitute for professional medical consultation, diagnosis, or treatment. Always consult a qualified healthcare provider for medical advice.

## Estimated Completion Time
30 minutes

## Learning Objectives
After completing this lab, learners will be able to:
1. Understand how AG2 (AutoGen) enables multi-agent AI systems for complex workflows
2. Integrate AG2 (AutoGen) with large language models (LLMs) like GPT-4 for dynamic AI conversations
3. Implement agent-to-agent communication for intelligent medical decision-making
4. Develop collaborative AI agents to handle specialized healthcare tasks

## Setup & Dependencies
### Required Libraries
| Library | Purpose |
|---------|---------|
| `autogen==0.7` | Orchestrate multi-agent AI interactions and automate LLM workflows |
| `openai==1.64.0` | Integrate OpenAI LLMs into AI workflows |
| `python-dotenv==1.1.0` | Manage environment variables and securely load API keys |

### Installation
Run the following command to install dependencies (not pre-installed in Skills Network Labs):
```python
!pip install autogen==0.7 openai==1.64.0 python-dotenv==1.1.0 | tail -n 1
```
> Note: If installation fails, restart the Jupyter kernel and re-run the command.

### Imports & Initial Configuration
```python
import warnings
# Suppress deprecation and user warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings('ignore', category=UserWarning)

from autogen import ConversableAgent, GroupChat, GroupChatManager
from openai import OpenAI
import logging

# Suppress AutoGen OAI client errors
logging.getLogger("autogen.oai.client").setLevel(logging.ERROR)

# Initialize OpenAI client (API key managed via environment variables)
client = OpenAI()

# Disable Docker execution to avoid runtime errors
code_execution_config = {"use_docker": False}
```

## Core Framework: AG2 (AutoGen)
### What is AutoGen?
AutoGen is an open-source Microsoft framework that enables developers to orchestrate and optimize AI workflows using multiple collaborative AI agents. Unlike isolated traditional AI systems, AutoGen agents (powered by LLMs like GPT) interact, exchange information, and refine outputs to solve complex tasks.

### Key Features of AutoGen
1. **Multi-Agent Collaboration**: Agents with specialized roles (e.g., problem solver, verifier, optimizer) communicate to solve tasks jointly
2. **Conversational & Task-Oriented AI**: Supports multi-turn LLM-driven dialogues to refine answers across use cases like cross-domain consulting
3. **Automated Workflow Generation**: Orchestrates end-to-end automation for use cases like AI-assisted programming, research, and document generation
4. **Human-AI Collaboration**: Allows human intervention to provide feedback or guide agents during workflows

### AutoGen vs Traditional AI Agents
| Feature | Traditional AI Agents | AutoGen AI Agents |
|---------|-----------------------|-------------------|
| Interactivity | Works in isolation | Collaborates with other agents |
| Learning Ability | Static | Adaptive & iterative |
| Workflow Handling | Predefined | Dynamic & evolving |
| Human Intervention | Limited | Supports structured human-AI collaboration |

## AutoMed Multi-Agent System Workflow
AutoMed activates a team of specialized agents to process user medical queries, rather than generating a single generic response. For a user reporting symptoms (e.g., persistent headaches and fatigue), the agent workflow is:
1. **Patient Agent**: Collects user symptoms, medical history, and ongoing treatments
2. **Symptom Analyzer Agent**: Evaluates potential conditions using AI medical knowledge
3. **Pharmacy Agent**: Suggests over-the-counter remedies and guidance on when to seek care
4. **Consultation Advisor Agent**: Determines if a doctor visit is required, and fetches real-time medical research updates

### LLM Selection: Why GPT-4o?
GPT-4o is used for its ability to:
- Accurately interpret medical symptoms
- Generate natural, human-like detailed responses
- Provide evidence-aligned condition suggestions from user input

Sample LLM configuration:
```python
llm_config = {"config_list": [{"model": "gpt-4o", "api_key": None}]}
```
> Note: Replace `api_key: None` with a valid OpenAI API key when running outside the Skills Network platform.

## Core AutoGen Components
### `ConversableAgent`
A class representing an AI agent capable of engaging in structured conversations, with a role defined via a system prompt and LLM configuration. For AutoMed, 4 specialized agents are defined:
```python
# 1. Patient Agent: Represents the user, describes symptoms
patient_agent = ConversableAgent(
    name="patient", 
    system_message="You describe symptoms and ask for medical help.", 
    llm_config=llm_config
)

# 2. Diagnosis Agent: Analyzes symptoms to provide a concise diagnosis
diagnosis_agent = ConversableAgent(
    name="diagnosis", 
    system_message="You analyze symptoms and provide a possible diagnosis. Summarize key points in one response.", 
    llm_config=llm_config
)

# 3. Pharmacy Agent: Recommends medications based on diagnosis
pharmacy_agent = ConversableAgent(
    name="pharmacy", 
    system_message="You recommend medications based on diagnosis. Only respond once.", 
    llm_config=llm_config
)

# 4. Consultation Agent: Determines need for doctor visit, ends conversation
consultation_agent = ConversableAgent(
    name="consultation", 
    system_message="You determine if a doctor's visit is required. Provide a final summary with clear next steps. IMPORTANT: End your response with 'CONSULTATION_COMPLETE' to signal the end of the conversation.", 
    llm_config=llm_config
)
```

### `GroupChat`
A class that manages structured, turn-based conversations between multiple agents to prevent infinite loops and ensure logical flow. Key parameters:
- `agents`: List of participating agents
- `messages`: Initial empty message list to ensure independent consultations
- `max_round`: Maximum number of conversation cycles to avoid infinite loops
- `speaker_selection_method`: Defines speaking order (e.g., `round_robin` for sequential turns)

AutoMed GroupChat configuration:
```python
groupchat = GroupChat(
    agents=[diagnosis_agent, pharmacy_agent, consultation_agent],
    messages=[], 
    max_round=5,
    speaker_selection_method="round_robin"
)
```

### `GroupChatManager`
A coordinator class that controls GroupChat execution, ensuring messages flow between agents according to the defined structure. Configuration:
```python
manager = GroupChatManager(name="manager", groupchat=groupchat)
```

## AutoMed Execution
To start a consultation, the patient agent initiates the chat with the manager, which orchestrates the agent workflow:
```python
print("\n🤖 Welcome to the AI Healthcare Consultation System!")
symptoms = input("🩺 Please describe your symptoms: ")

print("\n🩺 Diagnosing symptoms...")
response = patient_agent.initiate_chat(
    manager, 
    message=f"I am feeling {symptoms}. Can you help?",
)
```

## Lab Exercise: Build a Mental Health Chatbot
Create a 3-agent mental health support chatbot using AutoGen with the following agent roles:
| Agent | Role |
|-------|------|
| Patient Agent | Captures user mood, stress levels, and emotional concerns |
| Emotion Analysis Agent | Identifies dominant emotions from user input |
| Therapy Recommendation Agent | Provides relaxation techniques and coping strategies |

### Sample Solution
```python
from autogen import ConversableAgent, GroupChat, GroupChatManager

# LLM Configuration
llm_config = {"config_list": [{"model": "gpt-4o", "api_key": None}]}

# Define Agents
patient_agent = ConversableAgent(
    name="patient",
    system_message="You describe your emotions and mental health concerns.",
    llm_config=llm_config
