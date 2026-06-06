---
source: raw/04_技能与工具/Superpowers/superpowers-main/tests/subagent-driven-dev/go-fractals/design.md
raw_sha256: a78c95627d801c1b3e1cad71c13dc56de2fb4584b29f9886b7fdcfd32feaebeb
compiled_at: 2026-04-15T00:37:55.044Z
---
# Go Fractals CLI
## 摘要
Go Fractals CLI是一个使用Go语言开发的命令行工具，用于生成ASCII艺术分形图案，支持谢尔宾斯基三角形和曼德博集合两种分形类型，支持多种可配置输出参数。

## 概述
Go Fractals CLI是一款生成ASCII艺术分形的命令行工具，支持两种分形类型，提供可配置的输出参数，输出结果直接打印至标准输出。

## 使用示例
```bash
# 生成谢尔宾斯基三角形
fractals sierpinski --size 32 --depth 5

# 生成曼德博集合
fractals mandelbrot --width 80 --height 24 --iterations 100

# 使用自定义字符生成谢尔宾斯基三角形
fractals sierpinski --size 16 --char '#'

# 查看帮助
fractals --help
fractals sierpinski --help
```

## 命令说明
### `sierpinski`
使用递归细分方法生成谢尔宾斯基三角形。
**可用参数**：
- `--size`（默认值：32）：三角形底边的字符宽度
- `--depth`（默认值：5）：递归深度
- `--char`（默认值：`*`）：填充点使用的字符
**输出**：按行打印三角形到标准输出。

### `mandelbrot`
将曼德博集合渲染为ASCII艺术，会将迭代次数映射为对应字符。
**可用参数**：
- `--width`（默认值：80）：输出的字符宽度
- `--height`（默认值：24）：输出的字符高度
- `--iterations`（默认值：100）：逃逸计算的最大迭代次数
- `--char`（默认值：gradient）：指定单个字符，留空则使用渐变字符集`" .:-=+*#%@"`
**输出**：打印矩形分形图案到标准输出。

## 项目架构
```
cmd/
  fractals/
    main.go           # 入口点，CLI初始化
internal/
  sierpinski/
    sierpinski.go     # 分形算法实现
    sierpinski_test.go
  mandelbrot/
    mandelbrot.go     # 分形算法实现
    mandelbrot_test.go
  cli/
    root.go           # 根命令、帮助信息
    sierpinski.go     # 谢尔宾斯基子命令实现
    mandelbrot.go     # 曼德博子命令实现
```

## 依赖
- Go 1.21 及以上版本
- `github.com/spf13/cobra`：用于CLI框架开发

## 验收标准
1. `fractals --help`可以正常显示使用说明
2. `fractals sierpinski`可输出可识别的三角形
3. `fractals mandelbrot`可输出可识别的曼德博集合
4. `--size`、`--width`、`--height`、`--depth`、`--iterations`参数可正常工作
5. `--char`参数可以自定义输出字符
6. 非法输入会输出清晰的错误信息
7. 所有测试可以正常通过

## 关键要点
- 该工具是基于Go语言开发的命令行ASCII分形生成工具
- 支持谢尔宾斯基三角形、曼德博集合两种分形类型
- 所有输出直接打印到标准输出，支持自定义输出尺寸、渲染参数和填充字符
- 使用Cobra框架构建CLI，采用分层清晰的项目架构
