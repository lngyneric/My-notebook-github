<p style="text-align:center">
    <a href="https://skills.network" target="_blank">
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
    </a>
</p>


# Build a Multi-Agent Chatbot with AG2 (AutoGen) for Healthcare


Estimated time needed: **30** minutes


AutoMed is not just an ordinary chatbot—it’s a multi-agent AI system powered by AG2 (AutoGen), designed to simulate expert medical consultation through intelligent collaboration. Instead of relying on a single AI agent, AutoMed orchestrates multiple specialized agents, each dedicated to a specific task, ensuring comprehensive, accurate, and real-time medical guidance. By leveraging AutoGen’s multi-agent capabilities, AutoMed mimics the behavior of a real medical team, where different AI agents collaborate to analyze symptoms, suggest treatments, fetch real-time medical data, and provide follow-up care.

With its adaptive intelligence and multi-agent communication, AutoMed delivers human-like, context-aware conversations that go beyond basic symptom checkers. Unlike conventional AI chatbots that provide one-size-fits-all responses, AutoMed's specialized agents work together to deliver precise, tailored recommendations based on the user’s health history and real-time input. This results in a more interactive, intelligent, and reliable medical consultation experience.

<p style="color:red;"> Disclaimer: This guided project is designed to introduce learners to AG2 (AutoGen). The medical advice provided should not be considered a substitute for professional medical consultation, diagnosis, or treatment. Always seek guidance from a qualified healthcare professional.</p>


## __Table of Contents__

<ol>
    <li><a href="#Objectives">Objectives</a></li>
    <li>
        <a href="#Setup">Setup</a>
        <ol>
            <li><a href="#Installing-Required-Libraries">Installing Required Libraries</a></li>
            <li><a href="#Importing-Required-Libraries">Importing Required Libraries</a></li>
        </ol>
    </li>
    <li><a href="#What-is-AutoGen?">What is AutoGen?</a></li>
    <li><a href="#Key-Features-of-AutoGen">Key Features of AutoGen</a></li>
    <li><a href="#Comparison:-AutoGen-vs-Traditional-AI-Agents">Comparison: AutoGen vs Traditional AI Agents</a></li>
    <li><a href="#How-AutoMed-Works:-Multi-Agent-AI-in-Action">How AutoMed Works: Multi-Agent AI in Action</a></li>
    <li><a href="#Why-is-GPT-4o-Used?">Why is GPT-4o Used?</a></li>
    <li><a href="#What-is--ConversableAgent?">What is ConversableAgent?</a></li>
    <li><a href="#What-is-GroupChat?">What is GroupChat?</a></li>
    <li><a href="#Exercise:-Create-a-Mental-Health-Chatbot-Using-the-AutoGen-Library">Exercise: Create a Mental Health Chatbot Using the AutoGen Library</a></li>
</ol>

<ul>
    <li><a href="#Authors">Authors</a></li>
    <li><a href="#Other-Contributors">Contributors</a></li>
    <li><a href="#Change-Log">Change Log</a></li>
</ul>




## Objectives

After completing this lab you will be able to:

- Learn how AG2 (AutoGen) enables multi-agent AI systems for complex workflows.
- Explore how AG2 (AutoGen) integrates with LLMs like GPT-4 for dynamic AI-driven conversations.
- Implement agent-to-agent communication for intelligent medical decision-making.
- Develop multiple AI agents that interact and collaborate to handle different healthcare tasks.


----


## Setup


For this lab, we will be using the following libraries:

