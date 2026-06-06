---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/31-Appendix-D.md
raw_sha256: 64ecca4028e8a2e10ea36f0b365fd927e9bcdd5fa64d0ace576763ad948a1d67
compiled_at: 2026-04-24T08:11:31.269Z
---
# Appendix D: Building an Agent with AgentSpace
## Navigation
[[30-Appendix-C|< Previous Chapter]] | [[000-Home|Home]] | [[32-Appendix-E|Next Chapter >]]

## Important Note
> AgentSpace is now renamed to Gemini Enterprise. To maintain consistency with the original text, the name AgentSpace is used throughout this document.

## Abstract
AgentSpace (officially renamed to Gemini Enterprise) is a Google Cloud platform designed to enable "agent-driven enterprises" by integrating artificial intelligence into daily organizational workflows. It provides unified cross-asset search, autonomous AI agent deployment tools, enterprise knowledge graph capabilities, no-code agent building, multi-agent collaboration protocols, and enterprise-grade security to enhance productivity and data-driven decision-making.

## Core Platform Overview
### Key Capabilities
1. **Unified Organizational Search**: Cross-system search across an organization's full digital footprint (including documents, emails, and databases), powered by advanced AI models such as Google Gemini to comprehend and synthesize information from disparate sources.
2. **Autonomous AI Agents**: Specialized AI systems that can independently reason, plan, and execute multi-step complex tasks (e.g., topic research, cited report compilation, audio summary generation) beyond basic chatbot functionality.
3. **Enterprise Knowledge Graph**: A structured data layer that maps relationships between an organization's people, documents, and data to deliver context-aware, personalized AI outputs.
4. **No-Code Agent Development**: The Agent Designer graphical interface that enables custom agent creation without requiring advanced technical or programming expertise.
5. **Multi-Agent Interoperability**: Support for cross-agent communication and collaboration via the open Agent2Agent (A2A) Protocol to enable complex, orchestrated workflows.
6. **Enterprise-Grade Security**: Foundational security features including role-based access control (RBAC) and data encryption to protect sensitive organizational information.

## Step-by-Step Guide to Building an Agent with AgentSpace UI
### 1. Access AgentSpace
Navigate to Google Cloud Console and select *AI Applications* to access the AgentSpace platform.
![](https://cdn.nlark.com/yuque/0/2025/png/57829142/1761140597818-455d7428-484f-4bf5-858f-7495fd418bbd.png)
*Fig. 1: How to use Google Cloud Console to access AgentSpace*

### 2. Integrate External Services
Connect the agent to supported third-party and Google services, including but not limited to Calendar, Google Mail, Workday, Jira, Outlook, and ServiceNow.
![](https://cdn.nlark.com/yuque/0/2025/png/57829142/1761140597872-5c91627d-6ad6-4f13-a72e-82888c0b0eee.png)
*Fig. 2: Integrate with diverse services, including Google and third-party platforms.*

### 3. Configure Agent Prompts
Choose one of two prompt configuration paths:
   a. Select a pre-built prompt from Google's official prompt gallery
   ![](https://cdn.nlark.com/yuque/0/2025/png/57829142/1761140598084-0db2871e-1251-44d1-8bcd-ab4c9b13d6f1.png)
   *Fig. 3: Google's Gallery of Pre-assembled prompts*
   b. Create and customize a custom prompt tailored to specific use cases
   ![](https://cdn.nlark.com/yuque/0/2025/png/57829142/1761140598048-09bf9f3c-c8bd-4ff9-9514-fc76840344c5.png)
   *Fig. 4: Customizing the Agent's Prompt*

### 4. Enable Advanced Capabilities (Optional)
Activate optional advanced features based on requirements:
- Datastore integration for custom data storage
- Integration with Google Knowledge Graph or private enterprise knowledge graphs
- Public web interface deployment for external agent access
- Analytics dashboard for agent usage monitoring
![](https://cdn.nlark.com/yuque/0/2025/png/57829142/1761140598223-8f7249bf-931c-42c2-8f33-a916c0a4bdcb.png)
*Fig. 5: AgentSpace advanced capabilities*

### 5. Access Agent Chat Interface
Upon completion of configuration, users can interact with the custom agent via the native AgentSpace chat interface.
![](https://cdn.nlark.com/yuque/0/2025/png/57829142/1761140598253-264347cb-f46d-468c-abcc-a87eb21ef909.png)
*Fig. 6: The AgentSpace User Interface for initiating a chat with your Agent.*

## Conclusion
AgentSpace provides a full-stack functional framework for developing and deploying custom AI agents within an organization's existing digital infrastructure. It abstracts underlying technical complexity by linking backend systems (including autonomous reasoning and enterprise knowledge graph mapping) to a no-code graphical user interface, enabling non-technical users to build specialized multi-agent systems. The platform's core objective is to embed automated analytical and operational capabilities directly into core workflows to improve process efficiency and enhance data-driven analysis.

Practical hands-on training is available via the *"Build a Gen AI Agent with Agentspace"* lab on Google Cloud Skills Boost for structured skill development.

## References
1. Create a no-code agent with Agent Designer, https://cloud.google.com/agentspace/agentspace-enterprise/docs/agent-designer
2. Google Cloud Skills Boost, https://www.cloudskillsboost.google/
