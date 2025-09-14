# GitHub Pages 快速设置指南

## 🚀 快速部署步骤

### 1. GitHub Pages 设置

1. 进入仓库 `lngyneric/My-notebook-github`
2. **Settings** → **Pages**
3. **Source** 选择 **GitHub Actions**

### 2. Actions 权限配置

1. **Settings** → **Actions** → **General**
2. **Workflow permissions** 设置为：
   - ✅ **Read and write permissions**
   - ✅ **Allow GitHub Actions to create and approve pull requests**
3. 点击 **Save**

### 3. 访问令牌配置（如需要）

如果内容仓库是私有的：

1. GitHub **Settings** → **Developer settings** → **Personal access tokens**
2. 创建新令牌，权限选择：
   - ✅ `repo`
   - ✅ `workflow`
3. 复制生成的令牌

### 4. 仓库密钥设置

1. 仓库 **Settings** → **Secrets and variables** → **Actions**
2. 添加新密钥：
   - **Name**: `ACCESS_TOKEN`
   - **Value**: 上一步的令牌

### 5. 触发部署

选择以下任一方式：

- **推送代码**到 `v4` 分支
- **手动触发**：Actions → "Deploy Quartz to GitHub Pages" → Run workflow
- **自动触发**：每6小时运行一次

## ✅ 验证清单

- [ ] GitHub Pages 源设置为 "GitHub Actions"
- [ ] Actions 权限为 "Read and write permissions"
- [ ] `ACCESS_TOKEN` 密钥已配置（如需要）
- [ ] `baseUrl` 已更新为 `lngyneric.github.io/My-notebook-github`
- [ ] 代码已推送到 `v4` 分支

## 🌐 访问地址

部署成功后访问：
```
https://lngyneric.github.io/My-notebook-github/
```

## 🔧 已完成的配置

✅ **baseUrl 已更新**：`quartz.config.ts` 中的 baseUrl 已设置为正确的 GitHub Pages URL

✅ **GitHub Actions 工作流**：`.github/workflows/deploy.yml` 已配置完整的构建和部署流程

✅ **示例内容**：已创建 `content/index.md` 作为首页

✅ **构建测试**：本地构建测试通过，生成了15个文件到 `public` 目录

## 📝 下一步

1. 按照上述步骤完成 GitHub 仓库设置
2. 推送代码到 `v4` 分支触发部署
3. 在 Actions 页面监控部署进度
4. 访问您的网站！

---

💡 **提示**：详细的部署说明请参考 `GITHUB_PAGES_DEPLOYMENT.md` 文件。