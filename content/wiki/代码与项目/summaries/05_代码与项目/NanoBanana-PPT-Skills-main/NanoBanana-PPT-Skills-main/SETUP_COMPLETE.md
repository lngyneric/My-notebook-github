---
source: raw/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/SETUP_COMPLETE.md
raw_sha256: 72a86b3a57ea3e58bf70431a030799f0d1569a55d847bc50d3154b8a1a5dec6a
compiled_at: 2026-04-24T08:34:55.774Z
---
# NanoBanana PPT 生成器 环境配置完成指南
> 本文档为NanoBanana PPT生成器环境配置完成后的操作指引，涵盖已完成配置项、多种使用方式、快速测试流程、项目文件结构、环境安全规则、使用技巧及问题排查方案，帮助用户快速上手生成PPT。

## 一、已完成配置项
### 1. Python依赖安装 ✓
- 已安装核心依赖：google-genai (1.57.0)、pillow (12.1.0)
- 所有依赖均部署在项目专属Python虚拟环境中

### 2. API密钥配置 ✓
- GEMINI_API_KEY已完成设置
- 密钥存储在项目根目录的`.env`文件中
- 已配置`.gitignore`规则，防止密钥意外提交至公共代码仓库

### 3. 便捷脚本创建 ✓
- 已生成`run.sh`启动脚本，可自动激活虚拟环境、加载API密钥配置

## 二、PPT生成使用方式
### 方式1：使用便捷脚本（推荐）
自动处理所有环境配置，无需手动操作：
```bash
./run.sh --plan ../test_slides_plan.json --style styles/gradient-glass.md --resolution 2K
```

### 方式2：手动激活环境
适合需要自定义参数的场景：
```bash
# 激活Python虚拟环境
source venv/bin/activate

# 如需手动设置API密钥（未自动加载时使用）
export GEMINI_API_KEY="your-api-key-here"

# 运行核心生成脚本
python generate_ppt.py --plan ../test_slides_plan.json --style styles/gradient-glass.md --resolution 2K
```

### 方式3：在Claude Code中使用（操作最简单）
只需在Claude Code中输入自然语言需求即可，例如：
```
我想基于"莫伊兰箭.md"文档生成一个5页的PPT
```
Claude会自动完成所有分析与生成步骤。

## 三、快速测试流程
项目已预设测试用内容规划文件，可直接运行验证环境可用性：
### 1. 执行测试命令
```bash
cd /Users/guohao/Documents/code/ppt/ppt-generator
./run.sh --plan ../test_slides_plan.json --style styles/gradient-glass.md --resolution 2K
```
*注：测试规划文件`test_slides_plan.json`包含5页关于「莫伊兰箭」的PPT内容*

### 2. 生成耗时说明
- 单页PPT生成约需30秒
- 5页PPT总耗时约2.5分钟
- 生成完成后会自动输出结果文件的存储路径

### 3. 查看生成结果
生成完成后执行以下命令打开PPT播放器（将`TIMESTAMP`替换为实际输出的时间戳目录名）：
```bash
open outputs/TIMESTAMP/index.html
```

## 四、项目文件结构说明
```
ppt-generator/
├── run.sh                    # 便捷启动脚本（推荐使用）
├── .env                      # API密钥配置文件
├── .gitignore               # Git忽略规则文件（保护密钥安全）
├── venv/                    # Python虚拟环境目录
├── generate_ppt.py          # PPT生成核心脚本
├── ppt-generator.md         # PPT生成器Skill定义文件
├── README.md                # 项目完整说明文档
├── QUICKSTART.md            # 快速上手指南
├── styles/                  # PPT风格库目录
│   └── gradient-glass.md    # 渐变毛玻璃卡片风格配置
├── templates/               # HTML模板目录
│   └── viewer.html          # PPT播放器模板
└── outputs/                 # PPT生成结果目录（自动创建）
```

## 五、环境变量与安全提醒
### 密钥加载路径
GEMINI_API_KEY会从以下位置自动加载：
1. `run.sh`启动脚本内置的加载逻辑
2. 项目根目录的`.env`环境变量文件

### 安全注意事项
- ⚠️ 禁止将`.env`文件提交至公共代码仓库
- ⚠️ `.env`已加入`.gitignore`规则，默认不会被Git追踪
- ⚠️ 如需分享项目，请先删除`.env`文件中的密钥内容

## 六、下一步操作选项
### 选项1：立即测试环境
直接运行预设测试命令，验证全流程可用性：
```bash
./run.sh --plan ../test_slides_plan.json --style styles/gradient-glass.md --resolution 2K
```

### 选项2：生成自定义PPT
1. 准备好作为内容来源的Markdown或文本文档
2. 在Claude Code中说明PPT生成需求（页数、风格、受众、演讲时长等）
3. Claude将自动分析文档并完成PPT生成

### 选项3：查看项目文档
- 完整项目说明：`README.md`
- 快速上手指南：`QUICKSTART.md`
- 详细技术文档：`ppt-generator.md`

## 七、使用技巧
### 1. 输出分辨率选择
- **2K (2752x1536)**：日常场景使用，生成速度快
- **4K (5504x3072)**：重要正式场合使用，输出质量高

### 2. 页数与演讲时长适配建议
- 5页：适配5分钟快速演讲
- 5-10页：适配15分钟标准演示
- 10-15页：适配30分钟深度讲解
- 20-25页：适配60分钟完整展示

### 3. PPT播放器快捷键
生成的HTML格式PPT支持以下快捷操作：
- `←`/`→`：切换上/下一页
- `↑`/`Home`：跳转至首页
- `↓`/`End`：跳转至末页
- 空格键：控制自动播放/暂停
- `ESC`：切换全屏状态
- `H`：隐藏/显示播放控件

## 八、问题排查指南
### 1. 环境相关问题
```bash
# 重新激活Python虚拟环境
source venv/bin/activate

# 检查核心依赖是否正确安装
pip list | grep genai
```

### 2. API相关问题
```bash
# 检查当前环境中加载的API密钥
echo $GEMINI_API_KEY

# 手动设置API密钥（未自动加载时使用）
export GEMINI_API_KEY="your-key"
```

### 3. 生成失败处理方案
1. 检查网络连接是否正常
2. 确认GEMINI_API_KEY有效且有可用调用配额
3. 尝试降低生成分辨率后重试
4. 查看控制台输出的详细错误信息定位问题

## 九、准备就绪提示
您的PPT生成器已完成全部配置，可正常使用。推荐第一步先运行测试命令体验完整生成流程：
```bash
./run.sh --plan ../test_slides_plan.json --style styles/gradient-glass.md --resolution 2K
```
祝您使用愉快！🚀
