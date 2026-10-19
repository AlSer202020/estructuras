# Calcular el factorial de un número

def factorial(n):
    # caso base
    if (n <= 1):
        return 1
    # recursividad
    return n*factorial(n-1)

print(factorial(500))