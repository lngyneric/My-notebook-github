# 操作日志

按时间顺序记录所有维基操作，包括摄入、查询和维护活动。

## 日志格式

- **摄入**: `## [YYYY-MM-DD] ingest | Source Title`
- **查询**: `## [YYYY-MM-DD] query | Question`
- **维护**: `## [YYYY-MM-DD] lint | Description`

## 日志记录

## [2026-04-10] ingest | Wiki 架构设计文档
初始化维基架构，创建输入层、维基层和输出层目录结构。

## [2026-04-10] setup | 创建索引和日志文件
创建 `wiki/index.md` 和 `wiki/log.md` 两个核心文件。

## [2026-04-10] ingest | Karpathy LLM Wiki Gist
摄入 Andrej Karpathy 提出的 LLM Wiki 模式文档，创建以下页面：
- 概念页面: [[llm-wiki-pattern]]
- 摘要页面: [[karpathy-llm-wiki-20260410]]
- 实体页面: [[andrej-karpathy]]
- 架构设计: [[Wiki 架构设计]]
- 结构规范: [[SCHEMA]]

更新索引文件 `wiki/index.md`，添加所有新页面的条目。

## [2026-04-10] setup | 创建快速开始指南
创建 `wiki/QUICKSTART.md` 工作流程速查指南，方便日常使用。

## [2026-04-10] setup | 创建各层说明文档
创建以下说明文档：
- `input/README.md` - 输入层使用说明
- `output/README.md` - 输出层使用说明
- `wiki/README.md` - 维基层使用说明
- `维基工作区摘要.md` - 工作区概览

更新索引文件，添加新的核心文件条目。

---

*本日志自动追加更新，保留所有操作历史供查阅。*
## 2026-04-14 03:26:06.053 init
- root: C:\Users\lingyun\Documents\BaiduSyncdisk\xcxnotes\content
- created: raw/, wiki/, outputs/, prompts/, config/, .llm-wiki/
- config: config\llm-wiki.config.json

## 2026-04-14 03:37:43.061 compile
- rawTotal: 11
- wikiUpdated: 11
- wiki: wiki/sources/ARCHITECTURE.md
- wiki: wiki/sources/BITABLE_GUIDE.md
- wiki: wiki/sources/DEPLOYMENT.md
- wiki: wiki/sources/INTEGRATION_SPEC.md
- wiki: wiki/sources/Karpathy-LLM-Wiki-完整实现总结.md
- wiki: wiki/sources/LLM-Wiki-建立完成总结.md
- wiki: wiki/sources/org_chart.md
- wiki: wiki/sources/Wiki架构设计.md
- wiki: wiki/sources/企业微信智能表格对接MySQL数据源方案.md
- wiki: wiki/sources/第一阶段里程碑回顾与变更合并.md
- wiki: wiki/sources/维基工作区摘要.md
- status: ok

## 2026-04-14 03:43:38.216 query
- question: 从ai学习流程中现在比较关注的重点请列5个
- contextItems: 0
- output: outputs/20260414T034338-从ai学习流程中现在比较关注的重点请列5个.md
- status: ok

## 2026-04-14 03:54:04.084 query
- question: 从ai学习流程中现在比较关注的重点请列5个
- contextItems: 1
- output: outputs/20260414T035404-从ai学习流程中现在比较关注的重点请列5个.md
- status: ok

