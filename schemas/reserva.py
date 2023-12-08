from datetime import date
from pydantic import BaseModel
from typing import List
from model.reserva import Reserva

from schemas import LocalSchema

class ReservaSchema(BaseModel):
    """ Define como uma nova reserva deve ser representada
    """
    nome_pessoa: str = "Joana"
    data: date = "2023-09-25"
    local_id: int = 1

class ReservaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca de uma reserva. Que será
        feita apenas com base no id da reserva.
    """
    id: int = 1

def apresenta_reservas(reservas: List[Reserva]):
    """ Retorna uma representação de reservas seguindo o schema definido em
        ReservasViewSchema.
    """
    result = []
    for reserva in reservas:
        result.append({
            "id": reserva.id,
            "nome_pessoa": reserva.nome_pessoa,
            "data": reserva.data,
            "local_id": reserva.local_id,
            "local": reserva.local.nome
        })

    return {"reservas": result}

class ReservaViewSchema(BaseModel):
    """ Define como uma será exibida uma reserva: reserva + local.
    """
    id: int = 1
    nome_pessoa: str = "Joana"
    data: date = "2023-12-08"
    local_id: int = "1"
    local: LocalSchema

class ListagemReservasSchema(BaseModel):
    """ Define como uma listagem de reservar será retornada.
    """
    reservas:List[ReservaViewSchema]
    
class ReservaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    nome_pessoa: str

def apresenta_reserva(reserva: Reserva):
    """ Retorna uma representação de reserva seguindo o schema definido em
        ReservaViewSchema.
    """
    return {
        "nome_pessoa": reserva.nome_pessoa,
        "data": reserva.data,
        "local_id": reserva.local_id,
        "local": reserva.local.nome
    }
