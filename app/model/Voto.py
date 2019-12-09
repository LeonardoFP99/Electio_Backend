from .Base_Declarativa import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from . import Eleitor
from . import Candidato
from . import Eleicao

class Voto(Base):
    __tablename__ = 'voto'

    id = Column(Integer, primary_key=True)
    eleitor_id = Column(Integer, ForeignKey('eleitor.id'), nullable=False)
    candidato_id = Column(Integer, ForeignKey('candidato.id'), nullable=False)
    eleicao_id = Column(Integer, ForeignKey('eleicao.id'), nullable=False)


