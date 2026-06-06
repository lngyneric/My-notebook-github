---
source: raw/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/ENV_SETUP.md
raw_sha256: f688763d1fc095c56e0efe9c28bec8460eb783e550876e6350e44dd592d59687
compiled_at: 2026-04-24T08:28:33.175Z
---
# 系统环境变量配置指南（NanoBanana PPT Skills 项目）
## 摘要
本文档为NanoBanana PPT Skills项目的API密钥管理配置指南，介绍采用**系统环境变量存储API密钥**的最优安全方案，涵盖配置验证、Git提交安全规范、跨设备使用、密钥生命周期管理及安全最佳实践，确保项目代码无敏感信息、可安全提交至公开代码仓库。

## 关键要点
1. 密钥存储方案对比：系统环境变量在安全性、便利性、Git安全维度均优于硬编码、.env文件方案，为首选方案
2. 已完成配置项：系统环境变量写入`~/.zshrc`、`run.sh`优先读取系统环境变量、项目敏感文件已清理
3. Git提交安全保障：敏感信息（密钥、.env、虚拟环境、输出文件）不会被提交，仅保留安全模板与代码
4. 跨环境兼容：支持zsh、bash、fish等常见Shell的环境变量配置方法
5. 全生命周期管理：提供密钥查看、临时/永久修改、删除的完整操作指引
6. 安全风控机制：明确最佳实践与提交前检查清单，杜绝敏感信息泄露

## 详细配置说明
### 方案对比与当前状态
本项目采用系统环境变量管理API密钥，三种主流密钥存储方案对比如下：
| 方案 | 安全性 | 便利性 | Git安全 |
|------|--------|--------|---------|
| 硬编码 | ❌ 极低 | ✓ 方便 | ❌ 会泄露 |
| .env文件 | ⚠️ 中等 | ✓ 方便 | ⚠️ 需配置.gitignore |
| **系统环境变量** | ✅ **高** | ✅ **最方便** | ✅ **完全安全** |

---

### 已完成的配置验证
#### 1. 系统环境变量配置
API密钥已添加至`~/.zshrc`文件，配置内容如下：
```bash
# Google AI API Key for PPT Generator
export GEMINI_API_KEY="your-api-key-here"
```
验证命令：
```bash
echo $GEMINI_API_KEY
# 应显示您的API密钥
```

#### 2. `run.sh` 密钥读取优先级
启动脚本`run.sh`的密钥读取逻辑按优先级排序：
1. 系统环境变量（最高优先级）
2. `.env` 文件（备用方案）
运行`./run.sh`时若正常加载系统环境变量，将输出：
```
✅ 使用系统环境变量中的API密钥
```

#### 3. 项目文件清理结果
- ✅ `.env` 文件已删除
- ✅ `.env.example` 保留作为配置模板
- ✅ `run.sh` 无硬编码密钥
- ✅ 所有文档使用`your-api-key-here`占位符

---

### Git提交安全性规范
#### 提交范围说明
**不会被提交的敏感内容**：
- ❌ API密钥（存储于系统环境变量，不在项目目录内）
- ❌ `.env` 文件（已删除且纳入.gitignore规则）
- ❌ 虚拟环境目录（`venv/`）
- ❌ 输出文件目录（`outputs/`）

**可安全提交的内容**：
- ✅ `.env.example` - 配置模板
- ✅ `.gitignore` - Git忽略规则
- ✅ `run.sh` - 从环境变量读取密钥的启动脚本
- ✅ `generate_ppt.py` - 核心功能脚本
- ✅ 所有文档、风格文件

#### 安全验证命令
执行以下命令搜索项目中的API密钥特征串，无输出则为安全：
```bash
grep -r "AIzaSy" --exclude-dir=.git --exclude-dir=venv .
```

---

### 使用方法
#### 本地项目使用
直接运行启动脚本即可自动加载系统环境变量：
```bash
./run.sh --plan ../test_slides_plan.json --style styles/gradient-glass.md --resolution 2K
```

