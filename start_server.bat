@echo off
title SkinCheck Web Server
echo ==================================================
echo   SkinCheck Web Platform - Dedicated Server
echo   Server URL  : http://localhost:8000
echo   Admin Portal: http://localhost:8000/admin/dashboard
echo ==================================================
echo.
cd /d "%~dp0"
py -3.13 run.py
if errorlevel 1 (
    echo.
    echo Server terhenti atau terjadi kendala.
    pause
)
