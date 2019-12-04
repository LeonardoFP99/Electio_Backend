from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from db import engine, Session
from app import app
from flask_bcrypt import Bcrypt

Base = declarative_base()
session = Session()
bcrypt = Bcrypt(app)

class Eleicao(Base):
    __tablename__ = 'eleicao'

    id = Column(Integer, primary_key=True)
    descricao = Column(String(254), nullable=False)
    inicio = Column(DateTime, nullable=False)
    fim = Column(DateTime, nullable=False)
    candidatos = relationship("Candidato")
    votos = relationship("Voto")


Base.metadata.create_all(engine)