from base_de_datos import bd


class PrestamoModel(bd.Model):
    __tablename__ = "prestamo"
    id_prestamo = bd.Column('id_prestamo', bd.Integer,
                            primary_key=True, autoincrement=True, nullable=False)
    fechin_prestamo = bd.Column('prestamo_fechain', bd.Date, nullable=False)
    fechfin_prestamo = bd.Column('prestamo_fechafin', bd.Date)
    # RELACIONES
    usuario_prestamo = bd.Column('id_usuario', bd.Integer, bd.ForeignKey(
        'usuario.id_usuario'), nullable=False)
    libro_prestamo = bd.Column('id_libro', bd.Integer, bd.ForeignKey(
        'libro.id_libro'), nullable=False)

    def __init__(self, fecha_inicio, fecha_fin, usuario, libro):
        self.fechin_prestamo = fecha_inicio
        self.fechfin_prestamo = fecha_fin
        self.usuario_prestamo = usuario
        self.libro_prestamo = libro
    def save(self):
        bd.session.add(self)
        bd.session.commit()
    def devolverJson(self):
        return{
            'id':self.id_prestamo,
            'fecha_inicio':str(self.fechin_prestamo),
            'fecha_fin':str(self.fechfin_prestamo),
            'usuario':self.usuario_prestamo,
            'libro':self.libro_prestamo
        }