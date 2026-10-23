from PersonajeTeletubby import PersonajeTeletubby

if __name__ == "__main__":
    teletubby1 = PersonajeTeletubby("Tinky Winky", "azul", "1", "1")
    teletubby2 = PersonajeTeletubby("Po", "rojo", "2", "2")

    teletubby1.saludar()
    teletubby2.saludar()

    print(teletubby1)

    teletubby1.jugar()
    teletubby2.jugar()

    print(teletubby1.ver_estado())
    
    teletubby1.comer_tubby_papilla()

    print(teletubby1.ver_estado())