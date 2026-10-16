print("Hola mundo")

"""
a = 3
print(type(a))

a = "pepe"
print(type(a))


lista1 = [1,2,3]
lista2 = [1,2,3]

lista3 = lista1

print(lista1==lista2)

print(lista1 is lista2)
print(lista1 is lista3)

lista3.append(4)

print(lista1)

saludo ="Hola mundo"

print("Pepe" in saludo)
print("Pepe" not in saludo)

"""


# Lectura por teclado

"""
entero1 = int (input("Introduce un valor entero: "))
entero2 = int (input("Introduce otro valor entero: "))

if (entero1 > 0 and entero2 > 0):
    print("Los dos números son mayores que 0")

"""


# nota = int(input("Introduce su norta: "))
    
# if (nota < 5): 
#     print("suspendido")
# elif (nota < 7):
#     print("bien")
# elif (nota < 8.5):
#     print("notable")
# elif (nota <= 10):
#     print("sobresaliente")
# else:
#     print("Error: datos incorrectos")

# temperatura = float (input("Introduce la temperatura:"))
# if 18.0 <= temperatura <= 27.0:
#     print("Temperatura optima")
# elif temperatura <= 18.0:
#     print("Alerta frio")
# else:
#     print("Alerta calor")

# name = input("Introduce su nombre: ").strip().lower()
# cp = input("Introduce su codigo postal: ").strip()


# if not name:
#     print("Error: el nombre de usuario debe estar vacio")
# elif not cp.isdigit:
#     print("Error: el codigo postal solo puede contener números")
# else:
#     print(f"Registro valido. Usuario '{name}' | CP: '{cp}'")

# text1 = "Pepe"
# text2 = "pepe"
# texto3 = "pepa" \

# if text1 == text2:
#     print("Ambos textos son iguales")
# elif text1 < text2:
#     print(f"{text1} va antes que {text2}")
# else:
#     print("{text2} va antes que {text1}")




estado = int (input("Introduce el codigo de estado http: "))

match estado:
    case 200 | 201:
        print("Codigo exitoso")
    case 400 | 401 | 403 | 404:
        print("Error de cliente")
    case 500 | 503: 
        print("Error de servidor")
    case _:
        print("Código de estado no reconocido")