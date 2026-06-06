---
source: raw/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/SETUP_COMPLETE.md
raw_sha256: 72a86b3a57ea3e58bf70431a030799f0d1569a55d847bc50d3154b8a1a5dec6a
compiled_at: 2026-04-14T04:08:20.239Z
---
> [!INFO]
> 本文编译自原始路径：`raw/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/SETUP_COMPLETE.md`，原始内容未做修改

# NanoBanana PPT生成器 环境配置完成说明

## TL;DR
本页面记录NanoBanana PPT生成器的环境配置完成状态，所有Python依赖、API密钥、启动脚本均已配置完毕，可以直接使用。提供三种使用方式，支持快速测试生成演示PPT，并说明了项目结构、使用技巧和问题排查方法。

---

## 已完成的配置
所有配置项均已确认完成：
1. **Python依赖**（安装在虚拟环境中）：
   - google-genai 1.57.0
   - pillow 12.1.0
2. **API密钥配置**：
   - `GEMINI_API_KEY` 已完成设置
   - 密钥存储在 `.env` 文件中
   - `.gitignore` 已配置，可避免密钥意外泄露
3. **便捷启动脚本**：已创建 `run.sh`，可自动激活虚拟环境、加载API密钥

---

## 使用方式
### 方式1：使用便捷脚本（推荐）
```bash
# 直接运行，自动处理环境
./run.sh --plan ../test_slides_plan.json --style styles/gradient-glass.md --resolution 2K
```

### 方式2：手动激活环境运行
```bash
# 激活虚拟环境
source venv/bin/activate

# 设置API密钥（如果需要）
export GEMINI_API_KEY="your-api-key-here"

# 运行脚本
python generate_ppt.py --plan ../test_slides_plan.json --style styles/gradient-glass.md --resolution 2K
```

### 方式3：在Claude Code中使用（最简单）
直接在Claude Code中输入你的需求即可，例如：
```
我想基于"莫伊兰箭.md"文档生成一个5页的PPT
```
Claude会自动完成所有处理步骤。

---

## 快速测试
项目预置了测试规划文件 `test_slides_plan.json`，包含5页关于「莫伊兰箭」的PPT内容，可直接运行测试：
```bash
cd /Users/guohao/Documents/code/ppt/ppt-generator
./run.sh --plan ../test_slides_plan.json --style styles/gradient-glass.md --resolution 2K
```

### 生成说明
- 单页生成大约需要30秒
- 5页总共约2.5分钟
- 生成完成后会输出PPT的存放路径

### 查看生成结果
```bash
# 打开播放器（生成完成后会显示具体路径，替换TIMESTAMP为实际值即可）
open outputs/TIMESTAMP/index.html
```

---

## 项目文件结构
```
ppt-generator/
├── run.sh                    # 便捷启动脚本（推荐使用）
├── .env                      # API密钥配置文件
├── .gitignore               # Git忽略文件（保护密钥不被提交）
├── venv/                    # Python虚拟环境
├── generate_ppt.py          # 核心生成脚本
├── ppt-generator.md         # Skill定义
├── README.md                # 完整项目说明
├── QUICKSTART.md            # 快速开始指南
├── styles/                  # PPT风格库
│   └── gradient-glass.md    # 渐变毛玻璃卡片风格
├── templates/               # HTML模板
│   └── viewer.html          # PPT播放器模板
└── outputs/                 # 生成结果目录（运行时自动创建）
```

---

## 环境变量说明
`GEMINI_API_KEY` 已完成配置，可通过两种方式自动/手动加载：
1. `run.sh` 启动脚本会自动从 `.env` 加载密钥
2. `.env` 为本地环境变量配置文件

> [!WARNING] 安全提醒
> - ⚠️ 不要将 `.env` 文件提交到公共代码仓库
> - ⚠️ `.env` 已经加入 `.gitignore` 排除列表
> - ⚠️ 分享项目前请删除 `.env` 中的密钥内容

