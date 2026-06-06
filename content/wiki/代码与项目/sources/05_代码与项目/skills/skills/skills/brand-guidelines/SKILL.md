---
source: raw/05_代码与项目/skills/skills/skills/brand-guidelines/SKILL.md
raw_sha256: 1120b3769e2985cefb3d25be981b1f914abeba57ae079b83c20c666c164fa9fe
compiled_at: 2026-04-14T05:03:29.636Z
---
# Anthropic Brand Guidelines Skill
> 来源路径：`raw/05_代码与项目/skills/skills/skills/brand-guidelines/SKILL.md`

---

## TL;DR
`brand-guidelines` 是一个用于给各类工件应用 Anthropic 官方品牌风格的技能，会自动按照 Anthropic 官方规范配置品牌色和字体，可在任何需要符合 Anthropic 品牌设计规范的场景下使用。

---

## 基本信息
| 项目 | 内容 |
|------|------|
| 标识符 | `brand-guidelines` |
| 许可证 | 完整条款见 `LICENSE.txt` |
| 用途 | 对任何需要 Anthropic 视觉风格的工件应用 Anthropic 官方品牌色和排版，当需要符合品牌色/风格规范/视觉格式/公司设计标准时使用 |

---

## 要点
### 关键词
branding, corporate identity, visual identity, post-processing, styling, brand colors, typography, Anthropic brand, visual formatting, visual design

### 官方品牌规范
#### 品牌色
| 分类 | 颜色名称 | 色值 | 用途 |
|------|----------|------|------|
| 主色 | Dark | `#141413` | 主文本和深色背景 |
| 主色 | Light | `#faf9f5` | 浅色背景和深色背景上的文本 |
| 主色 | Mid Gray | `#b0aea5` | 二级元素 |
| 主色 | Light Gray | `#e8e6dc` | 柔和背景 |
| 强调色 | Orange | `#d97757` | 一级强调 |
| 强调色 | Blue | `#6a9bcc` | 二级强调 |
| 强调色 | Green | `#788c5d` | 三级强调 |

#### 排版规范
- 标题：Poppins（降级 fallback 为 Arial）
- 正文：Lora（降级 fallback 为 Georgia）
- 说明：为获得最佳效果，需要环境预先安装对应字体

### 核心功能
1. **智能字体应用**
   - 自动对 24pt 及更大的标题应用 Poppins 字体
   - 对正文自动应用 Lora 字体
   - 自定义字体不可用时自动降级到 Arial/Georgia
   - 保证全系统可读性
2. **文本样式处理**
   - 保留文本层级和原始格式
   - 根据背景自动选择匹配文本颜色
3. **图形配色**
   - 非文本图形使用强调色
   - 在橙、蓝、绿三色中循环使用，保持品牌一致性同时增加视觉层次

### 技术细节
- 字体管理：优先使用系统已安装的 Poppins 和 Lora，自动降级 fallback，无需强制安装字体即可使用，预安装对应字体可获得最佳效果
- 颜色实现：使用 RGB 色值保证品牌色精准，通过 `python-pptx` 的 `RGBColor` 类实现，跨系统保持颜色一致性

---

## 引用证据片段
```markdown
---
name: brand-guidelines
description: Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply.
license: Complete terms in LICENSE.txt
---

# Anthropic Brand Styling

## Overview

To access Anthropic's official brand identity and style resources, use this skill.

**Keywords**: branding, corporate identity, visual identity, post-processing, styling, brand colors, typography, Anthropic brand, visual formatting, visual design

## Brand Guidelines

### Colors

**Main Colors:**

- Dark: `#141413` - Primary text and dark backgrounds
- Light: `#faf9f5` - Light backgrounds and text on dark
- Mid Gray: `#b0aea5` - Secondary elements
- Light Gray: `#e8e6dc` - Subtle backgrounds

**Accent Colors:**

- Orange: `#d97757` - Primary accent
- Blue: `#6a9bcc` - Secondary accent
- Green: `#788c5d` - Tertiary accent

### Typography

- **Headings**: Poppins (with Arial fallback)
- **Body Text**: Lora (with Georgia fallback)
- **Note**: Fonts should be pre-installed in your environment for best results

## Features

### Smart Font Application

- Applies Poppins font to headings (24pt and larger)
- Applies Lora font to body text
- Automatically falls back to Arial/Georgia if custom fonts unavailable
- Preserves readability across all systems

### Text Styling

- Headings (24pt+): Poppins font
- Body text: Lora font
- Smart color selection based on background
- Preserves text hierarchy and formatting

### Shape and Accent Colors

- Non-text shapes use accent colors
- Cycles through orange, blue, and green accents
- Maintains visual interest while staying on-brand

## Technical Details

### Font Management

- Uses system-installed Poppins and Lora fonts when available
- Provides automatic fallback to Arial (headings) and Georgia (body)
- No font installation required - works with existing system fonts
- For best results, pre-install Poppins and Lora fonts in your environment

### Color Application

- Uses RGB color values for precise brand matching
- Applied via python-pptx's RGBColor class
- Maintains color fidelity across different systems
```

---

> [!WARNING] 冲突：
> 本页仅编译自上述单一原始来源，未与其他来源比对，若其他来源的 Anthropic 品牌规范与本页内容存在差异，请以官方最新发布的品牌指南为准。
