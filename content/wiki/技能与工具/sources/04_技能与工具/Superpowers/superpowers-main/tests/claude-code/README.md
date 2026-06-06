---
source: raw/04_技能与工具/Superpowers/superpowers-main/tests/claude-code/README.md
raw_sha256: fe14823ed262997c61454510b6b1725a2e82eba393c28940f0da0407f09a8d67
compiled_at: 2026-04-14T16:50:50.641Z
---
# Claude Code Skills Tests
## 摘要
Claude Code Skills Tests是用于superpowers技能的自动化测试套件，基于Claude Code CLI以无头模式运行，用于验证技能是否被正确加载、Claude是否能按照技能规范执行预期行为。该测试套件区分快速测试与完整集成测试，提供了辅助脚本、灵活的运行参数和测试编写规范，支持自定义测试扩展与CI/CD集成。

## 概述
本测试套件通过无头模式调用Claude Code CLI（`claude -p`），验证superpowers技能的正确性，核心目标是确认技能加载正常、Claude能够遵循技能规则产生预期行为。

## 运行依赖
- 已安装Claude Code CLI并添加到系统PATH，可通过`claude --version`正常输出版本信息
- 已本地安装superpowers插件，安装步骤参考项目主README文档

## 运行方式
| 运行需求 | 执行命令 |
| ---- | ---- |
| 运行所有快速测试（推荐） | `./run-skill-tests.sh` |
| 运行完整集成测试（耗时10-30分钟） | `./run-skill-tests.sh --integration` |
| 运行指定单个测试 | `./run-skill-tests.sh --test test-subagent-driven-development.sh` |
| 开启详细输出模式运行 | `./run-skill-tests.sh --verbose` |
| 设置自定义超时时间 | `./run-skill-tests.sh --timeout 1800`（示例为设置30分钟超时，适配集成测试） |

## 测试结构
### 辅助脚本 test-helpers.sh
提供测试通用函数：
- `run_claude "prompt" [timeout]`：使用指定prompt运行Claude
- `assert_contains output pattern name`：验证输出中存在指定模式
- `assert_not_contains output pattern name`：验证输出中不存在指定模式
- `assert_count output pattern count name`：验证指定模式出现的精确次数
- `assert_order output pattern_a pattern_b name`：验证两个模式出现的先后顺序
- `create_test_project`：创建临时测试目录
- `create_test_plan project_dir`：创建示例计划文件

### 单个测试文件规范
每个测试文件遵循统一结构：
1. 引入`test-helpers.sh`
2. 使用指定prompt调用Claude Code
3. 通过断言工具验证预期行为
4. 测试成功返回0，失败返回非0值

## 现有测试
### 默认运行的快速测试
#### `test-subagent-driven-development.sh`
测试技能内容与要求，耗时约2分钟，验证点包括：
- 技能可正常加载与访问
- 工作流程顺序（规范合规先于代码质量）
- 自我检查要求已明确文档化
- 计划读取效率要求已明确文档化
- 规范合规审查的质疑原则已明确文档化
- 审查循环已明确文档化
- 任务上下文提供要求已明确文档化

### 需要添加`--integration`标记运行的集成测试
#### `test-subagent-driven-development-integration.sh`
完整工作流执行测试，耗时10-30分钟，核心内容：
- 创建带Node.js环境的真实测试项目
- 创建包含2个任务的实现计划
- 使用子代理驱动开发执行计划
- 验证实际行为，包括：计划仅在开始时读取一次、每个子代理提示包含完整任务文本、子代理提交前完成自我检查、规范合规审查先于代码质量审查、规范审查员独立阅读代码、生成可用的实现、测试全部通过、生成正确的git提交

该测试的核心验证目标：工作流端到端可用、改进已正确应用、子代理正确遵循技能要求、最终代码可用且经过测试。

## 添加新测试步骤
1. 创建新测试文件，命名格式为`test-<技能名称>.sh`
2. 引入`test-helpers.sh`
3. 使用`run_claude`和断言函数编写测试逻辑
4. 将测试添加到`run-skill-tests.sh`的测试列表中
5. 添加执行权限：`chmod +x test-<技能名称>.sh`

## 其他说明
### 超时设置
- 默认每个测试超时时间为5分钟
- 可通过`--timeout`参数根据需要调整超时时间
- 测试应聚焦核心验证点，避免运行时间过长

### 失败调试
添加`--verbose`参数运行可查看完整的Claude输出，方便定位问题，不开启verbose时仅失败测试会输出日志。示例：
```bash
./run-skill-tests.sh --verbose --test test-subagent-driven-development.sh
```

### CI/CD集成
在CI环境中可通过以下方式运行测试：
```bash
# 为CI环境设置显式超时
./run-skill-tests.sh --timeout 900

# 退出码0表示测试全部成功，非0表示存在失败测试
```

### 注意事项
- 快速测试仅验证技能指令的正确性，不执行完整工作流
- 完整工作流测试耗时极长
- 测试应聚焦验证核心技能要求，保持确定性，避免测试实现细节
