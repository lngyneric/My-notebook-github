---
source: raw/04_技能与工具/Superpowers/superpowers-main/docs/windows/polyglot-hooks.md
raw_sha256: 6ab79f0a8fc90e61bd0723ba153630e75d883883f6b9a15d07025e341c18c565
compiled_at: 2026-04-14T16:51:07.050Z
---
# 多语言钩子（Polyglot Hooks）for Claude Code
Claude Code 的跨平台钩子技术，用于解决Claude Code钩子在Windows、macOS和Linux多系统下正常运行的兼容问题。

## 摘要
Claude Code运行钩子命令时，Windows默认使用CMD.exe，macOS/Linux默认使用bash/sh，原生环境存在脚本无法直接执行、路径格式不兼容、环境变量语法不兼容、bash默认不在PATH中等问题。本文介绍的多语言`.cmd`包装器技术，通过创建同时兼容CMD和bash语法的polyglot入口脚本，实现了Claude Code插件钩子的跨平台运行支持。

## 问题背景
Claude Code通过系统默认shell运行钩子命令，带来了多项兼容性挑战：
1. **脚本执行**：Windows CMD无法直接执行`.sh`文件，默认会用文本编辑器打开
2. **路径格式**：Windows使用反斜杠路径，Unix系统使用正斜杠路径
3. **环境变量语法**：Unix风格`$VAR`语法在CMD中不生效
4. **PATH问题**：即使安装了Git Bash，CMD运行环境中默认也不会将bash加入PATH

## 解决方案：多语言`.cmd`包装器
多语言脚本是同时符合多种编程语言语法的脚本，本方案的包装器同时兼容CMD和bash两种语法，作为跨平台入口点，实际钩子逻辑存放在单独的bash脚本中。

### 工作原理
#### Windows（CMD.exe）运行流程
1. `: << 'CMDBLOCK'`：CMD将`:`识别为标签，忽略后续`<< 'CMDBLOCK'`内容
2. 关闭命令输出回显，通过Git默认安装路径调用bash.exe，使用`-l`参数启动登录shell加载正确PATH，通过`cygpath -u`将Windows路径转换为Unix格式，执行实际钩子脚本
3. 执行`exit /b`退出批处理脚本，不会执行后续内容

#### Unix（bash/sh）运行流程
1. `: << 'CMDBLOCK'`：`:`是空操作，`<< 'CMDBLOCK'`开启 heredoc，直到`CMDBLOCK`标记的内容都会被作为 heredoc 忽略
2. 直接使用Unix路径执行实际钩子脚本

## 推荐文件结构
```
hooks/
├── hooks.json           # 钩子配置，指向.cmd包装器
├── session-start.cmd    # 多语言包装器（跨平台入口）
└── session-start.sh     # 实际钩子逻辑（bash脚本）
```

### 钩子配置示例（hooks.json）
将入口指向`.cmd`包装器，路径需要添加引号，避免`CLAUDE_PLUGIN_ROOT`包含空格时出错：
```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume|clear|compact",
        "hooks": [
          {
            "type": "command",
            "command": "\"${CLAUDE_PLUGIN_ROOT}/hooks/session-start.cmd\""
          }
        ]
      }
    ]
  }
}
```

## 环境要求
| 平台 | 要求 |
|------|------|
| Windows | 需要安装Git for Windows，提供bash.exe和cygpath，默认安装路径为`C:\Program Files\Git\bin\bash.exe`，安装路径变更需要修改包装器内的路径 |
| macOS/Linux | 需要标准bash或sh shell，`.cmd`文件需要添加可执行权限（`chmod +x`） |

## 跨平台钩子编写规范
实际钩子逻辑编写在`.sh`文件中，在Windows通过Git Bash运行，需要遵循以下规范：
### 推荐做法
- 尽量使用纯bash内置命令
- 使用`$(command)`代替反引号
- 给所有变量扩展添加引号：`"$VAR"`
- 使用`printf`或here-document输出内容

### 不推荐做法
- 尽量避免使用可能不在PATH中的外部命令（如sed、awk、grep）
- 如果必须使用，需要确保通过`bash -l`启动登录shell配置正确PATH

## 可复用包装器模式
如果插件包含多个钩子，可以创建通用包装器通过参数指定要执行的脚本，简化配置：
1. 创建通用`run-hook.cmd`包装器，接收脚本名称作为参数
2. 在`hooks.json`中通过通用包装器调用不同的业务钩子脚本

## 常见问题排查
| 问题 | 原因 | 解决方法 |
|------|------|----------|
| "bash is not recognized" | CMD找不到bash | 修改包装器中的bash.exe路径为实际Git安装路径 |
| "cygpath: command not found"或"dirname: command not found" | bash未以登录shell运行 | 确保包装器中给bash添加了`-l`参数 |
| 路径出现错误的`\/`混合格式 | Windows路径末尾反斜杠和后续正斜杠拼接错误 | 使用`cygpath`转换完整路径 |
| 脚本在文本编辑器中打开而非运行 | hooks.json直接指向了`.sh`文件 | 修改配置指向`.cmd`包装器 |
| 终端中可以运行但作为钩子无法运行 | Claude Code钩子运行环境与终端不同 | 使用CMD模拟钩子环境测试验证 |

## 相关问题
- [anthropics/claude-code#9758](https://github.com/anthropics/claude-code/issues/9758) - Windows下.sh文件会在编辑器中打开
- [anthropics/claude-code#3417](https://github.com/anthropics/claude-code/issues/3417) - Windows下钩子无法运行
- [anthropics/claude-code#6023](https://github.com/anthropics/claude-code/issues/6023) - 找不到CLAUDE_PROJECT_DIR
