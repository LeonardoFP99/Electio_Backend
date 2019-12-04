from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from db import engine, Session
from app import app
from flask_bcrypt import Bcrypt

Base = declarative_base()
session = Session()
bcrypt = Bcrypt(app)

class Usuario(Base):
    __tablename__ = 'usuario'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(254), nullable=False)
    senha = Column(String(32), nullable=False)
    token = Column(String(254), nullable=False) #Token para recuperação de senha
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity':'usuario',
        'polymorphic_on':type
    }

    def registrar(self, novo_email, nova_senha):
        pass

    def login(self, log_email, log_senha):
        pass


Base.metadata.create_all(engine)