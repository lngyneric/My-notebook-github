---
source: raw/04_文档与参考/Markdown文档/Build Reasoning and Acting AI Agents with LangGraph.md
raw_sha256: 40653d05fe1007a9186c93ab9fb1d4c8c61944c300be2a7501c6f4453702554b
compiled_at: 2026-04-14T03:50:54.115Z
---
# ReAct: Build Reasoning and Acting AI Agents with LangGraph

> 来源路径：`raw/04_文档与参考/Markdown文档/Build Reasoning and Acting AI Agents with LangGraph.md`

---

## TL;DR
这是一份90分钟的实践教程，指导开发者使用 LangGraph 框架基于 ReAct（推理+行动）范式构建可调用外部工具的AI智能体。教程从 ReAct 基础概念讲起，逐步完成依赖安装、工具开发、状态管理、手动推理循环演示，最终自动化构建出完整可运行的 ReAct 智能体，并配套练习帮助学习者拓展能力。

---

## 目录
<ol>
    <li><a href="#what-is-react">What is ReAct</a></li>
    <li><a href="#objectives">Objectives</a></li>
    <li>
        <a href="#setup--installation">Setup & Installation</a>
        <ol>
            <li><a href="#installing-required-libraries">Installing Required Libraries</a></li>
        </ol>
    </li>
    <li>
        <a href="#understanding-tools-in-react">Understanding Tools in ReAct</a>
        <ol>
            <li><a href="#1-web-search-tool">1. Web Search Tool</a></li>
            <li><a href="#theory-behind-web-search-tools">Theory behind Web Search Tools</a></li>
            <li><a href="#testing-the-search-tool">Testing the Search Tool</a></li>
            <li><a href="#2-clothing-recommendation-tool">2. Clothing Recommendation Tool</a></li>
            <li><a href="#why-this-tool-matters">Why this Tool Matters</a></li>
            <li><a href="#creating-the-tool-registry">Creating the tool Registry</a></li>
        </ol>
    </li>
    <li>
        <a href="#setting-up-the-language-model">Setting up the Language Model</a>
        <ol>
            <li><a href="#initializing-the-ai-model">Initializing the AI Model</a></li>
            <li><a href="#creating-the-system-prompt">Creating the System Prompt</a></li>
            <li><a href="#the-system-prompts-role">The System Prompt's Role</a></li>
            <li><a href="#binding-tools-to-the-model">Binding Tools to the Model</a></li>
            <li>
                <a href="#understanding-agent-state">Understanding Agent State</a>
                <ol>
                    <li><a href="#what-is-agent-state">What is Agent State?</a></li>
                    <li><a href="#demonstrating-state-management">Demonstrating State Management</a></li>
                </ol>
            </li>
            <li>
                <a href="#manual-react-execution-understanding-the-flow">Manual ReAct Execution (Understanding the Flow)</a>
                <ol>
                    <li><a href="#step-1-initial-query-processing">Step 1: Initial Query Processing</a></li>
                    <li><a href="#step-2-tool-execution">Step 2: Tool Execution</a></li>
                    <li><a href="#step-3-processing-results-and-next-action">Step 3: Processing Results and Next Action</a></li>
                    <li><a href="#step-4-final-response-generation">Step 4: Final Response Generation</a></li>
                </ol>
            </li>
            <li>
                <a href="#automating-react-with-graphs">Automating ReAct with Graphs</a>
                <ol>
                    <li><a href="#why-use-graphs">Why Use Graphs?</a></li>
                    <li><a href="#building-the-core-functions">Building the Core Functions</a></li>
                    <li><a href="#constructing-the-state-graph">Constructing the State Graph</a></li>
                    <li><a href="#visualizing-the-graph">Visualizing the Graph</a></li>
                </ol>
            </li>
            <li>
                <a href="#running-the-complete-react-agent">Running the Complete ReAct Agent</a>
                <ol>
                    <li><a href="#final-execution">Final Execution</a></li>
                    <li><a href="#the-complete-react-cycle">The Complete ReAct Cycle</a></li>
                </ol>
            </li>
        </ol>
    </li>
    <li>
        <a href="#key-takeaways">Key Takeaways</a>
        <ol>
            <li><a href="#what-makes-react-powerful">What Makes ReAct Powerful</a></li>
            <li><a href="#best-practices">Best Practices</a></li>
        </ol>
    </li>
    <li>
        <a href="#exercises">Exercises</a>
        <ol>
            <li><a href="#exercise-1---build-a-calculator-tool">Exercise 1 - Build a Calculator Tool</a></li>
            <li><a href="#exercise-2---create-a-news-summary-tool">Exercise 2 - Create a News Summary Tool</a></li>
        </ol>
    </li>
    <li><a href="#testing-your-solutions">Testing Your Solutions</a></li>
    <li><a href="#authors">Authors</a></li>
</ol>

---

## What is ReAct?

**ReAct** stands for **Reasoning + Acting**. It's a framework that combines:
1. **Reasoning**: The agent thinks through problems step by step, maintaining an internal dialogue about what it needs to do.
2. **Acting**: The agent can use external tools (search engines, calculators, APIs) to gather information or perform actions.
3. **Observing**: The agent processes the results from its actions and incorporates them into its reasoning.

This creates a powerful loop: **Think → Act → Observe → Think → Act → ...**

### Why ReAct Matters
Traditional language models are limited by their training data cutoff and can't access real-time information. ReAct agents overcome this by:
- Accessing current information through web searches
- Performing calculations with specialized tools
- Breaking down complex problems into manageable steps
- Adapting their approach based on intermediate results

---

## Objectives
After completing this lab you will be able to:
 - Use the ReAct framework to solve multi-step problems with external tools
 - Teach an AI agent to reason step by step, take actions, and adapt based on results
 - Build a smart assistant that can handle tasks requiring logic and tool use

----

## Setup & Installation

For this lab, we will be using the following libraries:

- [`LangGraph`](https://www.langchain.com/langgraph): A framework for building stateful, multi-step AI applications using graphs.
- [`LangChain`](https://www.langchain.com/): A toolkit that provides tools and abstractions for working with language models.
- [`LangChain-OpenAI`](https://python.langchain.com/docs/integrations/llms/openai/): OpenAI integration for LangChain.
- [`LangChain-Community`](https://python.langchain.com/api_reference/community/index.html): Community-contributed tools and integrations.

### Installing Required Libraries

```python
!pip install -U langgraph langchain-openai
```

```python
%%capture
!pip install langgraph==0.3.34 langchain-openai==0.3.14 langchainhub==0.1.21 langchain==0.3.24 pygraphviz==1.14 langchain-community==0.3.23
```

---

## Understanding Tools in ReAct

Tools are the "acting" part of ReAct. They give the agent capabilities beyond just generating text. Let's build two essential tools:

### 1. Web Search Tool
#### Tavily Search API Key Setup

We'll use Tavily search as our external research tool. You can get an API key at https://app.tavily.com/sign-in   

**Disclaimer:** Signing up for Tavily provides you with free credits, more than enough for this project's needs. If you require additional credits for further use, please add them at your own discretion.

![Tavily API Key screenshot](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/UjJx1-0vss4_3lwsUF8n0w/image.png)

You need to copy the key from Tavily's API website and paste the key on the line ```os.environ["TAVILY_API_KEY"] = "YOUR_KEY_HERE"```   

```python
import warnings 
warnings.filterwarnings('ignore')

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import tool
