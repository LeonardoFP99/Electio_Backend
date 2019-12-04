from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from db import engine, Session
from app import app
from flask_bcrypt import Bcrypt

Base = declarative_base()
session = Session()
bcrypt = Bcrypt(app)

class Candidato(Base):
    __tablename__ = 'candidato'

    id = Column(Integer, primary_key=True)
    nome = Column(String(60), nullable=False)
    partido = Column(String(60))
    eleicao_id = Column(Integer, ForeignKey('eleicao.id'), nullable=False)
    votos = relationship("Voto")


Base.metadata.create_all(engine)