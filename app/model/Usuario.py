from .Base_Declarativa import Base
from sqlalchemy import Column, Integer, String, DateTime
from app.db import engine, Session
from app import app
from app import bcrypt
from flask_bcrypt import Bcrypt

session = Session()

class UsuarioAbstrato(Base):
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


