@echo off
chcp 65001 >nul
echo ================================================
echo Git-AI Quartz 版本发布跟踪工具
echo ================================================
echo.

set "GIT_AI_PATH=C:\Users\lingyun\.git-ai\bin\git-ai.exe"
set "PROJECT_DIR=C:\Users\lingyun\Documents\BaiduSyncdisk\xcxnotes"

cd /d "%PROJECT_DIR%"

echo [1/4] 检查 git-ai 版本...
"%GIT_AI_PATH%" --version
if %errorlevel% neq 0 (
    echo 错误: git-ai 命令无法执行
    pause
    exit /b 1
)

echo.
echo [2/4] 获取 upstream 仓库最新版本...
git fetch upstream

echo.
echo [3/4] 检查版本差异...
git log --oneline upstream/v4 | head -10

echo.
echo [4/4] 分析版本变更统计...
echo 本地当前版本:
git rev-parse --short HEAD
echo upstream 最新版本:
git rev-parse --short upstream/v4

echo.
echo ================================================
echo 版本对比分析
echo ================================================
git log --oneline HEAD..upstream/v4

echo.
echo ================================================
echo git-ai 统计信息
echo ================================================
"%GIT_AI_PATH%" stats upstream/v4 2>nul

echo.
echo ================================================
echo 配置说明
echo ================================================
echo 1. 你的项目已配置 git-ai，可以跟踪 AI 代码贡献
echo 2. 已配置 upstream 远程仓库: https://github.com/jackyzha0/quartz.git
echo 3. 当前 upstream 最新版本: v4.5.2
echo 4. 使用 git-ai blame 命令查看代码作者信息
echo.
echo 使用方法:
echo - 查看提交详情: git show upstream/v4
echo - 对比本地与 upstream: git diff HEAD upstream/v4
echo - AI 作者统计: git-ai stats upstream/v4
echo - AI 注释: git-ai blame [文件名]
echo.
echo 更新项目: git merge upstream/v4
echo.

pause
