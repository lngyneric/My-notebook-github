---
source: raw/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/SKILL.md
raw_sha256: 7eed995592ffd0b19f8aaa75d8d5b280b5c112af94b5467772cdc14b9e24b722
compiled_at: 2026-04-24T08:36:43.611Z
---
<wiki>
# PPT Generator Pro - Claude Code Skill
## 摘要
本技能是由歸藏开发的AI驱动PPT生成工具（当前版本2.0.0），可基于输入文档自动规划内容结构、生成多风格高清PPT图片，还支持通过可灵AI生成智能转场视频、交互式播放与完整视频导出，适用于商务演示、教育培训、产品发布等多场景。

## 元数据
| 项 | 内容 |
| --- | --- |
| Skill 名称 | ppt-generator-pro |
| 版本 | 2.0.0 |
| 描述 | 基于 AI 自动生成高质量 PPT 图片和视频，支持智能转场和交互式播放 |
| 作者 | 歸藏 |
| 标签 | ppt, presentation, video, ai, nano-banana, kling-ai, image-generation |

## 功能特性
### 核心功能
- 🤖 **智能文档分析** - 自动提取核心要点，规划 PPT 内容结构
- 🎨 **多风格支持** - 内置渐变毛玻璃、矢量插画两种专业风格
- 🖼️ **高质量图片** - 使用 Nano Banana Pro 生成 16:9 高清 PPT
- 🎬 **AI 转场视频** - 可灵 AI 生成流畅的页面过渡动画
- 🎮 **交互式播放器** - 视频+图片混合播放，支持键盘导航
- 🎥 **完整视频导出** - FFmpeg 合成包含所有转场的完整 PPT 视频

### v2.0 新增功能
- 🔄 **首页循环预览** - 自动生成吸引眼球的循环动画
- 🎞️ **智能转场** - 自动生成页面间的过渡视频
- 🔧 **参数统一** - 自动统一所有视频分辨率和帧率

## 系统要求
### 环境变量
**必需：**
- `GEMINI_API_KEY`: Google AI API 密钥（用于生成 PPT 图片）

**可选（用于视频功能）：**
- `KLING_ACCESS_KEY`: 可灵 AI Access Key
- `KLING_SECRET_KEY`: 可灵 AI Secret Key

### Python 依赖
```bash
pip install google-genai pillow python-dotenv
```

### 视频功能依赖
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt-get install ffmpeg
```

## 使用方法
### 在 Claude Code 中调用
直接执行命令：
```bash
/ppt-generator-pro
```
或通过自然语言指令触发：
```
我想基于以下文档生成一个 5 页的 PPT，使用渐变毛玻璃风格。

[文档内容...]
```

## 执行流程
### 阶段 1: 收集用户输入
#### 1.1 获取文档内容
支持三种输入方式：
- **选项 A: 文档路径**：用户提供文档路径时，使用Read工具读取文件内容
- **选项 B: 直接文本**：用户直接粘贴文档内容或核心要点
- **选项 C: 主动询问**：用户未提供内容时，主动询问用户提供文档路径或文本内容

#### 1.2 选择风格
自动扫描`styles/`目录下的可用风格，若存在多个风格则通过询问用户选择：
```
问题: 请选择 PPT 风格
选项:
- 渐变毛玻璃卡片风格（科技感、商务演示）
- 矢量插画风格（温暖、教育培训）
```

#### 1.3 选择页数范围
根据演讲时长匹配页数，询问用户选择：
```
问题: 希望生成多少页 PPT？
选项:
- 5 页（5 分钟演讲）
- 5-10 页（10-15 分钟演讲）
- 10-15 页（20-30 分钟演讲）
- 20-25 页（45-60 分钟演讲）
```

#### 1.4 选择分辨率
```
问题: 选择图片分辨率
选项:
- 2K (2752x1536) - 推荐，快速生成
- 4K (5504x3072) - 高质量，适合打印
```

#### 1.5 选择是否生成视频（可选）
仅当配置可灵AI密钥时触发询问：
```
问题: 是否生成转场视频？
选项:
- 仅图片（快速）
- 图片 + 转场视频（完整体验）
```

### 阶段 2: 文档分析与内容规划
#### 2.1 内容规划策略
根据用户选择的页数范围智能规划页面结构：
- **5 页版本**：封面 → 核心观点×3 → 总结
- **5-10 页版本**：封面 → 引言/背景×2 → 核心内容×3-4 → 案例/数据×2 → 总结
- **10-15 页版本**：封面 → 引言/目录×2 → 第一章节×3 → 第二章节×3 → 案例研究×3 → 数据可视化×2 → 总结
- **20-25 页版本**：封面 → 目录 → 引言背景×2 → 三个核心部分各4页 → 案例研究×3 → 数据分析×3 → 发现建议×2 → 总结致谢

#### 2.2 生成 slides_plan.json
生成包含页面规划的JSON文件，示例如下：
```json
{
  "title": "文档标题",
  "total_slides": 5,
  "slides": [
    {
      "slide_number": 1,
      "page_type": "cover",
      "content": "标题：AI 产品设计指南\n副标题：构建以用户为中心的智能体验"
    },
    {
      "slide_number": 2,
      "page_type": "content",
      "content": "核心原则\n- 简单直观\n- 快速响应\n- 透明可控"
    }
  ]
}
```
文件保存路径：
- 独立使用：`./slides_plan.json`
- Skill 模式：`.claude/skills/ppt-generator/slides_plan.json`

### 阶段 3: 生成 PPT 图片
#### 3.1 确定工作目录
- 独立模式：进入PPT生成工具所在目录
- Skill 模式：进入`~/.claude/skills/ppt-generator`目录

#### 3.2 执行生成命令
```bash
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

#### 3.3 监控生成进度
脚本会实时输出生成进度、单页耗时与输出目录，所有图片生成完成后进入下一阶段。

### 阶段 4: 生成转场提示词（视频模式专属）
自动读取已生成的PPT图片，分析相邻页面的布局、元素、色彩差异，生成首页循环预览提示词与页面转场提示词，保存为`transition_prompts.json`，无需额外Claude API密钥，提示词针对实际图片定制，保障文字清晰度。

### 阶段 5: 生成转场视频（可选）
用户选择生成视频时，执行以下命令生成相关内容：
```bash
python generate_ppt_video.py \
  --slides-dir outputs/[TIMESTAMP]/images \
  --output-dir outputs/[TIMESTAMP]_video \
  --prompts-file outputs/[TIMESTAMP]/transition_prompts.json
```
生成内容包含：首页循环预览视频、页面转场视频、交互式视频播放器、完整合成视频。

### 阶段 6: 返回结果
#### 仅图片模式
返回图片目录、HTML播放器路径与快捷键说明，支持通过键盘方向键、空格等控制播放。

#### 视频模式
返回视频目录、转场视频路径、交互式播放器路径、完整视频路径与播放逻辑、快捷键说明，支持转场动画自动播放与键盘导航。

## 环境变量配置
### .env 文件查找顺序
1. 脚本所在目录
2. 向上查找至项目根目录（包含`.git`或`.env`的目录）
3. Claude Skill 标准位置：`~/.claude/skills/ppt-generator/.env`
4. 系统环境变量

### .env 文件示例
```bash
# Google AI API 密钥（必需）
GEMINI_API_KEY=your_gemini_api_key_here

# 可灵 AI API 密钥（可选，用于视频功能）
KLING_ACCESS
