# AI-技术 维基领域规范

## 概述
AI/LLM/RAG/Agent 技术

## 目录结构

```
wiki/AI-技术/
├── entities/   # 实体（LLM模型, Agent框架, 知识图谱工具, RAG系统）
├── concepts/   # 概念（大语言模型, 检索增强生成, 智能体模式, 提示工程, 知识图谱, 语义搜索）
├── summaries/  # raw/ 源文件摘要
├── sources/    # 源文件处理记录
├── SCHEMA.md   # 本领域规范
├── index.md    # 领域索引
└── log.md      # 操作日志

raw/AI-技术/  # 不可变源文件
```

## 页面类型
- **entities/** — 人、组织、系统、项目、工具
- **concepts/** — 理论、方法、模型、模式
- **summaries/** — 源文件摘要（LLM 生成）
- **sources/** — 源文件处理记录

## 交叉引用规范
- 使用 `[[页面名]]` 格式
- 跨领域引用: `[[领域/页面名]]`
- 源文件: `source: 文件名`