## 2026-04-14 05:20:57.444 compile
- rawTotal: 231
- wikiUpdated: 218
- wiki: wiki/sources/01_每日工作记录/zou_fengjing_status_report.md
- wiki: wiki/sources/02_项目文档/AI培训与学习系统/12月到1月AI使用情况收集.md
- wiki: wiki/sources/02_项目文档/AI培训与学习系统/Training_Flowchart.md
- wiki: wiki/sources/02_项目文档/AI培训与学习系统/Training_Reinforcement_Plan.md
- wiki: wiki/sources/02_项目文档/AI培训与学习系统/Tutor_Mentoring_Guide.md
- wiki: wiki/sources/02_项目文档/AI培训与学习系统/人力资源培训提纲.md
- wiki: wiki/sources/02_项目文档/AI培训与学习系统/创建企业培训机器人.md
- wiki: wiki/sources/Openmaic/ARCHITECTURE.md
- wiki: wiki/sources/Openmaic/BITABLE_GUIDE.md
- wiki: wiki/sources/Openmaic/checklist.md
- wiki: wiki/sources/Openmaic/DEPLOYMENT.md
- wiki: wiki/sources/Openmaic/INTEGRATION_SPEC.md
- wiki: wiki/sources/Openmaic/README-zh.md
- wiki: wiki/sources/Openmaic/README.md
- wiki: wiki/sources/Openmaic/spec.md
- wiki: wiki/sources/Openmaic/tasks.md
- wiki: wiki/sources/04_文档与参考/Markdown文档/academic_tutor_skill.md
- wiki: wiki/sources/04_文档与参考/Markdown文档/AI github 汇总.md
- wiki: wiki/sources/04_文档与参考/Markdown文档/AI-Math-Assistant Tool Calling.md
- wiki: wiki/sources/04_文档与参考/Markdown文档/AI流程：网页改造APP.md
- wiki: wiki/sources/04_文档与参考/Markdown文档/Astrill VPN 配置 Antigravity_Gemini CLI_Claude Code 分离规则教程.md
- wiki: wiki/sources/04_文档与参考/Markdown文档/Build Multi-Agent Chatbot with AG2 AutoGen for Healthcare.md
- wiki: wiki/sources/04_文档与参考/Markdown文档/Build Reasoning and Acting AI Agents with LangGraph.md
- wiki: wiki/sources/04_文档与参考/Markdown文档/Implement Workflow Patterns with LangGraph.md
- wiki: wiki/sources/04_文档与参考/Markdown文档/JSON Canvas.md
- wiki: wiki/sources/04_文档与参考/Markdown文档/Obsidian Bases.md
- wiki: wiki/sources/04_文档与参考/Markdown文档/Obsidian 笔记本教程(高级).md
- wiki: wiki/sources/04_文档与参考/Markdown文档/Ohms_Law_Water_Analogy.md
- wiki: wiki/sources/04_文档与参考/Markdown文档/pydanticai-101.md
- wiki: wiki/sources/04_文档与参考/Markdown文档/RA_AI_Platform.openspec.md
- wiki: wiki/sources/04_文档与参考/Markdown文档/RA_AI_Platform_OpenSpec_Proposal.md
- wiki: wiki/sources/04_文档与参考/Markdown文档/SKILL.md
- wiki: wiki/sources/04_文档与参考/Markdown文档/注意.md
- wiki: wiki/sources/04_文档与参考/Markdown文档/知识图谱嵌入技术全解析：原理、调优与业务价值.md
- wiki: wiki/sources/02_项目文档/AI智能问答平台/RA部门AI智能问答平台搭建全攻略：从0到1的实践经验.md
- wiki: wiki/sources/02_项目文档/AI智能问答平台/RA部门AI智能问答平台搭建经验总结.md
- wiki: wiki/sources/03_技能与工具/Claude_Code/Claude Code.md
- wiki: wiki/sources/03_技能与工具/Claude_Code/claude_skill_automation_guide.md
- wiki: wiki/sources/03_技能与工具/Graph-RAG/Agentic Graph-RAG Over Social-Network Knowledge Graphs.md
- wiki: wiki/sources/03_技能与工具/多模态RAG/Multimodal_RAG_KG_Diagrams.md
- wiki: wiki/sources/03_技能与工具/多模态RAG/Multimodal_RAG_KG_Tutor_Guide.md
- wiki: wiki/sources/03_技能与工具/多模态RAG/多模态RAG与知识图谱构建技术全解析.md
- wiki: wiki/sources/03_技能与工具/NotebookLM/notebooklm-report-beyond-intelligence-an-introduction-to-building-re-2026-01-17.md
- wiki: wiki/sources/03_技能与工具/NotebookLM/NotebookLM_Batch_Guide.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/00-Table-of-Contents.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/000-Home.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/01-Dedication.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/02-Acknowledgment.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/03-Foreword.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/04-Thought-Leader.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/05-Introduction.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/06-What-Makes-Agent.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/07-Chapter-01-Prompt-Chaining.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/08-Chapter-02-Routing.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/09-Chapter-03-Parallelization.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/10-Chapter-04-Reflection.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/11-Chapter-05-Tool-Use.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/12-Chapter-06-Planning.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/13-Chapter-07-Multi-Agent-Collaboration.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/14-Chapter-08-Memory-Management.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/15-Chapter-09-Learning-and-Adaptation.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/16-Chapter-10-Model-Context-Protocol.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/17-Chapter-11-Goal-Setting-And-Monitoring.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/18-Chapter-12-Exception-Handling-and-Recovery.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/19-Chapter-13-Human-in-the-Loop.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/20-Chapter-14-Knowledge-Retrieval-RAG.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/21-Chapter-15-Inter-Agent-Communication.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/22-Chapter-16-Resource-Aware-Optimization.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/23-Chapter-17-Reasoning-Techniques.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/24-Chapter-18-Guardrails-Safety-Patterns.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/25-Chapter-19-Evaluation-and-Monitoring.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/26-Chapter-20-Prioritization.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/27-Chapter-21-Exploration-and-Discovery.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/28-Appendix-A.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/29-Appendix-B.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/30-Appendix-C.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/31-Appendix-D.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/32-Appendix-E.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/33-Appendix-F.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/34-Appendix-G.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/35-Conclusion.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/36-Glossary.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/37-Index.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/AGENTS.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/CLAUDE.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/README.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/WARP.md
- wiki: wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/ANTIGRAVITY_WORKFLOW.md
- wiki: wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/API_MANAGEMENT.md
- wiki: wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/ARCHITECTURE.md
- wiki: wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/ENV_SETUP.md
- wiki: wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/QUICKSTART.md
- wiki: wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/README.md
- wiki: wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/SECURITY.md
- wiki: wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/SETUP_COMPLETE.md
- wiki: wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/SKILL.md
- wiki: wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/README.md
- wiki: wiki/sources/05_代码与项目/team-awareness-training/team-awareness-training/forms.md
- wiki: wiki/sources/05_代码与项目/team-awareness-training/team-awareness-training/README.md
- wiki: wiki/sources/05_代码与项目/skills/skills/README.md
- wiki: wiki/sources/05_代码与项目/skills/skills/THIRD_PARTY_NOTICES.md
- wiki: wiki/sources/05_代码与项目/TA/TA/RA部门AI智能问答平台搭建全攻略：从0到1的实践经验.md
- wiki: wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/prompts/transition_template.md
- wiki: wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/styles/gradient-glass.md
- wiki: wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/styles/vector-illustration.md
- wiki: wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/Video/首尾帧视频生成提示词.md
- wiki: wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/3D信息图.md
- wiki: wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/Anthropic 风格的PPT生成.md
- wiki: wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/云端岛屿城市海报.md
- wiki: wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/任意领域领域从夯到拉打分.md
- wiki: wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/天气移轴 Q 版模型.md
- wiki: wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/屏幕使用时长可视化海报.md
- wiki: wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/影视剧、小说、游戏场景海报.md
- wiki: wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/影视剧、小说、游戏武器海报.md
- wiki: wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/渐变拟物玻璃卡片风格 PPT.md
- wiki: wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/玻璃瓶微缩地点模型.md
- wiki: wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/矢量插画风格PPT生成.md
- wiki: wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/社交媒体信息展示卡片.md
- wiki: wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/诺基亚手机照片滤镜.md
- wiki: wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/邪恶大香蕉吐槽世间万物.md
- wiki: wiki/sources/05_代码与项目/team-awareness-training/team-awareness-training/sessions/session-01-stress.md
- wiki: wiki/sources/05_代码与项目/team-awareness-training/team-awareness-training/sessions/session-02-meditation.md
- wiki: wiki/sources/05_代码与项目/team-awareness-training/team-awareness-training/sessions/session-03-mindfulness.md
- wiki: wiki/sources/05_代码与项目/team-awareness-training/team-awareness-training/sessions/session-04-eq.md
- wiki: wiki/sources/05_代码与项目/team-awareness-training/team-awareness-training/sessions/session-05-flow.md
- wiki: wiki/sources/05_代码与项目/team-awareness-training/team-awareness-training/sessions/session-06-culture.md
- wiki: wiki/sources/05_代码与项目/team-awareness-training/team-awareness-training/sessions/session-07-well-being.md
- wiki: wiki/sources/05_代码与项目/team-awareness-training/team-awareness-training/sessions/session-08-further-training.md
- wiki: wiki/sources/05_代码与项目/skills/skills/template/SKILL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/spec/agent-skills-spec.md
- wiki: wiki/sources/06_素材资源/附件与资料/附件/academic_tutor_skill.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/doc-coauthoring/SKILL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/LICENSE.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/SKILL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/brand-guidelines/LICENSE.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/brand-guidelines/SKILL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/algorithmic-art/LICENSE.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/algorithmic-art/SKILL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/docx/docx-js.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/docx/LICENSE.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/docx/ooxml.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/docx/SKILL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/frontend-design/LICENSE.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/frontend-design/SKILL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/mcp-builder/LICENSE.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/mcp-builder/SKILL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/internal-comms/LICENSE.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/internal-comms/SKILL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/pdf/forms.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/pdf/LICENSE.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/pdf/reference.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/pdf/SKILL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/pptx/html2pptx.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/pptx/LICENSE.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/pptx/ooxml.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/pptx/SKILL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/skill-creator/LICENSE.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/skill-creator/SKILL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/skill-creator/未命名.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/slack-gif-creator/LICENSE.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/slack-gif-creator/requirements.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/slack-gif-creator/SKILL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/LICENSE.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/SKILL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/ArsenalSC-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/BigShoulders-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/Boldonse-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/BricolageGrotesque-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/CrimsonPro-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/DMMono-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/EricaOne-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/GeistMono-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/Gloock-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/IBMPlexMono-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/InstrumentSans-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/Italiana-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/JetBrainsMono-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/Jura-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/LibreBaskerville-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/Lora-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/NationalPark-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/NothingYouCouldDo-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/Outfit-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/PixelifySans-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/PoiretOne-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/RedHatMono-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/Silkscreen-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/SmoochSans-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/Tektur-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/WorkSans-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/YoungSerif-OFL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/web-artifacts-builder/LICENSE.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/web-artifacts-builder/SKILL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/webapp-testing/LICENSE.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/webapp-testing/SKILL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/xlsx/LICENSE.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/xlsx/SKILL.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/mcp-builder/reference/evaluation.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/mcp-builder/reference/mcp_best_practices.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/mcp-builder/reference/node_mcp_server.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/mcp-builder/reference/python_mcp_server.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/mcp-builder/scripts/requirements.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/skill-creator/references/output-patterns.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/skill-creator/references/workflows.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/internal-comms/examples/3p-updates.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/internal-comms/examples/company-newsletter.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/internal-comms/examples/faq-answers.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/internal-comms/examples/general-comms.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/themes/arctic-frost.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/themes/botanical-garden.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/themes/desert-rose.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/themes/forest-canopy.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/themes/golden-hour.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/themes/midnight-galaxy.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/themes/modern-minimalist.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/themes/ocean-depths.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/themes/sunset-boulevard.md
- wiki: wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/themes/tech-innovation.md
- status: error
- error: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/rules/chinese-copywriting-guidelines.md: Error: net::ERR_NETWORK_IO_SUSPENDED\n    at SimpleURLLoaderWrapper.<anonymous> (node:electron/js2c/browser_init:2:124140)\n    at SimpleURLLoaderWrapper.emit (node:events:519:28)
- error: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/rules/rules.md: Error: net::ERR_NETWORK_IO_SUSPENDED\n    at SimpleURLLoaderWrapper.<anonymous> (node:electron/js2c/browser_init:2:124140)\n    at SimpleURLLoaderWrapper.emit (node:events:519:28)

