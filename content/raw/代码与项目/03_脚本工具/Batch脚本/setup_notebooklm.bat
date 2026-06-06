@echo off
cd /d "c:\Users\lingyun\Documents\GOG\.trae\skills\notebooklm"
echo Starting NotebookLM Authentication Setup...
echo A browser window will open. Please log in to your Google account.
python scripts/run.py auth_manager.py setup
pause
