# OpenMAIC-Feishu-Lab 任务列表 (Tasks)

## 1. 环境搭建 (Environment Setup)
- [x] 克隆 OpenMAIC 仓库并初始化。
- [x] 配置豆包 (Doubao-Ark) 模型 API Key 和 Base URL。
- [x] 配置 OpenClaw Gateway 环境。

## 2. 核心集成开发 (Core Integration)
- [x] 适配 Next.js `basePath: '/hr'` 模式。
- [x] 开发 `getApiPath` / `withBasePath` 路径工具函数。
- [x] 全局替换 20+ 个组件中的 API 请求和静态资源路径。
- [x] 修正 `providers.ts` 以兼容 `doubao/ark-code-latest` 模型解析。

## 3. 飞书 Bitable 自动化 (Feishu Automation)
- [x] 编写 `bitable-sync.js` 同步得分的原型脚本。
- [ ] 开发 `Bitable.RecordCreated` 事件监听器 (OpenClaw Plugin 层)。
- [ ] 自动化发送课堂邀请链接逻辑。

## 4. 部署与配置 (Deployment)
- [x] 生成 `hr-portal.conf` Nginx 配置文件。
- [x] 测试子路径 `/hr` 访问。
- [x] 测试 WebSocket 转发。

## 5. 文档与规范 (Documentation)
- [x] 编写 `README.md` (项目入口)。
- [x] 编写 `ARCHITECTURE.md` (架构图解)。
- [x] 编写 `BITABLE_GUIDE.md` (飞书接入指南)。
- [x] 编写 `DEPLOYMENT.md` (部署手册)。
- [x] 编写 `spec.md` (技术规格)。
- [x] 编写 `tasks.md` (任务进度)。
- [x] 编写 `checklist.md` (核对表)。