## 2026-04-14 08:36:16.194 init
- root: C:\Users\lingyun\Documents\BaiduSyncdisk\xcxnotes\content
- created: raw/, wiki/, outputs/, prompts/, config/, .llm-wiki/
- config: config\llm-wiki.config.json

## 2026-04-14 08:37:25.509 compile
- rawTotal: 231
- wikiUpdated: 2
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/rules/chinese-copywriting-guidelines.md
- wiki: wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/rules/rules.md
- status: error
- error: Embedding failed for wiki/sources/ARCHITECTURE.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/BITABLE_GUIDE.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/DEPLOYMENT.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/INTEGRATION_SPEC.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/Karpathy-LLM-Wiki-完整实现总结.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/LLM-Wiki-建立完成总结.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/org_chart.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/Wiki架构设计.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/企业微信智能表格对接MySQL数据源方案.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/第一阶段里程碑回顾与变更合并.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/维基工作区摘要.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/01_每日工作记录/zou_fengjing_status_report.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/Openmaic/ARCHITECTURE.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/Openmaic/BITABLE_GUIDE.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/Openmaic/checklist.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/Openmaic/DEPLOYMENT.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/Openmaic/INTEGRATION_SPEC.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/Openmaic/README-zh.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/Openmaic/README.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/Openmaic/spec.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/Openmaic/tasks.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/04_文档与参考/Markdown文档/academic_tutor_skill.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/04_文档与参考/Markdown文档/AI github 汇总.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/04_文档与参考/Markdown文档/AI-Math-Assistant Tool Calling.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/04_文档与参考/Markdown文档/AI流程：网页改造APP.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/04_文档与参考/Markdown文档/Astrill VPN 配置 Antigravity_Gemini CLI_Claude Code 分离规则教程.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/04_文档与参考/Markdown文档/Build Multi-Agent Chatbot with AG2 AutoGen for Healthcare.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/04_文档与参考/Markdown文档/Build Reasoning and Acting AI Agents with LangGraph.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/04_文档与参考/Markdown文档/Implement Workflow Patterns with LangGraph.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/04_文档与参考/Markdown文档/JSON Canvas.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/04_文档与参考/Markdown文档/Obsidian Bases.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/04_文档与参考/Markdown文档/Obsidian 笔记本教程(高级).md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/04_文档与参考/Markdown文档/Ohms_Law_Water_Analogy.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/04_文档与参考/Markdown文档/pydanticai-101.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/04_文档与参考/Markdown文档/RA_AI_Platform.openspec.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/04_文档与参考/Markdown文档/RA_AI_Platform_OpenSpec_Proposal.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/04_文档与参考/Markdown文档/SKILL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/04_文档与参考/Markdown文档/注意.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/04_文档与参考/Markdown文档/知识图谱嵌入技术全解析：原理、调优与业务价值.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/03_技能与工具/Claude_Code/Claude Code.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/03_技能与工具/Claude_Code/claude_skill_automation_guide.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/03_技能与工具/NotebookLM/notebooklm-report-beyond-intelligence-an-introduction-to-building-re-2026-01-17.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/03_技能与工具/NotebookLM/NotebookLM_Batch_Guide.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/03_技能与工具/多模态RAG/Multimodal_RAG_KG_Diagrams.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/03_技能与工具/多模态RAG/Multimodal_RAG_KG_Tutor_Guide.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/03_技能与工具/多模态RAG/多模态RAG与知识图谱构建技术全解析.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/02_项目文档/AI培训与学习系统/12月到1月AI使用情况收集.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/02_项目文档/AI培训与学习系统/Training_Flowchart.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/02_项目文档/AI培训与学习系统/Training_Reinforcement_Plan.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/02_项目文档/AI培训与学习系统/Tutor_Mentoring_Guide.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/02_项目文档/AI培训与学习系统/人力资源培训提纲.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/02_项目文档/AI培训与学习系统/创建企业培训机器人.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/03_技能与工具/Graph-RAG/Agentic Graph-RAG Over Social-Network Knowledge Graphs.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/02_项目文档/AI智能问答平台/RA部门AI智能问答平台搭建全攻略：从0到1的实践经验.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/02_项目文档/AI智能问答平台/RA部门AI智能问答平台搭建经验总结.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/README.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/README.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/THIRD_PARTY_NOTICES.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/TA/TA/RA部门AI智能问答平台搭建全攻略：从0到1的实践经验.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/ANTIGRAVITY_WORKFLOW.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/API_MANAGEMENT.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/ARCHITECTURE.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/ENV_SETUP.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/QUICKSTART.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/README.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/SECURITY.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/SETUP_COMPLETE.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/SKILL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/team-awareness-training/team-awareness-training/forms.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/team-awareness-training/team-awareness-training/README.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/00-Table-of-Contents.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/000-Home.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/01-Dedication.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/02-Acknowledgment.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/03-Foreword.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/04-Thought-Leader.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/05-Introduction.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/06-What-Makes-Agent.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/07-Chapter-01-Prompt-Chaining.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/08-Chapter-02-Routing.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/09-Chapter-03-Parallelization.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/10-Chapter-04-Reflection.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/11-Chapter-05-Tool-Use.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/12-Chapter-06-Planning.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/13-Chapter-07-Multi-Agent-Collaboration.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/14-Chapter-08-Memory-Management.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/15-Chapter-09-Learning-and-Adaptation.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/16-Chapter-10-Model-Context-Protocol.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/17-Chapter-11-Goal-Setting-And-Monitoring.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/18-Chapter-12-Exception-Handling-and-Recovery.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/19-Chapter-13-Human-in-the-Loop.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/20-Chapter-14-Knowledge-Retrieval-RAG.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/21-Chapter-15-Inter-Agent-Communication.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/22-Chapter-16-Resource-Aware-Optimization.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/23-Chapter-17-Reasoning-Techniques.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/24-Chapter-18-Guardrails-Safety-Patterns.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/25-Chapter-19-Evaluation-and-Monitoring.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/26-Chapter-20-Prioritization.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/27-Chapter-21-Exploration-and-Discovery.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/28-Appendix-A.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/29-Appendix-B.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/30-Appendix-C.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/31-Appendix-D.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/32-Appendix-E.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/33-Appendix-F.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/34-Appendix-G.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/35-Conclusion.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/36-Glossary.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/37-Index.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/AGENTS.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/CLAUDE.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/README.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/WARP.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/06_素材资源/附件与资料/附件/academic_tutor_skill.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/3D信息图.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/Anthropic 风格的PPT生成.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/云端岛屿城市海报.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/任意领域领域从夯到拉打分.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/天气移轴 Q 版模型.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/屏幕使用时长可视化海报.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/影视剧、小说、游戏场景海报.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/影视剧、小说、游戏武器海报.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/渐变拟物玻璃卡片风格 PPT.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/玻璃瓶微缩地点模型.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/矢量插画风格PPT生成.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/社交媒体信息展示卡片.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/诺基亚手机照片滤镜.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/image/邪恶大香蕉吐槽世间万物.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/guizang-s-prompt-main/guizang-s-prompt-main/Video/首尾帧视频生成提示词.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/template/SKILL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/spec/agent-skills-spec.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/prompts/transition_template.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/styles/gradient-glass.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/styles/vector-illustration.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/team-awareness-training/team-awareness-training/sessions/session-01-stress.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/team-awareness-training/team-awareness-training/sessions/session-02-meditation.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/team-awareness-training/team-awareness-training/sessions/session-03-mindfulness.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/team-awareness-training/team-awareness-training/sessions/session-04-eq.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/team-awareness-training/team-awareness-training/sessions/session-05-flow.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/team-awareness-training/team-awareness-training/sessions/session-06-culture.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/team-awareness-training/team-awareness-training/sessions/session-07-well-being.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/team-awareness-training/team-awareness-training/sessions/session-08-further-training.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/rules/chinese-copywriting-guidelines.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/agentic-design-patterns/agentic-design-patterns/rules/rules.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/algorithmic-art/LICENSE.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/algorithmic-art/SKILL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/brand-guidelines/LICENSE.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/brand-guidelines/SKILL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/doc-coauthoring/SKILL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/LICENSE.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/SKILL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/frontend-design/LICENSE.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/frontend-design/SKILL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/docx/docx-js.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/docx/LICENSE.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/docx/ooxml.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/docx/SKILL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/internal-comms/LICENSE.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/internal-comms/SKILL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/pdf/forms.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/pdf/LICENSE.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/pdf/reference.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/pdf/SKILL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/pptx/html2pptx.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/pptx/LICENSE.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/pptx/ooxml.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/pptx/SKILL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/skill-creator/LICENSE.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/skill-creator/SKILL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/skill-creator/未命名.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/mcp-builder/LICENSE.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/mcp-builder/SKILL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/slack-gif-creator/LICENSE.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/slack-gif-creator/requirements.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/slack-gif-creator/SKILL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/LICENSE.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/SKILL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/web-artifacts-builder/LICENSE.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/web-artifacts-builder/SKILL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/webapp-testing/LICENSE.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/webapp-testing/SKILL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/xlsx/LICENSE.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/xlsx/SKILL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/ArsenalSC-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/BigShoulders-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/Boldonse-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/BricolageGrotesque-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/CrimsonPro-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/DMMono-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/EricaOne-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/GeistMono-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/Gloock-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/IBMPlexMono-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/InstrumentSans-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/Italiana-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/JetBrainsMono-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/Jura-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/LibreBaskerville-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/Lora-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/NationalPark-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/NothingYouCouldDo-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/Outfit-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/PixelifySans-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/PoiretOne-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/RedHatMono-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/Silkscreen-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/SmoochSans-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/Tektur-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/WorkSans-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/canvas-design/canvas-fonts/YoungSerif-OFL.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/internal-comms/examples/3p-updates.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/internal-comms/examples/company-newsletter.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/internal-comms/examples/faq-answers.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/internal-comms/examples/general-comms.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/skill-creator/references/output-patterns.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/skill-creator/references/workflows.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/mcp-builder/reference/evaluation.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/mcp-builder/reference/mcp_best_practices.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/mcp-builder/reference/node_mcp_server.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/mcp-builder/reference/python_mcp_server.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/mcp-builder/scripts/requirements.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/themes/arctic-frost.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/themes/botanical-garden.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/themes/desert-rose.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/themes/forest-canopy.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/themes/golden-hour.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/themes/midnight-galaxy.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/themes/modern-minimalist.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/themes/ocean-depths.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/themes/sunset-boulevard.md: Embeddings request failed: 404  404 page not found\n
- error: Embedding failed for wiki/sources/05_代码与项目/skills/skills/skills/theme-factory/themes/tech-innovation.md: Embeddings request failed: 404  404 page not found\n

