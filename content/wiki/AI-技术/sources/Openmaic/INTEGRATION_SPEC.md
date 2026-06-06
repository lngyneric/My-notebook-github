---
source: raw/Openmaic/INTEGRATION_SPEC.md
raw_sha256: c2177f12bb1af7fbd5eea858c3a7fe00e08fe30ec2aee6e53f05c2c3d637ef1d
compiled_at: 2026-04-14T03:48:14.022Z
---
# OpenMAIC + 飞书多维表格 (Bitable) 融合部署方案

> 来源路径：`raw/Openmaic/INTEGRATION_SPEC.md`

---

## TL;DR
本方案是为解决中国大陆地区无法访问 Google Classroom 的问题，将 OpenMAIC 的 AI 互动课堂能力与飞书多维表格的低代码教务管理能力，通过 OpenClaw 连接器对接，实现全链路自动化教学教务管理的融合部署方案，数据可完全存储在企业内部飞书环境，可零成本替代 Google Classroom。

---

## 要点
1. **方案定位**：中国大陆地区 Google Classroom 不可用场景下的替代教务教学方案
2. **核心角色分工**：
   - OpenMAIC：负责生成课程大纲、课件、测验及互动 H5，提供 AI 互动课堂能力
   - 飞书多维表格：作为教务后台，存储学生、进度、成绩、签到等全量教务数据
   - OpenClaw：作为网关连接器，实现飞书消息监听、OpenMAIC 接口调用、数据双向流转
3. **全链路数据流向**：从学员报名召集、课堂学习到成绩统计全流程自动化
4. **提供了标准飞书多维表格（学生成绩统计）Schema 定义**
5. **提供了可落地的从环境配置到集成开发的实施步骤**

---

## 完整方案内容

### 1. 方案背景
> 原始引用：
> 针对中国大陆地区无法访问 Google Classroom 的问题，利用飞书多维表格作为教务管理与成绩统计的替代方案。本项目将 OpenMAIC 的 AI 互动课堂能力与飞书多维表格的低代码管理能力相结合，通过 OpenClaw 实现消息分发与数据流转。

### 2. 核心架构设计

#### 2.1 角色分配
> 原始引用：
> - **OpenMAIC (教学引擎)**: 负责生成 outline、scenes（课件）、quiz（测验）及互动 H5。
> - **飞书多维表格 (教务后台)**: 存储学生名单、课程进度、测验得分、签到记录。
> - **OpenClaw (连接器)**: 作为 Gateway 监听飞书消息，调用 OpenMAIC 接口，并将结果写入 Bitable。

#### 2.2 数据流向
> 原始引用：
> 1. **学员召集**: 教师在飞书群发布报名表单（Bitable Form） -> 学生填写 -> Bitable 自动增加记录 -> OpenClaw 监听到新增记录 -> 自动私发课程邀请码。
> 2. **学习过程**: 学生点击链接进入 OpenMAIC 课堂 -> 完成 Quiz -> OpenMAIC 推送得分。
> 3. **成绩统计**: OpenClaw 接收得分 -> 调用 Bitable API 更新对应学生的“得分”字段 -> 自动触发飞书卡片通知学生：“你本次课程得分 95”。

### 3. 数据库与表格设计 (Bitable Schema)

#### 3.1 [学生成绩统计表]
> 原始引用：

| 字段名 | 类型 | 说明 |
| :--- | :--- | :--- |
| 学生姓名 | 文本 | - |
| 飞书 ID | 文本 | 用于私聊推送 (OpenID) |
| 课程名称 | 选项 | - |
| 签到状态 | 复选框 | - |
| 测验得分 | 数字 | 由 OpenMAIC 回传 |
| 学习进度 | 百分比 | - |
| 完成时间 | 日期 | - |

### 4. 实施步骤
> 原始引用：
> #### 4.1 环境配置
> - 克隆源码至 `workspace/openmaic-feishu-lab`。
> - 配置 `.env.local` 复用火山引擎 (Doubao) 模型。
> 
> #### 4.2 飞书集成
> - 在飞书开放平台开启“机器人”和“多维表格”权限。
> - 在 OpenClaw 中配置 `feishu` 插件并确保 WebSocket 连接正常。
> 
> #### 4.3 自动化逻辑编写
> - 编写 `integration_bridge.js`:
>     - 监听 OpenMAIC 的 `onQuizComplete` 事件。
>     - 调用 `openclaw.feishu.bitable.record.update` 同步数据。

### 5. 预期效果
> 原始引用：
> - 零成本替代 Google Classroom。
> - 实现“教-学-测-统”全链路自动化。
> - 数据完全存储在企业内部飞书环境中。

---

> [!WARNING]
> 冲突：当前仅收录本来源定义，未与其他来源做一致性校验，若存在其他方案定义需手动补充冲突标注。
