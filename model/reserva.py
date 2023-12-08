from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Reserva(Base):
    __tablename__ = 'reservas'

    id = Column(Integer, primary_key=True)
    nome_pessoa = Column(String(100), unique=True)
    data = Column(DateTime)

    # Definição do relacionamento entre reserva,nome e local.
    # Essa relação é implicita, não está salva na tabela 'reserva',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    local_id = Column(Integer, ForeignKey("locais.id"))
    local = relationship('Local',
                           uselist=False)
    

    def __init__(self, nome_pessoa:str, data:DateTime, local_id:int):
        """
        Cria uma Reserva

        Arguments:
            nome_pessoa: nome da pessoa efetuando a reserva.
            data: data da reserva
            local_id: id do local selecionado para a reserva
        """
        self.nome_pessoa = nome_pessoa
        self.data = data
        self.local_id = local_id
