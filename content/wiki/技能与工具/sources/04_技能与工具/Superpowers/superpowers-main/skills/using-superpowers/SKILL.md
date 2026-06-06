---
source: raw/04_技能与工具/Superpowers/superpowers-main/skills/using-superpowers/SKILL.md
raw_sha256: 81d921b16502091f44e8669bbcfae74b87bbf4295d03fff70a98e81d73af60a6
compiled_at: 2026-04-15T00:34:04.595Z
---
# 使用 Superpowers 技能规范
## 摘要
本文档是 Superpowers 体系下`using-superpowers`技能的使用规范，核心要求是任何对话开始时，只要存在1%的可能性有技能适应当前任务，就必须在任何响应（包括澄清问题）之前调用对应技能，明确了技能调用的流程、优先级和需要规避的合理化误区。

## 核心规则
只要存在1%的可能性有技能适用于当前任务，**必须在任何响应或操作（包括澄清问题）前调用相关技能进行检查**；若调用后发现技能不适用，可不使用该技能，这是强制不可协商的要求。

## 技能访问方式
- 在 Claude Code 环境：使用`Skill`工具调用技能，调用后会加载技能内容，直接遵循执行即可，禁止使用Read工具读取技能文件。
- 在其他环境：查阅对应平台的技能加载文档获取调用方式。

## 技能调用流程
```mermaid
digraph skill_flow {
    "User message received" [shape=doublecircle];
    "Might any skill apply?" [shape=diamond];
    "Invoke Skill tool" [shape=box];
    "Announce: 'Using [skill] to [purpose]'" [shape=box];
    "Has checklist?" [shape=diamond];
    "Create TodoWrite todo per item" [shape=box];
    "Follow skill exactly" [shape=box];
    "Respond (including clarifications)" [shape=doublecircle];

    "User message received" -> "Might any skill apply?";
    "Might any skill apply?" -> "Invoke Skill tool" [label="yes, even 1%"];
    "Might any skill apply?" -> "Respond (including clarifications)" [label="definitely not"];
    "Invoke Skill tool" -> "Announce: 'Using [skill] to [purpose]'";
    "Announce: 'Using [skill] to [purpose]'" -> "Has checklist?";
    "Has checklist?" -> "Create TodoWrite todo per item" [label="yes"];
    "Has checklist?" -> "Follow skill exactly" [label="no"];
    "Create TodoWrite todo per item" -> "Follow skill exactly";
}
```
完整流程为：
1. 接收用户消息后判断是否有技能可能适用
2. 若有可能性（哪怕仅1%），先调用Skill工具，再声明使用技能及对应目的
3. 若技能包含检查清单，为每个清单项创建TodoWrite待办
4. 严格遵循技能内容执行，最后给出响应（含澄清说明）
5. 若确定无适用技能，可直接给出响应

## 需要规避的合理化误区（红牌）
以下想法属于需要停止的合理化逃避行为，不符合规范：
| 错误想法 | 实际要求 |
|---------|---------|
| "这只是一个简单问题" | 任何问题都是任务，必须检查技能 |
| "我需要先获取更多上下文" | 检查技能必须在澄清问题之前完成 |
| "我先探索一下代码库" | 技能会告知探索方法，必须先检查技能 |
| "我可以快速检查git/文件" | 文件不包含对话上下文，必须先检查技能 |
| "我先收集信息" | 技能会告知收集信息的方法，必须先检查 |
| "这不需要正式技能" | 只要有对应技能就必须使用 |
| "我记得这个技能" | 技能会迭代更新，必须读取当前版本 |
| "这不算是一个任务" | 任何操作都是任务，必须检查技能 |
| "这个技能大材小用了" | 简单任务也可能变复杂，必须使用 |
| "我先做这一件事再说" | 任何操作前都必须先检查技能 |
| "这样做感觉效率很高" | 无规则行动会浪费时间，技能可避免该问题 |
| "我知道这个概念" | 了解概念不等于正确使用技能，必须调用 |

## 多技能优先级
当多个技能都可能适用时，按以下顺序调用：
1. 优先调用**流程类技能**（如头脑风暴、调试）：这类技能会确定任务的处理方式
2. 其次调用**实现类技能**（如前端设计、mcp构建）：这类技能指导具体执行

示例："搭建X"→先调用头脑风暴技能，再调用对应实现技能；"修复bug"→先调用调试技能，再调用对应领域技能。

## 技能类型
- **刚性技能**（如TDD、调试）：必须严格遵循，不能为了适配调整破坏规则
- **弹性技能**（如模式类技能）：可以根据上下文适配技能原则
技能本身会标注自身类型。

## 用户指令说明
用户指令仅说明做什么，不说明怎么做，不能因为用户只给出了目标指令就跳过技能调用流程。
