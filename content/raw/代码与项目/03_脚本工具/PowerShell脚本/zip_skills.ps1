$path = "C:\Users\lingyun\Downloads\skills-main\skills-main\skills"
Get-ChildItem -Path $path -Directory | ForEach-Object {
    $zipName = "$($_.FullName).zip"
    if (-not (Test-Path $zipName)) {
        Write-Host "Zipping $($_.Name)..."
        try {
            Compress-Archive -Path $_.FullName -DestinationPath $zipName -ErrorAction Stop
            Write-Host "Successfully zipped $($_.Name)"
        } catch {
            Write-Host "Error zipping $($_.Name): $($_.Exception.Message)"
        }
    } else {
        Write-Host "Skipping $($_.Name) (zip exists)"
    }
}
