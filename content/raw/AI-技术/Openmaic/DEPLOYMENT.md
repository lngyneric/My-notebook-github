# 部署与运维手册 (DEPLOYMENT.md)

## 1. 部署环境准备
- **操作系统**: Windows 10/11 或 Linux (Ubuntu 20.04+)。
- **Node.js**: v20.x+ (建议使用 nvm 管理)。
- **pnpm**: v9.x+ (建议使用 `npm install -g pnpm`)。
- **OpenClaw**: v2026.2.1-zh.3+ (已安装并配置好飞书插件)。

## 2. 部署步骤

### 2.1 获取源码
```powershell
mkdir -p C:\Users\Administrator\.openclaw\workspace\openmaic-feishu-lab
cd C:\Users\Administrator\.openclaw\workspace\openmaic-feishu-lab
git clone https://github.com/THU-MAIC/OpenMAIC.git .
```

### 2.2 安装依赖
由于在 Windows 环境下可能会遇到二进制兼容性问题，建议使用以下命令：
```powershell
pnpm install --shamefully-hoist --force --registry https://registry.npmmirror.com
```

### 2.3 配置环境变量
1.  **复制模板**: `cp .env.example .env.local`
2.  **配置模型**: 填入火山引擎 (Doubao) API Key。
3.  **配置网关**: 填入 OpenClaw Gateway Token。

### 2.4 启动服务
```powershell
pnpm dev
```
服务启动后，本地可通过 `http://localhost:3000/hr` 访问。

### 2.5 Nginx 配置 (外网访问)
将项目根目录下的 [hr-portal.conf](./hr-portal.conf) 内容添加到 Nginx 的配置文件中。
配置完成后，可通过 [https://tool.sysmex.com.cn/hr](https://tool.sysmex.com.cn/hr) 访问。

## 3. 运维与监控

### 3.1 日志查看
- **教学日志**: 查看 `openmaic-feishu-lab/logs` (如果配置了日志输出)。
- **消息网关日志**: 查看 `C:\Users\Administrator\.openclaw\gateway-stdout.log`。

### 3.2 常见问题处理
- **服务无法启动**: 检查端口 3000 是否被占用。
- **消息不回传**: 检查飞书 WebSocket 是否在线 (`openclaw status`)。
- **模型报错**: 检查 API Key 是否余额充足并已订阅 Coding Plan。

## 4. 数据备份
- 定期备份 `memory/main.sqlite` (OpenMAIC 学习进度)。
- 飞书 Bitable 数据由飞书云端自动备份。
