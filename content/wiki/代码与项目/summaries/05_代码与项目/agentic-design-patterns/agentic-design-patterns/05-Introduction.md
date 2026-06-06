---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/05-Introduction.md
raw_sha256: 43fbe87d5d25baa1d68ebf69653cc64d88c3c2fc6c598a497923996456d1b9bc
compiled_at: 2026-04-24T07:12:45.707Z
---
# Introduction | Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems
[[04-Thought-Leader|< Previous Chapter]] | [[000-Home|Home]] | [[06-What-Makes-Agent|Next Chapter >]]

## Preface
This book outlines the evolution of artificial intelligence from simple reactive programs to sophisticated **autonomous intelligent agents and systems**, which use powerful Large Language Models (LLMs) as cognitive engines to understand context, make decisions, and interact dynamically with environments. It defines the **agentic canvas** as the underlying infrastructure and frameworks that manage state, communication, tool access, and logic flow for agent operation. It emphasizes that building reliable complex agentic systems requires more than strong LLMs: it requires **agentic design patterns**—proven reusable solutions for common agent design challenges, analogous to architectural or software design patterns.

## What are Agentic Systems?
### Core Definition
An agentic system is a computational entity that:
1. Perceives its digital/physical environment
2. Makes informed decisions based on perceptions and predefined/learned goals
3. Executes autonomous actions to achieve goals
It differs from traditional rigid, step-by-step software by exhibiting flexibility and initiative.

### Key Defining Characteristics
- **Autonomy**: Operates without constant human oversight
- **Proactiveness**: Initiates actions aligned with its goals
- **Reactiveness**: Responds effectively to environmental changes
- **Goal-Oriented**: Persistently works toward defined objectives
- **Tool Use**: Interacts with external APIs, databases, or services to extend capabilities
- **Memory**: Retains information across multiple interactions
- **Communication**: Engages with users, other systems, or other agents on connected canvases

### Associated Complexity Challenges
Effective implementation of agentic systems introduces unresolved complexity questions, including:
- Maintaining state across multiple operational steps
- Deciding when and how to use tools
- Managing communication between different agents
- Building system resilience to handle unexpected outcomes or errors

## Why Patterns Matter in Agent Development
Agentic design patterns are battle-tested templates/blueprints (not rigid rules) that provide proven solutions to standard agent design and implementation challenges. Key benefits include:
1. Avoiding "reinventing the wheel" for tasks like conversational flow management, external capability integration, and multi-agent coordination
2. Providing a common language and structure for clear, maintainable agent logic
3. Enhancing system robustness and reliability via patterns for error handling and state management
4. Accelerating development by allowing focus on unique application features rather than foundational agent mechanics
This book covers 21 key agentic design patterns as core building blocks for agents across technical canvases.

## Overview of the Book and How to Use It
### Core Focus
The book prioritizes practical, accessible learning by clearly explaining 21 agentic patterns and providing concrete, runnable code examples for their implementation. Patterns range from foundational topics (e.g., Prompt Chaining, Tool Use) to advanced concepts (e.g., Multi-Agent Collaboration, Self-Correction).

### Standard Chapter Structure (Per Pattern)
Each dedicated pattern chapter includes:
1. **Pattern Overview**: Clear explanation of the pattern and its role in agentic design
2. **Practical Applications & Use Cases**: Real-world scenarios where the pattern delivers value and its associated benefits
3. **Hands-On Code Example**: Runnable code using prominent agent development frameworks to demonstrate implementation on a technical canvas
4. **Key Takeaways**: Summarized critical points for quick review
5. **References**: Resources for deeper exploration of the pattern and related concepts

### Usage Guidance
- Chapters are ordered to build concepts progressively, but the book can be used as a reference for specific project challenges
- Appendices cover advanced prompting techniques, real-world AI agent deployment principles, and overviews of key agent frameworks
- Online-only tutorials provide step-by-step guidance for building agents on specific platforms (e.g., AgentSpace) or for CLI environments
- Emphasis is placed on practical application: users are encouraged to run, experiment with, and adapt code examples

### Rationale for Publication
Despite rapid AI evolution, core agentic patterns (e.g., RAG, Reflection, Routing, Memory) are emerging as foundational building blocks. This book invites reflection on these stable core principles to support long-term, robust agent development.

## Introduction to the Frameworks Used
Three prominent agent development frameworks serve as tangible "canvases" for code examples, each with unique strengths:
1. **LangChain + LangGraph**: LangChain provides flexible chaining of LLMs and other components, while LangGraph adds stateful support to create a robust canvas for complex sequential and graph-based operations
2. **Crew AI**: A structured framework specifically designed for orchestrating multiple AI agents, their roles, and tasks, acting as a canvas optimized for collaborative agent systems
3. **Google Agent Developer Kit (Google ADK)**: A set of tools and components for building, evaluating, and deploying agents, often integrated with Google's AI infrastructure as an operational canvas
Examples across these frameworks demonstrate pattern applicability regardless of the chosen technical environment, focusing on core logic and practical implementation.

## Closing Note
By the end of the book, users will understand 21 essential agentic patterns and possess practical code and knowledge to apply them effectively, enabling the construction of more intelligent, capable, and autonomous systems on their chosen development canvas.
