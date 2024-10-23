@ECHO OFF
@REM INSTALL THE SCRIPT USING SETUP.PY
cd /d "%~dp0"
chcp 65001 >nul
python ./setup.py
TIMEOUT 5