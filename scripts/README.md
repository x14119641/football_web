# Script xlsx to json
Pasa el excel a json.
Muy importante cambiar el nombre de las columnas.

Tal vez en un futuro usaria el excel principal, pero de momento exporto la hoja de calculo que necessito a xlsx y transformo a json desde ahi.

## Workflow
```
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