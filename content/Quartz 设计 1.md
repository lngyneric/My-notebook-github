
---
title: Quartz 设计方案
date: 2024-01-01
tags: ["设计", "Quartz"]
---

## 🤖 Assistant

太棒了！我们专注于**首页设计**。对于 Quartz 这种基于笔记的站点，将首页从“普通文章页”转变为“**探索仪表盘**”是提升用户体验的关键一步。

我为你构思了一个名为 **"The Knowledge Hub"（知识枢纽）** 的首页设计方案。这个设计的核心理念是将“被动阅读”转变为“主动探索”。

### 1. 设计概念：三栏式情报仪表盘

我们将屏幕分为三个主要视觉区域，布局响应式（移动端会自动垂直堆叠）：

#### **A. 顶部：Hero 区域（极简导向）**
* **视觉：** 去掉默认的巨大 Page Title，保留副标题。
* **元素：**
 * **欢迎语：** “Welcome to my Digital Garden”（或你的自定义语）。
 * **超级搜索框：** 不是那个小图标，而是一个显眼的、带有淡色背景的大输入框占位符，提示文字 “Type `k` to search...”。这是用户的直接入口。

#### **B. 主体：三列卡片网格 (核心交互区)**
我们将内容分为三个逻辑块，帮助用户不同维度地获取信息：

1. **左侧：Freshly Inked (最近更新)**
 * **功能：** 展示最近修改的 3-5 篇笔记。
 * **UI 细节：**不仅显示链接，还在右侧显示一个小小的“时间戳”图标（如 `2d ago`）。
 * **UX 目的：** 吸引老用户回访，查看动态。

2. **中间：The Core (核心领域/文件夹)**
 * **功能：** 手动挑选你最重要的 3 个分类（例如：开发笔记、读书感悟、生活随笔）。
 * **UI 细节：** 使用大卡片，配上图标。每个卡片显示该分类下的文章数量 badge（如 `12 notes`）。
 * **UX 目的：** 帮助新用户快速建立知识结构的认知。

3. **右侧：Serendipity (随机发现/图谱)**
 * **功能：** 一个小型的最近文章列表，或者嵌入一个缩小版的 Graph View。
 * **UX 目的：** Quartz 的魅力在于连接。在这里展示图谱或“随机一篇”，鼓励非线性浏览。

#### **C. 底部：Footer 简化版**
* 保留版权，增加简单的社交链接。

---

### 2. 实施指南：如何在 Quartz V4 中实现这个设计

Quartz V4 是高度组件化的，要实现上述设计，不需要去修改核心引擎，我们只需要**创建一个自定义组件**并在 `content/index.md` 中调用它。

#### **第一步：创建自定义组件 `Quartz/components/Dashboard.tsx`**

在你的 Quartz 项目文件夹中，创建这个文件。我会给你提供一个**代码骨架**，你可以基于此修改。

```tsx
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import style from "./styles/dashboard.scss"
// 如果你想获取所有文件数据来生成“最近更新”，需要解析 fullSlug
// 这里为了演示，我们主要展示结构

const Dashboard: QuartzComponent = ({ fileData, displayClass }: QuartzComponentProps) => {
  return (
    <div class="dashboard-container">
      
      {/* Hero Section */}
      <div class="dashboard-hero">
        <h1>欢迎来到我的笔记本</h1>
        <p>探索思想的连接 · 记录成长的轨迹</p>
        <div class="search-trigger">
          <span>⌘K 开始搜索...</span>
        </div>
      </div>

      {/* Grid Section */}
      <div class="dashboard-grid">
        
        {/* Column 1: Updates (你可以预留位置，或者硬编码链接） */}
        <div class="dashboard-card recent">
          <h3>最近更新</h3>
          <ul>
            <li><a href="/posts/design-systems">设计系统思维</a> <span class="date">刚刚</span></li>
            <li><a href="/posts/react-hooks">React Hooks 深度解析</a> <span class="date">2天前</span></li>
            <li><a href="/notes/reading-list">2023 阅读清单</a> <span class="date">1周前</span></li>
          </ul>
        </div>

        {/* Column 2: Categories */}
        <div class="dashboard-card categories">
          <h3>探索领域</h3>
          <div class="category-grid">
            <a href="/category/tech" class="cat-item">
              <span>💻 技术栈</span>
            </a>
            <a href="/category/product" class="cat-item">
              <span>📈 产品思维</span>
            </a>
            <a href="/category/essay" class="cat-item">
              <span>✍️ 随笔</span>
            </a>
          </div>
        </div>

        {/* Column 3: Graph / Random */}
        <div class="dashboard-card graph">
          <h3>知识图谱</h3>
          <p class="hint">点击下方查看全貌</p>
          {/* 这里可以放 graph 组件的引用，或者直接放一个链接 */}
          <a href="/m/graph" class="btn-outline">查看全站图谱</a>
        </div>

      </div>
    </div>
  )
}

// 默认导出，并在之后注册
export default (() => Dashboard) as QuartzComponentConstructor
```

