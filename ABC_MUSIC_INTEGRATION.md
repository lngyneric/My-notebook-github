# ABC音乐记谱集成指南

本文档介绍如何在Quartz项目中使用ABC音乐记谱功能。

## 功能概述

本集成方案为Quartz静态网站生成器添加了ABC音乐记谱支持，允许您在Markdown文件中直接编写ABC记谱法，并自动渲染为可视化的乐谱和可播放的音频。

## 已集成的组件

### 1. AbcMusic组件 (`quartz/components/AbcMusic.tsx`)
- 自动检测并渲染页面中的`music-abc`代码块
- 使用abcjs库生成SVG乐谱
- 提供音频播放控件
- 支持响应式设计和暗黑模式

### 2. AbcMusicTransformer (`quartz/plugins/transformers/abcmusic.ts`)
- 在构建时处理`music-abc`代码块
- 将ABC记谱代码转换为特殊的HTML容器
- 与AbcMusic组件配合工作

### 3. 样式文件 (`quartz/styles/abcmusic.scss`)
- 专门为ABC音乐记谱设计的CSS样式
- 包含乐谱容器、音频控件、加载状态等样式
- 支持暗黑模式和响应式设计

## 使用方法

### 基本语法

在Markdown文件中使用以下语法来添加ABC音乐记谱：

````markdown
```music-abc
X:1
T:曲名
M:4/4
L:1/4
K:C
C D E F | G A B c |
```
````

### 完整示例

````markdown
```music-abc
X:1
T:The Legacy Jig
M:6/8
L:1/8
R:jig
K:G
GFG BAB | gfg gab | GFG BAB | d2A AFD |
GFG BAB | gfg gab | age edB |1 dBA AFD :|2 dBA ABd |:
efe edB | dBA ABd | efe edB | gdB ABd |
efe edB | d2d def | gfe edB |1 dBA ABd :|2 dBA AFD |]
```
````

### ABC记谱法基础

- `X:` - 曲目编号
- `T:` - 曲名
- `M:` - 拍号 (如 4/4, 3/4, 6/8)
- `L:` - 默认音符长度
- `R:` - 节奏类型 (如 jig, reel, waltz)
- `K:` - 调号 (如 C, G, D, Am, Em)

音符表示：
- `C D E F G A B` - 基本音符
- `c d e f g a b` - 高八度音符
- `C, D, E,` - 低八度音符
- `C2` - 二分音符
- `C/2` - 八分音符
- `|` - 小节线
- `:|` - 重复结束
- `|:` - 重复开始

## 项目配置

### 1. 依赖项

项目已自动安装以下依赖：
- `abcjs`: ABC音乐记谱渲染库

### 2. 配置文件更新

以下文件已自动配置：

#### `quartz.config.ts`
```typescript
plugins: {
  transformers: [
    // ... 其他transformers
    Plugin.AbcMusicTransformer(),
  ],
  // ...
}
```

#### `quartz/components/index.ts`
```typescript
export { AbcMusic } from "./AbcMusic"
```

#### `quartz/components/pages/Content.tsx`
```typescript
import { AbcMusic } from "../AbcMusic"

// 在组件中包含
<AbcMusic {...props} />
```

#### `quartz/styles/custom.scss`
```scss
@use "./abcmusic.scss";
```

## 部署说明

### 1. 构建项目

```bash
npx quartz build
```

### 2. 本地预览

由于Quartz没有内置的开发服务器，可以使用以下方法之一进行本地预览：

#### 方法1：使用项目提供的服务器
```bash
node server.cjs
```
然后访问 `http://localhost:8080`

#### 方法2：使用其他HTTP服务器
```bash
# 使用Python
python -m http.server 8080 --directory public

# 使用Node.js http-server
npx http-server public -p 8080

# 使用PHP
php -S localhost:8080 -t public
```

### 3. 生产部署

构建完成后，`public`目录包含所有静态文件，可以部署到任何静态网站托管服务：

- **Vercel**: 直接连接GitHub仓库自动部署
- **Netlify**: 拖拽`public`文件夹或连接Git仓库
- **GitHub Pages**: 将`public`内容推送到`gh-pages`分支
- **传统服务器**: 将`public`目录内容上传到web根目录

## 功能特性

### 1. 自动渲染
- 页面加载时自动检测并渲染所有`music-abc`代码块
- 无需手动初始化或额外配置

### 2. 音频播放
- 每个乐谱都包含播放控件
- 支持播放、暂停、停止功能
- 音频基于MIDI合成

### 3. 响应式设计
- 乐谱在不同屏幕尺寸下自适应
- 移动设备友好

### 4. 主题支持
- 自动适配网站的明暗主题
- 乐谱颜色随主题变化

### 5. 错误处理
- 无效的ABC代码会显示错误信息
- 不会影响页面其他内容的正常显示

## 故障排除

### 1. 乐谱不显示
- 检查ABC语法是否正确
- 确认代码块使用`music-abc`标识符
- 查看浏览器控制台是否有错误信息

### 2. 音频无法播放
- 确认浏览器支持Web Audio API
- 检查是否有浏览器安全策略阻止音频播放
- 某些浏览器需要用户交互后才能播放音频

### 3. 样式问题
- 确认`abcmusic.scss`已正确导入
- 检查是否有CSS冲突
- 验证构建过程是否包含了样式文件

## 扩展和自定义

### 1. 修改样式
编辑`quartz/styles/abcmusic.scss`文件来自定义乐谱外观。

### 2. 调整渲染选项
在`quartz/components/AbcMusic.tsx`中修改abcjs的渲染参数：

```typescript
const renderOptions = {
  responsive: "resize",
  staffwidth: 740,
  scale: 1.0,
  // 添加更多选项
};
```

### 3. 添加更多功能
可以扩展组件以支持：
- MIDI文件导出
- 乐谱图片下载
- 更多音频选项
- 自定义播放控件

## 参考资源

- [ABC记谱法标准](http://abcnotation.com/)
- [abcjs库文档](https://paulrosen.github.io/abcjs/)
- [Quartz文档](https://quartz.jzhao.xyz/)
- [ABC记谱法教程](http://abcnotation.com/learn)

## 许可证

本集成方案遵循项目原有许可证。abcjs库使用MIT许可证。