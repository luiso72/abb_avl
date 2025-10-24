@echo off
REM Script para ejecutar el servidor con el entorno virtual (Windows CMD/Batch)

REM Activar el entorno virtual
call .venv\Scripts\activate.bat

REM Instalar dependencias si no están instaladas
python -m pip install -r requirements.txt

REM Ejecutar el servidor
python -m uvicorn main:app --reload

pause
