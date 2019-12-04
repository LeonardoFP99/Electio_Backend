from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from db import engine, Session
from app import app
from flask_bcrypt import Bcrypt

Base = declarative_base()
session = Session()
bcrypt = Bcrypt(app)

class Voto(Base):
    __tablename__ = 'voto'

    id = Column(Integer, primary_key=True)
    eleitor_id = Column(Integer, ForeignKey('eleitor.id'), nullable=False)
    candidato_id= Column(Integer, ForeignKey('candidato.id'), nullable=False)
    eleicao_id = Column(Integer, ForeignKey('eleicao.id'), nullable=False)


Base.metadata.create_all(engine)