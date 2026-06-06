---
source: raw/04_文档与参考/Markdown文档/Implement Workflow Patterns with LangGraph.md
raw_sha256: 207100f9b7bb095fb6bbe0bf8166bb26402b9548b6534bc4a6faa1b4ae0e2f4f
compiled_at: 2026-04-24T06:00:16.208Z
---
# Implement Workflow Patterns with LangGraph
## Summary
This is a 45-minute hands-on lab that teaches 3 core workflow patterns for building coordinated multi-agent AI systems using LangGraph and LangChain. Learners implement practical projects including job application assistants, intelligent task routers, and multilingual processors, and complete a final exercise building a multi-agent routing system for ride hailing, restaurant orders, and grocery services.

## Estimated Time
45 minutes

## Core Prerequisites & Dependencies
Required Python packages for implementation:
- `langchain-openai==0.3.27`
- `langgraph==0.6.6`
- `pygraphviz==1.14`

Core LLM configuration: `gpt-4o-mini` model via the `ChatOpenAI` interface.

---
## LangGraph Fundamentals
### Core Components
1. **StateGraph**: The foundational workflow class that defines the structure of data (via TypedDict) flowing through the workflow, validates data types, and manages state transitions between nodes.
2. **Nodes**: Discrete, modular steps in the workflow, each representing a specialized agent or task. Nodes receive the current state, process data (typically via LLM calls), and return an updated state.
3. **Edges**: Connections between nodes that define the execution order of the workflow:
   - Standard edges: Define sequential execution between two nodes
   - Conditional edges: Dynamically route execution to different nodes based on a state value
4. **State Management**: Shared memory for the workflow, defined using Python's `TypedDict`, that stores all intermediate and final outputs passed between nodes.
5. **Entry/Finish Points**: Define the start and end nodes of the workflow, marking where execution begins and terminates.

### Utility Function
```python
def print_workflow_info(workflow, app=None):
    """Prints comprehensive information about a LangGraph workflow."""
    print("WORKFLOW INFORMATION")
    print("====================")
    print(f"Nodes: {workflow.nodes}")
    print(f"Edges: {workflow.edges}")

    # Access finish points if available
    try:
        finish_points = workflow.finish_points
        print(f"Finish points: {finish_points}")
    except:
        try:
            print(f"Finish point: {workflow._finish_point}")
        except:
            print("Finish points attribute not directly accessible")
    
    # Visualize workflow if compiled app is provided
    if app:
        print("\nWorkflow Visualization:")
        from IPython.display import display
        display(app.get_graph().draw_png())
```

---
## Core Workflow Patterns
### 1. Sequential Agent Coordination (Prompt Chaining)
#### Definition
A workflow design pattern where complex tasks are decomposed into a sequence of LLM calls. Each step depends on the output of the previous one, allowing for step-by-step refinement or evolution of the data being processed. The pattern supports modularity, function calling, and external tool injection between steps.
#### Common Use Cases
- Step-by-step content generation (idea → outline → draft → polish)
- Automated report generation (extract → analyze → summarize)
- Educational content creation
#### Implementation Example: Job Application Assistant
- State management via `ChainState` TypedDict (stores `job_description`, `resume_summary`, `cover_letter`)
- 2 sequential nodes:
  1. `generate_resume_summary`: Creates role-tailored resume summary from the input job description
  2. `generate_cover_letter`: Generates a personalized cover letter using the generated resume summary and original job description
- Workflow structure: Entry point → `generate_resume_summary` → `generate_cover_letter` → End

---
### 2. Intent-Based Routing
#### Definition
A pattern where a specialized router agent classifies incoming input (based on user intent) and routes it to the appropriate specialized sub-process or agent, acting as an intelligent switchboard for multi-task systems.
#### Routing Techniques
1. Hard-coded keyword-based routing (primitive)
2. LLM-based routing via classification prompts
3. Embedding-based semantic matching with routing maps
#### Common Use Cases
- AI customer service bots (routing billing, tech support, or general inquiries)
- Multi-skill AI agents
- Adaptive educational bots
#### Implementation Example: Summarization/Translation Task Router
- State management via `RouterState` TypedDict (stores `user_input`, `task_type`, `output`)
- Nodes:
  1. `router_node`: Classifies user intent as either "summarize" or "translate" using LLM tool binding
  2. `summarize`: Processes summarization requests
  3. `translate`: Processes French translation requests
- Workflow structure: Entry point → `router_node` → Conditional edge routing to appropriate task node → End

---
### 3. Parallel Agent Execution
#### Definition
A pattern where independent LLM tasks are executed simultaneously instead of sequentially, reducing processing time and improving system throughput for tasks with no interdependencies.
#### Parallelization Techniques
1. **Format Diversity**: Run the same input through different prompt styles, languages, or output formats, then combine all results
2. **Task Splitting**: Divide large input into smaller parts, run the same task on each part in parallel, then merge partial results
3. **Consensus Voting**: Run the same task multiple times with different agents or prompt styles, then select the best result via ranking or majority vote
#### Common Use Cases
- Simultaneous summarization of different sections of a large document
- Batch translation of multiple user messages
- Multi-variation content generation for marketing or product materials
- Ensembled safety checks for AI outputs
#### Implementation Example: Multilingual Translation Assistant
- State management via `State` TypedDict (stores `text`, `french`, `spanish`, `japanese`, `combined_output`)
- Nodes:
  1. `translate_french`, `translate_spanish`, `translate_japanese`: All run in parallel immediately from workflow start
  2. `aggregator`: Combines all parallel translation outputs into a single formatted final result
- Workflow structure: Start → All 3 translation nodes (parallel execution) → `aggregator` → End

---
## Exercise: Build a Multi-Agent Routing System
### Task Overview
Learners build a production-ready routing system for 3 service categories plus a default fallback handler:
1. Ride hailing requests
2. Restaurant orders
3. Grocery delivery requests
4. Default handler for unclassified requests
### Core Implementation Steps
1. Define a `RouterState` TypedDict for state management and a `Router` Pydantic model for LLM tool binding
2. Implement router logic with a fallback to `default_handler` for unrecognized requests
3. Implement 4 specialized processing nodes for each service category and fallback
4. Assemble the StateGraph with conditional routing rules and compile to an executable application
5. Test the system with sample test cases covering all request types.

---
## Authors & Version
### Authors
- Kunal Makwana (IBM, Generative AI & Machine Learning Specialist)
- Joseph Santarcangelo (IBM, PhD in Electrical Engineering, ML/Computer Vision Researcher)
### Change Log
| Date (YYYY-MM-DD) | Version | Changed By | Change Description |
|---|---|---|---|
| 2025-07-17 | 0.1 | Kunal Makwana | Initial version created |
| 2025-07-22 | 0.2 | Steve Ryan | ID review |
| 2025-07-22 | 0.3 | Leah Hanson | QA review |
### Copyright
© IBM Corporation. All rights reserved.
