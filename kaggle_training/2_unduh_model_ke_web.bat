@echo off
title Unduh dan Pasang Model YOLOv8 ke Web SkinCheck
cd /d "%~dp0"
python sync_trained_model.py download
echo.
pause
