# ============================================================
# EJEMPLO 2: TEMPERATURA DEL MOTOR
# ============================================================

print("\n" + "=" * 50)
print("EJEMPLO 2: TEMPERATURA DEL MOTOR")
print("=" * 50)

temperaturas = np.array([85, 90, 91, 87, 95, 84])

print("Temperaturas:", temperaturas)
print("Temperatura promedio:", temperaturas.mean())
print("Temperatura máxima:", temperaturas.max())

print("Temperaturas superiores a 90°C:")
print(temperaturas[temperaturas > 90])
