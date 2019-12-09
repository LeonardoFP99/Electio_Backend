from sqlalchemy import Column, Integer, ForeignKey
from .Usuario import UsuarioAbstrato

class Administrador(UsuarioAbstrato):
    __tablename__ = 'administrador'
    
    id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity':'administrador',
    }