#### **第二步：添加样式 `Quartz/components/styles/dashboard.scss`**

设计感来源于 CSS。我们需要让布局看起来像一个现代的 Dashboard，而不是传统的 Markdown 列表。

```scss
.dashboard-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1rem;

  .dashboard-hero {
    text-align: center;
    margin-bottom: 3rem;
    animation: fadeIn 0.8s ease-out;

    h1 {
      font-size: 2.5rem;
      margin-bottom: 0.5rem;
      background: linear-gradient(135deg, var(--secondary) 0%, var(--primary) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    
    .search-trigger {
      display: inline-block;
      margin-top: 1rem;
      padding: 0.5rem 1rem;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      color: var(--gray);
      font-size: 0.9rem;
      cursor: pointer;
      transition: all 0.2s;
      box-shadow: 0 2px 5px rgba(0,0,0,0.05);

      &:hover {
        border-color: var(--primary);
        color: var(--primary);
      }
    }
  }

  .dashboard-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    
    .dashboard-card {
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.5rem;
      transition: transform 0.2s, box-shadow 0.2s;

      &:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        border-color: var(--primary);
      }

      h3 {
        margin-top: 0;
        border-bottom: 2px solid var(--border);
        padding-bottom: 0.5rem;
        margin-bottom: 1rem;
        font-size: 1.2rem;
        color: var(--dark);
      }

      // Styling for the "Recent" list
      ul {
        list-style: none;
        padding: 0;
        li {
          margin-bottom: 0.8rem;
          display: flex;
          justify-content: space-between;
          align-items: center;
          a {
            text-decoration: none;
            color: var(--text);
            font-weight: 500;
            &:hover { color: var(--primary); }
          }
          .date {
            font-size: 0.8rem;
            color: var(--gray);
            background: var(--highlight);
            padding: 2px 6px;
            border-radius: 4px;
          }
        }
      }

      // Styling for "Categories" grid
      .category-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.5rem;
        .cat-item {
          display: block;
          text-align: center;
          padding: 0.8rem;
          background: var(--secondary);
          color: white;
          border-radius: 8px;
          text-decoration: none;
          font-size: 0.9rem;
          &:hover { opacity: 0.9; }
        }
      }
    }
  }
}
```

#### **第三步：在 `content/index.md` 中调用**

你不需要写长长的 Markdown 文章了，把你的 `content/index.md` 内容清空，放入：

```markdown
---
title: Home
---

<Dashboard />
```

---

### 3. UX/UI 专家反馈与优化建议

* **视觉层级：** 注意我在 CSS 中使用了 `box-shadow` 和 `hover` 效果。这能让用户潜意识里知道“这些都是可点击的”。
* **关于数据的获取：**
 * 上述代码中“最近更新”是手动写的。如果你希望能**自动获取**最近 3 篇文章，你需要利用 Quartz 的 `DataServer` API。
 * *高级技巧：* 你可以修改 `quartz/plugins/emitters/contentPage.tsx` 或者利用 `getResources` 函数（在组件构造函数中）来读取文件列表，然后按 `frontmatter.date` 排序。如果这对你来说太复杂，目前的“手动精选 3 篇”其实也是一种很好的策展方式。
* **响应式检查：** 请务必在手机上查看。我使用了 `grid-template-columns: repeat(auto-fit, minmax(300px, 1fr))`，这能确保在手机窄屏上，三个卡片会自动变成竖向排列，无需手动写复杂的媒体查询。

**下一步：**

如果你喜欢这个设计，你需要：
1. 在你的本地 Quartz 目录中创建 `.tsx` 和 `.scss` 文件。
2. 按照 Quartz 文档注册这个新组件（修改 `quartz/components.ts`）。
3. 运行 `npx quartz build` 并在本地预览。

你要我提供如何“**注册组件**”的具体步骤吗？或者你想对卡片的内容做些调整？
