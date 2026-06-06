---
source: raw/05_代码与项目/skills/skills/skills/web-artifacts-builder/SKILL.md
raw_sha256: 81c5002c6643b0de7b8710b00e7a9038daa6fb9b68d59870ee6adb12da8d10f8
compiled_at: 2026-04-14T05:17:10.968Z
---
# web-artifacts-builder

> 本页编译自 `raw/05_代码与项目/skills/skills/skills/web-artifacts-builder/SKILL.md`，原始内容未修改

---

## TL;DR
web-artifacts-builder 是一套用于为 claude.ai 构建、打包多组件复杂 HTML 产物的工具集，基于 React + Tailwind CSS + shadcn/ui 技术栈，最终输出可直接在 Claude 对话中分享的单文件自包含 HTML，不适合简单单文件 HTML/JSX 产物场景。

---

## 基本信息
| 项目 | 说明 |
| --- | --- |
| 名称 | `web-artifacts-builder` |
| 协议 | 完整条款见 `LICENSE.txt` |

---

## 核心要点
1. **适用场景**：需要状态管理、路由或 shadcn/ui 组件的复杂产物，**不适合**简单单文件 HTML/JSX 产物
2. **技术栈**：React 18 + TypeScript + Vite + Parcel（打包） + Tailwind CSS + shadcn/ui
3. **工作流**：初始化项目 → 开发 → 打包为单 HTML → 分享给用户 → （可选）测试
4. **设计规范**：避免过度居中布局、紫色渐变、统一圆角、Inter 字体，防止产生所谓的"AI 垃圾"效果
5. **产物特点**：打包后得到自包含单文件 `bundle.html`，所有 JS、CSS、依赖都已内联，可直接在 Claude 对话中作为产物分享

---

## 流程说明
### 1. 初始化项目
运行初始化脚本创建新的 React 项目：
```bash
bash scripts/init-artifact.sh <project-name>
cd <project-name>
```
初始化完成后自动包含：
- React + TypeScript（基于 Vite）
- Tailwind CSS 3.4.1 + shadcn/ui 主题系统
- 路径别名 `@/` 已配置
- 40+ 预安装的 shadcn/ui 组件
- 所有 Radix UI 依赖
- Parcel 打包配置（`.parcelrc`）
- Node 18+ 兼容（自动检测并固定 Vite 版本）

### 2. 开发产物
编辑生成的代码文件，可参考下文「常见开发任务」（原始资料未提供具体内容）。

### 3. 打包为单 HTML 文件
打包命令：
```bash
bash scripts/bundle-artifact.sh
```
输出为项目根目录的 `bundle.html`，要求项目根目录本身存在入口 `index.html`。

打包脚本会自动完成：
1. 安装打包依赖（parcel、@parcel/config-default、parcel-resolver-tspaths、html-inline）
2. 创建支持路径别名的 `.parcelrc` 配置
3. 使用 Parcel 构建（不生成 source map）
4. 使用 html-inline 将所有资源内联到单个 HTML 文件中

### 4. 分享给用户
将打包得到的 `bundle.html` 分享到 Claude 对话中，供用户作为产物查看。

### 5. （可选）测试产物
仅在必要或用户要求时执行，一般建议先分享产物，避免增加延迟；如果后续出现问题或用户要求再测试。可使用 Playwright、Puppeteer 或其他可用技能工具测试。

---

## 设计风格规范
> [!IMPORTANT]
> 非常重要：为了避免通常所说的"AI slop（AI垃圾）"，请避免使用过度居中布局、紫色渐变、统一圆角和 Inter 字体。

---

## 参考链接
- **shadcn/ui 组件文档**：https://ui.shadcn.com/docs/components

---

## 引用原始证据片段
<details>
<summary>点击展开原始完整内容</summary>

```markdown
---
name: web-artifacts-builder
description: Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.
license: Complete terms in LICENSE.txt
---

# Web Artifacts Builder

To build powerful frontend claude.ai artifacts, follow these steps:
1. Initialize the frontend repo using `scripts/init-artifact.sh`
2. Develop your artifact by editing the generated code
3. Bundle all code into a single HTML file using `scripts/bundle-artifact.sh`
4. Display artifact to user
5. (Optional) Test the artifact

**Stack**: React 18 + TypeScript + Vite + Parcel (bundling) + Tailwind CSS + shadcn/ui

## Design & Style Guidelines

VERY IMPORTANT: To avoid what is often referred to as "AI slop", avoid using excessive centered layouts, purple gradients, uniform rounded corners, and Inter font.

## Quick Start

### Step 1: Initialize Project

Run the initialization script to create a new React project:
```bash
bash scripts/init-artifact.sh <project-name>
cd <project-name>
```

This creates a fully configured project with:
- ✅ React + TypeScript (via Vite)
- ✅ Tailwind CSS 3.4.1 with shadcn/ui theming system
- ✅ Path aliases (`@/`) configured
- ✅ 40+ shadcn/ui components pre-installed
- ✅ All Radix UI dependencies included
- ✅ Parcel configured for bundling (via .parcelrc)
- ✅ Node 18+ compatibility (auto-detects and pins Vite version)

### Step 2: Develop Your Artifact

To build the artifact, edit the generated files. See **Common Development Tasks** below for guidance.

### Step 3: Bundle to Single HTML File

To bundle the React app into a single HTML artifact:
```bash
bash scripts/bundle-artifact.sh
```

This creates `bundle.html` - a self-contained artifact with all JavaScript, CSS, and dependencies inlined. This file can be directly shared in Claude conversations as an artifact.

**Requirements**: Your project must have an `index.html` in the root directory.

**What the script does**:
- Installs bundling dependencies (parcel, @parcel/config-default, parcel-resolver-tspaths, html-inline)
- Creates `.parcelrc` config with path alias support
- Builds with Parcel (no source maps)
- Inlines all assets into single HTML using html-inline

### Step 4: Share Artifact with User

Finally, share the bundled HTML file in conversation with the user so they can view it as an artifact.

### Step 5: Testing/Visualizing the Artifact (Optional)

Note: This is a completely optional step. Only perform if necessary or requested.

To test/visualize the artifact, use available tools (including other Skills or built-in tools like Playwright or Puppeteer). In general, avoid testing the artifact upfront as it adds latency between the request and when the finished artifact can be seen. Test later, after presenting the artifact, if requested or if issues arise.

## Reference

- **shadcn/ui components**: https://ui.shadcn.com/docs/components
```
</details>
