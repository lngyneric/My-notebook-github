---
source: raw/05_代码与项目/skills/skills/skills/algorithmic-art/SKILL.md
raw_sha256: 3bc4092c09804853186524c826bc0621b940bb6122c05b84496dff95388e6eef
compiled_at: 2026-04-14T05:04:05.915Z
---
# algorithmic-art

> [!INFO] 来源路径
> `raw/05_代码与项目/skills/skills/skills/algorithmic-art/SKILL.md`

---

## TL;DR
本技能定义了使用 p5.js 创建原创生成式算法艺术的标准流程，要求分两步输出：先创作算法艺术哲学文档，再基于哲学实现可交互、带种子随机控制的单文件自包含 HTML 作品，要求保证可复现性、专业工匠级细节与原创性，避免版权问题。

---

## 核心要点
### 基本信息
| 属性 | 内容 |
|------|------|
| 名称 | `algorithmic-art` |
| 使用场景 | 用户请求代码创作艺术、生成艺术、算法艺术、流场、粒子系统时使用 |
| 许可协议 | 完整条款见 `LICENSE.txt` |
| 核心要求 | 必须创作原创算法艺术，禁止复制现有艺术家作品以避免版权侵权 |

### 创作流程
创作分为两个固定阶段：
1. 算法哲学创作（输出 `.md` 文件）
2. p5.js 生成艺术实现（输出 `.html` + 内嵌 `.js` 代码）

---

### 第一阶段：算法哲学创作
#### 核心定义
算法哲学是通过代码表达的计算美学运动，核心围绕以下主题：
- 计算过程、涌现行为、数学之美
- 种子随机、噪声场、有机系统
- 粒子、流、场、力
- 参数变异与受控混沌

#### 创作要求
1. 先提取用户需求中的微妙概念线索：将其作为创作基础，不限制创作自由
2. 输出结构：
   - **运动命名**：1-2个词，例如 `Organic Turbulence`、`Quantum Harmonics`
   - **哲学阐述**：4-6个完整段落，需覆盖以下维度：
     - 计算过程与数学关系
     - 噪声函数与随机模式
     - 粒子行为与场动力学
     - 时间演化与系统状态
     - 参数变异与涌现复杂度
3. 关键规范：
   - 避免冗余：每个算法概念仅提及一次，除非增加新深度
   - **必须反复强调工匠级精度**：需要多次提及「精心 crafted 的算法」「深度计算专业能力的产物」「精心优化」「大师级实现」这类表述
   - 预留创作空间：明确算法方向，但为后续代码实现保留解读空间
   - 核心强调：美存在于算法过程，而非最终帧

#### 必要原则
| 原则 | 说明 |
|------|------|
| 算法哲学 | 创造一个可通过代码表达的计算世界观 |
| 过程优先于结果 | 始终强调美来自算法执行，每次运行都是独特的 |
| 参数化表达 | 思想通过数学关系、力、行为传递，而非静态构图 |
| 艺术自由 | 为代码实现阶段保留创意实现空间 |
| 纯生成艺术 | 创作活的算法，而非带随机性的静态图像 |
| 专业工匠技艺 | 反复强调最终算法必须是精心设计、经无数次迭代优化、由顶级计算美学专家产出的 |

---

### 第二阶段：p5.js 实现
#### 前置要求
1. **必须先读取 `templates/viewer.html` 模板**，以该模板为起点创作，不能从零编写 HTML
2. 保留模板所有固定部分：布局结构、Anthropic 品牌标识（颜色、字体）、侧边栏结构、种子控制、操作按钮
3. 仅替换模板标记的可变部分：p5.js 算法、参数定义、参数控制区 UI

#### 技术要求
1. **种子随机（遵循 Art Blocks 模式）**：必须始终使用种子保证可复现性，示例代码：
```javascript
let seed = 12345; // 可使用用户输入哈希生成
randomSeed(seed);
noiseSeed(seed);
```

