# GitHub Pages 部署指南

本指南将帮助您将 Quartz 项目部署到 GitHub Pages。

## 前置条件

1. 确保您有一个 GitHub 账户
2. 项目已推送到 GitHub 仓库
3. 仓库名称为 `My-notebook-github`

## 部署步骤

### 1. 配置 GitHub 仓库设置

1. 进入您的 GitHub 仓库 `lngyneric/My-notebook-github`
2. 点击 **Settings** 标签页
3. 在左侧菜单中找到 **Pages** 选项
4. 在 **Source** 部分选择 **GitHub Actions**

### 2. 配置 GitHub Actions 权限

1. 在仓库的 **Settings** 页面
2. 点击左侧菜单的 **Actions** → **General**
3. 在 **Workflow permissions** 部分：
   - 选择 **Read and write permissions**
   - 勾选 **Allow GitHub Actions to create and approve pull requests**
4. 点击 **Save** 保存设置

### 3. 创建访问令牌（如果需要）

如果您的内容仓库是私有的，需要创建个人访问令牌：

1. 进入 GitHub **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. 点击 **Generate new token (classic)**
3. 设置令牌名称，如 "Quartz Deployment"
4. 选择适当的过期时间
5. 勾选以下权限：
   - `repo` (完整仓库访问权限)
   - `workflow` (工作流权限)
6. 点击 **Generate token** 并复制生成的令牌

### 4. 配置仓库密钥

1. 在您的仓库中，进入 **Settings** → **Secrets and variables** → **Actions**
2. 点击 **New repository secret**
3. 名称设置为 `ACCESS_TOKEN`
4. 值设置为上一步生成的个人访问令牌
5. 点击 **Add secret**

### 5. 触发部署

部署可以通过以下方式触发：

1. **自动触发**：推送代码到 `v4` 分支
2. **定时触发**：每6小时自动运行一次
3. **手动触发**：
   - 进入 **Actions** 标签页
   - 选择 "Deploy Quartz to GitHub Pages" 工作流
   - 点击 **Run workflow** 按钮

### 6. 验证部署

1. 在 **Actions** 标签页查看工作流运行状态
2. 部署成功后，您的网站将在以下地址可用：
   ```
   https://lngyneric.github.io/My-notebook-github/
   ```

## 配置文件说明

### quartz.config.ts

已更新 `baseUrl` 配置为：
```typescript
baseUrl: "lngyneric.github.io/My-notebook-github"
```

### GitHub Actions 工作流

工作流文件位于 `.github/workflows/deploy.yml`，包含以下主要步骤：

1. **构建阶段**：
   - 检出站点仓库代码
   - 检出内容仓库
   - 清理不需要的文件
   - 安装依赖并构建 Quartz
   - 上传构建产物

2. **部署阶段**：
   - 部署到 GitHub Pages

## 故障排除

### 常见问题

1. **权限错误**：确保 Actions 权限设置正确
2. **访问令牌错误**：检查 `ACCESS_TOKEN` 密钥是否正确设置
3. **构建失败**：查看 Actions 日志了解具体错误信息
4. **页面无法访问**：确保 GitHub Pages 设置为使用 GitHub Actions

### 检查清单

- [ ] GitHub Pages 源设置为 "GitHub Actions"
- [ ] Actions 权限设置为 "Read and write permissions"
- [ ] `ACCESS_TOKEN` 密钥已正确配置
- [ ] `baseUrl` 已更新为正确的 GitHub Pages URL
- [ ] 代码已推送到 `v4` 分支

## 更新内容

要更新网站内容：

1. 修改您的 Markdown 文件
2. 提交并推送到 `v4` 分支
3. GitHub Actions 将自动重新构建和部署网站

---

部署完成后，您的 Quartz 网站将在 `https://lngyneric.github.io/My-notebook-github/` 上线！