"""
Excel to JSON converter for player data.

Converts Spanish column names to camelCase and prepares clean data
for the Vue frontend application.
"""

import json
import os

import numpy as np
import pandas as pd


# Column mapping: Spanish (with spaces/underscores) -> camelCase
# Note: "Posición" = player position; "Posicion" (no accent) = multiplicador column
COLUMN_MAPPING = {
    "Nº": "numero",
    "Numero": "numero",
    "Número": "numero",
    "Nombre": "nombre",
    "Equipo_Actual": "equipoActual",
    "Equipo Actual": "equipoActual",
    "Nacionalidad": "nacionalidad",
    "Segunda_Nacionalidad": "segundaNacionalidad",
    "Segunda Nacionalidad": "segundaNacionalidad",
    "Posición": "posicion",
    "Media_Jugador": "mediaJugador",
    "Media Jugador": "mediaJugador",
    "Edad": "edad",
    "Valor": "valor",
    "Precio_Mercado": "precioMercado",
    "Precio Mercado": "precioMercado",
    "Salario": "salario",
    "Contrato": "contrato",
    "Clausula": "clausula",
    "Cláusula": "clausula",
    "Importancia_Deportiva": "importanciaDeportiva",
    "Importancia Deportiva": "importanciaDeportiva",
    "Filial": "filial",
    "Origen_Formativo": "origenFormativo",
    "Origen Formativo": "origenFormativo",
    "Nuevo_Fichaje": "nuevoFichaje",
    "Nuevo Fichaje": "nuevoFichaje",
    "Nuevo fichaje": "nuevoFichaje",
    "Reputacion_Equipo": "reputacionEquipo",
    "Reputación Equipo": "reputacionEquipo",
    "Repu. Equipo": "reputacionEquipo",
    "Multiplicador_Edad": "multiplicadorEdad",
    "Multiplicador Edad": "multiplicadorEdad",
    "Edad.1": "multiplicadorEdad",
    "Multiplicador_Importancia": "multiplicadorImportancia",
    "Multiplicador Importancia": "multiplicadorImportancia",
    "Multiplicador_deportivo": "multiplicadorImportancia",
    "Impor depor": "multiplicadorImportancia",
    "Multiplicador_Posicion": "multiplicadorPosicion",
    "Multiplicador Posicion": "multiplicadorPosicion",
    "Multiplicador_Posición": "multiplicadorPosicion",
    "Posicion": "multiplicadorPosicion",  # Last col in Excel = multiplicador
}

# Columns that should be treated as numeric (may contain commas/spaces)
NUMERIC_COLUMNS = [
    "numero",
    "mediaJugador",
    "edad",
    "valor",
    "precioMercado",
    "salario",
    "clausula",
    "importanciaDeportiva",
    "filial",
    "origenFormativo",
    "nuevoFichaje",
    "reputacionEquipo",
    "multiplicadorEdad",
    "multiplicadorImportancia",
    "multiplicadorPosicion",
]


def load_excel(file_path: str) -> pd.DataFrame:
    """
    Load an Excel file into a pandas DataFrame.

    Args:
        file_path: Path to the .xlsx file

    Returns:
        DataFrame with raw Excel data
    """
    df = pd.read_excel(file_path)
    print("Loaded columns:", list(df.columns))
    return df


def check_columns(df: pd.DataFrame) -> None:
    """
    Validate that required columns exist in the Excel file.
    """
    required_columns = [
        "Nombre",
        "Equipo_Actual",
        "Nacionalidad",
        "Posición",
        "Edad",
        "Media_Jugador",
    ]
    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}. "
            f"Available columns: {list(df.columns)}"
        )

    print("Column check passed")


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rename Spanish column names to camelCase for frontend consistency.

    Uses COLUMN_MAPPING dictionary. Expects Excel to be pre-cleaned
    (empty columns removed before export).

    Args:
        df: DataFrame with original column names

    Returns:
        DataFrame with camelCase column names
    """
    rename_map = {col: COLUMN_MAPPING[col] for col in df.columns if col in COLUMN_MAPPING}
    return df.rename(columns=rename_map)


def clean_numeric_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean numeric fields: remove commas/spaces and convert to int/float.

    Handles values like "1,000,000" or "1 000 000" -> 1000000.
    Also strips whitespace from string columns.

    Args:
        df: DataFrame with potentially messy numeric/string values

    Returns:
        DataFrame with cleaned numeric types and trimmed strings
    """
    df = df.copy()

    for col in df.columns:
        if col not in NUMERIC_COLUMNS:
            # Strip whitespace from string columns (skip if duplicate columns)
            series = df[col]
            if isinstance(series, pd.Series) and series.dtype == object:
                df[col] = series.apply(
                    lambda x: x.strip() if isinstance(x, str) else x
                )
            continue

        series = df[col]
        if not isinstance(series, pd.Series):
            continue  # Skip duplicate columns

        # Convert to string, remove commas and spaces, then to numeric
        def clean_numeric(val):
            if pd.isna(val) or val == "" or val is None:
                return np.nan
            if isinstance(val, bool):
                return 1 if val else 0
            if isinstance(val, (int, float)):
                # Avoid float precision issues (e.g. 1518000.0000000002 -> 1518000)
                return int(round(val)) if abs(val - round(val)) < 1e-9 else val
            cleaned = str(val).replace(",", "").replace(" ", "").strip()
            if cleaned == "":
                return np.nan
            try:
                f = float(cleaned)
                return int(round(f)) if abs(f - round(f)) < 1e-9 else f
            except (ValueError, TypeError):
                return np.nan

        df[col] = series.apply(clean_numeric)

    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replace empty strings and NaN with None for clean JSON output.

    Ensures consistent null representation in the exported JSON.

    Args:
        df: DataFrame with possible NaN/empty values

    Returns:
        DataFrame with None for missing values
    """
    df = df.copy()
    df = df.replace({np.nan: None, "": None, "nan": None})
    # Replace any remaining empty strings
    df = df.map(lambda x: None if x == "" else x)
    return df


def convert_excel_to_json(input_path: str, output_path: str) -> None:
    """
    Main conversion pipeline: load Excel, clean, and export to JSON.

    Args:
        input_path: Path to the .xlsx file
        output_path: Path for the output .json file
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    df = load_excel(input_path)
    check_columns(df)
    df = rename_columns(df)
    df = clean_numeric_values(df)
    df = handle_missing_values(df)

    # Convert to records, fix integers and any remaining NaN
    records = df.to_dict(orient="records")
    for record in records:
        for key, val in record.items():
            if pd.isna(val) or val is None:
                record[key] = None
            elif isinstance(val, (int, float)) and abs(val - round(val)) < 1e-9:
                record[key] = int(val)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    print(f"Successfully converted to {output_path}")


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    convert_excel_to_json(
        input_path=os.path.join(script_dir, "ejemplo2.xlsx"),
        output_path=os.path.join(script_dir, "jugadores.json"),
    )