## 2026-04-14 08:48:03.971 query
- question: 关于培训项目的业绩总结;3项成功案例+3项不足
- contextItems: 8
- output: outputs/20260414T084803-关于培训项目的业绩总结-3项成功案例-3项不足.md
- status: ok

## 2026-04-14 08:48:21.365 compile
- rawTotal: 231
- wikiUpdated: 0
- status: ok

## 2026-04-14 09:12:35.443 query
- question: 从ai学习流程中现在比较关注的重点请列5个
- contextItems: 8
- output: outputs/20260414T091235-从ai学习流程中现在比较关注的重点请列5个.md
- status: ok

## 2026-04-14 09:29:20.360 query
- question: 向上模板格式
- contextItems: 1
- output: outputs/20260414T092920-向上模板格式.md
- status: ok

## 2026-04-14 13:19:48.436 compile
- rawTotal: 232
- wikiUpdated: 1
- wiki: wiki/sources/HR部门AI应用汇报 (2).md
- status: ok

## 2026-04-15 00:38:52.205 compile
- rawTotal: 317
- wikiUpdated: 85
- wiki: wiki/sources/02_每日工作记录/Daily_Report_2026-02-10.md
- wiki: wiki/sources/02_每日工作记录/Daily_Report_2026-02-11.md
- wiki: wiki/sources/02_每日工作记录/Daily_Work_20260120.md
- wiki: wiki/sources/02_每日工作记录/Daily_Work_20260120_CN_EN.md
- wiki: wiki/sources/02_每日工作记录/Daily_Work_20260121.md
- wiki: wiki/sources/01_项目文档/产品需求与功能设计/bulk-course-import.md
- wiki: wiki/sources/01_项目文档/产品需求与功能设计/产品需求文档.md
- wiki: wiki/sources/01_项目文档/产品需求与功能设计/功能准备.md
- wiki: wiki/sources/01_项目文档/产品需求与功能设计/智能课程推荐系统-V0.1.md
- wiki: wiki/sources/01_项目文档/培训体系设计/2025年度培训计划表.md
- wiki: wiki/sources/01_项目文档/培训体系设计/培训课程建议.md
- wiki: wiki/sources/01_项目文档/培训体系设计/培训需求调查表.md
- wiki: wiki/sources/04_技能与工具/Claude_Skill/claude_skill_automation_guide.md
- wiki: wiki/sources/05_示例数据/Sample/2025_new_org_structure.md
- wiki: wiki/sources/05_示例数据/Sample/zou_fengjing_status_report.md
- wiki: wiki/sources/07_文档与参考/Markdown文档/2026年1月的AIx信息.md
- wiki: wiki/sources/07_文档与参考/Markdown文档/README.md
- wiki: wiki/sources/07_文档与参考/Markdown文档/未命名.md
- wiki: wiki/sources/07_文档与参考/Markdown文档/注册过程人工智能典型应用场景清单-96cd7be1fc.md
- wiki: wiki/sources/07_文档与参考/其他文档/HR部门AI应用汇报 (2).md
- wiki: wiki/sources/07_文档与参考/其他文档/tomorrow.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/README.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/RELEASE-NOTES.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/agents/code-reviewer.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/commands/brainstorm.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/commands/execute-plan.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/commands/write-plan.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/docs/README.codex.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/docs/README.opencode.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/docs/testing.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/tests/claude-code/README.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/docs/windows/polyglot-hooks.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/docs/plans/2025-11-22-opencode-support-design.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/docs/plans/2025-11-22-opencode-support-implementation.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/docs/plans/2025-11-28-skills-improvements-from-user-feedback.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/brainstorming/SKILL.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/dispatching-parallel-agents/SKILL.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/executing-plans/SKILL.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/finishing-a-development-branch/SKILL.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/receiving-code-review/SKILL.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/requesting-code-review/code-reviewer.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/requesting-code-review/SKILL.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/subagent-driven-development/code-quality-reviewer-prompt.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/subagent-driven-development/implementer-prompt.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/subagent-driven-development/SKILL.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/subagent-driven-development/spec-reviewer-prompt.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/systematic-debugging/condition-based-waiting.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/systematic-debugging/CREATION-LOG.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/systematic-debugging/defense-in-depth.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/systematic-debugging/root-cause-tracing.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/systematic-debugging/SKILL.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/systematic-debugging/test-academic.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/systematic-debugging/test-pressure-1.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/systematic-debugging/test-pressure-2.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/systematic-debugging/test-pressure-3.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/test-driven-development/SKILL.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/test-driven-development/testing-anti-patterns.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/using-git-worktrees/SKILL.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/verification-before-completion/SKILL.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/using-superpowers/SKILL.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/writing-skills/anthropic-best-practices.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/writing-skills/persuasion-principles.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/writing-skills/SKILL.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/writing-skills/testing-skills-with-subagents.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/writing-plans/SKILL.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/tests/explicit-skill-requests/prompts/action-oriented.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/tests/explicit-skill-requests/prompts/after-planning-flow.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/tests/explicit-skill-requests/prompts/claude-suggested-it.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/tests/explicit-skill-requests/prompts/i-know-what-sdd-means.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/tests/explicit-skill-requests/prompts/mid-conversation-execute-plan.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/tests/explicit-skill-requests/prompts/please-use-brainstorming.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/tests/explicit-skill-requests/prompts/skip-formalities.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/tests/explicit-skill-requests/prompts/subagent-driven-development-please.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/tests/explicit-skill-requests/prompts/use-systematic-debugging.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/tests/skill-triggering/prompts/dispatching-parallel-agents.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/tests/skill-triggering/prompts/executing-plans.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/tests/skill-triggering/prompts/requesting-code-review.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/tests/skill-triggering/prompts/systematic-debugging.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/tests/skill-triggering/prompts/test-driven-development.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/tests/skill-triggering/prompts/writing-plans.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/tests/subagent-driven-dev/go-fractals/design.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/tests/subagent-driven-dev/go-fractals/plan.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/tests/subagent-driven-dev/svelte-todo/design.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/tests/subagent-driven-dev/svelte-todo/plan.md
- wiki: wiki/sources/04_技能与工具/Superpowers/superpowers-main/skills/writing-skills/examples/CLAUDE_MD_TESTING.md
- status: ok

