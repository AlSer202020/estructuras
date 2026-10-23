class PersonajeTeletubby:
    def __init__(self, nombre, color, antena, objeto_favorito):
        self.nombre = nombre
        self.color = color
        self.antena = antena
        self.objeto_favorito = objeto_favorito
        self.__nivel_hambre = 50
        self.__nivel_felicidad = 100

    def saludar(self):
        print(f"Nombre: {self.nombre}, Color: {self.color}, Forma de antena: {self.antena}")

    def jugar(self):
        print(f"{self.nombre} esta jugando con {self.objeto_favorito}")
        self.__nivel_hambre += 20
        self.__nivel_felicidad += 10

    def comer_tubby_papilla(self):
        print(f"{self.nombre} ha comido")
        self.__nivel_hambre = 0
        self.__nivel_felicidad += 20
    
    def ver_estado(self):
        return f"Nivel de hambre: {self.__nivel_hambre}, Nivel de felicidad: {self.__nivel_felicidad}"
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Color: {self.color}, Forma de antena: {self.antena}, Nivel de hambre: {self.__nivel_hambre}, Nivel de felicidad: {self.__nivel_felicidad}"