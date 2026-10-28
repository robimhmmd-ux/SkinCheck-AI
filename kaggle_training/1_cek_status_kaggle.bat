@echo off
title Memeriksa Status Training Kaggle
cd /d "%~dp0"
python sync_trained_model.py
echo.
pause
