---
source: raw/04_技能与工具/Superpowers/superpowers-main/skills/finishing-a-development-branch/SKILL.md
raw_sha256: dd2f82c6dc8582b621f9eb57fcb65f557f88eadf872727ac81d0840ae12c504e
compiled_at: 2026-04-14T16:52:49.313Z
---
# Finishing a Development Branch
## 摘要
Finishing a Development Branch是一套标准化的开发分支收尾工作流程，用于开发实现完成、所有测试通过后，规范分支整合、清理的决策与执行过程，核心流程为「验证测试→确定基础分支→给出结构化选项→执行选择→清理工作区」，常被用于开发任务完成后的收尾阶段。

## 核心原则
核心工作流程：`Verify tests → Present options → Execute choice → Clean up`（验证测试→呈现选项→执行选择→清理）。使用前需声明：`I'm using the finishing-a-development-branch skill to complete this work.`

## 完整流程
### 步骤1：验证测试
提供选项前必须先运行项目测试套件验证测试通过：
- 若测试失败，展示失败信息，终止流程，必须修复失败后才能继续
- 若测试通过，进入下一步

常用测试命令示例：`npm test` / `cargo test` / `pytest` / `go test ./...`

### 步骤2：确定基础分支
可通过Git命令自动查找常见主分支，或直接确认分支来源：
```bash
# 自动查找基础分支命令
git merge-base HEAD main 2>/dev/null || git merge-base HEAD master 2>/dev/null
```

### 步骤3：呈现选项
必须展示以下4个精简选项，不得添加额外解释：
```
Implementation complete. What would you like to do?

1. Merge back to <base-branch> locally
2. Push and create a Pull Request
3. Keep the branch as-is (I'll handle it later)
4. Discard this work

Which option?
```

### 步骤4：执行选择
#### 选项1：本地合并回基础分支
1. 切换到基础分支并拉取最新代码
2. 合并功能分支
3. 验证合并结果的测试
4. 测试通过后删除功能分支
5. 进入步骤5清理工作区

#### 选项2：推送分支创建Pull Request
1. 推送当前分支到远程仓库
2. 使用GitHub CLI创建标准格式PR（包含变更总结、测试计划）
3. 保留工作区，进入步骤5仅执行对应清理规则

#### 选项3：保留分支
输出保留提示，**不清理工作区**，流程结束。

#### 选项4：丢弃当前工作
1. 先展示将永久删除的内容，要求输入`discard`确认，未确认则终止
2. 确认后切换到基础分支，强制删除功能分支
3. 进入步骤5清理工作区

### 步骤5：清理工作区
仅对选项1、选项2、选项4执行清理：检查当前是否为git worktree，若是则移除对应工作区；选项3保留工作区不清理。

## 选项快速参考表
| 选项 | 执行合并 | 推送远程 | 保留工作区 | 清理分支 |
|--------|-------|------|---------------|----------------|
| 1. 本地合并 | ✓ | - | - | ✓ |
| 2. 创建PR | - | ✓ | ✓ | - |
| 3. 保持现状 | - | - | ✓ | - |
| 4. 丢弃工作 | - | - | - | ✓（强制） |

## 常见错误与规避
| 错误 | 问题 | 修复方式 |
|------|------|----------|
| 跳过测试验证 | 合并损坏代码、创建无法通过的PR | 提供选项前始终验证测试 |
| 开放式提问 | 需求模糊 | 必须呈现固定的4个结构化选项 |
| 自动清理工作区 | 误删可能还需要的工作区 | 仅对选项1和选项4清理工作区 |
| 丢弃前不确认 | 误删除工作 | 要求输入`discard`明确确认 |

## 红线规则
- 禁止：测试失败继续流程、合并后不验证测试、未确认删除工作、无明确请求强制推送
- 必须：提供选项前验证测试、呈现固定4个选项、丢弃前要求明确确认、仅对选项1和4清理工作区

## 集成关系
- 被调用场景：`subagent-driven-development`（步骤7，所有任务完成后）、`executing-plans`（步骤5，所有批次完成后）
- 配合工具：和`using-git-worktrees`配合使用，负责清理该技能创建的工作区
