from flask_restful import Resource, reqparse
from models.libro import LibroModel


class LibrosController(Resource):
    def get(self):
        resultado = LibroModel.query.all()
        respuesta = []
        for libro in resultado:
            respuesta.append(libro.devolverJson())
            print(libro.devolverJson())
        return{
            'ok': True,
            'content': respuesta,
            'message': None
        }

    def post(self):
        parseador = reqparse.RequestParser()
        parseador.add_argument(
            'titulo',
            type=str,
            required=True,
            location='json',
            help='Falta el campo titulo'
        )
        parseador.add_argument(
            'autor',
            type=str,
            required=True,
            location='json',
            help='Falta el autor'
        )
        parseador.add_argument(
            'año',
            type=int,
            required=True,
            location='json',
            help='Falta la año'
        )
        parseador.add_argument(
            'cantidad',
            type=int,
            required=True,
            location='json',
            help='Falta la cantidad'
        )
        parseador.add_argument(
            'isb',
            type=str,
            required=True,
            location='json',
            help='Falta el isb'
        )
        resultado = parseador.parse_args()
        nuevoLibro = LibroModel(resultado['titulo'], resultado['autor'], resultado['año'],
                                resultado['cantidad'],  resultado['isb'])
        nuevoLibro.save()
        # print(nuevoLibro.id_libro)
        return{
            'ok': True,
            'message':'Libro creado con exito',
            'content': nuevoLibro.devolverJson()
        }, 201


class LibroController(Resource):
    def get(self, id):
        # Select * from libro where param=valor
        # al usar el metodo first() va a devolver la primera coincidencia y ya
        # no una lista, sino un objeto en concreto
        resultado = LibroModel.query.filter_by(id_libro=id).first()
        if resultado:
            return {
                'ok': True,
                'content': resultado.devolverJson(),
                'message': None
            }
        else:
            return{
                'ok': False,
                'content': None,
                'message': 'No existe ese libro'
            }, 404

    def put(self, id):
        resultado = LibroModel.query.filter_by(id_libro=id).first()
        if resultado:
            parseador = reqparse.RequestParser()
            parseador.add_argument(
                'titulo',
                type=str,
                required=True,
                location='json',
                help='Falta el campo titulo'
            )
            parseador.add_argument(
                'autor',
                type=str,
                required=True,
                location='json',
                help='Falta el autor'
            )
            parseador.add_argument(
                'año',
                type=int,
                required=True,
                location='json',
                help='Falta la año'
            )
            parseador.add_argument(
                'cantidad',
                type=int,
                required=True,
                location='json',
                help='Falta la cantidad'
            )
            parseador.add_argument(
                'isb',
                type=str,
                required=True,
                location='json',
                help='Falta el isb'
            )
            body = parseador.parse_args()
            resultado.update(titulo=body['titulo'], autor=body['autor'],
                            año=body['año'], cantidad=body['cantidad'],  isb=body['isb'])
            return{
                'ok':True,
                'content':resultado.devolverJson(),
                'message':'Libro actualizado con exito'
            },201
        else:
            return{
                'ok': False,
                'content': None,
                'message':'No existe ese libro'
            },404
    def delete(self, id):
        resultado = LibroModel.query.filter_by(id_libro=id).first()
        if resultado:
            resultado.delete()
            return{
                'ok':True,
                'content':None,
                'message':'Se ha eliminado exitosamente el libro'
            }
        else:
            return{
                'ok': False,
                'content': None,
                'message': 'No existe ese libro'
            },404
