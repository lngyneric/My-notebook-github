---
source: raw/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/API_MANAGEMENT.md
raw_sha256: 8216703a9906812d1c941f172708525807a5e3a32628ea512a01a4a9c5deff72
compiled_at: 2026-04-24T08:25:12.072Z
---
<wiki>
# API 密钥管理规范
## 摘要
本文档为NanoBanana PPT生成项目的API密钥统一管理规范，明确了密钥的存储规则、安全防护要求、使用规范、多环境配置方案及安全最佳实践，保障密钥的安全性、可维护性与跨环境兼容性。

## 一、当前配置
### 1.1 API存储位置
所有API密钥统一存储于项目路径：
```
📁 ppt-generator/.env
```

### 1.2 安全验证
当前已完成的安全配置：
- ✅ `.env` 文件已创建
- ✅ 已被 `.gitignore` 第15行规则保护
- ✅ 不会被提交到Git版本库
- ✅ `run.sh` 脚本可正确加载密钥

### 1.3 使用方法
无需额外配置，直接调用脚本即可自动加载密钥：
```bash
./run.sh --plan slides_plan.json --style styles/gradient-glass.md --resolution 2K
```
加载成功输出示例：
```
📌 从 .env 文件加载API密钥
```

## 二、API管理核心规范
### 2.1 新增API密钥
编辑`.env`文件添加新密钥，格式要求如下：
```bash
# API 名称说明
# 用途：描述这个 API 的用途
# 获取地址：https://...
API_NAME=your-api-key-here
```
示例：
```bash
# OpenAI API
# 用途：未来可能用于文档分析
# 获取地址：https://platform.openai.com/api-keys
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx
```

### 2.2 代码中调用API密钥
#### ❌ 错误做法（硬编码，严格禁止）
```python
# 绝对不要这样做！
api_key = "AIzaSyAfHE4vctPhMF2mVn96aEZZp8WuURlaGpM"
```

#### ✅ 正确做法（从环境变量读取）
```python
import os

# 从环境变量读取
api_key = os.environ.get("GEMINI_API_KEY")

# 或带默认值
api_key = os.getenv("GEMINI_API_KEY", "")

# 检查是否存在
if not api_key:
    raise ValueError("未找到 GEMINI_API_KEY 环境变量")
```

### 2.3 环境变量加载优先级
`run.sh` 脚本的密钥加载逻辑如下（优先级从高到低）：
```
1. 系统环境变量（~/.zshrc 等）
   ↓ 未找到则加载
2. .env 文件
   ↓ 均未找到则
3. 报错提示用户配置
```
该逻辑的优势：
- ✅ CI/CD环境可直接使用系统环境变量
- ✅ 本地开发默认使用`.env`文件
- ✅ 支持灵活切换不同环境的密钥配置

### 2.4 多环境密钥管理
如需区分开发/测试/生产环境，可使用独立的环境配置文件：
```bash
# 开发环境配置
.env.development
# 测试环境配置
.env.test
# 生产环境配置
.env.production
```
切换环境方式：
```bash
# 方式1：复制对应环境配置为.env
cp .env.development .env
# 方式2：使用符号链接
ln -sf .env.development .env
```

## 三、.env文件结构说明
### 3.1 当前文件结构
```bash
.env
├─ [注释区域]
│  ├─ 安全提醒
│  ├─ 使用说明
│  └─ 加载优先级说明
│
├─ [主要 API 密钥]
│  └─ GEMINI_API_KEY (已配置)
│
├─ [备用 API 密钥]
│  ├─ OPENAI_API_KEY (注释状态)
│  ├─ ANTHROPIC_API_KEY (注释状态)
│  └─ STABILITY_API_KEY (注释状态)
│
└─ [项目配置]
   ├─ DEFAULT_RESOLUTION (注释状态)
   ├─ DEFAULT_STYLE (注释状态)
   └─ OUTPUT_DIR (注释状态)
```

