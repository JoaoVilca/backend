def saludar():
    """Funcion que te saluda"""
    print("Hola buenas noches")


saludar()


def saludarNombre(nombre):
    print(f"Hola {nombre}")


saludarNombre('Joao')


def saludoOpcional(nombre=""):
    print(f"Hola{nombre}")


saludoOpcional()
saludoOpcional('Joao')


def suma(num1, num2):
    """Funcion que recibe dos numeros y retorna su sumatoria"""
    return num1 + num2


resultado = suma(5, 2)
print(resultado)


def hobbies(*args):
    print(args)


hobbies('bicicleta', 'puenting', 'rafting')
# **kuargs 'keywords arguments' es un parametro para recibir un numero
# ilimitado de parametros pero usando llave y valor (diccionario)


def personas(**kwargs):
    print(kwargs)


personas(nombre='Eduardo', apellido='De rivero', mascotas=False)

def indeterminada(*args, **kwargs):
    print(args)
    print(kwargs)
indeterminada(5,'juan','otoño',False,pais='peru', epoca='republicana')

# Funciones lambda
# Pequeña y anonima
# Nombre = lambda Param: return(rpta)
resultado = lambda numero: numero+30
resultado2 = lambda numero1, numero2: numero1+numero2
print(resultado(10))
print(resultado2(80,20))
# Generalmente se usa para operaciones cortas de un maximo de una linea de resolucion


