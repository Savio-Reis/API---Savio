from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from  model import Base


class Local(Base):
    __tablename__ = 'locais'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)

    def __init__(self, nome:str):
        """
        Cria um Local

        Arguments:
            nome: o texto de um comentário.
            data_insercao: data de quando o comentário foi feito ou inserido
                           à base
        """
        self.nome = nome
