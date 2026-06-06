---
source: raw/05_代码与项目/skills/skills/README.md
raw_sha256: d7c5c2f9b248c7c0b31f093cf22b9a7407f5b093c8ca9ebe75a5b6845b02b76e
compiled_at: 2026-04-14T04:09:21.141Z
---
# Claude Skills 官方示例仓库

> [!NOTE]
> 来源路径：`raw/05_代码与项目/skills/skills/README.md`

---

## TL;DR
本仓库是 Anthropic 官方提供的 Claude Agent Skills 示例实现，包含可直接参考的技能样例、官方规格说明和创建模板，支持在 Claude Code、Claude.ai 和 Claude API 中使用，可用于学习如何为 Claude 创建自定义技能、复用生产级成熟技能模式。

---

## 核心要点

### 什么是 Skills？
Skills 是 Claude 动态加载的指令、脚本和资源集合，用于提升 Claude 在特定任务上的表现，让 Claude 可以按照可重复的流程完成特定任务，常见场景包括：
- 遵循企业品牌规范创建文档
- 按照组织特定工作流分析数据
- 自动化个人任务

### 本仓库内容说明
| 分类 | 路径 | 说明 | 许可协议 |
|------|------|------|----------|
| 技能示例 | `./skills` | 覆盖创意设计、开发技术、企业沟通、文档处理等多个领域 | 大部分为 Apache 2.0 开源，文档处理类（docx/pdf/pptx/xlsx）为源码可用，非开源 |
| 规格说明 | `./spec` | Agent Skills 官方标准 | - |
| 创建模板 | `./template` | 自定义技能起步模板 | - |

### 使用方式

#### Claude Code
可将本仓库注册为插件市场，安装后即可使用：
```bash
# 注册市场
/plugin marketplace add anthropics/skills

# 直接安装技能包
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```
安装后仅需在提问中提及对应技能即可使用，例如：`Use the PDF skill to extract the form fields from path/to/some-file.pdf`

#### Claude.ai
本仓库的所有示例技能已默认对 Claude.ai 付费计划开放，上传自定义技能可参考官方使用指南。

#### Claude API
支持通过 API 使用预构建技能、上传自定义技能，可参考官方快速开始文档。

### 如何创建自定义技能
创建技能非常简单，仅需一个文件夹+一个`SKILL.md`文件即可：
`SKILL.md`结构示例：
```markdown
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---

# My Skill Name
[此处添加 Claude 激活技能后需要遵循的指令]

## Examples
- Example usage 1
- Example usage 2

## Guidelines
- Guideline 1
- Guideline 2
```
必填的YAML前置元数据仅两个字段：
- `name`：技能唯一标识，要求小写、用连字符分隔空格
- `description`：完整描述技能的功能和适用场景

下方的Markdown内容包含 Claude 需要遵循的指令、示例和规则。

### 合作伙伴技能
本仓库会展示第三方合作伙伴创建的优秀技能示例，目前已收录：
- [Notion Skills for Claude](https://www.notion.so/notiondevs/Notion-Skills-for-Claude-28da4445d27180c7af1df7d8615723d0)

---

## 引用证据（原始片段）

> **Note:** This repository contains Anthropic's implementation of skills for Claude. For information about the Agent Skills standard, see [agentskills.io](http://agentskills.io).
>
> Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. Skills teach Claude how to complete specific tasks in a repeatable way, whether that's creating documents with your company's brand guidelines, analyzing data using your organization's specific workflows, or automating personal tasks.
>
> This repository contains skills that demonstrate what's possible with Claude's skills system. These skills range from creative applications (art, music, design) to technical tasks (testing web apps, MCP server generation) to enterprise workflows (communications, branding, etc.).
>
> Many skills in this repo are open source (Apache 2.0). We've also included the document creation & editing skills that power [Claude's document capabilities](https://www.anthropic.com/news/create-files) under the hood in the [`skills/docx`](./skills/docx), [`skills/pdf`](./skills/pdf), [`skills/pptx`](./skills/pptx), and [`skills/xlsx`](./skills/xlsx) subfolders. These are source-available, not open source, but we wanted to share these with developers as a reference for more complex skills that are actively used in a production AI application.
>
> **Disclaimer**
> **These skills are provided for demonstration and educational purposes only.** While some of these capabilities may be available in Claude, the implementations and behaviors you receive from Claude may differ from what is shown in these skills. These skills are meant to illustrate patterns and possibilities. Always test skills thoroughly in your own environment before relying on them for critical tasks.

---

## 相关链接
- 官方说明文档：
  - [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
  - [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
  - [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
  - [Equipping agents for the real world with Agent Skills](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
  - [Skills API Quickstart](https://docs.claude.com/en/api/skills-guide#creating-a-skill)
- Agent Skills 标准官网：[agentskills.io](http://agentskills.io)

---

## 冲突标注
当前本页未发现与其他已知来源存在内容分歧。
