# OpenMAIC + 飞书多维表格 (Bitable) 融合部署方案

## 1. 方案背景
针对中国大陆地区无法访问 Google Classroom 的问题，利用飞书多维表格作为教务管理与成绩统计的替代方案。本项目将 OpenMAIC 的 AI 互动课堂能力与飞书多维表格的低代码管理能力相结合，通过 OpenClaw 实现消息分发与数据流转。

## 2. 核心架构设计

### 2.1 角色分配
- **OpenMAIC (教学引擎)**: 负责生成 outline、scenes（课件）、quiz（测验）及互动 H5。
- **飞书多维表格 (教务后台)**: 存储学生名单、课程进度、测验得分、签到记录。
- **OpenClaw (连接器)**: 作为 Gateway 监听飞书消息，调用 OpenMAIC 接口，并将结果写入 Bitable。

### 2.2 数据流向
1. **学员召集**: 教师在飞书群发布报名表单（Bitable Form） -> 学生填写 -> Bitable 自动增加记录 -> OpenClaw 监听到新增记录 -> 自动私发课程邀请码。
2. **学习过程**: 学生点击链接进入 OpenMAIC 课堂 -> 完成 Quiz -> OpenMAIC 推送得分。
3. **成绩统计**: OpenClaw 接收得分 -> 调用 Bitable API 更新对应学生的“得分”字段 -> 自动触发飞书卡片通知学生：“你本次课程得分 95”。

## 3. 数据库与表格设计 (Bitable Schema)

### 3.1 [学生成绩统计表]
| 字段名 | 类型 | 说明 |
| :--- | :--- | :--- |
| 学生姓名 | 文本 | - |
| 飞书 ID | 文本 | 用于私聊推送 (OpenID) |
| 课程名称 | 选项 | - |
| 签到状态 | 复选框 | - |
| 测验得分 | 数字 | 由 OpenMAIC 回传 |
| 学习进度 | 百分比 | - |
| 完成时间 | 日期 | - |

## 4. 实施步骤

### 4.1 环境配置
- 克隆源码至 `workspace/openmaic-feishu-lab`。
- 配置 `.env.local` 复用火山引擎 (Doubao) 模型。

### 4.2 飞书集成
- 在飞书开放平台开启“机器人”和“多维表格”权限。
- 在 OpenClaw 中配置 `feishu` 插件并确保 WebSocket 连接正常。

### 4.3 自动化逻辑编写
- 编写 `integration_bridge.js`:
    - 监听 OpenMAIC 的 `onQuizComplete` 事件。
    - 调用 `openclaw.feishu.bitable.record.update` 同步数据。

## 5. 预期效果
- 零成本替代 Google Classroom。
- 实现“教-学-测-统”全链路自动化。
- 数据完全存储在企业内部飞书环境中。
