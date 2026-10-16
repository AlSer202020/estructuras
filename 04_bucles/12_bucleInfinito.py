sum = 0
while(True):
    n = int(input("Introduzca un numero (0 para salir): "))
    if n == 0:
        break
    sum += n
print("La suma es ", sum)