class Vehiculo:
    pass
    # def __init__(self, peso):
    #     self.peso = peso
class Automovil(Vehiculo):
    def movilidad(self):
        print('Me muevo en 4 ruedas')
class Bicicleta(Vehiculo):
    def movilidad(self):
        print('Me muevo en 2 ruedas')
class Patines(Vehiculo):
    def movilidad(self):
        print('Me muevo en 6 ruedas')

miAuto = Automovil()
miAuto.movilidad()
miBicicleta = Bicicleta()
miBicicleta.movilidad()
misPatines = Patines()
misPatines.movilidad()