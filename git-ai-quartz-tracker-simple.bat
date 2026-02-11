@echo off
chcp 65001 >nul
echo ================================================
echo Git-AI Quartz 版本发布跟踪工具
echo ================================================
echo.

set "GIT_AI_PATH=C:\Users\lingyun\.git-ai\bin\git-ai.exe"
set "PROJECT_DIR=C:\Users\lingyun\Documents\BaiduSyncdisk\xcxnotes"

cd /d "%PROJECT_DIR%"

echo [1/6] 检查 git-ai 版本...
"%GIT_AI_PATH%" --version
if %errorlevel% neq 0 (
    echo 错误: git-ai 命令无法执行
    pause
    exit /b 1
)

echo.
echo [2/6] 获取 upstream 仓库最新版本...
git fetch upstream

echo.
echo [3/6] 显示本地信息...
echo 本地当前提交:
for /f %%i in ('git rev-parse --short HEAD') do set "LOCAL_COMMIT=%%i"
echo %LOCAL_COMMIT%
for /f %%i in ('git log -1 --format="%%cd" --date=format:"%%Y-%%m-%%d %%H:%%M:%%S"') do set "LOCAL_DATE=%%i"
echo 最后提交时间: %LOCAL_DATE%

echo.
echo [4/6] 显示 upstream 信息...
echo Upstream 最新提交:
for /f %%i in ('git rev-parse --short upstream/v4') do set "UPSTREAM_COMMIT=%%i"
echo %UPSTREAM_COMMIT%
for /f %%i in ('git log -1 --format="%%cd" --date=format:"%%Y-%%m-%%d %%H:%%M:%%S" upstream/v4') do set "UPSTREAM_DATE=%%i"
echo 最后提交时间: %UPSTREAM_DATE%

echo.
echo [5/6] 版本差异统计...
for /f %%i in ('git rev-list HEAD --count') do set "LOCAL_COUNT=%%i"
for /f %%i in ('git rev-list upstream/v4 --count') do set "UPSTREAM_COUNT=%%i"
set /a DIFFERENCE=%UPSTREAM_COUNT%-%LOCAL_COUNT%

echo 本地提交数量: %LOCAL_COUNT%
echo Upstream 提交数量: %UPSTREAM_COUNT%
echo 差异提交数量: %DIFFERENCE%

if %DIFFERENCE% gtr 0 (
    echo.
    echo 需要更新的提交:
    git log --oneline HEAD..upstream/v4
) else (
    echo.
    echo ✅ 本地版本已最新
)

echo.
echo [6/6] 配置说明
echo ================================================
echo.
echo 使用方法:
echo - 更新项目: git merge upstream/v4
echo - 查看差异: git diff HEAD upstream/v4
echo - 查看统计: "%GIT_AI_PATH%" stats upstream/v4
echo - 代码分析: "%GIT_AI_PATH%" blame [文件名]
echo.

pause
