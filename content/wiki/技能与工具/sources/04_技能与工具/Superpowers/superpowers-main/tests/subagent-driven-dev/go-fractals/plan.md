---
source: raw/04_技能与工具/Superpowers/superpowers-main/tests/subagent-driven-dev/go-fractals/plan.md
raw_sha256: 4aeba93884c280be622de3a08402baf08172fcf77c45e09ebd51392099722344
compiled_at: 2026-04-15T00:38:11.910Z
---
# Go Fractals CLI 实现计划
Go Fractals CLI 是一个基于 Go 语言开发、用于生成 ASCII 分形图案的命令行工具，本页面记录了该工具的分步实现计划。

## 摘要
本计划基于 `superpowers:subagent-driven-development` 技能推进，将 Go Fractals CLI 的开发拆解为10个顺序执行的任务，覆盖项目初始化、框架搭建、核心算法实现、命令行集成、功能完善、测试验证和文档编写全流程，每个任务都明确了开发要求与验证标准。

## 上下文
项目目标为构建可生成ASCII分形的命令行工具，完整规格定义参考 `design.md` 文件，开发使用Go语言，基于Cobra框架实现CLI结构。

## 任务列表与要求
### Task 1：项目初始化
- **开发要求**：
  1. 初始化Go模块，模块名为 `github.com/superpowers-test/fractals`
  2. 创建目录结构：`cmd/fractals/`、`internal/sierpinski/`、`internal/mandelbrot/`、`internal/cli/`
  3. 创建最简 `cmd/fractals/main.go`，输出内容`fractals cli`
  4. 添加 `github.com/spf13/cobra` 依赖
- **验证标准**：`go build ./cmd/fractals` 构建成功，运行 `./fractals` 输出`fractals cli`

### Task 2：带帮助功能的CLI框架
- **开发要求**：
  1. 在 `internal/cli/root.go` 中创建根命令
  2. 配置帮助文本，展示所有可用子命令
  3. 将根命令接入 `main.go`
- **验证标准**：`./fractals --help` 显示用法，列出`sierpinski`和`mandelbrot`两个可用命令；无参数运行`./fractals`默认显示帮助

### Task 3：谢尔宾斯基三角形算法实现
- **开发要求**：
  1. 创建 `internal/sierpinski/sierpinski.go`
  2. 实现 `Generate(size, depth int, char rune) []string` 方法，返回三角形的所有行文本
  3. 使用递归中点细分算法实现
  4. 创建 `internal/sierpinski/sierpinski_test.go`，添加测试用例：尺寸4深度2的小三角形匹配预期输出；尺寸1返回单个字符；深度0返回实心三角形
- **验证标准**：`go test ./internal/sierpinski/...` 所有测试通过

### Task 4：谢尔宾斯基功能CLI集成
- **开发要求**：
  1. 在 `internal/cli/sierpinski.go` 中创建`sierpinski`子命令
  2. 添加参数标记：`--size`（默认值32）、`--depth`（默认值5）、`--char`（默认值`*`）
  3. 调用`Generate`方法生成结果并输出到标准输出
- **验证标准**：`./fractals sierpinski` 可输出三角形；指定`--size 16 --depth 3`可输出更小三角形；`./fractals sierpinski --help`显示参数文档

### Task 5：曼德博集合算法实现
- **开发要求**：
  1. 创建 `internal/mandelbrot/mandelbrot.go`
  2. 实现 `Render(width, height, maxIter int, char string) []string` 方法
  3. 将复平面区域（实轴-2.5到1.0、虚轴-1.0到1.0）映射到输出尺寸
  4. 将迭代次数映射到字符梯度`" .:-=+*#%@"`，指定字符时使用单个字符渲染
  5. 创建 `internal/mandelbrot/mandelbrot_test.go`，添加测试用例：输出尺寸匹配请求的宽高；集合内已知点(0,0)映射到最大迭代对应字符；集合外已知点(2,0)映射到低迭代对应字符
- **验证标准**：`go test ./internal/mandelbrot/...` 所有测试通过

### Task 6：曼德博集合功能CLI集成
- **开发要求**：
  1. 在 `internal/cli/mandelbrot.go` 中创建`mandelbrot`子命令
  2. 添加参数标记：`--width`（默认80）、`--height`（默认24）、`--iterations`（默认100）、`--char`（默认空字符串）
  3. 调用`Render`方法生成结果并输出到标准输出
- **验证标准**：`./fractals mandelbrot`可输出可识别的曼德博集合；指定`--width 40 --height 12`可输出更小版本；`./fractals mandelbrot --help`显示参数文档

### Task 7：字符配置统一化
- **开发要求**：
  1. 验证谢尔宾斯基命令的`--char`参数可正确将字符传入算法
  2. 曼德博集合命令的`--char`指定字符时，使用单个字符替代梯度字符渲染
  3. 添加自定义字符输出的测试用例
- **验证标准**：`./fractals sierpinski --char '#'` 使用`#`字符渲染；`./fractals mandelbrot --char '.'`对所有填充点使用`.`；所有测试通过

### Task 8：输入验证与错误处理
- **开发要求**：
  1. 谢尔宾斯基命令：要求`size > 0`、`depth >= 0`
  2. 曼德博集合命令：要求`width/height > 0`、`iterations > 0`
  3. 对非法输入返回清晰的错误信息
  4. 添加错误场景的测试用例
- **验证标准**：`./fractals sierpinski --size 0`打印错误并以非零状态退出；`./fractals mandelbrot --width -1`打印错误并以非零状态退出；错误信息清晰有用

### Task 9：集成测试
- **开发要求**：
  1. 创建`cmd/fractals/main_test.go`或`test/integration_test.go`
  2. 添加两个命令的完整CLI调用测试
  3. 验证输出格式和退出码
  4. 验证错误场景返回非零退出码
- **验证标准**：`go test ./...` 运行所有测试（包含集成测试）全部通过

### Task 10：编写README文档
- **开发要求**：创建`README.md`，包含：项目描述、安装方式`go install ./cmd/fractals`、两个命令的使用示例、小样例输出
- **验证标准**：README准确描述工具、文档中的示例可正常运行

## 执行要求
本计划需要使用`superpowers:subagent-driven-development`技能执行。
