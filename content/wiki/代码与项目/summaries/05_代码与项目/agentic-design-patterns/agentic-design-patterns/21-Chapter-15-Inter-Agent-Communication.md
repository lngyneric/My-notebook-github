---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/21-Chapter-15-Inter-Agent-Communication.md
raw_sha256: 0d88906a17bc7768d2b074181b367baf1bcf66936a8833576883db16a7619a58
compiled_at: 2026-04-24T07:52:04.338Z
---
<wiki>
# Chapter 15: Inter-Agent Communication (A2A)
[[20-Chapter-14-Knowledge-Retrieval-RAG|< Previous Chapter]] | [[000-Home|Home]] | [[22-Chapter-16-Resource-Aware-Optimization|Next Chapter >]]

## Summary
Individual AI agents often face limitations when tackling complex, multifaceted problems, even with advanced capabilities. Inter-Agent Communication (A2A) is an open standard protocol developed by Google to enable diverse AI agents (potentially built with different frameworks) to collaborate effectively via seamless coordination, task delegation, and information exchange. This chapter explores the A2A protocol, its core concepts, interaction mechanisms, security features, comparison with related standards, practical applications, and implementation examples within the Google Agent Development Kit (ADK).

## Inter-Agent Communication Pattern Overview
The Agent2Agent (A2A) protocol is an open standard designed to enable communication and collaboration between different AI agent frameworks, ensuring interoperability for agents developed with technologies like LangGraph, CrewAI, or Google ADK regardless of their underlying framework.
A2A is supported by a range of technology companies and service providers including Atlassian, Box, LangChain, MongoDB, Salesforce, SAP, and ServiceNow. Microsoft plans to integrate A2A into Azure AI Foundry and Copilot Studio, while Auth0 and SAP are adding native A2A support to their platforms and agents. As an open-source protocol, A2A welcomes community contributions to drive its evolution and widespread adoption.

## Core Concepts of A2A
The A2A protocol defines a structured framework for agent interactions built on six foundational pillars: Core Actors, Agent Card, Agent Discovery, Communication and Tasks, Interaction Mechanisms, and Security.

### Core Actors
A2A interactions involve three primary entities:
- **User**: The entity that initiates requests for agent assistance.
- **A2A Client (Client Agent)**: An application or AI agent that acts on the user's behalf to request actions or information from remote agents.
- **A2A Server (Remote Agent)**: An AI agent or system that exposes an HTTP endpoint to process client requests and return results. It operates as an "opaque" system, meaning clients do not need to understand its internal operational details.

### Agent Card
An agent's digital identity is defined by its Agent Card, a JSON file containing all key information required for client interaction and automatic discovery. This includes the agent's identity, endpoint URL, version, supported capabilities (e.g., streaming, push notifications), specific skills, default input/output modes, and authentication requirements.
Below is an example Agent Card for a WeatherBot:
```json
{
  "name": "WeatherBot",
  "description": "Provides accurate weather forecasts and historical data.",
  "url": "http://weather-service.example.com/a2a",
  "version": "1.0.0",
  "capabilities": {
    "streaming": true,
    "pushNotifications": false,
    "stateTransitionHistory": true
  },
  "authentication": {
    "schemes": [
      "apiKey"
    ]
  },
  "defaultInputModes": [
    "text"
  ],
  "defaultOutputModes": [
    "text"
  ],
  "skills": [
    {
      "id": "get_current_weather",
      "name": "Get Current Weather",
      "description": "Retrieve real-time weather for any location.",
      "inputModes": [
        "text"
      ],
      "outputModes": [
        "text"
      ],
      "examples": [
        "What's the weather in Paris?",
        "Current conditions in Tokyo"
      ],
      "tags": [
        "weather",
        "current",
        "real-time"
      ]
    },
    {
      "id": "get_forecast",
      "name": "Get Forecast",
      "description": "Get 5-day weather predictions.",
      "inputModes": [
        "text"
      ],
      "outputModes": [
        "text"
      ],
      "examples": [
        "5-day forecast for New York",
        "Will it rain in London this weekend?"
      ],
      "tags": [
        "weather",
        "forecast",
        "prediction"
      ]
    }
  ]
}
```

