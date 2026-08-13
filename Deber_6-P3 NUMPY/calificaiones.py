# EJEMPLO 1: CALIFICACIONES
# ============================================================

print("\n" + "=" * 50)
print("EJEMPLO 1: CALIFICACIONES")
print("=" * 50)

notas = np.array([87, 71, 92, 60, 86])

print("Notas:", notas)
print("Promedio:", notas.mean())
print("Nota más alta:", notas.max())
print("Nota más baja:", notas.min())

print("Notas aprobadas:")
print(notas[notas >= 70])