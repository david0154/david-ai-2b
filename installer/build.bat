@echo off
echo [🔧] Starting build of David AI 2B Offline Installer...

REM === Set the path to Inno Setup Compiler ===
set INNO_PATH="C:\Program Files (x86)\Inno Setup 6\ISCC.exe"

REM === Check if ISCC.exe exists ===
if not exist %INNO_PATH% (
    echo ❌ Inno Setup not found at: %INNO_PATH%
    echo 🔍 Please install from https://jrsoftware.org/isinfo.php
    pause
    exit /b 1
)

REM === Compile the installer script ===
%INNO_PATH% inno_setup.iss

REM === Show result ===
if %errorlevel% neq 0 (
    echo ❌ Installer build failed.
) else (
    echo ✅ Installer built successfully!
    echo 📦 Check: dist\DavidAI2BInstaller.exe
)
pause
