@echo off
setlocal EnableDelayedExpansion
cd /d "C:\Users\lingyun\Documents\GOG\.trae\skills\notebooklm"

echo ==========================================
echo Manual Setup for NotebookLM Skill (V3)
echo ==========================================

:: Set Python Path Variable for clarity
set "VENV_PYTHON=.venv\Scripts\python.exe"
set "VENV_PIP=.venv\Scripts\pip.exe"

if not exist ".venv" (
    echo [1/4] Creating virtual environment...
    python -m venv .venv
) else (
    echo [1/4] Virtual environment exists.
)

echo.
echo [2/4] Installing dependencies...
:: Use call to prevent script termination on error and handle execution context
call "%VENV_PYTHON%" -m pip install --upgrade pip
if %ERRORLEVEL% NEQ 0 goto :ERROR

call "%VENV_PYTHON%" -m pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 goto :ERROR

echo.
echo [3/4] Installing Chromium for browser automation...
call "%VENV_PYTHON%" -m patchright install chromium
if %ERRORLEVEL% NEQ 0 goto :ERROR

echo.
echo [4/4] Starting Authentication...
echo A browser window will open. Please log in to Google.
call "%VENV_PYTHON%" scripts/auth_manager.py setup
if %ERRORLEVEL% NEQ 0 goto :ERROR

echo.
echo ==========================================
echo Setup Complete!
echo You can now use the NotebookLM skill in Trae.
echo ==========================================
pause
goto :EOF

:ERROR
echo.
echo [ERROR] An error occurred during setup.
pause
exit /b %ERRORLEVEL%
