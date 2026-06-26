@echo off
title XONIMAIL 2026 - Cliente de Gmail para Terminal
color 0A

:: ============================================================
:: SOLICITAR PERMISOS DE ADMINISTRADOR
:: ============================================================
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Solicitando permisos de administrador...
    echo.
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B
)

:: ============================================================
:: EJECUTAR start.py CON PERMISOS DE ADMINISTRADOR
:: ============================================================
cls
echo ============================================================
echo           XONIMAIL 2026 - Cliente de Gmail para Terminal
echo              (Modo Administrador)
echo ============================================================
echo.
echo [OK] Permisos de administrador obtenidos
echo.
echo Iniciando XONIMAIL...
echo.
echo [INFO] Cliente de Gmail para dispositivos de bajos recursos
echo [INFO] Archivo de token: %USERPROFILE%\.xonimail\token.txt
echo.
echo Para salir: Presiona Ctrl+C
echo ============================================================
echo.

python start.py

pause
