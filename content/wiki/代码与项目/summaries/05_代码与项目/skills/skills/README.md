---
source: raw/05_代码与项目/skills/skills/README.md
raw_sha256: d7c5c2f9b248c7c0b31f093cf22b9a7407f5b093c8ca9ebe75a5b6845b02b76e
compiled_at: 2026-04-24T07:00:56.384Z
---
# Anthropic Claude Skills Repository
> **Note:** This repository contains Anthropic's implementation of skills for Claude. For information about the Agent Skills standard, see [agentskills.io](http://agentskills.io).

## Overview of Skills
Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. Skills teach Claude how to complete specific tasks in a repeatable way, including use cases such as creating branded documents, analyzing data per custom organizational workflows, and automating personal tasks.

Official support resources for skills:
- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Equipping agents for the real world with Agent Skills](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

## About This Repository
This repository hosts demonstration skills to showcase the capabilities of Claude's skills system, covering use cases including creative applications (art, music, design), technical tasks (testing web apps, MCP server generation), and enterprise workflows (communications, branding, etc.).

Each skill is self-contained in its own folder with a `SKILL.md` file that stores the instructions and metadata used by Claude. Developers may browse these skills for inspiration for custom skills, or to learn common implementation patterns.

Most skills in this repository are open source under the Apache 2.0 license. The document creation and editing skills that power [Claude's document capabilities](https://www.anthropic.com/news/create-files) are included in the [`skills/docx`](./skills/docx), [`skills/pdf`](./skills/pdf), [`skills/pptx`](./skills/pptx), and [`skills/xlsx`](./skills/xlsx) subfolders: these are source-available (not open source) and shared as a reference for complex production-grade skill implementations.

### Disclaimer
**These skills are provided for demonstration and educational purposes only.** While some capabilities may be available in live Claude, official implementations and behaviors may differ from the examples in this repository. All skills should be tested thoroughly in a target environment before being used for critical tasks.

## Repository Structure (Skill Sets)
The repository is organized into three core sets of resources:
- [./skills](./skills): Example skills for Creative & Design, Development & Technical, Enterprise & Communication, and Document Skills
- [./spec](./spec): The official Agent Skills specification
- [./template](./template): A pre-built template for creating custom skills

## Usage Instructions
Skills from this repository can be used across Claude Code, Claude.ai, and the Claude API.

### Claude Code
1. Register this repository as a Claude Code Plugin marketplace by running the following command in Claude Code:
```
/plugin marketplace add anthropics/skills
```
2. Install a specific skill set via the marketplace UI:
   1. Select `Browse and install plugins`
   2. Select `anthropic-agent-skills`
   3. Select `document-skills` or `example-skills`
   4. Select `Install now`

Alternatively, install skill sets directly via command:
```
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

After installation, skills can be invoked by mentioning them in a prompt. For example: "Use the PDF skill to extract the form fields from `path/to/some-file.pdf`"

### Claude.ai
All example skills in this repository are available by default to paid Claude.ai plans. To use repository skills or upload custom skills, follow the instructions in the [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude#h_a4222fa77b) support article.

### Claude API
Pre-built Anthropic skills and custom skills can be used via the Claude API. See the [Skills API Quickstart](https://docs.claude.com/en/api/skills-guide#creating-a-skill) for implementation details.

## Creating a Basic Custom Skill
Skills require only a folder containing a `SKILL.md` file with YAML frontmatter and instruction content. The official template-skill in this repository can be used as a starting point:
```markdown
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---

# My Skill Name

[Add your instructions here that Claude will follow when this skill is active]

## Examples
- Example usage 1
- Example usage 2

## Guidelines
- Guideline 1
- Guideline 2
```

The YAML frontmatter requires two mandatory fields:
- `name`: A unique lowercase identifier for the skill, using hyphens in place of spaces
- `description`: A complete explanation of the skill's function and appropriate use cases

The markdown body of the file contains the instructions, usage examples, and guidelines that Claude will follow when the skill is active. For more details, see the [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills) support article.

## Partner Skills
Skills are a standard way to teach Claude to integrate with third-party software. High-quality partner skills are featured in this section:
- **Notion**: [Notion Skills for Claude](https://www.notion.so/notiondevs/Notion-Skills-for-Claude-28da4445d27180c7af1df7d8615723d0)