2. **参数结构**：参数从算法哲学自然衍生，示例结构：
```javascript
let params = {
  seed: 12345,  // 始终包含种子保证可复现
  // 根据作品添加以下类型参数：
  // - 数量（多少个？）
  // - 尺度（多大？多快？）
  // - 概率（可能性？）
  // - 比例（比例关系？）
  // - 角度（方向？）
  // - 阈值（行为何时改变？）
};
```

3. **核心算法**：算法必须由算法哲学驱动，而非套用现有模式：
   - 有机涌现 → 使用累积生长、自然规则约束的随机过程、反馈循环
   - 数学之美 → 使用几何关系、三角谐波、精确计算生成意外模式
   - 受控混沌 → 使用严格边界内的随机变异、分岔相变、从无序中诞生有序

4. **画布标准结构**：
```javascript
function setup() {
  createCanvas(1200, 1200);
  // 初始化你的系统
}
function draw() {
  // 你的生成算法
  // 支持静态（noLoop）或动画
}
```

#### 工匠技艺要求
- 平衡：复杂度无视觉噪声，秩序无僵硬感
- 色彩和谐：使用经过思考的调色板，不使用随机 RGB 值
- 构图：即使随机也保持视觉层次与流动感
- 性能：如果是动画需要优化到流畅运行
- 可复现：相同种子始终产生完全相同的输出

---

### 交互作品输出规范
#### 固定与可变部分划分
| 分类 | 内容 |
|------|------|
| **固定（必须完全保留）** | 布局结构（头部、侧边栏、主画布区）、Anthropic 品牌（UI 颜色、字体、渐变）、侧边栏 Seed 区块、侧边栏 Actions 区块 |
| **可变（自定义）** | p5.js 完整算法、参数对象、参数控制区、色彩控制区（可选） |

#### 必须功能
1. **参数控制**：数值参数使用滑块、颜色使用取色器、参数变化实时更新、重置按钮恢复默认值
2. **种子导航**：显示当前种子、支持上一个/下一个种子循环、随机种子、跳转指定种子
3. **单文件结构**：除 p5.js CDN 外无外部依赖，所有代码样式全部内联，可直接在浏览器运行
4. **侧边栏固定结构**：
   1. Seed 区块（固定）
   2. Parameters 区块（可变）
   3. Colors 区块（可选，按需添加）
   4. Actions 区块（固定，包含重新生成、重置、下载 PNG 按钮）

---

### 变异探索
作品默认自带种子导航，允许用户探索不同变异；如果用户需要可在同一作品中添加种子预设、画廊模式等功能，同一算法不同种子会展现不同潜力。

---

## 引用证据片段
```markdown
---
name: algorithmic-art
description: Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems. Create original algorithmic art rather than copying existing artists' work to avoid copyright violations.
license: Complete terms in LICENSE.txt
---

Algorithmic philosophies are computational aesthetic movements that are then expressed through code. Output .md files (philosophy), .html files (interactive viewer), and .js files (generative algorithms).

This happens in two steps:
1. Algorithmic Philosophy Creation (.md file)
2. Express by creating p5.js generative art (.html + .js files)
```

> 原始核心要求片段
```
**CRITICAL: BEFORE writing any HTML:**
1. **Read** `templates/viewer.html` using the Read tool
2. **Study** the exact structure, styling, and Anthropic branding
3. **Use that file as the LITERAL STARTING POINT** - not just inspiration
4. **Keep all FIXED sections exactly as shown** (header, sidebar structure, Anthropic colors/fonts, seed controls, action buttons)
5. **Replace only the VARIABLE sections** marked in the file's comments (algorithm, parameters, UI controls for parameters)
```

> 工匠要求片段
```
**CRITICAL**: To achieve mastery, create algorithms that feel like they emerged through countless iterations by a master generative artist. Tune every parameter carefully. Ensure every pattern emerges with purpose. This is NOT random noise - this is CONTROLLED CHAOS refined through deep expertise.

- **Balance**: Complexity without visual noise, order without rigidity
- **Color Harmony**: Thoughtful palettes, not random RGB values
- **Composition**: Even in randomness, maintain visual hierarchy and flow
- **Performance**: Smooth execution, optimized for real-time if animated
- **Reprodu
