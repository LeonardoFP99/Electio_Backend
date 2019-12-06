from .Base_Declarativa import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.db import engine, Session
from app import app
from . import Eleitor
from . import Candidato
from . import Eleicao

session = Session()

class Voto(Base):
    __tablename__ = 'voto'

    id = Column(Integer, primary_key=True)
    eleitor_id = Column(Integer, ForeignKey('eleitor.id'), nullable=False)
    candidato_id = Column(Integer, ForeignKey('candidato.id'), nullable=False)
    eleicao_id = Column(Integer, ForeignKey('eleicao.id'), nullable=False)


