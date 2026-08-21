import random


# Ejercicio A
# Generar un número aleatorio entre 1 y 100 que sea primo.

def es_primo(numero):
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True


numeros_primos = [numero for numero in range(1, 101) if es_primo(numero)]
numero_aleatorio = random.choice(numeros_primos)

print("Ejercicio A")
print("Número primo aleatorio:", numero_aleatorio)


# Ejercicio B
# Pedir un valor N y mostrar todos los números primos hasta N.

n = int(input("\nEjercicio B\nIngrese un valor N: "))

print(f"Números primos hasta {n}:")

for numero in range(2, n + 1):
    if es_primo(numero):
        print(numero, end=" ")

print()
