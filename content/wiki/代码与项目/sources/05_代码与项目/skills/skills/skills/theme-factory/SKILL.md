---
source: raw/05_代码与项目/skills/skills/skills/theme-factory/SKILL.md
raw_sha256: c35893e221e28895c52143cc11bf30e41a44817796b39d4b15727dadc9796552
compiled_at: 2026-04-14T05:10:47.948Z
---
# Theme Factory Skill
> 来源路径：`raw/05_代码与项目/skills/skills/skills/theme-factory/SKILL.md`

---

## TL;DR
Theme Factory 是一个为各类产出物（演示文稿、文档、报告、落地页等）应用主题样式的工具集，内置10套预设专业主题，也支持动态生成自定义主题，可快速为产出物赋予统一协调的专业视觉风格。

---

## 要点
### 基本信息
- 名称：`theme-factory`
- 功能：为任意产出物应用预设/自定义主题样式，支持幻灯片、文档、报告、HTML落地页等多种类型产出物
- 许可证：完整条款见 `LICENSE.txt`
- 预设主题数量：共10套

### 核心用途
为演示幻灯片等各类产出物应用一致、专业的样式，每个主题包含：
- 带十六进制色值的协调调色板
- 适合标题和正文的互补字体组合
- 适配不同场景和受众的独特视觉风格

### 使用流程（应用预设主题）
1. 展示 `theme-showcase.pdf` 供用户直观查看所有可用主题（不得修改该文件，仅用于展示）
2. 询问用户需要应用的主题
3. 获取用户对所选主题的明确确认
4. 将选中主题的配色和字体应用到目标产出物

### 可用预设主题列表
1. **Ocean Depths** - 专业沉稳的海事风格主题
2. **Sunset Boulevard** - 温暖明亮的日落配色主题
3. **Forest Canopy** - 自然沉稳的大地色调主题
4. **Modern Minimalist** - 干净现代的灰度主题
5. **Golden Hour** - 浓郁温暖的秋日调色板主题
6. **Arctic Frost** - 清爽干净的冬季灵感主题
7. **Desert Rose** - 柔和精致的灰调主题
8. **Tech Innovation** - 大胆现代的科技美学主题
9. **Botanical Garden** - 清新自然的园林配色主题
10. **Midnight Galaxy** - 富有戏剧感的宇宙深色调主题

### 主题结构
所有预设主题的完整定义存放在 `themes/` 目录，每个主题包含完整的配色、字体和视觉规范。

### 自定义主题生成流程
如果现有主题不符合需求，可以生成自定义主题：
1. 根据用户提供的需求描述选择适配的配色和字体
2. 为新主题赋予符合其字体/配色风格的名称
3. 生成后展示给用户审核确认
4. 确认后按上述流程应用到目标产出物

---

## 引用证据片段（原始资料完整保留）
```raw
---
name: theme-factory
description: Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly.
license: Complete terms in LICENSE.txt
---


# Theme Factory Skill

This skill provides a curated collection of professional font and color themes themes, each with carefully selected color palettes and font pairings. Once a theme is chosen, it can be applied to any artifact.

## Purpose

To apply consistent, professional styling to presentation slide decks, use this skill. Each theme includes:
- A cohesive color palette with hex codes
- Complementary font pairings for headers and body text
- A distinct visual identity suitable for different contexts and audiences

## Usage Instructions

To apply styling to a slide deck or other artifact:

1. **Show the theme showcase**: Display the `theme-showcase.pdf` file to allow users to see all available themes visually. Do not make any modifications to it; simply show the file for viewing.
2. **Ask for their choice**: Ask which theme to apply to the deck
3. **Wait for selection**: Get explicit confirmation about the chosen theme
4. **Apply the theme**: Once a theme has been chosen, apply the selected theme's colors and fonts to the deck/artifact

## Themes Available

The following 10 themes are available, each showcased in `theme-showcase.pdf`:

1. **Ocean Depths** - Professional and calming maritime theme
2. **Sunset Boulevard** - Warm and vibrant sunset colors
3. **Forest Canopy** - Natural and grounded earth tones
4. **Modern Minimalist** - Clean and contemporary grayscale
5. **Golden Hour** - Rich and warm autumnal palette
6. **Arctic Frost** - Cool and crisp winter-inspired theme
7. **Desert Rose** - Soft and sophisticated dusty tones
8. **Tech Innovation** - Bold and modern tech aesthetic
9. **Botanical Garden** - Fresh and organic garden colors
10. **Midnight Galaxy** - Dramatic and cosmic deep tones

## Theme Details

Each theme is defined in the `themes/` directory with complete specifications including:
- Cohesive color palette with hex codes
- Complementary font pairings for headers and body text
- Distinct visual identity suitable for different contexts and audiences

## Application Process

After a preferred theme is selected:
1. Read the corresponding theme file from the `themes/` directory
2. Apply the specified colors and fonts consistently throughout the deck
3. Ensure proper contrast and readability
4. Maintain the theme's visual identity across all slides

## Create your Own Theme
To handle cases where none of the existing themes work for an artifact, create a custom theme. Based on provided inputs, generate a new theme similar to the ones above. Give the theme a similar name describing what the font/color combinations represent. Use any basic description provided to choose appropriate colors/fonts. After generating the theme, show it for review and verification. Following that, apply the theme as described above.
```

---

> [!WARNING] 本页无已知冲突，如有其他来源与本页内容矛盾，请在此处标注。
