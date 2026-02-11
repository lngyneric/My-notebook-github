# Git-AI 跟踪 Quartz 版本发布配置

## 概述

本项目已配置 git-ai 工具来跟踪 quartz 项目的版本发布。git-ai 是一个强大的 AI 驱动的 Git 助手，可以帮助分析代码变更和作者信息。

## 项目信息

- **项目地址**: https://github.com/lngyneric/My-notebook-github.git
- **Upstream 地址**: https://github.com/jackyzha0/quartz.git (v4 分支)
- **当前版本**: v4.5.1 (本地) → v4.5.2 (upstream)

## 配置内容

### 1. 远程仓库配置

项目已正确配置了两个远程仓库：

```bash
# 查看远程仓库
git remote -v

origin    https://github.com/lngyneric/My-notebook-github.git (fetch)
origin    https://github.com/lngyneric/My-notebook-github.git (push)
upstream  https://github.com/jackyzha0/quartz.git (fetch)
upstream  https://github.com/jackyzha0/quartz.git (push)
```

### 2. git-ai 工具

git-ai 版本：**1.1.1**

安装位置：`C:\Users\lingyun\.git-ai\bin\git-ai.exe`

## 使用方法

### 快速使用脚本

#### PowerShell 脚本 (推荐)

```powershell
cd "C:\Users\lingyun\Documents\BaiduSyncdisk\xcxnotes"
.\git-ai-quartz-tracker.ps1
```

**功能特性：**
- 自动检测更新
- 版本差异分析
- AI 作者统计
- 提供更新建议

#### 命令参数：

```powershell
# 显示帮助
.\git-ai-quartz-tracker.ps1 -ShowHelp

# 自动更新项目到最新版本
.\git-ai-quartz-tracker.ps1 -Update

# 执行完整的代码分析
.\git-ai-quartz-tracker.ps1 -FullAnalysis
```

#### 批处理脚本

```cmd
cd "C:\Users\lingyun\Documents\BaiduSyncdisk\xcxnotes"
git-ai-quartz-tracker.bat
```

### 直接使用 git-ai 命令

#### 查看当前状态

```bash
cd "C:\Users\lingyun\Documents\BaiduSyncdisk\xcxnotes"
"C:\Users\lingyun\.git-ai\bin\git-ai.exe" status
```

#### 查看统计信息

```bash
# 查看提交统计
"C:\Users\lingyun\.git-ai\bin\git-ai.exe" stats upstream/v4

# 查看 AI 作者比例
"C:\Users\lingyun\.git-ai\bin\git-ai.exe" stats --json
```

#### 代码作者分析

```bash
# 查看特定文件的作者信息
"C:\Users\lingyun\.git-ai\bin\git-ai.exe" blame quartz.config.ts

# 查看差异分析
"C:\Users\lingyun\.git-ai\bin\git-ai.exe" diff HEAD upstream/v4
```

#### 查看提交详情

```bash
# 查看提交记录
"C:\Users\lingyun\.git-ai\bin\git-ai.exe" show upstream/v4
```

## 版本跟踪工作流程

### 1. 定期检查更新

建议每天运行一次脚本来检查更新：

```powershell
# 每天检查更新
.\git-ai-quartz-tracker.ps1
```

### 2. 更新项目

当发现新版本时，使用以下命令更新：

```powershell
# 自动更新到最新版本
.\git-ai-quartz-tracker.ps1 -Update

# 或者手动执行
git fetch upstream
git merge upstream/v4
```

### 3. 分析版本差异

```powershell
# 完整分析
.\git-ai-quartz-tracker.ps1 -FullAnalysis

# 查看差异统计
git log --oneline HEAD..upstream/v4

# 详细差异对比
git diff HEAD upstream/v4 --stat
```

## git-ai 配置选项

### 查看配置

```bash
"C:\Users\lingyun\.git-ai\bin\git-ai.exe" config
```

### 常用配置设置

```bash
# 配置 git 路径
"C:\Users\lingyun\.git-ai\bin\git-ai.exe" config set git_path "C:\Program Files\Git\bin\git.exe"

# 启用/禁用自动更新
"C:\Users\lingyun\.git-ai\bin\git-ai.exe" config set disable_auto_updates false

# 配置更新频道
"C:\Users\lingyun\.git-ai\bin\git-ai.exe" config set update_channel latest
```

## 常见问题

### 1. git-ai 命令无法执行

如果出现错误 `git-ai: command not found`，请使用完整路径：

```bash
"C:\Users\lingyun\.git-ai\bin\git-ai.exe" --version
```

### 2. 权限问题

如果 PowerShell 执行受限，以管理员身份运行：

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. 更新失败

如果合并失败，尝试先保存本地更改：

```bash
git stash
git merge upstream/v4
git stash pop
```

## 当前状态

✅ **git-ai 配置完成**
✅ **upstream 仓库已配置**
✅ **版本跟踪脚本已创建**
✅ **git-ai 钩子已安装**
✅ **项目已准备好跟踪 quartz 版本**

## 更新日志

**2026-02-11**: 初始配置
- 创建 PowerShell 和批处理脚本
- 配置 git-ai 跟踪环境
- 测试 git-ai 功能正常
- 项目版本对比分析：v4.5.1 → v4.5.2
