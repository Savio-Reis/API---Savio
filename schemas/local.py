from pydantic import BaseModel
from typing import List
from model.local import Local


class LocalSchema(BaseModel):
    """ Define como um novo local a ser inserido deve ser representado
    """
    id: int = 1
    nome: str = "Academia"

class ListagemLocaisSchema(BaseModel):
    """ Define como uma listagem de locais que serão retornados.
    """
    reservas:List[LocalSchema]

def apresenta_locais(locais: List[Local]):
    """ Retorna uma representação de locais seguindo o schema definido em
        LocalSchema.
    """
    result = []
    for local in locais:
        result.append({
            "id": local.id,
            "nome": local.nome
        })

    return {"locais": result}