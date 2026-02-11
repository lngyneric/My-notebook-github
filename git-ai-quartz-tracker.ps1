<#
.SYNOPSIS
Git-AI Quartz 版本发布跟踪脚本
#>

# 配置
$GitAIExe = "C:\Users\lingyun\.git-ai\bin\git-ai.exe"
$ProjectDir = "C:\Users\lingyun\Documents\BaiduSyncdisk\xcxnotes"
$UpstreamBranch = "v4"
$UpstreamRemote = "upstream"

# 主程序
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "Git-AI Quartz 版本发布跟踪" -ForegroundColor Green
Write-Host "================================================" -ForegroundColor Cyan

try {
    # 检查 git-ai
    if (-not (Test-Path $GitAIExe)) {
        Write-Error "git-ai 未找到: $GitAIExe"
        return 1
    }

    # 检查项目目录
    if (-not (Test-Path $ProjectDir)) {
        Write-Error "项目目录不存在: $ProjectDir"
        return 1
    }

    Set-Location $ProjectDir

    # 获取 upstream 最新代码
    Write-Host "获取 upstream 最新代码..."
    git fetch $UpstreamRemote

    # 显示信息
    Write-Host "本地信息:" -ForegroundColor Yellow
    Write-Host "  当前分支: $(git rev-parse --abbrev-ref HEAD)"
    Write-Host "  当前提交: $(git rev-parse --short HEAD)"
    Write-Host "  最后提交: $(git log -1 --format="%cd" --date=format:"%Y-%m-%d %H:%M:%S")"

    Write-Host "Upstream 信息:" -ForegroundColor Yellow
    Write-Host "  远程地址: $(git remote get-url $UpstreamRemote)"
    Write-Host "  分支: $UpstreamBranch"
    Write-Host "  最新提交: $(git rev-parse --short $UpstreamRemote/$UpstreamBranch)"
    Write-Host "  最后提交: $(git log -1 --format="%cd" --date=format:"%Y-%m-%d %H:%M:%S" $UpstreamRemote/$UpstreamBranch)"

    # 版本差异
    $localCount = (git rev-list HEAD --count)
    $remoteCount = (git rev-list $UpstreamRemote/$UpstreamBranch --count)
    $difference = $remoteCount - $localCount

    Write-Host "================================================" -ForegroundColor Cyan
    Write-Host "版本差异统计" -ForegroundColor Green
    Write-Host "================================================" -ForegroundColor Cyan
    Write-Host "本地提交数量: $localCount"
    Write-Host "Upstream 提交数量: $remoteCount"
    Write-Host "差异提交数量: $difference"

    if ($difference -gt 0) {
        Write-Host "`n需要更新的提交:" -ForegroundColor Cyan
        git log --oneline HEAD..$UpstreamRemote/$UpstreamBranch
    } else {
        Write-Host "`n✅ 本地版本已最新" -ForegroundColor Green
    }

    Write-Host "================================================" -ForegroundColor Cyan
    Write-Host "使用建议" -ForegroundColor Green
    Write-Host "================================================" -ForegroundColor Cyan

    $remoteVersion = (git rev-parse --short $UpstreamRemote/$UpstreamBranch)
    $localVersion = (git rev-parse --short HEAD)

    if ($remoteVersion -ne $localVersion) {
        Write-Host "`n📢 发现新版本更新!" -ForegroundColor Red
        Write-Host "   本地版本: $localVersion"
        Write-Host "   最新版本: $remoteVersion"
        Write-Host "`n更新命令:" -ForegroundColor Cyan
        Write-Host "   git merge $UpstreamRemote/$UpstreamBranch"
    }

    Write-Host "`ngit-ai 常用命令:"
    Write-Host "   git-ai blame [文件名]    - 查看代码作者信息"
    Write-Host "   git-ai stats [提交]      - 查看提交统计"
    Write-Host "   git-ai diff [范围]       - 查看差异分析"
    Write-Host "   git-ai show [提交]       - 查看提交详情"

} catch {
    Write-Error "执行失败: $_"
    return 1
}
