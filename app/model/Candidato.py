from .Base_Declarativa import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db import engine, Session
from app import app
from . import Eleicao
from . import Voto

session = Session()

class Candidato(Base):
    __tablename__ = 'candidato'

    id = Column(Integer, primary_key=True)
    nome = Column(String(60), nullable=False)
    partido = Column(String(60))
    eleicao_id = Column(Integer, ForeignKey('eleicao.id'), nullable=False)
    votos = relationship("Voto")


