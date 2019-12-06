from .Base_Declarativa import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.db import engine, Session
from app import app
from . import Voto
from . import Candidato

session = Session()

class Eleicao(Base):
    __tablename__ = 'eleicao'

    id = Column(Integer, primary_key=True)
    descricao = Column(String(254), nullable=False)
    inicio = Column(DateTime, nullable=False)
    fim = Column(DateTime, nullable=False)
    candidatos = relationship("Candidato")
    votos = relationship("Voto")
