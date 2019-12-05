from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.db import engine, Session
from app.geradorToken import gerarToken
from app import app
from flask_bcrypt import Bcrypt
from .Usuario import UsuarioAbstrato

Base = declarative_base()
session = Session()
bcrypt = Bcrypt(app)

class Administrador(UsuarioAbstrato):
    __tablename__ = 'administrador'
    
    id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity':'administrador',
    }

    def registrar(self, novo_email, nova_senha):

        try:

            query = session.query(Administrador).filter(Administrador.email == novo_email)

            if not query.first():

                novo_usuario = Administrador(
                    email=novo_email, 
                    senha=bcrypt.generate_password_hash(nova_senha).decode('utf-8'), 
                    token=bcrypt.generate_password_hash(gerarToken()).decode('utf-8')
                )

                try:

                    session.add(novo_usuario)
                    session.commit()

                except:
                    
                    session.rollback()
                    raise Exception("Erro ao registrar usuário.")

            else:

                raise Exception(f'O email {novo_email} já está sendo usado.')

        except:

            raise Exception("Erro ao registrar usuário.")

    
    def login(self, log_email, log_senha):

        try:

            query = session.query(Administrador).filter(Administrador.email == log_email)

            if query.first():

                if bcrypt.check_password_hash(query.senha, log_senha):

                    return True

                else:

                    raise Exception("Credenciais incorretas.")

            else:

                raise Exception(f'Não existe uma conta de eleitor associada com o email {log_email}.')

        except:

            raise Exception("Erro ao realizar login.")


Base.metadata.create_all(engine)