### 3.2 字段说明
| 变量名 | 状态 | 用途 | 获取地址 |
|--------|------|------|----------|
| `GEMINI_API_KEY` | ✅ 已配置 | Nano Banana Pro 图像生成 | [Google AI Studio](https://makersuite.google.com/app/apikey) |
| `OPENAI_API_KEY` | 💤 预留 | 未来可能用于文档分析 | [OpenAI Platform](https://platform.openai.com/api-keys) |
| `ANTHROPIC_API_KEY` | 💤 预留 | 未来可能用于Claude API | [Anthropic Console](https://console.anthropic.com/) |
| `STABILITY_API_KEY` | 💤 预留 | 未来可能用于其他图像模型 | [Stability AI](https://platform.stability.ai/) |

## 四、安全检查清单
### 4.1 开发阶段
- [ ] 禁止在代码中硬编码API密钥
- [ ] 使用`os.environ.get()`或`os.getenv()`读取密钥
- [ ] 添加密钥缺失时的错误提示
- [ ] 在函数/类初始化时读取密钥，避免每次请求重复读取

### 4.2 代码提交前
- [ ] 运行`git status`确认`.env`不在待提交列表中
- [ ] 运行`grep -r "AIzaSy" --exclude-dir=.git .`检查无硬编码密钥
- [ ] 确认`.gitignore`包含`.env`规则
- [ ] 检查代码中无任何硬编码的敏感信息

### 4.3 项目分享时
- [ ] 提供`.env.example`作为配置模板
- [ ] 在README中说明API密钥配置方式
- [ ] 禁止通过聊天/邮件等渠道发送`.env`文件
- [ ] 要求使用者配置自己的API密钥

## 五、最佳实践
### 5.1 密钥轮换
建议每3-6个月更新一次API密钥，流程如下：
```bash
# 1. 在对应API平台生成新密钥
# 2. 更新.env文件中的密钥配置
# 3. 测试项目功能运行正常
# 4. 在API平台撤销旧密钥
```

### 5.2 密钥权限隔离
为不同用途/环境创建独立的API密钥，避免权限混用：
```bash
# 开发用密钥（限制配额与权限）
GEMINI_API_KEY_DEV=...
# 生产用密钥（完整权限与配额）
GEMINI_API_KEY_PROD=...
```

### 5.3 友好错误处理
封装密钥获取函数，添加清晰的错误提示：
```python
import os
import sys

def get_api_key(key_name):
    """安全获取 API 密钥"""
    api_key = os.getenv(key_name)

    if not api_key:
        print(f"❌ 错误: 未找到 {key_name} 环境变量")
        print("")
        print("请配置 API 密钥：")
        print("1. 编辑 .env 文件")
        print("2. 添加：{key_name}=your-key")
        print("3. 保存并重新运行")
        sys.exit(1)

    return api_key

# 调用示例
gemini_key = get_api_key("GEMINI_API_KEY")
```

### 5.4 日志安全处理
禁止在日志中输出完整API密钥，仅展示部分片段：
```python
# ❌ 危险做法
print(f"Using API key: {api_key}")

# ✅ 安全做法
print(f"Using API key: {api_key[:8]}...{api_key[-4:]}")
# 输出示例: Using API key: AIzaSyAf...GpM
```

## 六、迁移指南
### 6.1 从系统环境变量迁移到.env
如果之前在`~/.zshrc`中配置了密钥，按以下步骤迁移：
1. 从`.zshrc`中删除密钥导出配置
```bash
nano ~/.zshrc
# 删除 export GEMINI_API_KEY="..." 行
source ~/.zshrc
```
2. 确认密钥已添加到`.env`文件中
3. 测试加载状态：
```bash
./run.sh --help
# 输出应为：📌 从 .env 文件加载API密钥
```

### 6.2 从.env迁移到系统环境变量
如需跨项目共享密钥，可配置为系统环境变量：
1. 提取`.env`中的密钥：
```bash
cat .env | grep GEMINI_API_KEY
