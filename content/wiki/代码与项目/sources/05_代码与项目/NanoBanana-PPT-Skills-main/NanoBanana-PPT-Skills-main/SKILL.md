---
source: raw/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/SKILL.md
raw_sha256: 7eed995592ffd0b19f8aaa75d8d5b280b5c112af94b5467772cdc14b9e24b722
compiled_at: 2026-04-14T04:08:36.367Z
---
# ppt-generator-pro
> 来源路径：`raw/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/SKILL.md`

---

## TL;DR
ppt-generator-pro 是一个用于 Claude Code 的 AI PPT 生成技能，可以基于输入文档自动生成带高清图片、可选 AI 转场视频的交互式 PPT，支持两种专业演示风格，依赖 Google Gemini Nano Banana Pro 生成图片，可灵 AI 生成转场视频。

---

## 元数据
| 项 | 值 |
|----|----|
| Skill 名称 | ppt-generator-pro |
| 版本 | 2.0.0 |
| 描述 | 基于 AI 自动生成高质量 PPT 图片和视频，支持智能转场和交互式播放 |
| 作者 | 歸藏 |
| 标签 | `ppt` `presentation` `video` `ai` `nano-banana` `kling-ai` `image-generation` |

---

## 功能特性

### 核心功能
- 🤖 智能文档分析：自动提取核心要点，规划 PPT 内容结构
- 🎨 多风格支持：内置渐变毛玻璃、矢量插画两种专业风格
- 🖼️ 高质量图片：使用 Nano Banana Pro 生成 16:9 高清 PPT
- 🎬 AI 转场视频：可灵 AI 生成流畅的页面过渡动画
- 🎮 交互式播放器：视频+图片混合播放，支持键盘导航
- 🎥 完整视频导出：FFmpeg 合成包含所有转场的完整 PPT 视频

### v2.0 新增功能
- 🔄 首页循环预览：自动生成吸引眼球的循环动画
- 🎞️ 智能转场：自动生成页面间的过渡视频
- 🔧 参数统一：自动统一所有视频分辨率和帧率

---

## 系统要求

### 必需环境变量
`GEMINI_API_KEY`：Google AI API 密钥（用于生成 PPT 图片）

### 可选环境变量（视频功能）
- `KLING_ACCESS_KEY`：可灵 AI Access Key
- `KLING_SECRET_KEY`：可灵 AI Secret Key

### Python 依赖
```bash
pip install google-genai pillow python-dotenv
```

### 视频功能依赖（FFmpeg）
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt-get install ffmpeg
```

---

## 使用方法
在 Claude Code 中直接调用：
```bash
/ppt-generator-pro
```
或直接自然语言说明需求：
```
我想基于以下文档生成一个 5 页的 PPT，使用渐变毛玻璃风格。

[文档内容...]
```

---

## 执行流程

### 阶段 1: 收集用户输入
1. **获取文档内容**：支持提供文档路径读取、直接粘贴文本，未提供内容时主动询问用户
2. **选择风格**：自动扫描 `styles/` 目录列出可用风格，供用户选择
3. **选择页数范围**：按演示时长提供预设选项：
   - 5 页（5 分钟演讲）
   - 5-10 页（10-15 分钟演讲）
   - 10-15 页（20-30 分钟演讲）
   - 20-25 页（45-60 分钟演讲）
4. **选择分辨率**：
   - 2K (2752x1536) - 推荐，快速生成
   - 4K (5504x3072) - 高质量，适合打印
5. **是否生成视频**：配置可灵 AI 密钥时询问用户选项，仅图片/图片+转场视频

### 阶段 2: 文档分析与内容规划
根据选择的页数范围，智能规划每页内容结构，生成 `slides_plan.json` 保存内容规划。

内容规划模板：
| 页数范围 | 结构规划 |
|----------|----------|
| 5 页 | 封面 → 要点1 → 要点2 → 要点3 → 总结 |
| 5-10 页 | 封面 → 引言/背景(2-3页) → 核心内容(4-7页) → 案例/数据(8-9页) → 总结 |
| 10-15 页 | 封面 → 引言/目录(2-3页) → 三章节内容(各3页) → 案例研究(10-12页) → 数据可视化(13-14页) → 总结 |
| 20-25 页 | 封面 → 目录 → 引言背景(3-4页) → 三个部分内容(各4页) → 案例研究(17-19页) → 数据分析洞察(20-22页) → 关键发现建议(23-24页) → 总结致谢(25页) |

### 阶段 3: 生成 PPT 图片
切换到对应工作目录后执行生成命令：
```bash
# 通用方式
python generate_ppt.py \
  --plan slides_plan.json \
  --style styles/gradient-glass.md \
  --resolution 2K

