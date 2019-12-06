from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.db import engine, Session
from app.geradorToken import gerarToken
from app import app
from app import bcrypt
from .Usuario import UsuarioAbstrato
from . import Voto

session = Session()

class Eleitor(UsuarioAbstrato):
    __tablename__ = 'eleitor'
    
    id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)
    votos = relationship("Voto")

    __mapper_args__ = {
        'polymorphic_identity':'eleitor',
    }

    def registrar(self, novo_email, nova_senha):

        try:

            query = session.query(Eleitor).filter(Eleitor.email == novo_email)

            if not query.first():

                novo_usuario = Eleitor(
                    email=novo_email, 
                    senha=bcrypt.generate_password_hash(nova_senha).decode('utf-8'), 
                    token=bcrypt.generate_password_hash(gerarToken()).decode('utf-8')
                )

                try:

                    session.add(novo_usuario)
                    session.commit()
                    
                    return novo_usuario

                except:
                    
                    session.rollback()
                    raise Exception("Erro ao registrar usuário.")

            else:

                raise Exception(f'O email {novo_email} já está sendo usado.')

        except:

            raise Exception("Erro ao registrar usuário.")

    
    def login(self, log_email, log_senha):

        try:

            query = session.query(Eleitor).filter(Eleitor.email == log_email)

            if query.first():

                if bcrypt.check_password_hash(query.senha, log_senha):

                    return True

                else:

                    raise Exception("Credenciais incorretas.")

            else:

                raise Exception(f'Não existe uma conta de eleitor associada com o email {log_email}.')

        except:

            raise Exception("Erro ao realizar login.")


