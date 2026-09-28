@echo off
chcp 65001 >nul
title ComfyUI-tuning - Model & LoRA Auto Downloader
cd /d "%~dp0"
if exist "venv\Scripts\python.exe" (
    "venv\Scripts\python.exe" download_models.py
) else (
    python download_models.py
)
pause
