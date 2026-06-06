# 技能与工具 维基领域规范

## 概述
工具使用指南、工作流、模板、效率技巧

## 目录结构

```
wiki/技能与工具/
├── entities/   # 实体（Obsidian, Excalidraw, Dataview, Claude）
├── concepts/   # 概念（教程指南, 插件配置, 工作流优化, 笔记系统, 效率工具）
├── summaries/  # raw/ 源文件摘要
├── sources/    # 源文件处理记录
├── SCHEMA.md   # 本领域规范
├── index.md    # 领域索引
└── log.md      # 操作日志

raw/技能与工具/  # 不可变源文件
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
