@echo off
setlocal EnableDelayedExpansion

set "SKILLS_ROOT=C:\Users\lingyun\Documents\GOG\.trae\skills"
set "SKILL_DIR=%SKILLS_ROOT%\notebooklm"
set "ZIP_SOURCE=C:\Users\lingyun\Downloads\notebooklm-skill-main.zip"
set "ZIP_SOURCE_ALT=C:\Users\lingyun\Downloads\notebooklm.zip"

if not exist "%SKILLS_ROOT%" (
    mkdir "%SKILLS_ROOT%"
)

echo ==========================================
echo Installing NotebookLM Skill
echo ==========================================

if exist "%SKILL_DIR%" (
    echo [INFO] Skill directory already exists.
    goto :SETUP
)

echo [1/3] Checking for source files...

:: Method 1: Check for local zip file
if exist "%ZIP_SOURCE%" (
    echo [INFO] Found zip file at %ZIP_SOURCE%
    echo Extracting zip file...
    powershell -command "Expand-Archive -Path '%ZIP_SOURCE%' -DestinationPath '%SKILLS_ROOT%'"
    :: Handle folder name mismatch (github zips usually extract to repo-branch name)
    if exist "%SKILLS_ROOT%\notebooklm-skill-main" (
        rename "%SKILLS_ROOT%\notebooklm-skill-main" "notebooklm"
    )
    goto :SETUP
)

if exist "%ZIP_SOURCE_ALT%" (
    echo [INFO] Found zip file at %ZIP_SOURCE_ALT%
    echo Extracting zip file...
    powershell -command "Expand-Archive -Path '%ZIP_SOURCE_ALT%' -DestinationPath '%SKILLS_ROOT%'"
    goto :SETUP
)

:: Method 2: Git Clone (requires network)
echo [INFO] No local zip found. Attempting Git clone...
echo [NOTE] This requires a working internet connection to GitHub.
git clone https://github.com/PleasePrompto/notebooklm-skill "%SKILL_DIR%"

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Failed to clone repository.
    echo [SOLUTION] Please download the ZIP manually:
    echo 1. Go to https://github.com/PleasePrompto/notebooklm-skill
    echo 2. Click Code - Download ZIP
    echo 3. Save as "notebooklm-skill-main.zip" in your Downloads folder
    echo 4. Run this script again.
    pause
    exit /b
)

:SETUP
echo.
echo [2/3] Setting up Python Environment...
cd /d "%SKILL_DIR%"
if not exist "scripts\run.py" (
    echo [ERROR] scripts\run.py not found! Installation might be corrupted.
    pause
    exit /b
)

echo.
echo [3/3] Authenticating...
echo A browser window will open. Please log in to Google.
python scripts/run.py auth_manager.py setup

echo.
echo ==========================================
echo Installation Complete!
echo ==========================================
pause