## 2026-04-15 03:33:08.517 compile
- rawTotal: 318
- wikiUpdated: 1
- languageSetting: Original
- wiki: wiki/sources/00_202604统计/AI证书统计060415.md (lang: Original)
- status: ok

## 2026-04-15 03:34:20.433 query
- question: 202604统计各个部门AI证书获取的完成情况
- contextItems: 8
- output: outputs/20260415T033420-202604统计各个部门ai证书获取的完成情况.md
- status: ok

## 2026-04-15 03:41:32.933 query
- question: 从md第一行表头查看看取证情况和效率提升百分比 %数字，按部门和人名为每个人都生成统计表，如果没有具体信息也进行统计不要遗漏人名
- contextItems: 8
- output: outputs/20260415T034132-从md第一行表头查看看取证情况和效率提升百分比-数字-按部门和人名为每个人都生成统计表-如果没有具体信息也进行统计不要遗.md
- status: ok

## 2026-04-20 02:18:29.416 compile
- rawTotal: 318
- wikiUpdated: 1
- languageSetting: Original
- wiki: wiki/sources/00_202604统计/各部门AI个人能力提升计划.md (lang: Original)
- status: ok

## 2026-04-20 03:41:50.250 init
- root: C:\Users\lingyun\Documents\BaiduSyncdisk\xcxnotes\content
- created: raw/, wiki/, outputs/, prompts/, config/, .llm-wiki/
- config: config\llm-wiki.config.json

