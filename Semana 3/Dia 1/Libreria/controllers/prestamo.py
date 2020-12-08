from flask_restful import Resource, reqparse
from models.prestamo import PrestamoModel


class PrestamosController(Resource):
    def get(self):
        resultado = PrestamoModel.query.all()
        respuesta = []
        for prestamo in resultado:
            respuesta.append(prestamo.devolverJson())
        return{
            'ok': True,
            'message': None,
            'content': respuesta
        }

    def post(self):
        parseador = reqparse.RequestParser()
        parseador.add_argument(
            'fecha_inicio',
            type=str,
            required=True,
            location='json',
            help='Falta el campo titulo'
        )
        parseador.add_argument(
            'fecha_fin',
            type=str,
            required=True,
            location='json',
            help='Falta el campo titulo'
        )
        parseador.add_argument(
            'usuario',
            type=int,
            required=True,
            location='json',
            help='Falta el campo titulo'
        )
        parseador.add_argument(
            'libro',
            type=int,
            required=True,
            location='json',
            help='Falta el campo titulo'
        )
        resultado = parseador.parse_args()
        prestamo = PrestamoModel(resultado['fecha_inicio'], resultado['fecha_fin'], resultado['usuario'], resultado['libro'])
        prestamo.save()
        return{
            'ok': True,
            'content':prestamo.devolverJson(),
            'message':'Prestamo creado exitosamente'
        },201