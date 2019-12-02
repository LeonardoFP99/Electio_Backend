from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(254), nullable=False)
    senha = Column(String(32), nullable=False)
    tipo = Column(String(7), nullable=False) #Define se o usuário pode votar ou manter eleições
    token = Column(String(254), nullable=False) #Token para recuperação de senha
    votos = relationship("Voto")

class Eleicao(Base):
    __tablename__ = 'eleicoes'

    id = Column(Integer, primary_key=True)
    descricao = Column(String(254), nullable=False)
    inicio = Column(DateTime, nullable=False)
    fim = Column(DateTime, nullable=False)
    candidatos = relationship("Candidato")
    votos = relationship("Voto")


class Candidato(Base):
    __tablename__ = 'candidatos'

    id = Column(Integer, primary_key=True)
    nome = Column(String(60), nullable=False)
    partido = Column(String(60))
    eleicao_id = Column(Integer, ForeignKey('eleicoes.id'), nullable=False)
    votos = relationship("Voto")


class Voto(Base):
    __tablename__ = 'votos'

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    candidato_id= Column(Integer, ForeignKey('candidatos.id'), nullable=False)
    eleicao_id = Column(Integer, ForeignKey('eleicoes.id'), nullable=False)
    