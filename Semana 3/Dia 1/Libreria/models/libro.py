# https://flask-sqlalchemy.palletsprojects.com/en/2.x/
# https://docs.sqlalchemy.org/en/13/core/type_basics.html
from base_de_datos import bd

class LibroModel(bd.Model):
    __tablename__="libro"
    id_libro= bd.Column('id_libro', bd.Integer, primary_key=True, autoincrement=True, nullable=False)
    titulo_libro = bd.Column('titulo', bd.String(50), nullable=False)
    autor_libro = bd.Column('autor', bd.String(50))
    año_libro = bd.Column('año', bd.Integer, nullable=False)
    cantidad_libro = bd.Column('cantidad', bd.Integer, nullable=False)
    isb_libro = bd.Column('isb', bd.String(10), nullable=False)
    prestamosLibro = bd.relationship('PrestamoModel', backref='libroPrestamo')
    
    def __init__(self, titulo, autor, año, cantidad, isb):
        self.titulo_libro=titulo
        self.autor_libro=autor
        self.año_libro=año
        self.cantidad_libro=cantidad
        self.isb_libro=isb
    def save(self):
        bd.session.add(self)
        bd.session.commit()
    def __str__(self):
        return self.titulo_libro
    def devolverJson(self):
        return {
            'id': self.id_libro,
            'titulo': str(self.titulo_libro),
            'autor':str(self.autor_libro),
            'año':self.año_libro,
            'cantidad':self.cantidad_libro,
            'isb':str(self.isb_libro)
        }
    def update(self, **kwargs):
        print(kwargs)
        titulo = kwargs.get('titulo') if kwargs.get('titulo') else self.titulo_libro
        autor = kwargs.get('autor') if kwargs.get('autor') else self.autor_libro
        año = kwargs.get('año') if kwargs.get('año') else self.año_libro
        cantidad = kwargs.get('cantidad') if kwargs.get('cantidad') else self.cantidad_libro
        isb = kwargs.get('isb') if kwargs.get('isb') else self.isb_libro
        print(titulo)
        self.titulo_libro = titulo
        self.año_libro=autor
        self.año_libro=año
        self.cantidad_libro=cantidad
        self.isb_libro=isb
        self.save()
    
    def delete(self):
        bd.session.delete(self)
        bd.session.commmit()
    def inhabilitarLibro(self):
        pass