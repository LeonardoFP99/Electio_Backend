from .Base_Declarativa import Base
from sqlalchemy import Column, Integer, String

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


