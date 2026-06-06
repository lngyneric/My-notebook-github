$folderPath = "C:\Users\lingyun\Pictures\盘点照片上传表单-2025Nov\图一机器背面产品标签"
$pattern = "^2025-11-27 \d{2}_\d{2}_"

Get-ChildItem -Path $folderPath -Filter "*.jpg" | ForEach-Object {
    if ($_.Name -match $pattern) {
        $newName = $_.Name -replace $pattern, ""
        $newPath = Join-Path -Path $_.Directory.FullName -ChildPath $newName
        
        Write-Host "Renaming '$($_.Name)' to '$newName'"
        
        if (Test-Path $newPath) {
            Write-Warning "File '$newName' already exists. Skipping '$($_.Name)'."
        } else {
            Rename-Item -Path $_.FullName -NewName $newName -ErrorAction SilentlyContinue
            if (-not $?) {
                Write-Error "Failed to rename '$($_.Name)': $($Error[0].Exception.Message)"
            }
        }
    }
}