### Agent Discovery
Agent discovery is the process that allows A2A clients to locate Agent Cards describing the capabilities of available A2A Servers. Three primary strategies are supported:
1. **Well-Known URI**: Agents host their Agent Card at a standardized path (e.g., `/.well-known/agent.json`), enabling broad, automated accessibility for public or domain-specific use cases.
2. **Curated Registries**: Centralized catalogs where Agent Cards are published and can be queried based on specific criteria, ideal for enterprise environments requiring centralized management and access control.
3. **Direct Configuration**: Agent Card information is embedded or privately shared, suitable for tightly coupled or private systems where dynamic discovery is not required.
All Agent Card endpoints should be secured via access control, mutual TLS (mTLS), or network restrictions, especially if they contain sensitive (non-secret) information.

## Communications and Tasks
In the A2A framework, communication is structured around asynchronous tasks, the fundamental unit of work for long-running processes. Each task is assigned a unique identifier and progresses through a defined lifecycle of states (e.g., submitted, working, completed, failed) to support parallel processing for complex operations.
Inter-agent communication occurs via **Messages**, which contain:
- **Attributes**: Key-value metadata describing the message (e.g., priority, creation time)
- **Parts**: One or more content payloads (e.g., plain text, files, structured JSON data)
Tangible outputs generated by an agent during task execution are called **Artifacts**. Like messages, artifacts consist of one or more parts and can be streamed incrementally as results become available.
All A2A communication occurs over HTTP(S) using the JSON-RPC 2.0 protocol for payloads. A server-generated `contextId` is used to group related tasks and preserve conversational context across multiple interactions.

## Interaction Mechanisms
A2A provides four distinct interaction mechanisms to suit a range of AI application requirements:
1. **Synchronous Request/Response**: For quick, immediate operations. The client sends a request and waits for the server to process it and return a complete response in a single synchronous exchange.
2. **Asynchronous Polling**: For long-running tasks. The server immediately acknowledges requests with a "working" status and task ID, and the client periodically polls the server to check task status until it is marked as completed or failed.
3. **Streaming Updates (Server-Sent Events - SSE)**: For real-time, incremental results. A persistent one-way connection is established from server to client, allowing the remote agent to push status updates or partial results continuously without repeated client requests.
4. **Push Notifications (Webhooks)**: For very long-running or resource-intensive tasks where persistent connections or frequent polling are inefficient. The client registers a webhook URL, and the server sends an asynchronous notification when the task's status changes significantly (e.g., upon completion).
Agent Cards explicitly specify whether an agent supports streaming or push notification capabilities. A2A is modality-agnostic, meaning it supports these interaction patterns for text, audio, video, and other data types to enable multimodal AI applications.
Example synchronous request (uses `sendTask` method for single complete responses):
```json
{
  "jsonrpc": "2.0",
  "id": "1",
  "method": "sendTask",
  "params": {
    "id": "task-001",
    "sessionId": "session-001",
    "message": {
      "role": "user",
      "parts": [
        {
          "type": "text",
          "text": "What is the exchange rate from USD to EUR?"
        }
      ]
    },
    "acceptedOutputModes": [
      "text/plain"
    ],
    "historyLength": 5
  }
}
```
Example streaming request (uses `sendTaskSubscribe` method for persistent connections and incremental updates):
```json
{
  "jsonrpc": "2.0",
  "id": "2",
  "method": "sendTaskSubscribe",
  "params": {
    "id": "task-002",
    "sessionId": "session-001",
    "message": {
      "role": "user",
      "parts": [
        {
          "type": "text",
          "text": "What's the exchange rate for JPY to GBP today?"
        }
      ]
    },
    "acceptedOutputModes": [
      "text/plain"
    ],
    "historyLength": 5
  }
}
```

## Security
A2A
