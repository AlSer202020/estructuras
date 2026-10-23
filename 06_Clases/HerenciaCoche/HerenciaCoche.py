class Coche:

    ruedas = 4

    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    def acelera(self):
        self.velocidad += self.aceleracion

class CocheValor(Coche):
    ruedas = 6

    def __init__(self, color, aceleracion, esta_volando=False):
        super().__init__(color, aceleracion)
        self.esta_volando = esta_volando

    def vuela(self):
        self.esta_volando = True

cv1 = CocheValor("Rojo", 60)

cv1.acelera()
print(f"Velocdad coche valor: {cv1.velocidad}")
print(f"¿Vuela?: {cv1.esta_volando}")

# Verificacion explícita de tipos con instance e issubclass
print("cv1 es instancia de cochevalor?", isinstance(cv1, CocheValor))
print("cv1 es instancia de coche?", isinstance(cv1, Coche))
print("Cochevalores instancia de coche?", isinstance(cv1, Coche))
print("cv1 es instancia de coche?", isinstance(cv1, Coche))