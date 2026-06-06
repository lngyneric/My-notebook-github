---
source: raw/05_代码与项目/NanoBanana-PPT-Skills-main/NanoBanana-PPT-Skills-main/QUICKSTART.md
raw_sha256: 6b834176555aa4e3883fc7e47aaa9fb7354279aeaaacfc1439611625374b31ff
compiled_at: 2026-04-24T08:30:05.602Z
---
# NanoBanana PPT生成工具快速使用指南

## 摘要
本指南为NanoBanana PPT生成工具的官方快速操作说明，覆盖环境配置、基础PPT生成流程、使用优化技巧、风格自定义、高级功能、问题排查全链路操作，支持用户在5分钟内完成基于Markdown文档的AI驱动PPT生成，输出可交互的HTML格式演示文件。

## 🚀 5分钟快速上手
### 步骤1: 设置API密钥
```bash
export GEMINI_API_KEY='your-google-ai-api-key'
```
**API密钥获取渠道**：访问 [Google AI Studio](https://makersuite.google.com/app/apikey) 申请。

### 步骤2: 安装依赖
```bash
pip install google-genai pillow
```

### 步骤3: 准备输入文档
创建或准备Markdown格式的内容文档（示例`my-document.md`）：
```markdown
# 我的演示主题

## 第一部分：背景
这里是背景介绍...

## 第二部分：核心观点
- 观点1：...
- 观点2：...
- 观点3：...

## 第三部分：总结
关键发现和行动建议...
```

### 步骤4: Claude Code集成生成
打开Claude Code，输入自然语言指令触发全流程生成：
```
我想基于 my-document.md 生成一个5页的PPT，使用渐变毛玻璃卡片风格，2K分辨率。
```
Claude将自动完成以下操作：
1. 分析输入文档内容
2. 规划指定页数的PPT内容结构
3. 生成符合风格要求的高质量配图
4. 创建可交互的HTML播放网页

### 步骤5: 查看与播放结果
生成的文件存储在`outputs/TIMESTAMP/`目录下，执行命令打开播放器：
```bash
open outputs/TIMESTAMP/index.html
```
**播放器键盘操作快捷键**：
- ← / → ：切换前后页面
- ESC ：切换全屏模式
- 空格 ：开启/关闭自动播放

## 💡 使用技巧
### 技巧1: 页数与演示场景匹配规则
| PPT页数 | 适用场景 | 演示时长 |
|--------|----------|----------|
| 5页 | 电梯演讲 | 5分钟 |
| 5-10页 | 标准演示 | 10-15分钟 |
| 10-15页 | 深入讲解 | 20-30分钟 |
| 20-25页 | 完整培训 | 45-60分钟 |

### 技巧2: 输入文档结构优化建议
✅ **推荐的结构化文档格式**：
```markdown
# 主标题

## 核心观点1
- 要点1
- 要点2
- 要点3

## 核心观点2
[详细说明内容...]

## 总结
[关键结论与行动建议...]
```

❌ **不推荐的文档格式**：
```markdown
# 标题
一大段没有分段、无层级的纯文字内容...
```

### 技巧3: 分辨率选择参考
| 用途场景 | 推荐分辨率 | 单页生成时间 | 单页文件大小 |
|------|------------|----------|----------|
| 日常演示 | 2K | ~30秒/页 | ~2MB/页 |
| 正式场合 | 2K | ~30秒/页 | ~2MB/页 |
| 打印输出 | 4K | ~60秒/页 | ~8MB/页 |
| 大屏展示 | 4K | ~60秒/页 | ~8MB/页 |

### 技巧4: 多版本批量生成
通过命令行指定不同参数生成多个版本PPT，示例：
```bash
# 生成5页精简版
python generate_ppt.py --plan plan_5.json --style styles/gradient-glass.md --resolution 2K --output outputs/v1-brief

# 生成15页详细版
python generate_ppt.py --plan plan_15.json --style styles/gradient-glass.md --resolution 2K --output outputs/v2-detailed
```

## 🎨 自定义风格配置
### 创建自定义风格流程
1. 复制现有风格模板作为基础：
```bash
cp styles/gradient-glass.md styles/my-style.md
```
2. 编辑风格定义文件，修改风格ID、提示词模板等内容：
```markdown
# 我的自定义风格

## 风格ID
my-custom-style

## 基础提示词模板
[修改为自定义的风格描述内容...]
```
3. 生成PPT时指定自定义风格文件：
```bash
python generate_ppt.py --plan plan.json --style styles/my-style.md
```

## 🔧 高级功能用法
### 手动调整生成提示词
1. 查看生成过程中使用的完整提示词：
```bash
cat outputs/TIMESTAMP/prompts.json
```
2. 复制并修改需要调整的提示词内容
3. 创建新的规划文件后重新执行生成脚本

### 混合页面类型配置
在JSON格式的PPT规划文件中自定义每页的类型，示例：
```json
{
  "slides": [
    {"page_type": "cover", "content": "..."},
    {"page_type": "content", "content": "..."},
    {"page_type": "data", "content": "..."},
    {"page_type": "content", "content": "..."}
  ]
}
```

### 并行生成多版本PPT
通过后台并行执行命令同时生成多个版本，提升效率：
```bash
python generate_ppt.py --plan plan1.json --style styles/gradient-glass.md --output outputs/v1 &
python generate_ppt.py --plan plan2.json --style styles/gradient-glass.md --output outputs/v2 &
wait
echo "所有版本生成完成！"
```

## 📋 常见问题
### Q: 生成失败如何排查？
A: 按以下顺序检查：
1. Gemini API密钥是否正确设置为环境变量
2. 网络连接是否正常可访问Google服务
3. Python依赖包`google-genai`与`pillow`是否完整安装
4. 查看运行输出的详细错误信息定位问题

### Q: 支持生成中文内容的PPT吗？
A: 支持，Nano Banana Pro工具原生支持多语言内容生成，包括中文。

### Q: PPT生成需要多长时间？
A: 生成速度与分辨率相关：
- 2K分辨率：约30秒/页，5页PPT约2.5-5分钟
- 4K分辨率：约60秒/页

### Q: 如何将生成的PPT导出为PDF？
A: 通过浏览器打印功能导出：
1. 打开生成的HTML播放器页面
2. 按下快捷键`Cmd+P`（Mac）或`Ctrl+P`（Windows）
3. 打印目标选择「另存为PDF」

### Q: 可以修改已生成的PPT内容吗？
A: 可以通过以下方式调整后重新生成：
1. 编辑JSON格式的PPT规划文件
2. 修改生成用的提示词内容
3. 重新运行生成脚本

### Q: 支持哪些格式的输入文档？
A: 目前对Markdown格式的支持最佳，也可使用纯文本文档作为输入。

## 📞 帮助渠道
遇到问题可通过以下渠道获取支持：
1. 查看项目根目录的`README.md`文档
2. 查看`ppt-generator.md`详细开发文档
3. 在Claude Code中输入`/help`获取辅助

## 🎯 最佳实践清单
✅ 输入文档使用清晰的标题层级与分段
✅ 单页PPT内容不超过3-5个核心要点
✅ 根据演示场景选择匹配的PPT页数
✅ 日常使用优先选择2K分辨率平衡速度与质量
✅ 保留原始JSON规划文件便于后续修改
✅ 定期检查Google Gemini API的配额使用情况
✅ 测试HTML播放器在不同浏览器的兼容性表现

---
**开始创作吧！** 🚀
