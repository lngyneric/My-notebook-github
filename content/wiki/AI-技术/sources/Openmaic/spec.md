---
source: raw/Openmaic/spec.md
raw_sha256: 75e21dd2354f592028fa225ce7e7959e0d2c2c58ce01aec2c706bb7e93f481b6
compiled_at: 2026-04-14T03:48:53.838Z
---
# OpenMAIC-Feishu-Lab 技术规格

> [!INFO] 来源
> 原始文档路径：`raw/Openmaic/spec.md`

---

## TL;DR
OpenMAIC-Feishu-Lab 是整合清华大学开源 OpenMAIC AI 教学引擎与飞书多维表格的开源 AI 互动教学解决方案，面向中国大陆地区解决 Google Classroom 不可用的问题，基于飞书生态实现课程生成、自动化管理、成绩同步等全流程教学功能。

---

## 1 项目愿景
| 要点 | 内容 |
|------|------|
| 核心目标 | 整合清华大学 OpenMAIC AI 教学引擎 + 飞书多维表格，为中国大陆提供功能完备、低延迟、高自动化的 AI 互动教学方案 |
| 解决痛点 | 解决 Google Classroom 在中国大陆无法使用的问题 |

> 原始证据片段：
> > OpenMAIC-Feishu-Lab 旨在通过整合清华大学开源的 **OpenMAIC** AI 教学引擎与 **飞书多维表格 (Bitable)**，为中国大陆地区提供一个功能完备、低延迟且高度自动化的 AI 互动教学解决方案，彻底解决 Google Classroom 在国内无法使用的问题。

---

## 2 功能需求
| 功能模块 | 要点 |
|----------|------|
| AI 课程生成 | 支持根据输入主题调用豆包模型生成教学大纲、课件内容、互动测验 |
| 飞书 Bitable 集成 - 学生档案管理 | 存储学生 OpenID、姓名、所属课程等信息 |
| 飞书 Bitable 集成 - 成绩实时回传 | 学生完成 OpenMAIC 测验后分数自动同步至 Bitable |
| 飞书 Bitable 集成 - 报名自动化 | 学生填写 Bitable 表单后，自动通过飞书私聊发放课堂邀请 |
| 外网访问适配 | 支持 Nginx 反向代理子路径 `/hr` 访问，自动处理 API 请求、静态资源、WebSocket 的子路径前缀 |
| 多智能体互动 | 支持老师、助教、学生多个 AI Agent 课堂多边讨论 |

> 原始证据片段：
> ```
> - **AI 课程生成**: 支持根据用户输入的主题，调用豆包 (Doubao) 模型生成教学大纲、课件内容及互动测验。
> - **飞书 Bitable 集成**:
>   - **学生档案管理**: 存储学生 OpenID、姓名、所属课程等信息。
>   - **成绩实时回传**: 学生在 OpenMAIC 完成 Quiz 后，分数自动同步至 Bitable。
>   - **报名自动化**: 学生填写 Bitable 表单后，自动通过飞书私聊发放课堂邀请。
> - **外网访问适配**:
>   - 支持通过 Nginx 反向代理进行子路径 (`/hr`) 访问。
>   - 自动处理 API 请求、静态资源及 WebSocket 的子路径前缀。
> - **多智能体互动**: 支持多个 AI Agent (老师、助教、学生) 在课堂中进行多边讨论。
> ```

---

## 3 技术架构
| 层级 | 技术栈 |
|------|--------|
| 前端 | Next.js 15 (App Router), React 19, Tailwind CSS, Lucide Icons |
| 后端 | Next.js API Routes (支持 Serverless) |
| AI 驱动 | 火山引擎豆包 (Doubao-Ark) API，适配 `ark-code-latest` 模型 |
| 中间件 | OpenClaw Gateway 连接飞书与 OpenMAIC |
| 部署 | Nginx 反向代理 + Node.js Standalone 模式 |

> 原始证据片段：
> ```
> - **前端**: Next.js 15 (App Router), React 19, Tailwind CSS, Lucide Icons.
> - **后端**: Next.js API Routes (Serverless-ready).
> - **AI 驱动**: 火山引擎 (Doubao-Ark) API, 适配 `ark-code-latest` 模型。
> - **数据流转**: OpenClaw Gateway 作为中间件连接飞书与 OpenMAIC.
> - **部署**: Nginx 反向代理 + Node.js Standalone 模式。
> ```

---

## 4 飞书多维表格数据模型
| 配置项 | 内容 |
|--------|------|
| 表格名称 | `AI_Class_Stats` |
| 字段 `student_name` | 字符串类型 |
| 字段 `feishu_openid` | 字符串类型，唯一索引 |
| 字段 `course_name` | 选项类型 |
| 字段 `quiz_score` | 数字类型 |
| 字段 `status` | 多选选项类型，可选值：`Invited`, `Ongoing`, `Completed` |
| 字段 `last_active` | 日期时间类型 |

> 原始证据片段：
> ```
> - **Table Name**: `AI_Class_Stats`
> - **Fields**:
>   - `student_name`: String
>   - `feishu_openid`: String (Unique)
>   - `course_name`: Option
>   - `quiz_score`: Number
>   - `status`: Multi-select (Invited, Ongoing, Completed)
>   - `last_active`: DateTime
> ```

---

## 5 安全与权限
| 安全模块 | 规则 |
|----------|------|
| API 安全 | 所有 OpenMAIC API 路由通过 OpenClaw Gateway 的 Bearer Token 鉴权 |
| 访问控制 | 课堂链接包含短效 `access_token`，仅限通过飞书私聊分发 |

> 原始证据片段：
> ```
> - **API 安全**: 所有 OpenMAIC API 路由通过 OpenClaw Gateway 的 Bearer Token 鉴权。
> - **访问控制**: 课堂链接包含短效 `access_token`，仅限通过飞书私聊接收。
> ```

---

> [!WARNING] 冲突标注
> 本页面仅编译自 `raw/Openmaic/spec.md` 单来源，暂未发现与已收录文档的冲突，如有新来源引入冲突请在此处补充标注。
