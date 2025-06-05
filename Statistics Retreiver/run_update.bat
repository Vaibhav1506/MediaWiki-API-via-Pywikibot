@echo off
cd /d "C:\Users\path to Virtual Environment"
call YourVirtualEnvironmentName\Scripts\activate.bat
cd "ScriptFolder"
python update.py
pause
