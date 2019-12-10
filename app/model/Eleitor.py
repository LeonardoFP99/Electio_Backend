from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app import ma
from .Usuario import UsuarioAbstrato
from . import Voto

class Eleitor(UsuarioAbstrato):
    __tablename__ = 'eleitor'
    
    id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)
    votos = relationship("Voto")

    __mapper_args__ = {
        'polymorphic_identity':'eleitor',
    }


class EleitorSchema(ma.ModelSchema):
    class Meta:
        model = Eleitor