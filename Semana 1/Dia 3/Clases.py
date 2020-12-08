class Perro():
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

class Pastor_Aleman(Perro):
    def __init__(self, olfato, nombre, edad, raza):
        self.olfato = olfato
        super().__init__(nombre, edad, raza)

class Schnauzer(Perro):
    def __init__(self, velocidad, nombre, edad, raza):
        self.velocidad = velocidad
        super().__init__(nombre, edad, raza)

objPerro = Perro('Firulais', 5, 'Arto')
objSchnauzer = Schnauzer('alta', 'Morocha', 8, 'Poco')
nombrePero = objPerro.nombre
print(nombrePero)