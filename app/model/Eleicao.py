from .Base_Declarativa import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from app import ma
from . import Voto
from . import Candidato

class Eleicao(Base):
    __tablename__ = 'eleicao'

    id = Column(Integer, primary_key=True)
    descricao = Column(String(254), nullable=False)
    inicio = Column(DateTime)
    fim = Column(DateTime)
    agendada = Column(Boolean, nullable=False)
    candidatos = relationship("Candidato")
    votos = relationship("Voto")


class EleicaoSchema(ma.ModelSchema):
    class Meta:
        model = Eleicao
