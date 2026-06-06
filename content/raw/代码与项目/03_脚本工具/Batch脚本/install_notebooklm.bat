@echo off
set "SKILLS_ROOT=C:\Users\lingyun\Documents\GOG\.trae\skills"
set "SKILL_DIR=%SKILLS_ROOT%\notebooklm"

if not exist "%SKILLS_ROOT%" (
    mkdir "%SKILLS_ROOT%"
)

echo ==========================================
echo Installing NotebookLM Skill
echo Source: https://github.com/PleasePrompto/notebooklm-skill
echo ==========================================

if not exist "%SKILL_DIR%" (
    echo [1/3] Cloning repository...
    git clone https://github.com/PleasePrompto/notebooklm-skill "%SKILL_DIR%"
    if %ERRORLEVEL% NEQ 0 (
        echo Failed to clone repository. Please check your internet connection and git installation.
        pause
        exit /b
    )
) else (
    echo [1/3] Updating existing repository...
    cd /d "%SKILL_DIR%"
    git pull
)

echo.
echo [2/3] Setting up Python Environment and Dependencies...
echo This may take a few minutes.
cd /d "%SKILL_DIR%"

echo.
echo [3/3] Configuring Authentication...
echo A Chrome browser window will open shortly.
echo Please log in to your Google Account in the opened window.
echo.

python scripts/run.py auth_manager.py setup

echo.
echo ==========================================
echo Installation and Configuration Complete!
echo You can now use NotebookLM skill in Trae.
echo ==========================================
pause
