---
source: raw/Openmaic/checklist.md
raw_sha256: a8dee21bcc7b41dfd6388b9b36f4bb06b3f2e1b3a0b502155d5ed686a0828b11
compiled_at: 2026-04-24T05:09:43.139Z
---
# OpenMAIC-Feishu-Lab 项目核对表
## 页面概述
本页面为 OpenMAIC-Feishu-Lab 项目的全流程功能验证与部署状态核对清单，覆盖模型接入、路由配置、飞书集成、前端适配、服务部署5个核心验证维度，用于追踪项目开发进度与交付质量。

## 验证明细
### 1. 模型验证 (Model Validation)
所有验证项均已完成：
- [x] 豆包模型 API Key 有效性验证通过
- [x] 斜杠格式模型名 `doubao/ark-code-latest` 解析正常
- [x] 冒号格式模型名 `doubao:ark-code-latest` 解析正常

### 2. 子路径访问 (Sub-path Access - /hr)
所有验证项均已完成：
- [x] API 路由规则配置：所有 `/api/*` 请求自动重定向至 `/hr/api/*`
- [x] 静态资源路径统一适配：头像、图标、图片等资源路径均添加 `/hr` 前缀
- [x] Nginx 转发规则生效：`tool.sysmex.com.cn/hr` 可正常访问本地 `localhost:3000/hr` 服务
- [x] 流式通信支持：聊天SSE流在 `/hr` 路径下可正常开启并返回流式响应

### 3. 飞书 Bitable 集成 (Feishu Integration)
- [x] 数据同步能力：`bitable-sync.js` 原型测试通过，可通过 OpenClaw 写入飞书多维表格
- [x] Schema 兼容性：字段名（`学生姓名`、`飞书 ID`、`测验得分`）与 Bitable 模板完全匹配
- [ ] 自动化触发能力：待实现 Bitable 表单提交事件监听功能

### 4. 用户界面 (User Interface)
所有验证项均已完成：
- [x] 角色信息展示：老师、助教、学生的名称及头像显示正常
- [x] 多语言支持：已适配中文界面
- [x] 响应式适配：移动端、飞书工作台内页面展示正常

### 5. 部署状态 (Deployment)
所有验证项均已完成：
- [x] 配置文件生成：Nginx 配置文件 `hr-portal.conf` 已产出
- [x] 环境变量配置：`.env.local` 已正确注入火山引擎 API 凭据
- [x] 服务运行状态：`pnpm dev` 开发服务运行稳定，无崩溃错误
