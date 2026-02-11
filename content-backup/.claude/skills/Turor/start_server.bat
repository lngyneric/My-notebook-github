@echo off
echo ===================================================
echo   Academic Tutor API Server - Deployment Script
echo ===================================================

echo [1/2] Checking and installing dependencies...
pip install -r requirements.txt

echo.
echo [2/2] Starting server...
echo Server will run at http://127.0.0.1:8000
echo Press Ctrl+C to stop.
echo.

python -m uvicorn tutor_api:app --host 0.0.0.0 --port 8000

pause
