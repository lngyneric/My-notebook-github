---
source: raw/05_代码与项目/skills/skills/skills/skill-creator/references/output-patterns.md
raw_sha256: d6027800b9d8c26589edba85b42901a41ac36d753b4e9cebc7f4cbb03cdcf0a4
compiled_at: 2026-04-14T05:19:21.760Z
---
# 输出模式（Output Patterns）

> [!NOTE] TL;DR
> 本规范定义了Skill Creator中技能生成一致高质量输出的两种常用模式：模板模式（根据严格程度提供不同形式的输出模板）和示例模式（通过输入输出对明确期望的输出风格与格式）。

## 要点
1. 本规范用于统一技能输出格式，保障输出一致性与质量
2. **模板模式**：根据需求严格程度提供两种模板形式：
   - 严格要求场景（如API响应、数据格式）：要求使用完全固定的精确模板结构
   - 灵活引导场景：提供默认结构，允许根据实际情况调整适配
3. **示例模式**：对于输出质量依赖风格/细节感知的场景，提供输入输出示例对，比纯文字描述更能让模型理解预期输出

---

## 引用证据片段
> 原始来源：`raw/05_代码与项目/skills/skills/skills/skill-creator/references/output-patterns.md`

### 1. 模板模式（Template Pattern）
> 为输出格式提供模板，根据需求匹配严格程度：
> 
> **严格要求场景示例**（如API响应、数据格式）：
> ```markdown
> ## Report structure
> 
> ALWAYS use this exact template structure:
> 
> # [Analysis Title]
> 
> ## Executive summary
> [One-paragraph overview of key findings]
> 
> ## Key findings
> - Finding 1 with supporting data
> - Finding 2 with supporting data
> - Finding 3 with supporting data
> 
> ## Recommendations
> 1. Specific actionable recommendation
> 2. Specific actionable recommendation
> ```
> 
> **灵活引导场景示例**（允许适配调整）：
> ```markdown
> ## Report structure
> 
> Here is a sensible default format, but use your best judgment:
> 
> # [Analysis Title]
> 
> ## Executive summary
> [Overview]
> 
> ## Key findings
> [Adapt sections based on what you discover]
> 
> ## Recommendations
> [Tailor to the specific context]
> 
> Adjust sections as needed for the specific analysis type.
> ```

### 2. 示例模式（Examples Pattern）
> 适用于输出质量依赖风格感知的场景，通过输入输出对明确要求：
> ```markdown
> ## Commit message format
> 
> Generate commit messages following these examples:
> 
> **Example 1:**
> Input: Added user authentication with JWT tokens
> Output:
> ```
> feat(auth): implement JWT-based authentication
> 
> Add login endpoint and token validation middleware
> ```
> 
> **Example 2:**
> Input: Fixed bug where dates displayed incorrectly in reports
> Output:
> ```
> fix(reports): correct date formatting in timezone conversion
> 
> Use UTC timestamps consistently across report generation
> ```
> 
> Follow this style: type(scope): brief description, then detailed explanation.
> ```
> 
> 原文结论：示例比纯描述更能帮助Claude清晰理解期望的风格和细节粒度。

> [!WARNING] 冲突：
> 当前来源无已知与其他来源的矛盾冲突。
