---
source: raw/Openmaic/checklist.md
raw_sha256: a8dee21bcc7b41dfd6388b9b36f4bb06b3f2e1b3a0b502155d5ed686a0828b11
compiled_at: 2026-04-14T03:47:47.759Z
---
# OpenMAIC-Feishu-Lab 项目核对表

> [!NOTE] TL;DR
> 本页为 OpenMAIC-Feishu-Lab 项目的功能完成核对清单，目前大部分基础功能已开发验证完成，仅剩余飞书 Bitable 集成的自动化触发功能待开发。

## 核对状态汇总
| 核对项分类               | 完成状态 |
| :----------------------- | :------- |
| 模型验证                 | ✅ 全部完成 |
| 子路径访问 (`/hr`)       | ✅ 全部完成 |
| 飞书 Bitable 集成        | ⚠️ 部分完成 |
| 用户界面                 | ✅ 全部完成 |
| 部署状态                 | ✅ 全部完成 |

## 详细核对项
### 1. 模型验证 (Model Validation)
- [x] **Key 验证**: 豆包模型 API Key 验证通过。
- [x] **模型名解析**: `doubao/ark-code-latest` (斜杠格式) 解析正常。
- [x] **模型名解析**: `doubao:ark-code-latest` (冒号格式) 解析正常。

### 2. 子路径访问 (Sub-path Access - /hr)
- [x] **API 路由**: 所有 `/api/*` 请求自动重定向至 `/hr/api/*`。
- [x] **静态资源**: 头像、图标、图片等资源路径包含 `/hr` 前缀。
- [x] **Nginx 转发**: `tool.sysmex.com.cn/hr` 能够访问本地 `localhost:3000/hr`。
- [x] **WebSocket**: 聊天流 (SSE) 在 `/hr` 路径下能正常开启并流式响应。

### 3. 飞书 Bitable 集成 (Feishu Integration)
- [x] **数据同步**: `bitable-sync.js` 原型通过测试，能够通过 OpenClaw 写入多维表格。
- [x] **Schema 兼容**: 字段名 (`学生姓名`, `飞书 ID`, `测验得分`) 与 Bitable 模板一致。
- [ ] **自动化触发**: 监听 Bitable 表单提交事件。

### 4. 用户界面 (User Interface)
- [x] **角色显示**: 老师、助教、学生的名称及头像正常显示。
- [x] **多语言**: 支持中文界面。
- [x] **响应式**: 在移动端/飞书工作台内显示正常。

### 5. 部署状态 (Deployment)
- [x] **配置文件**: `hr-portal.conf` 已生成。
- [x] **环境变量**: `.env.local` 已正确注入火山引擎 API 凭据。
- [x] **服务状态**: `pnpm dev` 运行稳定，无崩溃错误。

---

## 引用原始证据
> 原始来源路径：`raw/Openmaic/checklist.md`
> ```markdown
# OpenMAIC-Feishu-Lab 项目核对表 (Checklist)

## 1. 模型验证 (Model Validation)
- [x] **Key 验证**: 豆包模型 API Key 验证通过。
- [x] **模型名解析**: `doubao/ark-code-latest` (斜杠格式) 解析正常。
- [x] **模型名解析**: `doubao:ark-code-latest` (冒号格式) 解析正常。

## 2. 子路径访问 (Sub-path Access - /hr)
- [x] **API 路由**: 所有 `/api/*` 请求自动重定向至 `/hr/api/*`。
- [x] **静态资源**: 头像、图标、图片等资源路径包含 `/hr` 前缀。
- [x] **Nginx 转发**: `tool.sysmex.com.cn/hr` 能够访问本地 `localhost:3000/hr`。
- [x] **WebSocket**: 聊天流 (SSE) 在 `/hr` 路径下能正常开启并流式响应。

## 3. 飞书 Bitable 集成 (Feishu Integration)
- [x] **数据同步**: `bitable-sync.js` 原型通过测试，能够通过 OpenClaw 写入多维表格。
- [x] **Schema 兼容**: 字段名 (`学生姓名`, `飞书 ID`, `测验得分`) 与 Bitable 模板一致。
- [ ] **自动化触发**: 监听 Bitable 表单提交事件。

## 4. 用户界面 (User Interface)
- [x] **角色显示**: 老师、助教、学生的名称及头像正常显示。
- [x] **多语言**: 支持中文界面。
- [x] **响应式**: 在移动端/飞书工作台内显示正常。

## 5. 部署状态 (Deployment)
- [x] **配置文件**: `hr-portal.conf` 已生成。
- [x] **环境变量**: `.env.local` 已正确注入火山引擎 API 凭据。
- [x] **服务状态**: `pnpm dev` 运行稳定，无崩溃错误。
> ```

> [!WARNING] 冲突：
> 本页无已知冲突。
