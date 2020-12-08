# setter = ingresar el valor a un atributo
# getter = devolver el valor del atributo
# deleter = elimina el atributo de una clase

class Persona:
    def __init__(self):
        self.__nombre=''
    def setNombre(self, nombre):
        print('El setNombre a sido llamado')
        self.__nombre = nombre
    def getNombre(self):
        print('El getNombre a sido llamado')
        return self.__nombre
    def deleteNombre(self):
        print('El deleteNombre a sido llamado')
        del self.__nombre
    # funcion property para reducir nuestras funcones de
    # get, set, y delete
    name = property(getNombre, setNombre, deleteNombre)

objPersona = Persona()
objPersona.name = 'Eduardo'

objPersona.name= 'Joao'
print(objPersona.name)