import random


def es_primo(numero):
    if numero < 2:
        return False

    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False

    return True


# EJERCICIO A
# Generar un número primo aleatorio entre 1 y 100

while True:
    numero = random.randint(1, 100)

    if es_primo(numero):
        break

print("EJERCICIO A")
print("Número primo generado:", numero)


# EJERCICIO B
# Mostrar todos los números primos hasta N

n = int(input("\nEJERCICIO B\nIngrese un número N: "))

print("Números primos hasta", n, ":")

for numero in range(2, n + 1):
    if es_primo(numero):
        print(numero, end=" ")

print()
