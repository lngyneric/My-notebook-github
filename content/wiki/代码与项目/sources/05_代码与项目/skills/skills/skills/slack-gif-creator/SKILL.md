---
source: raw/05_代码与项目/skills/skills/skills/slack-gif-creator/SKILL.md
raw_sha256: 2efca615ce55a3edd8fc05c779068a8085816617991987e446606403cd3abb22
compiled_at: 2026-04-14T05:10:18.394Z
---
# slack-gif-creator

> 来源路径：`raw/05_代码与项目/skills/skills/skills/slack-gif-creator/SKILL.md`
> 许可证：完整条款见 LICENSE.txt

## TL;DR
这是一个用于创建适配Slack的优化GIF的工具包与知识集合，提供了Slack GIF的规格约束、验证工具、动画实现思路和Python工具函数，适用于响应用户「制作用于Slack的X动画GIF」类需求。

---

## 要点
### Slack GIF 官方要求
| 用途          | 推荐尺寸  | 额外约束                 |
|---------------|-----------|--------------------------|
| Emoji GIF     | 128×128   | 时长保持在3秒以内         |
| 消息内GIF     | 480×480   | -                        |
通用参数要求：
- FPS：10~30（FPS越低文件体积越小）
- 颜色数：48~128（颜色越少文件体积越小）

### 核心工具组件
| 模块                 | 功能说明                     |
|----------------------|------------------------------|
| `core.gif_builder`   | 拼接帧并输出优化后的GIF      |
| `core.validators`    | 验证GIF是否符合Slack要求     |
| `core.easing`        | 提供缓动函数实现平滑动画运动 |
| `core.frame_composer`| 常用帧操作的便捷工具函数     |

### 设计原则
- 仅提供基础知识和工具，不提供预制模板、预制图形和Emoji字体渲染（跨平台不可靠）
- 用户上传图片时，根据用户需求选择直接使用或作为创意参考
- 鼓励创意组合不同动画效果，使用PIL全功能实现需求

---

## 详细内容

### 核心工作流 引用证据
```python
from core.gif_builder import GIFBuilder
from PIL import Image, ImageDraw

# 1. Create builder
builder = GIFBuilder(width=128, height=128, fps=10)

# 2. Generate frames
for i in range(12):
    frame = Image.new('RGB', (128, 128), (240, 248, 255))
    draw = ImageDraw.Draw(frame)

    # Draw your animation using PIL primitives
    # (circles, polygons, lines, etc.)

    builder.add_frame(frame)

# 3. Save with optimization
builder.save('output.gif', num_colors=48, optimize_for_emoji=True)
```

### 图形绘制
#### 处理用户上传图片 引用证据
如果用户上传了图片，根据需求区分两种场景：
- **直接使用**：例如需求为「将这个做成动画」「把这个拆分成帧」
- **作为灵感参考**：例如需求为「做一个和这个类似的」

使用PIL加载处理图片：
```python
from PIL import Image

uploaded = Image.open('file.png')
# Use directly, or just as reference for colors/style
```

#### 从零绘制图形 引用证据
使用PIL `ImageDraw` 基础绘图原语：
```python
from PIL import ImageDraw

draw = ImageDraw.Draw(frame)

# Circles/ovals
draw.ellipse([x1, y1, x2, y2], fill=(r, g, b), outline=(r, g, b), width=3)

# Stars, triangles, any polygon
points = [(x1, y1), (x2, y2), (x3, y3), ...]
draw.polygon(points, fill=(r, g, b), outline=(r, g, b), width=3)

# Lines
draw.line([(x1, y1), (x2, y2)], fill=(r, g, b), width=5)

# Rectangles
draw.rectangle([x1, y1, x2, y2], fill=(r, g, b), outline=(r, g, b), width=3)
```

> [!WARNING] 禁忌
> 不要使用Emoji字体（跨平台不可靠），不要默认本技能内置预制图形。

