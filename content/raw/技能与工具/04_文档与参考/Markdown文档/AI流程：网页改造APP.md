---
title: AI 流程：将网页改造为手机 APP
tags: [AI, 教程, PWA, Android, iOS, Capacitor]
date: 2026-01-12
---
#flashcards
# AI 流程：将网页改造为手机 APP

> [!SUMMARY] 教程简介
> 本教程介绍了如何将 AI 生成的网页应用打包成手机 APP 的三种方法：PWA 应用、Android APK 和 iPhone IPA。涵盖了从应用适配、PWA 改造到使用 Capacitor 框架打包原生应用的全流程。

## 方案概览

1.  **PWA (Progressive Web App)**：渐进式网页应用，轻量级，支持离线，体验接近原生。
2.  **Android APK**：使用 Capacitor 框架打包成原生安卓应用。
3.  **iPhone IPA**：使用 Capacitor 框架打包成原生 iOS 应用 (需 Mac 环境)。

---

## 一、应用准备与适配

在打包之前，需要确保网页应用适配手机端的操作习惯。

### 1. 案例选择
使用 Google AI Studio 的 [Browse App Gallery](https://aistudio.google.com/) 中的 3D 跑酷游戏作为案例。

### 2. 手机端适配
*   **问题**：手机无物理键盘，无法控制移动。
*   **AI 改造**：
    *   **Prompt**：`把项目改造一下适配手机端，用虚拟按键控制人物移动。如果遇到了页面显示不能符合手机端的需求，这里一并可以告诉Gemini让他帮我们修改。`
    *   **效果**：生成虚拟按键，支持触屏操作。
<!--SR:!2026-02-14,3,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250-->

### 3. 部署与测试
1.  **保存代码**：点击 `Save to GitHub` -> `Create` -> `Stage and Commit`。
2.  **修复引用**：在 `index.html` 底部引入 React 入口文件。
3.  **Netlify 部署**：
    *   `Import from GitHub`。
    *   添加环境变量 `GEMINI_API_KEY` (纯前端项目可随意填)。
    *   部署后在手机浏览器测试，发现存在地址栏占用空间等问题。
<!--SR:!2026-02-15,4,270!2026-02-15,4,270!2000-01-01,1,250-->

---

## 二、方案一：PWA 应用改造

PWA 让网页能被安装到桌面，全屏显示且支持离线使用。

### 1. 环境准备
*   克隆项目到本地 (使用 `git clone` 或 GitHub Desktop)。
*   安装 PWA 插件：
    ```bash
    npm install vite-plugin-pwa --save-dev
    ```
*   准备图标：在根目录新建 `public` 文件夹，放入应用图标图片。

### 2. AI 辅助配置
*   **工具**：Codex 或其他 AI 编程助手。
*   **Prompt**：`使用vite-plugin-pwa把这个项目改造成一个PWA应用，应用图片在public目录下面。`
*   **改动内容**：
    *   修改 Vite 配置文件，引入插件。
    *   定义 `manifest.webmanifest` (应用名、主题色、图标等)。
    *   生成 `sw.js` (Service Worker) 处理缓存与离线运行。

### 3. 效果验证
*   推送代码到 GitHub，触发 Netlify 自动部署。
*   手机浏览器打开，点击安装提示。
*   **结果**：桌面出现图标，启动后全屏无地址栏，支持离线运行。

---

## 三、方案二：Android APK 打包 (Capacitor)

使用 Capacitor 将网页封装为原生安卓应用。

### 1. 环境准备
*   安装 **Android Studio**。
*   在 VS Code 中创建新分支 `capacitor` (基于 PWA 改造前的提交)。

### 2. Capacitor 初始化
在终端执行以下命令：
```bash
# 1. 安装 Capacitor
npm install @capacitor/core
npm install @capacitor/cli --save-dev

# 2. 初始化项目 (需填写 App Name 和 Package ID)
npx cap init

# 3. 编译前端
npm run build

# 4. 安装安卓平台依赖
npm install @capacitor/android

# 5. 添加安卓平台
npx cap add android

# 6. 同步资源
npx cap sync
```

### 3. 调试与打包
1.  **打开工程**：`npx cap open android` (自动启动 Android Studio)。
2.  **模拟器运行**：等待依赖下载完成，点击 `Run` 按钮在模拟器中测试。
3.  **打包 APK**：
    *   菜单栏 `Build` -> `Generate Signed Bundle or APK`。
    *   生成的 APK 位于 `app/build/outputs/apk/debug/`。
4.  **真机安装**：将 APK 传输到手机进行安装测试。
<!--SR:!2000-01-01,1,250!2026-02-15,4,270!2026-02-15,4,276!2000-01-01,1,250-->

---

## 四、方案三：iOS IPA 打包 (Capacitor)

**注意**：开发 iOS 应用必须使用 **Mac 电脑**。
<!--SR:!2026-02-15,4,276!2026-02-15,4,276-->

### 1. 环境准备
*   Mac App Store 安装 **Xcode**。
*   安装 **CocoaPods**：`brew install cocoapods`。
*   克隆项目并创建新分支 `ios`。
<!--SR:!2000-01-01,1,250!2026-02-12,1,230-->

### 2. Capacitor 初始化
命令与安卓类似：
```bash
npm install @capacitor/core @capacitor/cli --save-dev
npx cap init
npm run build
npm install @capacitor/ios
npx cap add ios
npx cap sync
```

### 3. 调试与运行
1.  **打开工程**：`npx cap open ios` (自动启动 Xcode)。
2.  **模拟器运行**：点击左上角运行按钮。
3.  **真机调试**：连接 iPhone，选择设备进行安装 (有效期 7 天)。
4.  **上架**：需注册 Apple Developer Program 并通过 App Store 审核 (本教程未展开)。
<!--SR:!2000-01-01,1,250!2026-02-15,4,270!2026-02-15,4,270!2000-01-01,1,250-->

---

## 五、安全提示

> [!WARNING] API Key 安全
> *   **风险**：将 API Key 直接存放在客户端代码 (网页或 APP) 中极不安全。
> *   **最佳实践**：
>     1.  部署后端服务。
>     2.  API Key 存储在后端环境变量中。
>     3.  客户端请求后端，由后端代为调用 AI API。

---

## 六、相关资源

![[AI_Mobile_App_Dev.base]]
