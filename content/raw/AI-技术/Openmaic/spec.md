# OpenMAIC-Feishu-Lab 项目技术规格说明 (Spec)

## 1. 项目愿景 (Project Vision)
OpenMAIC-Feishu-Lab 旨在通过整合清华大学开源的 **OpenMAIC** AI 教学引擎与 **飞书多维表格 (Bitable)**，为中国大陆地区提供一个功能完备、低延迟且高度自动化的 AI 互动教学解决方案，彻底解决 Google Classroom 在国内无法使用的问题。

## 2. 功能需求 (Functional Requirements)
- **AI 课程生成**: 支持根据用户输入的主题，调用豆包 (Doubao) 模型生成教学大纲、课件内容及互动测验。
- **飞书 Bitable 集成**:
  - **学生档案管理**: 存储学生 OpenID、姓名、所属课程等信息。
  - **成绩实时回传**: 学生在 OpenMAIC 完成 Quiz 后，分数自动同步至 Bitable。
  - **报名自动化**: 学生填写 Bitable 表单后，自动通过飞书私聊发放课堂邀请。
- **外网访问适配**:
  - 支持通过 Nginx 反向代理进行子路径 (`/hr`) 访问。
  - 自动处理 API 请求、静态资源及 WebSocket 的子路径前缀。
- **多智能体互动**: 支持多个 AI Agent (老师、助教、学生) 在课堂中进行多边讨论。

## 3. 技术架构 (Technical Architecture)
- **前端**: Next.js 15 (App Router), React 19, Tailwind CSS, Lucide Icons.
- **后端**: Next.js API Routes (Serverless-ready).
- **AI 驱动**: 火山引擎 (Doubao-Ark) API, 适配 `ark-code-latest` 模型。
- **数据流转**: OpenClaw Gateway 作为中间件连接飞书与 OpenMAIC。
- **部署**: Nginx 反向代理 + Node.js Standalone 模式。

## 4. 数据模型 (Data Model - Bitable)
- **Table Name**: `AI_Class_Stats`
- **Fields**:
  - `student_name`: String
  - `feishu_openid`: String (Unique)
  - `course_name`: Option
  - `quiz_score`: Number
  - `status`: Multi-select (Invited, Ongoing, Completed)
  - `last_active`: DateTime

## 5. 安全与权限 (Security)
- **API 安全**: 所有 OpenMAIC API 路由通过 OpenClaw Gateway 的 Bearer Token 鉴权。
- **访问控制**: 课堂链接包含短效 `access_token`，仅限通过飞书私聊接收。
