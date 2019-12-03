from db import Session
from models import Usuario, Candidato, Eleicao, Voto
from token import gerarToken

session = Session()

class UsuarioController():

    def registrar(novo_email, nova_senha, novo_tipo):

        query = session.query(Usuario).filter(Usuario.email == novo_email)

        if not query.first():

            novo_usuario = Usuario(email=novo_email, senha=nova_senha, tipo=novo_tipo, token=gerarToken())

            try:

                session.add(novo_usuario)
                session.commit()

            except:
                
                session.rollback()
                raise Exception("Erro ao registrar usuário.")

        else:

            raise Exception(f'O email {novo_email} já está sendo usado.')