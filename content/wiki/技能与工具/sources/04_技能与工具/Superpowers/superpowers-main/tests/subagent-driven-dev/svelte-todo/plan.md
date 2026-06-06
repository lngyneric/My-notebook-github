---
source: raw/04_技能与工具/Superpowers/superpowers-main/tests/subagent-driven-dev/svelte-todo/plan.md
raw_sha256: b572f70f5d7cf995908b20f6f235b0bf9e6d79857b787c6515846fce4dc5c8de
compiled_at: 2026-04-15T00:38:35.845Z
---
# Svelte Todo List 实施计划
## 摘要
本文档是使用`superpowers:subagent-driven-development`技能开发基于Svelte的待办事项列表应用的分步实施计划，包含从项目初始化到文档编写的全流程任务划分与验证标准，完整规范参照`design.md`。

## 任务列表
### 1. 项目初始化
- 执行内容：
  - 使用Vite创建Svelte+TypeScript项目：`npm create vite@latest . -- --template svelte-ts`
  - 安装依赖并验证开发服务正常运行
  - 清理App.svelte的默认模板内容，仅保留标题
- 验证标准：
  - `npm run dev`可正常启动服务
  - 页面显示最小化的"Svelte Todos"标题
  - `npm run build`构建成功

### 2. 待办状态Store
- 执行内容：
  - 创建`src/lib/store.ts`，定义包含id、text、completed字段的`Todo`接口
  - 创建初始值为空数组的可写Store，导出`addTodo`、`toggleTodo`、`deleteTodo`、`clearCompleted`操作方法
  - 为每个方法创建单元测试文件`src/lib/store.test.ts`
- 验证标准：所有单元测试通过（需时安装vitest）

### 3. localStorage持久化
- 执行内容：
  - 创建`src/lib/storage.ts`，实现`loadTodos()`和`saveTodos()`方法，优雅处理JSON解析错误（出错返回空数组）
  - 与Store集成：初始化加载、变更时自动保存
  - 添加加载、保存、错误处理的测试
- 验证标准：测试通过；手动测试刷新页面后待办数据保留

### 4. TodoInput输入组件
- 执行内容：
  - 创建`src/lib/TodoInput.svelte`，文本输入绑定本地状态
  - 点击添加按钮/回车均可提交，输入为空时禁用添加按钮，提交后清空输入框
  - 添加组件测试
- 验证标准：测试通过；组件正常渲染输入框和按钮

### 5. TodoItem单项组件
- 执行内容：
  - 创建`src/lib/TodoItem.svelte`，接收`todo: Todo`属性
  - 勾选框切换完成状态，完成后文本添加删除线，删除按钮调用删除方法
  - 添加组件测试
- 验证标准：测试通过；组件正常渲染勾选框、文本、删除按钮

### 6. TodoList列表容器组件
- 执行内容：
  - 创建`src/lib/TodoList.svelte`，接收`todos: Todo[]`属性
  - 为每个待办渲染TodoItem，为空时显示"No todos yet"提示
  - 添加组件测试
- 验证标准：测试通过；组件正常渲染TodoItem列表

### 7. FilterBar筛选栏组件
- 执行内容：
  - 创建`src/lib/FilterBar.svelte`，接收`todos`、当前filter、筛选变更回调属性
  - 显示未完成待办数量、All/Active/Completed三个筛选按钮（当前筛选高亮）、"Clear completed"按钮（无已完成待办时隐藏）
  - 添加组件测试
- 验证标准：测试通过；组件正常渲染计数、筛选按钮、清空按钮

### 8. 应用集成
- 执行内容：
  - 在App.svelte导入所有组件和Store，维护筛选状态（默认'all'），根据筛选状态计算过滤后的待办列表
  - 按顺序渲染标题、TodoInput、TodoList、FilterBar，传递对应属性
- 验证标准：所有组件正常渲染；添加、切换、删除功能均可正常使用

### 9. 筛选功能端到端验证
- 执行内容：
  - 验证筛选按钮可正确过滤待办：All显示全部、Active仅显示未完成、Completed仅显示已完成
  - 验证清空已完成功能，必要时重置筛选状态，添加集成测试
- 验证标准：筛选测试通过；所有筛选状态手动验证正确

### 10. 样式优化
- 执行内容：
  - 按照设计稿添加样式：已完成待办添加删除线和低饱和度颜色、当前筛选按钮高亮、输入框聚焦样式、删除按钮 hover 显示（移动端默认显示）、适配响应式布局
- 验证标准：应用可用；样式不破坏原有功能

### 11. 端到端测试
- 执行内容：
  - 安装Playwright，创建`tests/todo.spec.ts`，覆盖添加待办、完成待办、删除待办、筛选、清空已完成、持久化等完整用户流程
- 验证标准：`npx playwright test`全部通过

### 12. 项目文档
- 执行内容：
  - 创建README.md，包含项目描述、安装、开发、测试、构建命令说明
- 验证标准：文档描述准确，说明可正常执行

## 关键要点
- 本计划基于子代理驱动开发技能`superpowers:subagent-driven-development`执行
- 每个任务都明确了执行内容和验证标准，覆盖功能开发、测试、文档全流程
- 要求为所有功能模块添加对应层级的测试，保证功能可靠性
- 数据通过localStorage实现持久化存储，刷新页面不丢失
