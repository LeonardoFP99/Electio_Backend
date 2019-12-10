from .Base_Declarativa import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app import ma
from . import Eleicao
from . import Voto

class Candidato(Base):
    __tablename__ = 'candidato'

    id = Column(Integer, primary_key=True)
    nome = Column(String(60), nullable=False)
    partido = Column(String(60), default="Independente")
    eleicao_id = Column(Integer, ForeignKey('eleicao.id'), nullable=False)
    votos = relationship("Voto")


class CandidatoSchema(ma.ModelSchema):
    class Meta:
        model = Candidato

