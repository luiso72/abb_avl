# Script para ejecutar el servidor con el entorno virtual (Windows PowerShell)

# Activar el entorno virtual
.venv\Scripts\Activate.ps1

# Ejecutar el servidor
python -m uvicorn main:app --reload
