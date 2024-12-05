#!/bin/bash
set -o errexit  # Detiene el script si ocurre un error.

# Instalar las dependencias.
pip install -r requirements.txt

# Recolectar archivos estáticos.
python manage.py collectstatic --noinput

# Aplicar migraciones de base de datos.
python manage.py migrate