# 推荐使用 uv
uv run python generate_ppt.py \
  --plan slides_plan.json \
  --style styles/gradient-glass.md \
  --resolution 2K
```

参数说明：
- `--plan`: slides 规划 JSON 文件路径
- `--style`: 风格文件路径
- `--resolution`: 分辨率（2K 或 4K）
- `--template`: HTML 模板路径（可选）

### 阶段 4: 生成转场提示词（视频模式）
分析所有生成的 PPT 图片，为首页循环和每段转场生成定制提示词，保存到 `outputs/TIMESTAMP/transition_prompts.json`。

优势：针对实际图片定制提示词，会考虑文字稳定性避免模糊，符合选定风格的视觉语言。

### 阶段 5: 生成转场视频（可选）
基于提示词生成转场视频：
```bash
python generate_ppt_video.py \
  --slides-dir outputs/20260112_143022/images \
  --output-dir outputs/20260112_143022_video \
  --prompts-file outputs/20260112_143022/transition_prompts.json
```

生成产物：
- 首页循环预览视频 `preview.mp4`
- 页面间转场视频 `transition_01_to_02.mp4`...
- 交互式视频播放器 `video_index.html`
- 完整合成视频 `full_ppt_video.mp4`

### 阶段 6: 返回结果
生成完成后会输出产物目录和使用说明，提供快捷键指南。

---

## 环境变量配置
### .env 文件查找顺序
1. 脚本所在目录 `./ppt-generator/.env`
2. 向上查找直到找到包含 `.git` 或 `.env` 的项目根目录
3. Claude Skill 标准位置 `~/.claude/skills/ppt-generator/.env`
4. 系统环境变量

### .env 示例
```bash
# Google AI API 密钥（必需）
GEMINI_API_KEY=your_gemini_api_key_here

# 可灵 AI API 密钥（可选，用于视频功能）
KLING_ACCESS_KEY=your_kling_access_key_here
KLING_SECRET_KEY=your_kling_secret_key_here
```

---

## 错误处理
| 常见错误 | 解决方案 |
|----------|----------|
| 未设置 GEMINI_API_KEY | 创建 `.env` 文件并添加 `GEMINI_API_KEY=你的密钥` |
| ModuleNotFoundError | 执行 `pip install google-genai pillow python-dotenv` |
| FFmpeg 不可用 | 按系统包管理器安装 ffmpeg：macOS `brew install ffmpeg`，Ubuntu `sudo apt-get install ffmpeg` |
| API 调用超时/失败 | 检查网络，确认 API 密钥有效，稍后重试 |
| 视频生成失败提示可灵密钥未配置 | 仅需要图片则跳过视频，需要视频则配置 `KLING_ACCESS_KEY` 和 `KLING_SECRET_KEY` |

---

## 风格系统
### 内置风格
| 风格 | 文件 | 视觉特点 | 适用场景 |
|------|------|----------|----------|
| 渐变毛玻璃卡片风格 | `gradient-glass.md` | Apple Keynote 极简主义、玻璃拟态效果、霓虹渐变、3D玻璃物体+电影级
