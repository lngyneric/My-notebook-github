---
source: raw/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/SECURITY.md
raw_sha256: 24485b9284641741e54082edeca30a35d5c99a37451a777783045f3f2e7b92fc
compiled_at: 2026-04-24T08:33:01.649Z
---
# Git提交安全检查清单（NanoBanana PPT生成器项目）
## 摘要
本文档为NanoBanana PPT生成器项目的Git提交安全规范，涵盖已落地的安全配置、提交前验证流程、标准Git工作流、敏感信息泄露应急方案及安全最佳实践，确保项目提交至GitHub时无API密钥、环境配置等敏感信息泄露风险。

## 一、已配置的安全措施
### 1. .gitignore 配置
已通过.gitignore规则屏蔽以下敏感/无需提交的文件与目录，不会被推送至GitHub：
```
✓ .env                  # API密钥配置文件
✓ venv/                 # Python虚拟环境
✓ outputs/              # 生成的PPT图片
✓ *.key, *.pem          # 其他密钥文件
✓ .DS_Store             # macOS系统文件
✓ __pycache__/          # Python缓存
✓ test_*.json           # 测试文件
```

### 2. 安全的环境变量管理
- 历史问题（已修复）：`run.sh`中曾硬编码API密钥
- 当前合规方案：
  ✅ API密钥统一存储在`.env`文件中
  ✅ `.env`已添加至.gitignore规则
  ✅ `run.sh`从`.env`文件动态读取密钥
  ✅ 提供`.env.example`作为无敏感信息的配置模板

### 3. 可安全提交的文件清单
以下文件无敏感内容，可正常提交至GitHub：
```
✓ .env.example          # 环境变量模板（不含真实密钥）
✓ .gitignore            # Git忽略规则
✓ README.md             # 项目说明
✓ QUICKSTART.md         # 快速开始指南
✓ SETUP_COMPLETE.md     # 配置完成说明
✓ generate_ppt.py       # Python生成脚本
✓ ppt-generator.md      # Skill定义
✓ run.sh                # 启动脚本（已修复，不含密钥）
✓ styles/*.md           # 风格定义文件
✓ templates/*.html      # HTML模板
```

## 二、提交前安全检查步骤
### 步骤1：验证敏感文件忽略规则生效
```bash
# 检查.env是否被正确忽略
git check-ignore -v .env
# 预期输出: .gitignore:15:.env	.env

# 模拟提交，查看会被纳入暂存区的文件
git add -n .
# 需确认列表中无.env等敏感文件
```

### 步骤2：全量搜索代码中的硬编码密钥
```bash
# 递归搜索可能的Gemini API密钥特征
grep -r "AIzaSy" --exclude-dir=.git --exclude-dir=venv --exclude-dir=outputs .

# 仅在.env文件中匹配为安全状态，其他文件匹配需删除硬编码内容
```

### 步骤3：检查Git历史是否存在敏感文件提交记录
```bash
# 检查历史提交中是否包含.env文件
git log --all --full-history --source -- .env

# 如有输出，说明.env曾被提交，需清理Git历史
```

## 三、安全Git工作流
### 首次提交流程
```bash
# 1. 初始化Git仓库（未初始化时执行）
git init

# 2. 验证.gitignore规则生效
git status
# 确认.env、venv/、outputs/未出现在未跟踪列表中

# 3. 暂存所有合规文件
git add .

# 4. 二次确认暂存区无敏感文件
git status

# 5. 提交代码
git commit -m "Initial commit: PPT Generator"

# 6. 关联远程GitHub仓库
git remote add origin https://github.com/你的用户名/ppt-generator.git

# 7. 推送至远程主分支
git push -u origin main
```

### 日常提交流程
```bash
# 1. 查看当前改动
git status

# 2. 暂存改动文件
git add .

# 3. 提交改动（需填写清晰的改动描述）
git commit -m "描述您的改动"

# 4. 推送至远程仓库
git push
```

## 四、密钥意外提交应急处理
若不慎提交包含密钥的文件，需立即执行以下操作：
1. **立即撤销泄露的密钥**
   访问 https://makersuite.google.com/app/apikey，删除或重新生成对应的API密钥
2. **从Git历史中清除敏感信息**
   ```bash
   # 使用git filter-branch重写历史，删除所有提交中的.env文件
   git filter-branch --force --index-filter \
     "git rm --cached --ignore-unmatch .env" \
     --prune-empty --tag-name-filter cat -- --all

   # 强制推送覆盖远程历史（慎用，会改写所有协作者的本地历史）
   git push origin --force --all
   ```
3. **后续处理**
   若仓库为公开仓库，可选择删除整个仓库后重建，或使用GitHub官方密钥扫描功能检测残留风险。

## 五、安全检查总结清单
提交至GitHub前，需确认所有项均已完成：
- [ ] `.env`文件已添加至`.gitignore`
- [ ] `run.sh`无硬编码的API密钥
- [ ] 运行`git status`确认无敏感文件待提交
- [ ] 运行`grep -r "AIzaSy" .`确认密钥仅存在于`.env`中
- [ ] `.env.example`仅包含配置模板，无真实密钥
- [ ] `outputs/`目录已被忽略（避免提交大量生成的图片文件）
- [ ] `venv/`目录已被忽略（避免提交依赖包）

## 六、.env.example 使用说明
供协作者配置环境的说明：
1. 克隆仓库后，复制`.env.example`生成本地配置文件：
   ```bash
   cp .env.example .env
   ```
2. 编辑`.env`，填入个人的API密钥：
   ```bash
   GEMINI_API_KEY=你的实际密钥
   ```
3. `.env`会被Git自动忽略，无需担心误提交。

## 七、安全最佳实践
### 合规操作（DO ✓）
- ✓ 使用`.env`文件存储敏感配置信息
- ✓ 将`.env`添加至`.gitignore`规则
- ✓ 提供`.env.example`作为无敏感信息的配置模板
- ✓ 定期轮换API密钥
- ✓ 优先使用环境变量而非硬编码敏感信息
- ✓ 每次提交前运行`git status`检查暂存内容

### 禁止操作（DON'T ✗）
- ✗ 在代码中硬编码API密钥等敏感信息
- ✗ 将`.env`文件提交至Git仓库
- ✗ 在公共仓库中存储任何形式的密钥
- ✗ 在README等公开文档中包含真实密钥
- ✗ 通过邮件、即时通讯工具传输明文密钥
- ✗ 多个项目共用同一API密钥

## 八、额外安全建议
1. **使用GitHub Secrets（适用于GitHub Actions场景）**
   在仓库设置中添加加密存储的密钥，工作流中通过`${{ secrets.GEMINI_API_KEY }}`调用，避免明文暴露。
2. **限制API密钥权限**
   仅为密钥授予必要的API访问权限，设置合理的API调用配额限制。
3. **监控API使用情况**
   定期查看API调用统计，发现异常访问立即撤销对应密钥。
4. **生产环境使用专业密钥管理服务**
   可选用AWS Secrets Manager、HashiCorp Vault、Azure Key Vault等专业服务管理敏感信息。

---
**当前项目状态**: ✅ 已完成安全配置，可安全提交至GitHub
