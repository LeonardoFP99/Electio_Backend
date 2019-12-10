from sqlalchemy.ext.declarative import declarative_base
from app.db import engine
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from marshmallow_sqlalchemy import ModelSchema

Base = declarative_base()



class UsuarioAbstrato(Base):
    __tablename__ = 'usuario'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(254), nullable=False)
    senha = Column(String(32), nullable=False)
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity':'usuario',
        'polymorphic_on':type
    }




class Voto(Base):
    __tablename__ = 'voto'

    id = Column(Integer, primary_key=True)
    eleitor_id = Column(Integer, ForeignKey('eleitor.id'), nullable=False)
    candidato_id = Column(Integer, ForeignKey('candidato.id'), nullable=False)
    eleicao_id = Column(Integer, ForeignKey('eleicao.id'), nullable=False)


class VotoSchema(ModelSchema):
    class Meta:
        model = Voto




class Eleitor(UsuarioAbstrato):
    __tablename__ = 'eleitor'
    
    id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)
    votos = relationship("Voto")

    __mapper_args__ = {
        'polymorphic_identity':'eleitor',
    }


class EleitorSchema(ModelSchema):
    class Meta:
        model = Eleitor




class Administrador(UsuarioAbstrato):
    __tablename__ = 'administrador'
    
    id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity':'administrador',
    }


class AdministradorSchema(ModelSchema):
    class Meta:
        model = Administrador




class Candidato(Base):
    __tablename__ = 'candidato'

    id = Column(Integer, primary_key=True)
    nome = Column(String(60), nullable=False)
    partido = Column(String(60), default="Independente")
    eleicao_id = Column(Integer, ForeignKey('eleicao.id'), nullable=False)
    votos = relationship("Voto")


class CandidatoSchema(ModelSchema):
    class Meta:
        model = Candidato




class Eleicao(Base):
    __tablename__ = 'eleicao'

    id = Column(Integer, primary_key=True)
    descricao = Column(String(254), nullable=False)
    inicio = Column(DateTime)
    fim = Column(DateTime)
    agendada = Column(Boolean, nullable=False)
    candidatos = relationship("Candidato")
    votos = relationship("Voto")


class EleicaoSchema(ModelSchema):
    class Meta:
        model = Eleicao







