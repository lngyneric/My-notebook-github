---
source: raw/05_代码与项目/skills/skills/skills/webapp-testing/SKILL.md
raw_sha256: 51b7349e77ec63b7744a6f63647e7566a0b4d2e301121cc10e8c2113af6556a2
compiled_at: 2026-04-14T05:17:39.317Z
---
# Web Application Testing (webapp-testing)
> 基于 Playwright 的本地 Web 应用交互与测试工具包

---

## TL;DR
webapp-testing 是一套基于 Python Playwright 的本地 Web 应用测试工具集，支持前端功能验证、UI 行为调试、浏览器截图和日志获取；提供了开箱即用的服务生命周期管理脚本，建议将内置脚本作为黑盒调用，优先通过 `--help` 获取使用方法，不建议直接读取源码污染上下文窗口。

## 要点
1. **核心能力**：支持前端功能验证、UI 行为调试、浏览器截图、浏览器日志获取，基于原生 Python Playwright 编写测试脚本
2. **内置工具**：提供 `scripts/with_server.py` 支持单/多服务的自动生命周期管理，适配前后端分离架构的本地测试场景
3. **选型决策树**：
   - 静态 HTML → 直接读取识别选择器 → 成功则写 Playwright 脚本；失败则按动态应用处理
   - 动态应用 → 服务未运行 → 使用 `with_server.py` 辅助 + 简化 Playwright 脚本
   - 动态应用 → 服务已运行 → 遵循「侦察-行动」模式：等待网络空闲 → 截图/DOM检查 → 识别选择器 → 执行操作
4. **核心规范**：
   - 动态应用必须等待 `networkidle` 后再操作 DOM
   - Playwright 脚本默认使用无头模式启动 Chromium
   - 内置脚本作为黑盒调用，优先看 `--help`，必要时再读源码
5. **最佳实践**：使用同步 API、用完关闭浏览器、优先使用语义化选择器、添加必要等待

---

## 引用证据片段
> 原始描述
> ```
> Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.
> ```

> 使用原则
> ```
> **Always run scripts with `--help` first** to see usage. DO NOT read the source until you try running the script first and find that a customized solution is abslutely necessary. These scripts can be very large and thus pollute your context window. They exist to be called directly as black-box scripts rather than ingested into your context window.
> ```

> 决策树
> ```
> User task → Is it static HTML?
>     ├─ Yes → Read HTML file directly to identify selectors
>     │         ├─ Success → Write Playwright script using selectors
>     │         └─ Fails/Incomplete → Treat as dynamic (below)
>     │
>     └─ No (dynamic webapp) → Is the server already running?
>         ├─ No → Run: python scripts/with_server.py --help
>         │        Then use the helper + write simplified Playwright script
>         │
>         └─ Yes → Reconnaissance-then-action:
>             1. Navigate and wait for networkidle
>             2. Take screenshot or inspect DOM
>             3. Identify selectors from rendered state
>             4. Execute actions with discovered selectors
> ```

> with_server.py 单服务调用示例
> ```bash
> python scripts/with_server.py --server "npm run dev" --port 5173 -- python your_automation.py
> ```

> with_server.py 多服务调用示例
> ```bash
> python scripts/with_server.py \
>   --server "cd backend && python server.py" --port 3000 \
>   --server "cd frontend && npm run dev" --port 5173 \
>   -- python your_automation.py
> ```

> 基础自动化脚本模板
> ```python
> from playwright.sync_api import sync_playwright
> 
> with sync_playwright() as p:
>     browser = p.chromium.launch(headless=True) # Always launch chromium in headless mode
>     page = browser.new_page()
>     page.goto('http://localhost:5173') # Server already running and ready
>     page.wait_for_load_state('networkidle') # CRITICAL: Wait for JS to execute
>     # ... your automation logic
>     browser.close()
> ```
> 常见陷阱
> ```
> ❌ **Don't** inspect the DOM before waiting for `networkidle` on dynamic apps
> ✅ **Do** wait for `page.wait_for_load_state('networkidle')` before inspection
> ```

## 参考文件
| 文件路径 | 说明 |
|---------|------|
| `LICENSE.txt` | 完整授权条款 |
| `examples/element_discovery.py` | 页面按钮、链接、输入框识别示例 |
| `examples/static_html_automation.py` | 本地静态HTML通过`file://`协议测试示例 |
| `examples/console_logging.py` | 自动化过程中捕获浏览器控制台日志示例 |

## 冲突标注
暂无已知冲突。
