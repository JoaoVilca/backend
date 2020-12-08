from base_de_datos import bd

class UsuarioModel(bd.Model):
    __tablename__="usuario"
    id_usuario = bd.Column('id_usuario', bd.Integer, primary_key = True, autoincrement=True, nullable=False)
    nombres_usuario = bd.Column('nombres', bd.String(50), nullable=False)
    apellidos_usuario = bd.Column('apellidos', bd.String(50), nullable=False)
    dni_usuario = bd.Column('dni', bd.Integer, nullable=False)
    direccion_usuario = bd.Column('direccion', bd.String(50), nullable=False)
    telefono_usuario = bd.Column('telefono', bd.Integer, nullable=False)
    prestamosUsuario = bd.relationship('PrestamoModel', backref='usuarioPrestamo')

    def __init__(self, nombres, apellidos, dni, direccion, telefono):
        self.nombres_usuario = nombres
        self.apellidos_usuario=apellidos
        self.dni_usuario=dni
        self.direccion_usuario=direccion
        self.telefono_usuario=telefono
    def save(self):
        bd.session.add(self)
        bd.session.commit()
    def devolverJson(self):
        return{
            'id_usuario':self.id_usuario,
            'nombres':self.nombres_usuario,
            'apellidos':self.apellidos_usuario,
            'dni':self.dni_usuario,
            'direccion':self.direccion_usuario,
            'telefono':self.telefono_usuario
        }
    def devolverUsuarioPrestamo(self):
        resultado = self.devolverJson()
        prestamos = []
        for prestamo in self.prestamosUsuario:
            prestamos.append(prestamo.devolverJson())
        resultado['prestamos']=prestamos
        return 
        {
            'id_usuario':self.id_usuario,
            'nombres':self.nombres_usuario,
            'apellidos':self.apellidos_usuario,
            'dni':self.dni_usuario,
            'direccion':self.direccion_usuario,
            'telefono':self.telefono_usuario,
            'prestamos':prestamos

        }
    