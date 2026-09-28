@echo off
title ComfyUI - GTX 1060 6GB Full Performance (DreamShaper 8 / Surreal)
cd /d "%~dp0"
echo Starting ComfyUI on NVIDIA GeForce GTX 1060 6GB...
if exist "venv\Scripts\python.exe" (
    "venv\Scripts\python.exe" main.py --force-fp16 --use-pytorch-cross-attention --auto-launch %*
) else (
    python main.py --force-fp16 --use-pytorch-cross-attention --auto-launch %*
)
pause
