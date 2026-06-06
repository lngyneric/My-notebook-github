---
source: raw/05_代码与项目/skills/skills/skills/internal-comms/SKILL.md
raw_sha256: 067b7587a344a928fc6534ef66b1bcd591fc7c26d207ea7ca3334aeb678d6475
compiled_at: 2026-04-14T05:06:52.113Z
---
# internal-comms 技能说明

> [!NOTE] 来源路径
> `raw/05_代码与项目/skills/skills/skills/internal-comms/SKILL.md`

---

## TL;DR
本技能是一套用于撰写符合公司要求格式的各类内部沟通材料的工具集合，Claude 在收到撰写内部沟通内容（包括状态报告、领导更新、3P更新、公司通讯等）请求时应调用本技能。

---

## 要点
1. 适用范围：本技能用于撰写多种类型的内部沟通内容，具体包含：
   - 3P更新（Progress 进度、Plans 计划、Problems 问题）
   - 公司通讯
   - FAQ（常见问题）回复
   - 状态报告
   - 领导层更新
   - 项目更新
   - 事件报告
2. 使用流程：
   1. 从用户请求中识别沟通内容类型
   2. 从 `examples/` 目录加载对应匹配的规范文件：
      - `examples/3p-updates.md`：3P团队更新
      - `examples/company-newsletter.md`：全公司范围内的通讯
      - `examples/faq-answers.md`：常见问题回答
      - `examples/general-comms.md`：上述分类不匹配的其他内部沟通内容
   3. 遵循对应文件中关于格式、语气、内容收集的具体要求撰写
3. 如果沟通类型无法匹配现有规范，需要请求用户澄清格式相关的更多上下文信息
4. 触发关键词：3P updates, company newsletter, company comms, weekly update, faqs, common questions, updates, internal comms
5. 完整许可条款见 `LICENSE.txt`

---

## 引用证据片段
```markdown
---
name: internal-comms
description: A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.).
license: Complete terms in LICENSE.txt
---

## When to use this skill
To write internal communications, use this skill for:
- 3P updates (Progress, Plans, Problems)
- Company newsletters
- FAQ responses
- Status reports
- Leadership updates
- Project updates
- Incident reports

## How to use this skill

To write any internal communication:

1. **Identify the communication type** from the request
2. **Load the appropriate guideline file** from the `examples/` directory:
    - `examples/3p-updates.md` - For Progress/Plans/Problems team updates
    - `examples/company-newsletter.md` - For company-wide newsletters
    - `examples/faq-answers.md` - For answering frequently asked questions
    - `examples/general-comms.md` - For anything else that doesn't explicitly match one of the above
3. **Follow the specific instructions** in that file for formatting, tone, and content gathering

If the communication type doesn't match any existing guideline, ask for clarification or more context about the desired format.

## Keywords
3P updates, company newsletter, company comms, weekly update, faqs, common questions, updates, internal comms
```

> [!WARNING] 冲突标注：
> 当前无其他来源内容，未发现冲突。
