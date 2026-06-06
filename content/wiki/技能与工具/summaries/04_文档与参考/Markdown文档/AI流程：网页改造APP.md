---
source: raw/04_文档与参考/Markdown文档/AI流程：网页改造APP.md
raw_sha256: b625471bf577f4681bf931b57df1c171166e392731a18058ff973a0fad9b3e6c
compiled_at: 2026-04-24T05:49:14.702Z
---
# AI 流程：将网页改造为手机 APP
> 标签：AI, 教程, PWA, Android, iOS, Capacitor
> 发布日期：2026-01-12

## 摘要
本教程介绍了如何将 AI 生成的网页应用打包成手机 APP 的三种实现方案，涵盖从应用适配、PWA 改造到使用 Capacitor 框架打包原生应用的全流程，最终可输出 PWA 应用、Android APK、iPhone IPA 三类产物。

## 方案概览
本教程提供三种将网页转为手机APP的实现路径：
1.  **PWA (Progressive Web App)**：渐进式网页应用，轻量级，支持离线运行，用户体验接近原生应用。
2.  **Android APK**：使用 Capacitor 框架打包生成原生安卓应用安装包。
3.  **iPhone IPA**：使用 Capacitor 框架打包生成原生 iOS 应用安装包（需 Mac 开发环境）。

---

## 一、应用准备与适配
打包前需先完成网页应用的手机端操作习惯适配，具体步骤如下：
### 1. 案例选择
本教程采用 Google AI Studio Browse App Gallery 中的 3D 跑酷游戏作为改造案例。
### 2. 手机端适配
- **适配问题**：手机端无物理键盘，原依赖键盘控制的网页应用无法直接使用。
- **AI 改造方案**：
  - 提示词（Prompt）：`把项目改造一下适配手机端，用虚拟按键控制人物移动。如果遇到了页面显示不能符合手机端的需求，这里一并可以告诉Gemini让他帮我们修改。
  - 改造效果：自动生成虚拟操作按键，支持触屏控制。
### 3. 部署与测试
1.  代码保存：点击 `Save to GitHub` -> `Create` -> `Stage and Commit` 提交代码到GitHub仓库。
2.  引用修复：在 `index.html` 底部引入React入口文件。
3.  Netlify 部署：
    - 选择 `Import from GitHub` 导入仓库
    - 添加环境变量 `GEMINI_API_KEY`（纯前端项目可随意填写）
    - 部署完成后在手机浏览器测试，排查地址栏占用空间等适配问题。

---

## 二、方案一：PWA 应用改造
PWA 可实现网页安装到设备桌面，全屏显示且支持离线使用，无需复杂的原生应用打包流程。
### 1. 环境准备
- 将项目克隆到本地（支持 `git clone` 或 GitHub Desktop 工具）
- 安装PWA插件：
  ```bash
  npm install vite-plugin-pwa --save-dev
  ```
- 图标准备：在项目根目录新建 `public` 文件夹，放入应用图标资源。
### 2. AI 辅助配置
- 工具：Codex 或其他 AI 编程助手
- 提示词（Prompt）：`使用vite-plugin-pwa把这个项目改造成一个PWA应用，应用图片在public目录下面。`
- 自动完成的改动内容：
  1. 修改Vite配置文件，引入PWA插件
  2. 生成并配置 `manifest.webmanifest` 文件（定义应用名称、主题色、图标等元信息）
  3. 生成 `sw.js`（Service Worker）脚本处理资源缓存与离线运行逻辑
### 3. 效果验证
1. 将修改后的代码推送到GitHub，触发Netlify自动部署
2. 手机浏览器访问部署地址，点击安装提示完成应用安装
3. 验证效果：设备桌面出现应用图标，启动后全屏无地址栏，支持离线运行。

---

## 三、方案二：Android APK 打包 (Capacitor)
使用Capacitor框架将网页封装为原生安卓应用，生成APK安装包。
### 1. 环境准备
- 安装 Android Studio 开发工具
- 在VS Code中基于PWA改造前的提交创建新分支 `capacitor`
### 2. Capacitor 初始化
在项目终端依次执行以下命令：
```bash
# 1. 安装 Capacitor 核心依赖与命令行工具
npm install @capacitor/core
npm install @capacitor/cli --save-dev

# 2. 初始化Capacitor项目（需填写应用名称与Package ID）
npx cap init

# 3. 编译前端项目产物
npm run build

# 4. 安装安卓平台依赖
npm install @capacitor/android

# 5. 添加安卓平台支持
npx cap add android

# 6. 同步前端资源到原生项目
npx cap sync
```
### 3. 调试与打包
1.  打开安卓工程：执行 `npx cap open android` 自动启动Android Studio
2.  模拟器测试：等待依赖下载完成后，点击`Run`按钮在安卓模拟器中运行测试
3.  APK打包：
    - 菜单栏选择 `Build` -> `Generate Signed Bundle or APK`
    - 生成的APK文件路径为 `app/build/outputs/apk/debug/`
4.  真机测试：将APK传输到安卓手机完成安装测试。

---

## 四、方案三：iOS IPA 打包 (Capacitor)
> [!WARNING] 环境要求：开发iOS应用必须使用Mac设备。
### 1. 环境准备
- 通过Mac App Store安装Xcode开发工具
- 安装CocoaPods依赖管理工具：`brew install cocoapods`
- 克隆项目并创建新分支 `ios`
### 2. Capacitor 初始化
在项目终端依次执行以下命令：
```bash
npm install @capacitor/core @capacitor/cli --save-dev
npx cap init
npm run build
npm install @capacitor/ios
npx cap add ios
npx cap sync
```
### 3. 调试与运行
1.  打开iOS工程：执行 `npx cap open ios` 自动启动Xcode
2.  模拟器测试：点击左上角运行按钮在iOS模拟器中测试
3.  真机调试：连接iPhone设备，选择对应设备完成安装（免费证书有效期为7天）
4.  应用上架：需注册Apple Developer Program并通过App Store审核，本教程不展开具体流程。

---

## 五、安全提示
> [!WARNING] API Key 安全风险提示
> *   **风险**：将API Key直接存放在客户端代码（网页或APP）中存在极高的泄露风险。
> *   **最佳实践**：
>     1.  部署独立后端服务
>     2.  将API Key存储在后端环境变量中
>     3.  客户端仅请求后端接口，由后端代为调用AI API。

---

## 六、相关资源
![[AI_Mobile_App_Dev.base]]