#### 新设备部署步骤
1. 克隆仓库：
```bash
git clone https://github.com/你的用户名/ppt-generator.git
cd ppt-generator
```
2. 按使用的Shell配置环境变量：
   - zsh用户（推荐）：
   ```bash
   echo 'export GEMINI_API_KEY="your-api-key"' >> ~/.zshrc
   source ~/.zshrc
   ```
   - bash用户：
   ```bash
   echo 'export GEMINI_API_KEY="your-api-key"' >> ~/.bashrc
   source ~/.bashrc
   ```
   - fish用户：
   ```bash
   set -Ux GEMINI_API_KEY "your-api-key"
   ```
3. 安装依赖并运行：
```bash
python3 -m venv venv
source venv/bin/activate
pip install google-genai pillow
./run.sh --help
```

---

### API密钥生命周期管理
#### 查看当前密钥
```bash
echo $GEMINI_API_KEY
```
#### 临时修改（仅当前会话有效）
```bash
export GEMINI_API_KEY="new-key-here"
```
#### 永久修改
1. 编辑配置文件：`nano ~/.zshrc`（或其他编辑器）
2. 修改`export GEMINI_API_KEY="新的密钥"`对应行
3. 重载配置：`source ~/.zshrc`
#### 删除密钥
1. 编辑`~/.zshrc`删除`GEMINI_API_KEY`对应行
2. 执行命令：
```bash
source ~/.zshrc
unset GEMINI_API_KEY
```

---

### 最佳实践
#### 推荐做法
1. 所有密钥均使用系统环境变量存储，支持多密钥统一管理：
```bash
export GEMINI_API_KEY="..."
export OPENAI_API_KEY="..."
export AWS_ACCESS_KEY="..."
```
2. 每3-6个月定期轮换API密钥，发现异常使用立即更新
3. （可选）不同项目使用不同密钥，便于追踪用量、降低泄露影响
4. 安全备份环境变量配置：
```bash
# 导出配置后需安全存储
grep "export.*_KEY" ~/.zshrc > ~/my-env-backup.txt
```

#### 禁止做法
- ❌ 在代码中硬编码密钥
- ❌ 将`.zshrc`等个人配置文件提交至Git
- ❌ 通过邮件、即时通讯工具传输密钥
- ❌ 在公开截图、文档中暴露密钥
- ❌ 在多个公共项目使用同一密钥

---

### 提交前安全检查清单
提交到GitHub前需确认所有项通过：
- [ ] 执行`grep -r "AIzaSy" .`无输出
- [ ] `.env`文件不存在或已纳入.gitignore
- [ ] `run.sh`无硬编码密钥
- [ ] 所有文档使用`your-api-key-here`占位符
- [ ] `git status`未显示敏感文件
- [ ] `.zshrc`不在Git仓库范围内

---

### 安全等级评估
系统环境变量方案的各项指标表现：
```
┌─────────────────────────────────────────────┐
│ 安全等级：系统环境变量方案                    │
├─────────────────────────────────────────────┤
│                                             │
│  Git泄露风险         ████████████ 0%       │
│  代码泄露风险         ████████████ 0%       │
│  文档泄露风险         ████████████ 0%       │
│  便利性             ████████████ 100%      │
│  多项目共享          ████████████ 100%      │
│                                             │
└─────────────────────────────────────────────┘
```

---

## 总结
本方案为API密钥管理的最优安全方案，具备以下特性：
✅ API密钥存储于系统环境变量，与项目代码完全隔离
✅ 项目代码无任何硬编码敏感信息，可安全提交至公开仓库
✅ 支持跨项目共享密钥，新设备配置流程简单
✅ 提供完整的密钥管理与安全检查机制

---
**帮助指引**
- 环境变量配置问题：参考「API密钥生命周期管理」章节
- Git提交安全问题：查看`SECURITY.md`
- 项目使用问题：查看`README.md`与`QUICKSTART.md`
