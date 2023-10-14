class Ninja:
    def __init__(self, nombre, apellido, mascota, premio, comida_mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.mascota = mascota
        self.premio = premio
        self.comida_mascota = comida_mascota
    
    def caminar (self):
        self.mascota.jugar()
        return self

    def alimentar(self):
        self.mascota.comer()
        return self

    def bañar(self):
        self.mascota.sonido()
        return self

class Mascota:
    def __init__(self, name, tipo , golosinas):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = 100
        self.energia = 100
    
    def dormir(self):
        self.energia += 25
        return self

    def comer(self):
        self.energia += 5
        self.salud += 10
        return self

    def jugar(self):
        self.salud += 5
        return self

    def sonido (self):
        print(f"{self.name} hace un sonido")
        
"""
Luna = Mascota("Luna", "Perro", "pizza")
lisa = Ninja("Lisa", "Park", Luna, "pollo", "bacon" )

print(f"{lisa.nombre} pasea a su mascota:")
lisa.caminar()

print(f"{lisa.nombre} alimenta a su mascota con {lisa.comida_mascota}:")
lisa.alimentar()

print(f"{lisa.nombre} baña a su mascota:")
lisa.bañar()
"""