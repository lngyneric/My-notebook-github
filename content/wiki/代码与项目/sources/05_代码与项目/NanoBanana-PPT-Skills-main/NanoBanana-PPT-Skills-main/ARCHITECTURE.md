---
source: raw/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/ARCHITECTURE.md
raw_sha256: 84810ed480074cfe603b86343791503973e8c16e51da37fdceccc52d9894b562
compiled_at: 2026-04-14T04:07:04.353Z
---
# PPT Generator Pro 架构文档
> 来源路径：`raw/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/ARCHITECTURE.md`

---

## TL;DR
PPT Generator Pro 是基于 Google Nano Banana Pro(Gemini) 和可灵 AI 实现的AI PPT生成工具，支持生成纯图片版在线PPT、带AI转场的交互式视频PPT、可直接分享的完整合成视频，整体采用模块化设计，分为核心生成、视频合成、播放器输出三层架构，依赖外部AI API完成生成能力。

---

## 系统架构图
```mermaid
graph TB
    %% 用户输入
    User[👤 用户] -->|文档内容| Input[📝 输入处理]
    
    %% 输入处理
    Input --> Plan[📋 内容规划<br/>slides_plan.json]
    
    %% 核心模块
    Plan --> PPTGen[🎨 PPT 图片生成模块<br/>generate_ppt.py]
    Plan --> VideoGen[🎬 视频生成模块<br/>generate_ppt_video.py]
    
    %% PPT 图片生成流程
    PPTGen --> StyleLoader[🎨 风格加载器<br/>styles/*.md]
    StyleLoader --> PromptEngine[✍️ 提示词引擎]
    PromptEngine --> NanoBanana[🤖 Nano Banana Pro API<br/>Google Gemini]
    NanoBanana --> Images[🖼️ PPT 图片<br/>slide-01.png ~ slide-N.png]
    
    %% 视频生成流程
    VideoGen --> TransPrompt[📝 转场提示词生成器<br/>transition_prompt_generator.py]
    TransPrompt --> KlingAPI[🎬 可灵 AI API<br/>kling_api.py]
    KlingAPI --> PreviewVideo[🔄 预览视频<br/>preview.mp4]
    KlingAPI --> TransVideos[🎞️ 转场视频<br/>transition_01_to_02.mp4]
    
    %% 视频合成
    Images --> VideoMat[📦 视频素材管理<br/>video_materials.py]
    PreviewVideo --> VideoMat
    TransVideos --> VideoMat
    
    VideoMat --> Composer[🎬 FFmpeg 视频合成器<br/>video_composer.py]
    Composer --> FullVideo[🎥 完整视频<br/>full_ppt_video.mp4]
    
    %% 播放器生成
    Images --> ImgPlayer[🎮 图片播放器<br/>templates/viewer.html]
    VideoMat --> VidPlayer[🎮 视频播放器<br/>templates/video_viewer.html]
    
    %% 输出
    ImgPlayer --> Output1[📤 输出 1: 图片版<br/>index.html + images/]
    VidPlayer --> Output2[📤 输出 2: 视频版<br/>video_index.html + videos/]
    FullVideo --> Output3[📤 输出 3: 完整视频<br/>full_ppt_video.mp4]
    
    Output1 --> User
    Output2 --> User
    Output3 --> User
    
    %% 样式定义
    classDef userNode fill:#e1f5ff,stroke:#0288d1,stroke-width:2px
    classDef inputNode fill:#fff9c4,stroke:#f9a825,stroke-width:2px
    classDef coreNode fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    classDef apiNode fill:#ffebee,stroke:#c62828,stroke-width:2px
    classDef outputNode fill:#e8f5e9,stroke:#388e3c,stroke-width:2px
    
    class User userNode
    class Input,Plan inputNode
    class PPTGen,VideoGen,StyleLoader,PromptEngine,TransPrompt,VideoMat,Composer coreNode
    class NanoBanana,KlingAPI apiNode
    class Images,PreviewVideo,TransVideos,FullVideo,ImgPlayer,VidPlayer,Output1,Output2,Output3 outputNode
```

---

## 模块架构

### 1️⃣ 核心生成模块
```
┌─────────────────────────────────────────────────────────────┐
│                    PPT Generator Pro                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌────────────────────┐        ┌──────────────────────┐    │
│  │  图片生成模块      │        │   视频生成模块       │    │
│  │  generate_ppt.py   │        │ generate_ppt_video.py│    │
│  └────────────────────┘        └──────────────────────┘    │
│           │                              │                  │
│           ▼                              ▼                  │
│  ┌────────────────────┐        ┌──────────────────────┐    │
│  │  风格系统          │        │  转场提示词生成      │    │
│  │  styles/*.md       │        │ transition_prompt_   │    │
│  │                    │        │   generator.py       │    │
│  └────────────────────┘        └──────────────────────┘    │
│           │                              │                  │
│           ▼                              ▼                  │
│  ┌────────────────────┐        ┌──────────────────────┐    │
│  │ Nano Banana Pro    │        │   可灵 AI API        │    │
│  │ (Gemini 3 Pro)     │        │   kling_api.py       │    │
│  └────────────────────┘        └──────────────────────┘    │
│           │                              │                  │
│           ▼                              ▼                  │
│    🖼️ PPT 图片                    🎬 转场视频               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 2️⃣ 视频合成模块
```
┌─────────────────────────────────────────────────────────────┐
│               FFmpeg 视频合成流程                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  输入素材:                                                   │
│  ├── 📷 PPT 图片 (slide-01.png ~ slide-N.png)              │
│  ├── 🔄 预览视频 (preview.mp4)                              │
│  └── 🎞️ 转场视频 (transition_XX_to_YY.mp4)                 │
│                                                              │
│  ┌────────────────────────────────────────────────┐         │
│  │     video_materials.py - 素材管理             │         │
│  │  • 收集所有素材                                │         │
│  │  • 验证文件完整性                              │         │
│  │  • 组织素材顺序                                │         │
│  └────────────────────────────────────────────────┘         │
│                       │                                      │
│                       ▼                                      │
│  ┌────────────────────────────────────────────────┐         │
│  │     video_composer.py - FFmpeg 合成器         │         │
│  │                                                │         │
│  │  步骤 1: 图片转静态视频                        │         │
│  │    • 转换为 2 秒静态视频                       │         │
│  │    • 统一分辨率 1920x1080                      │         │
│  │    • 统一帧率 24fps                            │         │
│  │                                                │         │
│  │  步骤 2: 标准化所有视频                        │         │
│  │    • 缩放到统一分辨率                          │         │
│  │    • 添加黑边保持宽高比                        │         │
│  │    • 统一帧率                                  │         │
│  │                                                │         │
│  │  步骤 3: 拼接视频序列                          │         │
│  │    预览 → 转场01-02 → 静态02 → 转场02-03...   │         │
│  │                                                │         │
│  │  步骤 4: H.264 编码输出                        │         │
│  └────────────────────────────────────────────────┘         │
│                       │                                      │
│                       ▼                                      │
│              🎥 full_ppt_video.mp4                          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 3️⃣ 播放器系统
```
┌─────────────────────────────────────────────────────────────┐
│                   播放器架构                                 │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌───────────────────────┐    ┌────────────────────────┐   │
│  │
