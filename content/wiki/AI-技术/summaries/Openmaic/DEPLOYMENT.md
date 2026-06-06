---
source: raw/Openmaic/DEPLOYMENT.md
raw_sha256: 06e67832fbc251265d2c4939061aabad50622a0c4b47c57f6b09133e329e5ec0
compiled_at: 2026-04-24T05:10:40.168Z
---
# OpenMAIC 部署与运维手册
## 摘要
本文档为OpenMAIC飞书实验室项目的官方部署与运维操作指引，覆盖部署前置环境要求、全流程部署步骤、日常运维监控方案、常见问题排查逻辑及数据备份规范。

## 1. 部署环境准备
部署前需满足以下基础环境要求：
| 依赖项 | 版本要求 | 备注 |
| --- | --- | --- |
| 操作系统 | Windows 10/11 或 Linux (Ubuntu 20.04+) | 两种操作系统均支持部署 |
| Node.js | v20.x+ | 建议使用nvm进行版本管理 |
| pnpm | v9.x+ | 建议通过`npm install -g pnpm`全局安装 |
| OpenClaw | v2026.2.1-zh.3+ | 需已完成安装并配置飞书插件 |

## 2. 部署步骤
### 2.1 获取项目源码
执行以下命令创建工作目录并拉取OpenMAIC源码：
```powershell
mkdir -p C:\Users\Administrator\.openclaw\workspace\openmaic-feishu-lab
cd C:\Users\Administrator\.openclaw\workspace\openmaic-feishu-lab
git clone https://github.com/THU-MAIC/OpenMAIC.git .
```

### 2.2 安装项目依赖
Windows环境下可能存在二进制兼容性问题，推荐使用以下命令安装依赖：
```powershell
pnpm install --shamefully-hoist --force --registry https://registry.npmmirror.com
```

### 2.3 配置环境变量
1. 复制环境变量模板：执行`cp .env.example .env.local`生成本地配置文件
2. 模型服务配置：在配置文件中填入火山引擎（Doubao）API Key
3. 网关服务配置：在配置文件中填入OpenClaw Gateway Token

### 2.4 本地启动服务
执行启动命令：
```powershell
pnpm dev
```
服务启动完成后，本地访问地址为：`http://localhost:3000/hr`

### 2.5 外网访问配置（Nginx）
如需对外提供访问，将项目根目录下的`hr-portal.conf`配置内容添加到Nginx的配置文件中，配置生效后外网访问地址为：`https://tool.sysmex.com.cn/hr`

## 3. 运维与监控
### 3.1 日志查看路径
| 日志类型 | 存储路径 | 说明 |
| --- | --- | --- |
| 教学日志 | `openmaic-feishu-lab/logs` | 需提前配置日志输出功能后生效 |
| 消息网关日志 | `C:\Users\Administrator\.openclaw\gateway-stdout.log` | 记录OpenClaw网关的运行输出 |

### 3.2 常见问题排查
| 问题现象 | 排查方向 |
| --- | --- |
| 服务无法启动 | 检查3000端口是否被其他进程占用 |
| 消息不回传 | 执行`openclaw status`检查飞书WebSocket连接状态是否正常 |
| 模型调用报错 | 检查火山引擎API Key是否余额充足，且已订阅Coding Plan服务 |

## 4. 数据备份规范
1. OpenMAIC学习进度数据：定期备份`memory/main.sqlite`文件
2. 飞书Bitable数据：由飞书云端自动完成备份，无需手动操作
