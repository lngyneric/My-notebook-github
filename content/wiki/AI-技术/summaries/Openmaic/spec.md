---
source: raw/Openmaic/spec.md
raw_sha256: 75e21dd2354f592028fa225ce7e7959e0d2c2c58ce01aec2c706bb7e93f481b6
compiled_at: 2026-04-24T05:14:50.826Z
---
# OpenMAIC-Feishu-Lab 项目技术规格说明
## 摘要
本规格说明定义了OpenMAIC-Feishu-Lab项目的整体设计与实现要求，该项目通过整合清华大学开源OpenMAIC AI教学引擎与飞书多维表格（Bitable），为中国大陆地区提供低延迟、高自动化的AI互动教学方案，替代国内无法使用的Google Classroom服务。

## 核心模块说明
### 1. 项目愿景
为中国大陆地区提供功能完备、低延迟、高度自动化的AI互动教学解决方案，彻底解决Google Classroom在国内无法使用的问题。

### 2. 功能需求
| 功能分类 | 具体能力说明 |
|---------|--------------|
| AI 课程生成 | 支持根据用户输入的主题，调用豆包（Doubao）模型生成教学大纲、课件内容及互动测验 |
| 飞书Bitable集成 | 1. 学生档案管理：存储学生OpenID、姓名、所属课程等信息<br>2. 成绩实时回传：学生在OpenMAIC完成Quiz后，分数自动同步至Bitable<br>3. 报名自动化：学生填写Bitable表单后，自动通过飞书私聊发放课堂邀请 |
| 外网访问适配 | 1. 支持通过Nginx反向代理进行子路径`/hr`访问<br>2. 自动处理API请求、静态资源及WebSocket的子路径前缀 |
| 多智能体互动 | 支持老师、助教、学生等多个AI Agent在课堂中进行多边讨论 |

### 3. 技术架构
| 架构层级 | 技术选型 |
|---------|----------|
| 前端 | Next.js 15（App Router）、React 19、Tailwind CSS、Lucide Icons |
| 后端 | Next.js API Routes（支持Serverless部署） |
| AI能力层 | 火山引擎（Doubao-Ark）API，适配`ark-code-latest`模型 |
| 数据流转中间件 | OpenClaw Gateway（连接飞书生态与OpenMAIC引擎） |
| 部署方案 | Nginx反向代理 + Node.js Standalone模式 |

### 4. 数据模型（飞书Bitable）
- 表名：`AI_Class_Stats`
- 字段定义：
| 字段名 | 数据类型 | 特殊属性 |
|-------|----------|----------|
| student_name | String | - |
| feishu_openid | String | 唯一值 |
| course_name | Option | - |
| quiz_score | Number | - |
| status | Multi-select | 可选值：Invited、Ongoing、Completed |
| last_active | DateTime | - |

### 5. 安全与权限机制
1. **API安全**：所有OpenMAIC API路由通过OpenClaw Gateway的Bearer Token进行鉴权
2. **访问控制**：课堂链接包含短效`access_token`，仅限通过飞书私聊渠道发放
