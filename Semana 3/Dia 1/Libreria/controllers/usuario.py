from flask_restful import Resource, reqparse
from models.usuario import UsuarioModel

class UsuariosController(Resource):
    def get(self):
        resultado = UsuarioModel.query.all()
        respuesta = []
        for usuario in resultado:
            respuesta.append(usuario.devolverUsuarioPrestamo())
            print(usuario.devolverJson())
        return{
            'ok': True,
            'content': respuesta,
            'message': None
        }
    def post(self):
        parseador = reqparse.RequestParser()
        parseador.add_argument(
            'nombres',
            type=str,
            required=True,
            location='json',
            help='Falta el campo titulo'
        )
        parseador.add_argument(
            'apellidos',
            type=str,
            required=True,
            location='json',
            help='Falta el campo titulo'
        )
        parseador.add_argument(
            'dni',
            type=int,
            required=True,
            location='json',
            help='Falta el campo titulo'
        )
        parseador.add_argument(
            'direccion',
            type=str,
            required=True,
            location='json',
            help='Falta el campo titulo'
        )
        parseador.add_argument(
            'telefono',
            type=int,
            required=True,
            location='json',
            help='Falta el campo titulo'
        )
        resultado = parseador.parse_args()
        nuevoUsuario = UsuarioModel(resultado['nombres'], resultado['apellidos'], resultado['dni'],
                                resultado['direccion'],  resultado['telefono'])
        nuevoUsuario.save()
        # print(nuevoLibro.id_libro)
        return{
            'ok': True,
            'message':'Usuario creado con exito',
            'content': nuevoUsuario.devolverJson()
        }, 201