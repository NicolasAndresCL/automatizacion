@echo off
title Ejecutor con Entorno Virtual

:: 1. Intentar activar el entorno virtual (asumiendo que se llama 'env' o 'venv')
if exist env\Scripts\activate (
    echo Activando entorno virtual 'env'...
    call env\Scripts\activate
) else if exist venv\Scripts\activate (
    echo Activando entorno virtual 'venv'...
    call venv\Scripts\activate
) else (
    echo [!] No se encontro la carpeta del entorno virtual. 
    echo Intentando ejecutar con el Python global...
)

:: 2. Ejecutar el script
python "automatizador.py"

:: 3. Pausar en caso de error para poder leerlo
pause