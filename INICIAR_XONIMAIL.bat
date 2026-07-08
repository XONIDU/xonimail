@echo off
title XONIMAIL 2026 - Cliente de Gmail para Terminal
color 0A

:: ============================================================
:: IR AL DIRECTORIO DONDE ESTA EL SCRIPT .BAT
:: ============================================================
cd /d "%~dp0"

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
:: VERIFICAR QUE start.py EXISTE
:: ============================================================
if not exist "%~dp0start.py" (
    echo [ERROR] No se encuentra start.py en esta carpeta
    echo.
    echo Ruta actual: %~dp0
    echo.
    echo Asegurate de que start.py esta en la misma carpeta que este .bat
    echo.
    pause
    exit /B
)

:: ============================================================
:: VERIFICAR QUE PYTHON ESTA INSTALADO
:: ============================================================
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python no esta instalado o no esta en el PATH
    echo.
    echo Descarga Python desde: https://www.python.org/downloads/
    echo Asegurate de marcar "Add Python to PATH" durante la instalacion
    echo.
    pause
    exit /B
)

:: ============================================================
:: MOSTRAR INFORMACION DEL SISTEMA
:: ============================================================
for /f "tokens=*" %%i in ('python --version 2^>^&1') do set PYTHON_VER=%%i

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
echo [INFO] Directorio de trabajo: %~dp0
echo [INFO] Python detectado: %PYTHON_VER%
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

:: ============================================================
:: PAUSA AL FINALIZAR (SI NO SE INTERRUMPIO CON CTRL+C)
:: ============================================================
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] El programa termino con errores (codigo: %errorlevel%)
    echo.
) else (
    echo.
    echo [OK] Programa finalizado correctamente
    echo.
)

pause