---

## 后续操作
### 选项1：立即体验测试
```bash
./run.sh --plan ../test_slides_plan.json --style styles/gradient-glass.md --resolution 2K
```

### 选项2：生成自定义PPT
1. 准备你的内容文档（支持Markdown或纯文本）
2. 在Claude Code中说明你的生成需求
3. Claude会自动分析文档并完成PPT生成

### 选项3：查看更多文档
- `README.md` - 完整项目说明
- `QUICKSTART.md` - 快速上手指南
- `ppt-generator.md` - 详细技术文档

---

## 使用技巧
### 分辨率选择
| 分辨率 | 参数 | 尺寸 | 适用场景 |
|--------|------|------|----------|
| 2K | `2K` | 2752x1536 | 日常使用，生成速度快 |
| 4K | `4K` | 5504x3072 | 重要场合，高质量输出 |

### 页数建议
- 5页：适合5分钟快速演讲
- 5-10页：适合15分钟标准演示
- 10-15页：适合30分钟深入讲解
- 20-25页：适合60分钟完整展示

### 播放器快捷键
- 方向键 `←` `→`：切换前后页面
- `↑` / `Home`：回到第一页
- `↓` / `End`：跳转到最后一页
- 空格：开启/暂停自动播放
- `ESC`：切换全屏状态
- `H`：隐藏/显示播放控件

---

## 问题排查
### 环境问题
```bash
# 重新激活虚拟环境
source venv/bin/activate

# 检查google-genai依赖是否正确安装
pip list | grep genai
```

### API问题
```bash
# 检查当前环境中的API密钥
echo $GEMINI_API_KEY

# 手动重新设置（如果密钥失效或未加载）
export GEMINI_API_KEY="your-key"
```

### 生成失败通用排查
1. 检查网络连接是否正常（需可访问Gemini API）
2. 确认API密钥有效且未过期
3. 降低分辨率后重试
4. 查看终端输出的详细错误信息定位问题

---

## 引用原始证据片段
<details>
<summary>点击展开原始完整内容</summary>

```markdown
# 环境配置完成！

## ✅ 已完成的配置

### 1. Python依赖安装 ✓
- google-genai (1.57.0)
- pillow (12.1.0)
- 所有依赖项已安装在虚拟环境中

### 2. API密钥配置 ✓
- GEMINI_API_KEY 已设置
- 密钥存储在 .env 文件中
- .gitignore 已配置，防止密钥泄露

### 3. 便捷脚本创建 ✓
- run.sh: 自动激活虚拟环境和设置API密钥的启动脚本

## 🚀 现在可以使用了！

### 方式1: 使用便捷脚本（推荐）

```bash
# 直接运行，自动处理环境
./run.sh --plan ../test_slides_plan.json --style styles/gradient-glass.md --resolution 2K
```

### 方式2: 手动激活环境

```bash
# 激活虚拟环境
source venv/bin/activate

# 设置API密钥（如果需要）
export GEMINI_API_KEY="your-api-key-here"

# 运行脚本
python generate_ppt.py --plan ../test_slides_plan.json --style styles/gradient-glass.md --resolution 2K
```

### 方式3: 在Claude Code中使用（最简单）

只需要在Claude Code中说：

```
我想基于"莫伊兰箭.md"文档生成一个5页的PPT
```

Claude会自动处理所有步骤。

## 🧪 快速测试

我已经为您创建了一个测试规划文件 `test_slides_plan.json`，包含5页关于"莫伊兰箭"的PPT内容。

### 运行测试：

```bash
cd /Users/guohao/Documents/code/ppt/ppt-generator
./run.sh --plan ../test_slides_plan.json --style styles/gradient-glass.md --resolution 2K
```

### 生成说明：
- 每页大约需要30秒
- 5页总共约2.5分钟
- 生成完成后会显示输出路径

### 查看结果：

```bash
# 打开播放器（生成完成后
