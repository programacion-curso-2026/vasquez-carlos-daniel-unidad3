# EJEMPLO 2: INFORMACIÓN DE VEHÍCULOS

vehiculos = {
    "Marca": ["Toyota", "Chevrolet", "Kia", "Hyundai", "Mazda"],
    "Modelo": ["Corolla", "Aveo", "Sportage", "Tucson", "3"],
    "Precio": [23100, 18000, 29000, 32000, 25000]
}

df_vehiculos = pd.DataFrame(vehiculos)

print("\nINFORMACIÓN DE VEHÍCULOS")
print(df_vehiculos)

print("\nPrecio promedio:")
print(df_vehiculos["Precio"].mean())

print("\nVehículos con precio menor a $25000:")
print(df_vehiculos[df_vehiculos["Precio"] < 25000]|