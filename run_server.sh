#!/bin/bash
# Script para ejecutar el servidor con el entorno virtual

# Activar el entorno virtual
source .venv/Scripts/activate

# Ejecutar el servidor
python -m uvicorn main:app --reload
