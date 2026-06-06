---
source: raw/04_技能与工具/Superpowers/superpowers-main/commands/execute-plan.md
raw_sha256: f9a7c251381f9a0466a3e67b9000ec59c5bd9665419b248d1c3887a9212d70ad
compiled_at: 2026-04-14T16:49:46.079Z
---
# execute-plan（Superpowers指令）
## 摘要
`execute-plan` 是Superpowers工具集中用于批量执行计划并设置审核检查点的指令，该指令会禁用模型调用能力，要求调用指定技能并严格遵循对应规则执行。

## 关键要点
- 功能定位：支持带审核检查点的批量计划执行
- 配置特性：默认禁用模型调用
- 执行要求：需要调用`superpowers:executing-plans`技能并严格遵循该技能的规则执行

## 基础配置
| 配置项 | 参数值 |
| ------ | ------ |
| 描述 | 带审核检查点的批量计划执行 |
| 模型调用 | 禁用 |
