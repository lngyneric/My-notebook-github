---
source: raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/AGENTS.md
raw_sha256: 47bd2a7fc39e246d6277e6dd47661264a2594a9acb9611eed4a73510f97048bb
compiled_at: 2026-04-14T04:05:43.639Z
---
# Agentic Design Patterns 仓库贡献指南

> [!TIP]
> TL;DR
> 本页面是 *agentic-design-patterns* 仓库的内容组织、开发、格式、提交等规范，要求所有内容以编号化 Markdown 文件放在仓库根目录，遵循双语排版规则，提交前需检查格式与链接，按约定编写提交信息与 PR 说明。

## 要点
### 项目结构与模块组织
- 所有内容放在仓库根目录，以 `NN-标题.md` 的编号格式命名，例如 `00-Table-of-Contents.md`
- 遵循 `rules.md` 要求维护双语排版，保留原有的章节编号与顺序
- 未经过讨论不得新增文件夹，图片优先使用外部直链，确需本地存储可在 PR 中提议新增 `images/` 文件夹

### 构建、测试与开发命令
- 快速预览可直接使用编辑器自带的 Markdown 预览功能（如 VS Code）
- 可选链接检查：对修改过的文件执行 `npx markdown-link-check <文件名> -q`
- 可选格式检查：执行 `npx markdownlint-cli2 .` 检查标题、列表、间距问题
- 如果需要本地查看嵌入图片效果，可执行 `python3 -m http.server` 启动本地服务，访问 `http://localhost:8000/` 查看

### 编码风格与命名约定
- 翻译规则以 `rules.md` 为唯一权威来源
- 文件名统一格式为 `NN-Title.md`，例如 `06-What-Makes-Agent.md`
- 双语格式默认遵循「英文段落 + 对应中文译文」顺序，短章节可分独立英文区/中文区
- 中文内容使用 `<mark>…</mark>` 标记，中文与英文、中文与数字之间需要添加空格
- 使用 GitHub 风格 Markdown，列表使用 2 空格缩进，避免不必要的加粗

### 测试规范
- 提交前需要确认：无断链、术语一致、中英段落对应、Markdown 渲染正常
- 使用工具检查时，修改后的文件需要通过 `markdownlint` 和 `markdown-link-check` 零错误检测
- 保持 diff 聚焦，不对未修改的英文原文做重排版

### 提交与 PR 规范
- 提交信息使用英文，遵循以下格式约定：
  - 新增翻译：`Add: [章节] translation`
  - 更新格式：`Update: [章节] formatting`
  - 修复问题：`Fix: [问题] in [章节]`
- PR 需要包含：清晰的范围与目的、修改文件列表、格式决策说明、关联议题，复杂格式修改建议附上截图

### Agent 专属规则
- 仅修改目标章节，不得修改文件编号
- 保留原始英文内容，不得改写原文，严格按照 `rules.md` 要求添加译文与格式
- 贡献保持最小可回退，未经过提前讨论不得新增工具或配置文件

## 引用原始证据片段
```raw
# Repository Guidelines

## Project Structure & Module Organization
- All content lives at the repository root as numbered Markdown files (e.g., `00-Table-of-Contents.md`, `03-Foreword.md`, `07-Chapter-01.md`).
- Keep bilingual layout per `rules.md` and preserve chapter numbering and order.
- Do not introduce new folders unless discussed; keep images inline links to external sources or propose an `images/` folder in the PR if needed.

## Build, Test, and Development Commands
- Preview Markdown: use your editor’s preview (e.g., VS Code) for quick checks.
- Optional link check: `npx markdown-link-check README.md -q` (run per edited file).
- Optional lint: `npx markdownlint-cli2 .` to catch headings, lists, and spacing issues.
- Quick local server (if embedding images): `python3 -m http.server` and open `http://localhost:8000/`.

## Coding Style & Naming Conventions
- Follow `rules.md` as the single source of truth for translation rules.
- File names: `NN-Title.md` (e.g., `06-What-Makes-Agent.md`, `21-Chapter-15.md`).
- Bilingual format: English paragraph followed by its Chinese translation; short chapters may use separate English/Chinese sections.
- Highlight Chinese with `<mark>…</mark>`; add spaces between Chinese/English and between Chinese/numbers.
- Markdown: GitHub‑flavored Markdown; lists use 2‑space indentation; avoid unnecessary bolding.

## Testing Guidelines
- Before submitting, ensure: no broken links, consistent terminology, matching English/Chinese paragraph pairs, and valid Markdown rendering.
- If using tools: run `markdownlint` and `markdown-link-check` with zero errors for changed files.
- Keep diffs focused—avoid reflowing untouched English source text.

## Commit & Pull Request Guidelines
- Commit messages (English):
  - `Add: [chapter] translation`
  - `Update: [chapter] formatting`
  - `Fix: [issue] in [chapter]`
- Pull Requests must include: clear scope/intent, list of touched files, notes on format decisions, and linked issues. Screenshots are helpful for complex formatting.

## Agent-Specific Instructions
- Only modify targeted chapters; do not renumber files.
- Preserve original English; do not paraphrase. Apply translations and formatting per `rules.md`.
- Keep contributions minimal and reversible; avoid adding tooling/config files without prior discussion.
```

> [!WARNING]
> 冲突：无已知冲突，本内容完全匹配原始资料。

---
来源路径：`raw/05_代码与项目/agentic-design-patterns/agentic-design-patterns/AGENTS.md`
