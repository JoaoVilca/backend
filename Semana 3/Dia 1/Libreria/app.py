from flask import Flask
from base_de_datos import bd
from flask_restful import Api
from controllers.libro import LibrosController, LibroController
from controllers.usuario import UsuariosController
from controllers.prestamo import PrestamosController
# from models.libro import LibroModel
from models.usuario import UsuarioModel
from models.prestamo import PrestamoModel
# pip3 install mysqlclient
app = Flask(__name__)
api = Api(app)
# 'tipobd://usuario:password@servidor/nomb-bd'
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#connection-uri-format
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/libreria'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.before_first_request
def creacion_bd():
    # Inicio la aplicacion pasandole la instancia app que internamente va a buscar la llave SQLALCHEMY_DATABASE_URI y si la encuentra va a conectar con la base de datos
    bd.init_app(app)
    # Va a realizar la eliminacion de todos los modelos en mi base de datos
    # bd.drop_all(app=app)
    # Va a realizar la creación de todos los modelos definidos anteriormente
    bd.create_all(app=app)


@app.route('/')
def inicio():
    return 'La api funciona exitosamente'

    # Definiendo las rutas de mi aplicacion
    # en el add_resource van dos o mas parametros, obligatoriamente en el primero va el Recurso (comportamiento)
    # y en el segundo
api.add_resource(LibrosController, '/libro')
api.add_resource(UsuariosController,'/usuario')
api.add_resource(PrestamosController, '/prestamo')
api.add_resource(LibroController, '/libro/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
