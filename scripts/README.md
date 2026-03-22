# Excel to JSON Script
Script en Python para convertir datos desde un archivo Excel (.xlsx) a formato JSON, adaptado para ser utilizado por el frontend.

## Descripción
Este script procesa un Excel previamente limpiado y convierte sus datos a JSON, asegurando:
- Normalización de nombres de columnas (camelCase)
- Conversión de tipos de datos
- Limpieza de valores vacíos o inconsistentes

⚠️ Importante:
El Excel debe estar previamente preparado (columnas renombradas y datos limpiados) antes de ejecutar el script.

## Workflow
```bash
# Crea maquina virtual
python -m venv .venv

# Activalo
source .venv/bin/activate

# ISntalar librerias necesarias
# pip install pandas openpyxl
pip install -r requirements.txt

# Ejecutar
python main.py

# Salir/desactivar venv
deactivate
```

## Work Flow
1. Partir del Excel original ("master")
2. Limpiar columnas y nombres manualmente
3. Exportar a .xlsx
4. Ejecutar el script para generar el JSON
5. Usar el JSON en el frontend


# Notas
- Actualmente no se procesa directamente el Excel original completo
- Se utiliza una versión simplificada del archivo para evitar complejidad innecesaria
- El objetivo es mantener el frontend lo más simple posible (sin parsing de Excel en el navegador)