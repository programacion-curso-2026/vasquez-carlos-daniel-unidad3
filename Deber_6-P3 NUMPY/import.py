# EJEMPLO 1: CREAR Y ANALIZAR UNA TABLA
import pandas as pd

datos = {
    "Producto": ["Aceite", "Filtro", "Bujía", "Batería"],
    "Cantidad": [10, 15, 20, 5],
    "Precio": [8.50, 12.00, 4.50, 90.00]
}

df = pd.DataFrame(datos)

print("\nEJEMPLO 1")
print(df)

df["Total"] = df["Cantidad"] * df["Precio"]

print("\nTotal por producto:")
print(df)

print("\nVentas totales:", df["Total"].sum())
