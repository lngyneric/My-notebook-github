---
source: raw/04_技能与工具/Superpowers/superpowers-main/docs/testing.md
raw_sha256: 04e45dd04d4238372f05ed3605df7af34b3c78e36758163353298e788021d51f
compiled_at: 2026-04-14T16:50:34.886Z
---
# 测试Superpowers技能
本文档介绍了Superpowers技能的测试方法，重点说明针对包含子代理的复杂技能的集成测试流程。

## 摘要
Superpowers中涉及子代理、工作流和复杂交互的技能，需要通过无头模式运行真实Claude Code会话，并基于会话记录验证行为。文档涵盖了测试目录结构、测试运行方法、`subagent-driven-development`技能集成测试的细节、令牌分析工具的使用、常见问题排查、新集成测试编写规范以及会话记录格式说明。

## 关键要点
### 测试概述
- 复杂技能测试需要：在无头模式下运行真实Claude Code会话，通过会话记录验证行为正确性

### 测试目录结构
```
tests/
├── claude-code/
│   ├── test-helpers.sh                    # 共享测试工具
│   ├── test-subagent-driven-development-integration.sh
│   ├── analyze-token-usage.py             # 令牌分析工具
│   └── run-skill-tests.sh                 # 测试运行器（可选）
```

### 运行集成测试要求
1. 必须从superpowers插件目录启动测试，不能从临时目录运行
2. Claude Code已安装并可通过`claude`命令调用
3. 需要在`~/.claude/settings.json`中启用本地开发市场：`"superpowers@superpowers-dev": true`
4. 集成测试通常需要10-30分钟才能执行完成

### `subagent-driven-development`集成测试验证点
该测试验证技能的以下能力：
1. 正确加载计划：在流程开始时读取一次计划
2. 向子代理提供完整任务描述，不要求子代理自行读取文件
3. 子代理在报告前执行自我检查
4. 在代码质量检查前先执行规范合规性检查
5. 发现问题时使用检查循环修复
6. 规范检查者独立读取代码，不依赖实现者报告

### `subagent-driven-development`测试流程
1. **准备阶段**：创建带最小实现计划的临时Node.js项目
2. **执行阶段**：使用对应技能在无头模式下运行Claude Code
3. **验证阶段**：解析JSONL格式的会话记录，验证技能调用、子代理分发、任务跟踪、文件生成、测试结果、Git提交流程等内容
4. **令牌分析**：按子代理输出令牌使用明细和成本估算

### 令牌分析工具
工具路径：`tests/claude-code/analyze-token-usage.py`，用于分析任意Claude Code会话的令牌使用，支持查看：
- 主协调会话的令牌用量
- 每个子代理的用量分解（含代理ID、描述、消息数、输入/输出令牌、缓存用量、预估成本）
- 整体总用量和成本估算
- 典型参考：高缓存读取属于正常（提示缓存生效），每个子代理成本通常在$0.05-$0.15区间

### 常见问题排查
| 问题 | 解决方案 |
|------|----------|
| 找不到技能 | 从superpowers目录启动，检查插件配置，确认技能文件存在 |
| 权限错误 | 添加`--permission-mode bypassPermissions`参数，用`--add-dir`授权测试目录，检查目录权限 |
| 测试超时 | 将超时增加到30分钟，检查技能逻辑是否存在死循环，检查子代理任务复杂度 |
| 找不到会话记录 | 确认`~/.claude/projects/`下的正确目录，查找最近生成的JSONL文件，确认测试实际执行成功 |

### 编写新集成测试最佳实践
1. 使用trap自动清理临时目录
2. 解析JSONL格式的会话文件，不要仅 grep 用户端输出
3. 使用`--permission-mode bypassPermissions`和`--add-dir`授权访问
4. 必须从superpowers插件目录运行
5. 始终输出令牌分析，便于掌握成本
6. 验证真实行为：检查文件生成、测试通过、Git提交等实际产出

## 证据片段
### 测试输出示例
```
========================================
 Integration Test: subagent-driven-development
========================================
...
STATUS: PASSED
```

### 会话记录格式
会话记录为JSONL格式，每行是一个JSON对象，代表一条消息或工具结果。子代理调用通过`agentId`关联，令牌用量存储在`usage`字段，包含`input_tokens`、`output_tokens`、`cache_read_input_tokens`等核心信息。