## 2026-04-20 03:44:39.473 init
- root: C:\Users\lingyun\Documents\BaiduSyncdisk\xcxnotes\content
- created: raw/, wiki/, outputs/, prompts/, config/, .llm-wiki/
- config: config\llm-wiki.config.json

## 2026-04-20 03:44:56.157 compile
- rawTotal: 318
- wikiUpdated: 0
- languageSetting: Original
- status: ok

## 2026-04-21 01:10:37.105 compile
- rawTotal: 319
- wikiUpdated: 1
- languageSetting: Original
- wiki: wiki/summaries/01_项目文档/HR信息生命周期管理系统/README.md (lang: Original)
- status: ok

## 2026-04-21 01:17:49.232 compile
- rawTotal: 319
- wikiUpdated: 0
- languageSetting: Original
- status: ok

## 2026-04-21 01:48:42.891 query
- question: 推荐5条和HR相关的AI发展项目
- contextItems: 0
- output: outputs/20260421T014842-推荐5条和hr相关的ai发展项目.md
- status: ok

## 2026-04-21 01:51:01.107 compile
- rawTotal: 319
- wikiUpdated: 0
- languageSetting: Original
- status: ok

## 2026-04-21 02:06:52.248 compile
- rawTotal: 319
- wikiUpdated: 0
- languageSetting: Original
- status: ok

