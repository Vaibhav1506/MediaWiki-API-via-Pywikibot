@echo off
cd /d "C:\Users\<path to Virtual Environment>"
call <Virtual Environment Name>\Scripts\activate.bat
cd "<Script Folder>"
python update.py
pause