#### 图形美化指南 引用证据
1. **使用更粗的线条**：描边和线条始终设置`width=2`或更粗，1px细线看起来粗糙业余
2. **增加视觉层次**：
   - 使用渐变背景（调用`create_gradient_background`）
   - 多层形状叠加增加复杂度（例如大星星内部叠小星星）
3. **让形状更生动**：
   - 不要只画纯色圆形，可增加高光、环或纹理
   - 星星可以增加外发光（在后方绘制更大的半透明形状）
   - 组合多个形状（星星+闪片、圆形+环）
4. **颜色注意事项**：
   - 使用鲜艳的互补色
   - 增加对比度（浅色形状用深色描边，深色形状用浅色描边）
   - 关注整体构图
5. **复杂形状（心形、雪花等）**：
   - 使用多边形和椭圆组合绘制
   - 仔细计算点保证对称
   - 增加细节（心形可以加高光曲线，雪花可以增加精细分支）

### 可用工具 引用证据
#### GIFBuilder (`core.gif_builder`)
拼接帧并输出适配Slack的优化GIF：
```python
builder = GIFBuilder(width=128, height=128, fps=10)
builder.add_frame(frame)  # Add PIL Image
builder.add_frames(frames)  # Add list of frames
builder.save('out.gif', num_colors=48, optimize_for_emoji=True, remove_duplicates=True)
```

#### Validators (`core.validators`)
检查GIF是否符合Slack要求：
```python
from core.validators import validate_gif, is_slack_ready

# Detailed validation
passes, info = validate_gif('my.gif', is_emoji=True, verbose=True)

# Quick check
if is_slack_ready('my.gif'):
    print("Ready!")
```

#### Easing Functions (`core.easing`)
实现平滑运动替代线性运动：
```python
from core.easing import interpolate

# Progress from 0.0 to 1.0
t = i / (num_frames - 1)

# Apply easing
y = interpolate(start=0, end=400, t=t, easing='ease_out')

# Available: linear, ease_in, ease_out, ease_in_out,
#           bounce_out, elastic_out, back_out
```

#### Frame Helpers (`core.frame_composer`)
常用需求的便捷函数：
```python
from core.frame_composer import (
    create_blank_frame,         # Solid color background
    create_gradient_background,  # Vertical gradient
    draw_circle,                # Helper for circles
    draw_text,                  # Simple text rendering
    draw_star                   # 5-pointed star
)
```

### 常见动画实现思路 引用证据
#### 抖动/振动
- 使用帧索引结合`math.sin()`或`math.cos()`计算位置偏移
- 增加微小随机变化让效果更自然
- 可同时应用在x轴和/或y轴位置

#### 脉冲/心跳
- 有节奏的缩放物体大小
- 使用`math.sin(t * frequency * 2 * math.pi)`实现平滑脉冲
- 心跳效果：两次快速脉冲后暂停（调整正弦波形即可）
- 大小在基础尺寸的0.8~1.2倍之间变化

#### 弹跳
- 物体下落并反弹
- 落地使用`interpolate()`搭配`easing='bounce_out'`
- 下落（加速）使用`easing='ease_in'`
- 每帧增加y方向速度模拟重力

#### 旋转
- 绕中心旋转物体
- PIL实现：`image.rotate(angle, resample=Image.BICUBIC)`
- 摇摆效果：使用正弦波计算角度替代线性递增

#### 淡入/淡出
- 逐渐出现或消失
- 创建RGBA图像，调整alpha通道
- 或使用`Image.blend(image1, image2, alpha)`
- 淡入：alpha从0到1；淡出：alpha从1到0

#### 滑动
- 物体从屏外移动到目标位置
- 起始位置：帧边界外；结束位置：目标位置
- 使用`interpolate()`搭配`easing='ease_out'`实现平滑停止
-  Overshoot 效果：使用`easing='back_out'`

#### 缩放
- 缩放和位置调整实现变焦效果
- 放大：从0.1倍缩放到2.0倍，裁剪中心区域
- 缩小：从2.0倍缩放到1.0倍
- 可增加运动
