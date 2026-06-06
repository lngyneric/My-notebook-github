---
source: raw/04_技能与工具/Claude_Skill/claude_skill_automation_guide.md
raw_sha256: 5170a15838bfeec2e6f21cbf6006ce50e2c28ac35959a1e592177e442764c2a2
compiled_at: 2026-04-14T16:47:17.600Z
---
# Claude Agent Skills 自动化“万能公式”操作指南
本指南基于「人人可用的自动化」理念，介绍如何通过简单步骤将任何Web操作转化为Claude AI可调用的技能，实现Web操作自动化。

## 核心公式
> 浏览器 F12 (Copy cURL) + Skill Creator = 全自动生成 AI Skill

## 关键实操步骤
### 第一步：获取数据源（无需API文档）
仅需通过浏览器即可获取所需的请求信息，无需后端提供API文档：
1. 在Chrome浏览器打开需要自动化的目标网页
2. 按F12或右键选择「检查」开启开发者工具，切换到Network（网络）标签页
3. 在网页上触发一次需要自动化的目标操作
4. 在Network列表找到对应请求（通常为Fetch/XHR类型），右键选择「Copy」→「Copy as cURL (bash)」复制请求

### 第二步：自动化生成Skill
利用Skill Creator（技能生成器）将cURL命令转化为标准的Skill结构：
1. 在Claude/Trae中调用Skill Creator，声明创建新技能
2. 输入指令：`请帮我创建一个名为 [技能名称] 的 Skill。核心逻辑是以下 cURL 命令，请将其封装为 Python 脚本，并生成对应的 SKILL.md`
3. 粘贴第一步复制的cURL内容，等待AI自动处理
4. AI会自动分析请求头、参数、请求体，生成包含`SKILL.md`和`script.py`的完整技能文件夹

### 第三步：安装与使用
1. 将生成的技能文件夹放入`.trae/skills/`目录完成部署
2. 直接通过自然语言调用AI，AI会自动匹配生成的Skill，运行脚本并返回结果

## 标准Skill结构
| 文件 | 类型 | 核心作用 |
| :--- | :--- | :--- |
| `SKILL.md` | 核心说明书 | YAML头定义技能名称和触发条件，供AI识别技能；正文说明AI何时、如何使用该技能 |
| `script.py` | 执行脚本 | 包含由cURL转换而来的具体API调用逻辑，处理数据请求与响应 |

## 进阶技巧
1. **参数化**：生成技能时要求AI将cURL中的固定值提取为Python脚本的输入参数，让技能支持通用场景
2. **错误处理**：要求AI在脚本中增加对HTTP 4xx、5xx错误码的处理逻辑，提升技能稳定性
3. **组合使用**：可生成多个细分小技能，通过自然语言让AI将多个技能串联完成复杂工作流
