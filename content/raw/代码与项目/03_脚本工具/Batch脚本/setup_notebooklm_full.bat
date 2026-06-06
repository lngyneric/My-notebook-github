@echo off
cd /d "C:\Users\lingyun\Documents\GOG\.trae\skills\notebooklm"

echo ==========================================
echo Manual Setup for NotebookLM Skill
echo ==========================================

if not exist ".venv" (
    echo [1/4] Creating virtual environment...
    python -m venv .venv
) else (
    echo [1/4] Virtual environment exists.
)

echo.
echo [2/4] Installing dependencies...
".venv\Scripts\pip" install --upgrade pip
".venv\Scripts\pip" install -r requirements.txt

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Failed to install dependencies.
    echo Please check your internet connection (PyPI access required).
    pause
    exit /b
)

echo.
echo [3/4] Installing Chromium for browser automation...
".venv\Scripts\python" -m patchright install chromium

echo.
echo [4/4] Starting Authentication...
echo A browser window will open. Please log in to Google.
".venv\Scripts\python" scripts/auth_manager.py setup

echo.
echo ==========================================
echo Setup Complete!
echo You can now use the NotebookLM skill in Trae.
echo ==========================================
pause