## 2026-04-21 02:07:57.803 compile
- rawTotal: 319
- wikiUpdated: 0
- languageSetting: Original
- status: ok

## 2026-04-24 03:53:49.458 init
- root: C:\Users\lingyun\Documents\BaiduSyncdisk\xcxnotes\content
- created: raw/, wiki/, outputs/, prompts/, config/, .llm-wiki/
- config: config\llm-wiki.config.json

## 2026-04-24 04:00:35.847 init
- root: C:\Users\lingyun\Documents\BaiduSyncdisk\xcxnotes\content
- created: raw/, wiki/, outputs/, prompts/, config/, .llm-wiki/
- config: config\llm-wiki.config.json

## 2026-04-24 04:07:24.883 query
- question: 三分法对培训分析
- contextItems: 0
- output: outputs/20260424T040724-三分法对培训分析.md
- status: ok

## 2026-04-24 04:07:46.721 compile
- rawTotal: 332
- wikiUpdated: 13
- languageSetting: Original
- wiki: wiki/summaries/Books/PMP考试全程指南/PMP考试全程指南.md (lang: Original)
- wiki: wiki/summaries/Books/SAP ECC 5.06.0 总账系统应用指南（第2版）/SAP ECC 5.06.0 总账系统应用指南（第2版）.md (lang: Original)
- wiki: wiki/summaries/Books/心灵奇旅 Soul（迪士尼大电影英文原版）/心灵奇旅 Soul（迪士尼大电影英文原版）.md (lang: Original)
- wiki: wiki/summaries/Books/教育新语：人工智能时代教什么，怎么学/教育新语：人工智能时代教什么，怎么学.md (lang: Original)
- wiki: wiki/summaries/Books/朝花夕拾（人文社·语文阅读推荐丛书）/朝花夕拾（人文社·语文阅读推荐丛书）.md (lang: Original)
- wiki: wiki/summaries/Books/永夜君王/永夜君王.md (lang: Original)
- wiki: wiki/summaries/Books/汪博士解读PMP®考试（第6版）/汪博士解读PMP®考试（第6版）.md (lang: Original)
- wiki: wiki/summaries/Books/汪子熙/汪子熙.md (lang: Original)
- wiki: wiki/summaries/Books/猎魔人套装全集（1-7）/猎魔人套装全集（1-7）.md (lang: Original)
- wiki: wiki/summaries/Books/琉璃美人煞/琉璃美人煞.md (lang: Original)
- wiki: wiki/summaries/Books/认知觉醒：伴随一生的学习方法论（青少年学习版）/认知觉醒：伴随一生的学习方法论（青少年学习版）.md (lang: Original)
- wiki: wiki/summaries/Books/长安十二时辰（全集）/长安十二时辰（全集）.md (lang: Original)
- wiki: wiki/summaries/Books/银河英雄传说/银河英雄传说.md (lang: Original)
- status: ok

## 2026-06-06 03:53:53.686 init
- root: C:\Users\lingyun\Documents\BaiduSyncdisk\el-notepad-v5\content
- created: raw/, wiki/, outputs/, prompts/, config/, .llm-wiki/
- config: config\llm-wiki.config.json

## 2026-06-06 03:54:04.401 init
- root: C:\Users\lingyun\Documents\BaiduSyncdisk\el-notepad-v5\content
- created: raw/, wiki/, outputs/, prompts/, config/, .llm-wiki/
- config: config\llm-wiki.config.json

## 2026-06-06 03:57:47.164 query
- question: 对hr的ai应对要求
- contextItems: 0
- output: outputs/20260606T035747-对hr的ai应对要求.md
- status: ok

