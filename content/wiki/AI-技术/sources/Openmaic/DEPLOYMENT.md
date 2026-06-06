---
source: raw/Openmaic/DEPLOYMENT.md
raw_sha256: 06e67832fbc251265d2c4939061aabad50622a0c4b47c57f6b09133e329e5ec0
compiled_at: 2026-04-14T03:48:03.632Z
---
# OpenMAIC 飞书实验环境部署与运维手册
> 来源路径：`raw/Openmaic/DEPLOYMENT.md`

---

## TL;DR
本文档是 OpenMAIC 飞书实验环境的完整部署运维指南，涵盖环境准备、源码获取、依赖安装、配置启动、外网配置、日常运维、故障排查和数据备份全流程，适用于需要本地或服务器部署该项目的开发者/运维人员。

---

## 1. 核心要点
### 1.1 部署环境要求
| 依赖项 | 最低版本要求 | 补充说明 |
|--------|--------------|----------|
| 操作系统 | Windows 10/11 或 Ubuntu 20.04+ | 支持两类主流平台 |
| Node.js | v20.x+ | 推荐使用 nvm 进行版本管理 |
| pnpm | v9.x+ | 推荐通过 `npm install -g pnpm` 全局安装 |
| OpenClaw | v2026.2.1-zh.3+ | 需要提前安装并完成飞书插件配置 |

### 1.2 完整部署步骤
#### 1.2.1 获取源码
```powershell
mkdir -p C:\Users\Administrator\.openclaw\workspace\openmaic-feishu-lab
cd C:\Users\Administrator\.openclaw\workspace\openmaic-feishu-lab
git clone https://github.com/THU-MAIC/OpenMAIC.git .
```

#### 1.2.2 安装依赖
针对 Windows 环境二进制兼容性问题，推荐使用以下命令：
```powershell
pnpm install --shamefully-hoist --force --registry https://registry.npmmirror.com
```

#### 1.2.3 配置环境变量
1. 复制模板：`cp .env.example .env.local`
2. 配置大模型：填入火山引擎豆包（Doubao）的 API Key
3. 配置网关：填入 OpenClaw Gateway Token

#### 1.2.4 启动开发服务
```powershell
pnpm dev
```
服务启动后，本地访问地址：`http://localhost:3000/hr`

#### 1.2.5 外网访问配置（Nginx）
将项目根目录下的 `hr-portal.conf` 配置内容并入 Nginx 配置文件，重载配置后即可通过示例地址 `https://tool.sysmex.com.cn/hr` 访问。

### 1.3 运维与故障排查
#### 1.3.1 日志路径
- OpenMAIC 业务日志：`openmaic-feishu-lab/logs`（仅开启日志输出后生效）
- OpenClaw 消息网关日志：`C:\Users\Administrator\.openclaw\gateway-stdout.log`

#### 1.3.2 常见问题处理
| 故障现象 | 排查方向 |
|----------|----------|
| 服务无法启动 | 检查 3000 端口是否被占用 |
| 消息不回传 | 执行 `openclaw status` 检查飞书 WebSocket 连接状态 |
| 大模型调用报错 | 检查 API Key 余额、是否已订阅 Coding Plan |

### 1.4 数据备份
- OpenMAIC 本地学习进度：定期备份 `memory/main.sqlite`
- 飞书 Bitable 业务数据：由飞书云端自动备份，无需手动备份

---

## 2. 原始引用证据片段
> 以下为未修改的原始文档核心内容片段：
> 
> <details>
> <summary>点击展开完整原始内容</summary>
> 
> # 部署与运维手册 (DEPLOYMENT.md)
> 
> ## 1. 部署环境准备
> - **操作系统**: Windows 10/11 或 Linux (Ubuntu 20.04+)。
> - **Node.js**: v20.x+ (建议使用 nvm 管理)。
> - **pnpm**: v9.x+ (建议使用 `npm install -g pnpm`)。
> - **OpenClaw**: v2026.2.1-zh.3+ (已安装并配置好飞书插件)。
> 
> ## 2. 部署步骤
> 
> ### 2.1 获取源码
> ```powershell
> mkdir -p C:\Users\Administrator\.openclaw\workspace\openmaic-feishu-lab
> cd C:\Users\Administrator\.openclaw\workspace\openmaic-feishu-lab
> git clone https://github.com/THU-MAIC/OpenMAIC.git .
> ```
> 
> ### 2.2 安装依赖
> 由于在 Windows 环境下可能会遇到二进制兼容性问题，建议使用以下命令：
> ```powershell
> pnpm install --shamefully-hoist --force --registry https://registry.npmmirror.com
> ```
> 
> ### 2.3 配置环境变量
> 1.  **复制模板**: `cp .env.example .env.local`
> 2.  **配置模型**: 填入火山引擎 (Doubao) API Key。
> 3.  **配置网关**: 填入 OpenClaw Gateway Token。
> 
> ### 2.4 启动服务
> ```powershell
> pnpm dev
> ```
> 服务启动后，本地可通过 `http://localhost:3000/hr` 访问。
> 
> ### 2.5 Nginx 配置 (外网访问)
> 将项目根目录下的 [hr-portal.conf](./hr-portal.conf) 内容添加到 Nginx 的配置文件中。
> 配置完成后，可通过 [https://tool.sysmex.com.cn/hr](https://tool.sysmex.com.cn/hr) 访问。
> 
> ## 3. 运维与监控
> 
> ### 3.1 日志查看
> - **教学日志**: 查看 `openmaic-feishu-lab/logs` (如果配置了日志输出)。
> - **消息网关日志**: 查看 `C:\Users\Administrator\.openclaw\gateway-stdout.log`。
> 
> ### 3.2 常见问题处理
> - **服务无法启动**: 检查端口 3000 是否被占用。
> - **消息不回传**: 检查飞书 WebSocket 是否在线 (`openclaw status`)。
> - **模型报错**: 检查 API Key 是否余额充足并已订阅 Coding Plan。
> 
> ## 4. 数据备份
> - 定期备份 `memory/main.sqlite` (OpenMAIC 学习进度)。
> - 飞书 Bitable 数据由飞书云端自动备份。
> 
> </details>

---

## 冲突说明
当前未发现本文档与其他已收录来源存在内容矛盾，无冲突标注。
