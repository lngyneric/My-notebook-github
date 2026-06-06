---
source: raw/04_技能与工具/Superpowers/superpowers-main/skills/systematic-debugging/root-cause-tracing.md
raw_sha256: a81bee9448794d261b4aca8487c595d11ff4bd4e10a5f96bca1117dd32527050
compiled_at: 2026-04-14T16:55:17.174Z
---
# 根因追溯（Root Cause Tracing）
## 摘要
根因追溯是一种面向深度嵌套Bug的系统化调试方法，核心原则是不直接修复错误出现位置的表象，而是沿调用链反向追溯找到问题的原始触发源，在源头修复问题，并补充多层纵深防御，避免问题再次发生。

## 核心原则
不要只在错误出现的位置修复问题，需要沿调用链反向追溯直到找到最初的触发源，在源头完成修复。永远不要只修复症状。

## 适用场景
- 错误发生在执行流程深处，而非入口点
- 堆栈跟踪显示较长的调用链
- 不清楚无效数据的来源
- 需要定位触发问题的测试或代码

## 关键流程
1. **观察症状**：记录错误发生时的错误信息
2. **定位直接原因**：找到直接引发错误的代码
3. **反向追溯调用方**：逐层向上梳理调用关系
4. **持续向上追溯**：追踪参数、数据的来源与传递
5. **定位原始触发源**：找到问题最初产生的位置

## 调试技巧与工具
### 手动添加堆栈跟踪 instrumentation
当无法手动追溯时，可以在问题操作前添加 instrumentation 打印调试信息，要点：
- 使用`console.error()`输出（测试中日志不会被抑制，比通用logger更可靠
- 包含完整上下文：参数值、当前工作目录、环境信息
- 通过`new Error().stack`获取完整调用链
- 示例捕获命令：`npm test 2>&1 | grep 'DEBUG [目标关键词'`

### 定位测试污染的脚本
如果不清楚哪个测试造成了环境污染，可以使用仓库提供的`find-polluter.sh`二分脚本，逐个运行测试并定位第一个造成污染的测试。

## 实际案例：空`projectDir`问题
|环节|案例详情
|---|---
|症状|`.git`被错误创建在源代码目录`packages/core/`
|追溯链|`git init`在`process.cwd()`运行 ← 空的cwd参数 ← WorktreeManager接收到空projectDir ← Session.create()传入空字符串 ← 测试在`beforeEach`执行前访问了`context.tempDir` ← `setupCoreTest()`初始返回`{ tempDir: '' }`
|根因|顶层变量初始化访问了未初始化的空值
|修复方案|将`tempDir`修改为getter，在`beforeEach`之前访问会直接抛出错误
|补充纵深防御|1. `Project.create()`增加目录校验 2. `WorkspaceManager`校验目录非空 3. 环境守卫禁止在临时目录外执行`git init` 4. `git init`前增加堆栈日志记录

## 关键要点总结
- 永远不要只修复错误表象，持续反向追溯直到找到原始触发源
- 在源头修复问题后，最好补充多层纵深防御，让Bug无法再次发生
- 调试时在问题操作前打印日志，包含完整上下文和调用栈，比错误发生后再记录更有效
