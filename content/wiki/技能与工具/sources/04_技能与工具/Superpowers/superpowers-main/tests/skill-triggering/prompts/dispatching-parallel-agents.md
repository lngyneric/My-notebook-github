---
source: raw/04_技能与工具/Superpowers/superpowers-main/tests/skill-triggering/prompts/dispatching-parallel-agents.txt
raw_sha256: 67b28b5f81077f615fe0451bfba88808f2f5c67deded1749203310387c59e9e7
compiled_at: 2026-04-15T00:37:05.982Z
---
# 多模块独立测试失败调查请求

## 摘要
这是一份针对代码仓库中四个不同模块独立发生的不相关测试失败的调查请求，要求对所有失败问题进行排查分析。

## 关键要点
- 所有测试失败均为独立问题，分布在代码库的不同部分，相互之间无关联
- 一共存在4个测试失败案例，覆盖了认证、API、组件、工具四个不同功能模块

## 失败测试清单
| 测试文件路径 | 失败测试用例 | 失败表现 |
| ---- | ---- | ---- |
| `tests/auth/login.test.ts` | should redirect after login | 测试未通过 |
| `tests/api/users.test.ts` | should return user list | 接口返回500错误 |
| `tests/components/Button.test.tsx` | N/A | 快照不匹配 |
| `tests/utils/date.test.ts` | N/A | 时区处理功能损坏 |