*   [`AG2 (AutoGen)`](https://microsoft.github.io/autogen/0.2/docs/installation/) for orchestrating multi-agent AI interactions and automating LLM-based workflows.  
*   [`OpenAI`](https://platform.openai.com/docs/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMML0187ENSkillsNetwork31430127-2021-01-01) for integrating OpenAI's large language models (LLMs) into our AI workflows.  
*   [`python-dotenv`](https://pypi.org/project/python-dotenv/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMML0187ENSkillsNetwork31430127-2021-01-01) for managing environment variables and securely loading API keys and configurations.  


### Installing Required Libraries

The following required libraries are __not__ pre-installed in the Skills Network Labs environment. __You must run the following cell__ to install them. This step could take **several minutes**; please be patient:

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/crvBKBOkg9aBzXZiwGEXbw/Restarting-the-Kernel.png" width="50%" alt="Restart kernel">

**NOTE**: If you encounter any issues, restart the kernel and run it again by clicking the **Restart the kernel** icon.




```python
!pip install autogen==0.7 openai==1.64.0 python-dotenv==1.1.0 | tail -n 1
```

### Importing Required Libraries
Import all required libraries:



```python
import warnings

# Suppress autogen and other deprecation/user warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings('ignore', category=UserWarning)

from autogen import ConversableAgent, GroupChat, GroupChatManager
from openai import OpenAI
import logging
```


```python
# Suppress warnings from autogen.oai.client
logging.getLogger("autogen.oai.client").setLevel(logging.ERROR)

```

# What is AutoGen?

AutoGen is an open-source framework developed by Microsoft that enables developers to orchestrate and optimize AI workflows using multiple AI agents. These agents can collaborate, automate decision-making, and dynamically generate responses in complex problem-solving tasks.

Unlike traditional AI systems that work in isolation, AutoGen enables multiple AI agents (LLMs such as GPT) to interact, exchange information, and refine their outputs, making it more powerful and flexible for various applications.

# Key Features of AutoGen
### 1. Multi-Agent Collaboration

AutoGen allows multiple AI agents to communicate and solve tasks collaboratively. Each agent can have a specific role, such as a problem solver, verifier, or optimizer.

Example:

- One agent generates code, another reviews it, and another tests it.
- A research agent collects information, while another summarizes it.

### 2. Conversational and Task-Oriented AI

AutoGen supports LLM-driven conversations where AI agents engage in multi-turn dialogues to refine answers.

Example:

- A chatbot that consults different AI agents, such as one for legal advice and another for finance.
- A customer support AI that escalates unresolved queries to another AI agent.

### 3. Automated Workflow Generation

You can orchestrate workflows for AI-driven automation, such as AI-assisted programming, research, and document generation.

Example:

- Automating software debugging where AI identifies issues, suggests fixes, and verifies solutions.

### 4. Supports Human-AI Collaboration

AutoGen allows humans to intervene in AI-driven workflows by providing feedback or manually guiding agents when necessary.

Example:

- A research assistant AI drafts a report, but a human expert refines it.








# Comparison: AutoGen vs Traditional AI Agents

<table width="60%" align="left" >
        <thead>
            <tr>
                <th>Feature</th>
                <th>Traditional AI Agents</th>
                <th>AutoGen AI Agents</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Interactivity</td>
                <td>Works alone</td>
                <td>Collaborates with other agents</td>
            </tr>
            <tr>
                <td>Learning Ability</td>
                <td>Static</td>
                <td>Adaptive & iterative</td>
            </tr>
            <tr>
                <td>Workflow Handling</td>
                <td>Predefined</td>
                <td>Dynamic & evolving</td>
            </tr>
            <tr>
                <td>Human Intervention</td>
                <td>Limited</td>
                <td>Supports human-AI collaboration</td>
            </tr>
        </tbody>
</table>


The OpenAI() function initializes an API client object by calling its constructor, which automatically manages API key retrieval.

The code_execution_config dictionary is set up to signal to other functions that Docker should not be used during code execution, thus ensuring that your code runs directly on the host environment and avoiding Docker-related issues.



```python

# Initialize OpenAI Client (API Key is automatically managed from environment variables or configured in OpenAI settings)
client = OpenAI()

# Disable Docker execution to prevent runtime errors
code_execution_config = {"use_docker": False}
```

# How AutoMed Works: Multi-Agent AI in Action
When a user interacts with AutoMed, the system does not simply generate a response—it triggers a team of AI agents, each with a specific role in processing the query. These agents collaborate in real-time, cross-validating and optimizing their responses to ensure accuracy and reliability.

For example, consider a patient experiencing persistent headaches and fatigue. Instead of offering generic advice, AutoMed intelligently activates multiple specialized AI agents:

1. **Patient Agent** – Collects user symptoms, medical history, and any ongoing treatments.
2. **Symptom Analyzer Agent** – Evaluates potential conditions such as migraines, dehydration, or anemia based on AI-driven medical knowledge.
3. **Pharmacy Agent** – Suggests remedies, over-the-counter medications, and when to seek professional medical attention.
4.  **Consultation Advisor Agent** (Decides if a doctor visit is needed) – Fetches real-time updates from trusted healthcare medical research papers.

These agents work seamlessly together, analyzing, validating, and optimizing their recommendations to deliver the most relevant, personalized, and up-to-date medical guidance. The collaborative approach ensures that users receive a well-rounded medical consultation experience, similar to interacting with multiple healthcare professionals at once, but through an AI-driven, automated system.


### Why is GPT-4o Used?
GPT-4o is well-suited for:
- Understanding medical symptoms
- Generating detailed, human-like responses
- Providing accurate condition suggestions based on user input



```python
# Sample LLM Configuration (Replace with actual API keys/config if needed)
llm_config = {"config_list": [{"model": "gpt-4", "api_key": None}]}  # Replace with real API key
```

Now, let's understand the parameters:
- llm_config={"model": "gpt-4o", "api_key": None} : This configures the Large Language Model (LLM) that powers the Diagnosis Agent.
- "model": "gpt-4o" → Specifies that the agent is using OpenAI’s GPT-4o to generate responses.
- "api_key": None → This suggests that the OpenAI API key is not explicitly defined here and is likely set elsewhere in the system configuration- which is provided here by Skills Network. You need an active API key if you plan to run the project outside the CognitiveClass platform.


## What is  ConversableAgent?
- Represents an AI agent that can engage in conversations.
- Each agent has a specific role, defined by its system message.
- Uses LLM (Language Model) configurations to process responses.

 Here, each agent is assigned a specific role, allowing structured communication between AI agents and the user.
- The patient_agent represents the user and is responsible for describing symptoms and requesting medical assistance, but it does not process responses.
- The diagnosis_agent analyzes the symptoms provided by the patient and generates a concise diagnosis in a single response, ensuring clarity and brevity.
- The pharmacy_agent follows up on the diagnosis by recommending medications, but it is restricted to responding only once to prevent unnecessary repetition.
- The consultation_agent plays a critical role in determining whether the patient needs to visit a doctor, providing a final summary of the consultation along with clear next steps. To ensure structured conversation flow, the consultation_agent includes a termination condition by adding "CONSULTATION_COMPLETE" to its response, signaling the end of the consultation session. All agents are configured with the llm_config, which specifies the underlying language model (GPT-4) for processing responses. This structured setup allows for an efficient and logical multi-agent conversation, ensuring that the patient receives a diagnosis, medication recommendations, and a final decision on whether further medical consultation is necessary.



```python

# Step 1: Create AI Agents with Defined Roles
patient_agent = ConversableAgent(
    name="patient", 
    system_message="You describe symptoms and ask for medical help.", 
    llm_config=llm_config
)

diagnosis_agent = ConversableAgent(
    name="diagnosis", 
    system_message="You analyze symptoms and provide a possible diagnosis. Summarize key points in one response.", 
    llm_config=llm_config
)

pharmacy_agent = ConversableAgent(
    name="pharmacy", 
    system_message="You recommend medications based on diagnosis. Only respond once.", 
    llm_config=llm_config
)

consultation_agent = ConversableAgent(
    name="consultation", 
    system_message="You determine if a doctor's visit is required. Provide a final summary with clear next steps. IMPORTANT: End your response with 'CONSULTATION_COMPLETE' to signal the end of the conversation.", 
    llm_config=llm_config
)

```

## What is GroupChat?

- Manages a structured conversation between multiple AI agents
- Ensures turn-based speaking using speaker selection methods (e.g., round_robin)
- Prevents infinite loops by using max_round

The GroupChat class structures the interaction between multiple AI agents, ensuring a logical conversation flow. Below is a breakdown of each parameter used in the code:

- agents=[diagnosis_agent, pharmacy_agent, consultation_agent]
    - Specifies the AI agents participating in the conversation.
    - The diagnosis agent analyzes symptoms, the pharmacy agent recommends medications, and the consultation agent determines if a doctor's visit is necessary.
    - The patient agent only initiates the conversation and does not actively participate in the group chat.
- messages=[]
    - Initializes the conversation with an empty list of messages.
    - Ensures that no previous data is retained, making each consultation independent.
- max_round=5
    - Limits the conversation to five full cycles through all agents.
    - Prevents infinite loops by restricting the number of exchanges.
    - Ensures the conversation remains efficient and focused.
- speaker_selection_method="round_robin"
    - Controls the order in which agents respond.
    - Uses a "round-robin" approach, meaning each agent takes turns speaking in a structured sequence.
    - Prevents repetition or chaotic interactions, ensuring each agent contributes in a logical order.



```python
# Step 2: Create GroupChat for Structured Interaction
groupchat = GroupChat(
    agents=[diagnosis_agent, pharmacy_agent, consultation_agent],  # Patient only initiates
    messages=[], 
    max_round=5,  # Limits conversation to 5 rounds
    speaker_selection_method="round_robin"  # Ensures structured conversation flow
)
```

GroupChatManager

- Controls the execution of GroupChat
- Ensures messages flow between agents in an organized manner
- Acts as the conversation coordinator
- Coordinates the multi-agent conversation

It has two parameters. Let's understand both parameters.
- name="manager"
    - Assigns a name to the GroupChatManager.
    - The name "manager" represents the AI-driven entity responsible for orchestrating the conversation between agents.
- groupchat=groupchat
    - Connects the manager to a predefined GroupChat instance.
    - The groupchat parameter contains all agents, including the diagnosis agent, pharmacy agent, and consultation agent.
    - Ensures that all messages and responses follow the structured flow defined in the GroupChat.



```python
# Step 3: Create GroupChatManager to Handle Conversation
manager = GroupChatManager(name="manager", groupchat=groupchat)
```

- patient_agent.initiate_chat() starts the conversation by sending a message to the AI system.
- manager (GroupChatManager) coordinates the conversation flow.
- The message string dynamically includes the user-provided symptoms.



```python
# Step 4: Get Patient Input and Start Consultation
print("\n🤖 Welcome to the AI Healthcare Consultation System!")
symptoms = input("🩺 Please describe your symptoms: ")

print("\n🩺 Diagnosing symptoms...")
response = patient_agent.initiate_chat(
    manager, 
    message=f"I am feeling {symptoms}. Can you help?",
)
```

## Exercise: Create a Mental Health Chatbot Using the AutoGen Library

<table border="1" cellspacing="0" align="left">
    <thead>
        <tr>
            <th>Agent</th>
            <th>Role</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Patient Agent</strong></td>
            <td>Captures user input (mood, stress level, emotional concerns).</td>
        </tr>
        <tr>
            <td><strong>Emotion Analysis Agent</strong></td>
            <td>Identifies emotions based on user input.</td>
        </tr>
        <tr>
            <td><strong>Therapy Recommendation Agent</strong></td>
            <td>Provides relaxation techniques and coping strategies.</td>
        </tr>
    </tbody>
</table>




```python
# TODO
```

<details>
    <summary>Click here for a sample solution</summary>

```python
from autogen import ConversableAgent, GroupChat, GroupChatManager

# LLM Configuration (Replace None with actual API key if needed) 
llm_config = {"config_list": [{"model": "gpt-4o", "api_key": None}]}  # Provide OpenAI API key if required

# Create AI Agents with distinct roles 
patient_agent = ConversableAgent(
    name="patient",
    system_message="You describe your emotions and mental health concerns.",
    llm_config=llm_config
)

emotion_analysis_agent = ConversableAgent(
    name="emotion_analysis",
    system_message="You analyze the user's emotions based on their input."
                   "Do not provide treatment or self-care advice."
                   "Instead, just summarize the dominant emotions they may be experiencing.",
    llm_config=llm_config
)

therapy_recommendation_agent = ConversableAgent(
    name="therapy_recommendation",
    system_message="You suggest relaxation techniques and self-care methods"
                   "only based on the analysis from the Emotion Analysis Agent."
                   "Do not analyze emotions—just give recommendations based on the prior response.",
    llm_config=llm_config
)

# Create GroupChat for AI Agents 
groupchat = GroupChat(
    agents=[emotion_analysis_agent, therapy_recommendation_agent],
    messages=[], 
    max_round=3,  # Ensures the conversation does not stop too early 
    speaker_selection_method="round_robin"
)

# Create GroupChatManager 
manager = GroupChatManager(name="manager", groupchat=groupchat)

# Function to start the chatbot interaction 
def start_mental_health_chat():
    """Runs a chatbot for mental health support with distinct agent roles.""" 
    print("\nWelcome to the AI Mental Health Chatbot!") 
    user_feelings = input("How are you feeling today?")

    # Initiate conversation
    print("\nAnalyzing emotions...")
    response = patient_agent.initiate_chat(
        manager, 
        message=f"I have been feeling {user_feelings}. Can you help?"
    )

    # Ensure the therapy agent gets triggered
    if not response:  # If the initial response is empty, retry with explicit therapy agent prompt
        response = therapy_recommendation_agent.initiate_chat(
            manager, 
            message="Based on the user's emotions, please provide therapy recommendations."
        )

# Run the chatbot 
start_mental_health_chat()


## Authors


[Jigisha Barbhaya](https://www.linkedin.com/in/jigisha-barbhaya/) has always been driven by a passion for sharing knowledge and helping others learn about data science. This belief—that everyone should have the opportunity to learn about the field, regardless of their background or experience—has inspired her work as a learning content provider. Educational materials that are both accessible and engaging have been created and shared to make learning about data science easier for everyone.


### Other Contributors


[Faranak Heidari](https://author.skills.network/instructors/faranak_heidari) is a Data Scientist at IBM.

## Change Log

<details>
    <summary>Click here for the changelog</summary>

|Date (YYYY-MM-DD)|Version|Changed By|Change Description|
|-|-|-|-|
|2025-07-22|0.1|Jigisha Barbhaya|Initial version created|
|2025-07-22|0.2|Steve Ryan|ID review|
|2025-07-22|0.3|Andrea Hansis|Content QA review|

</details>

---



Copyright © IBM Corporation. All rights reserved.


```python

```
