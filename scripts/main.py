import pandas as pd 

df = pd.read_excel("ejemplo.xlsx")

# REnombrar columnas!
df = df.rename(columns={
    "Nombre": "nombre",
    "Equipo_Actual": "equipoActual",
    "Nacionalidad": "nacionalidad",
    "Posición": "posicion",
    "Media_Jugador": "mediaJugador",
    "Edad": "edad",
    "Valor": "valor",
    "Precio_Mercado": "precioMercado"
})

# Limpiar valores numericos
df["valor"] = df["valor"].str.replace(" ", "").astype(int)
df["precioMercado"] = df["precioMercado"].str.replace(" ", "").astype(int)

# Guardar en json
df.to_json("jugadores.json", orient="records")

print("Excel convertido a JSON correctamente")
