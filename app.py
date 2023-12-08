from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Reserva, Local
from logger import logger
from schemas import *
from flask_cors import CORS

from datetime import datetime

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
reserva_tag = Tag(name="Reserva", description="Adição, visualização e remoção de reservas à base")
local_tag = Tag(name="Local", description="Visualização de locais")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

# adiciona as reservas no baco de dados
@app.post('/reserva', tags=[reserva_tag],
          responses={"200": ReservaViewSchema,"409": ErrorSchema, "400": ErrorSchema})
def add_reserva(form: ReservaSchema):
    """Adiciona uma nova reserva à base de dados

    Retorna uma representação da reserva e local associado.
    """
    print(form.data)
    # criar nova classe reserva com base nos dados recebidos
    reserva = Reserva(
        nome_pessoa = form.nome_pessoa,
        data = form.data,
        local_id = form.local_id)
    
    logger.debug(f"Adicionando nova reserva: '{reserva.nome_pessoa}'")
    
    try:
        # criando conexão com a base
        session = Session()

        # adicionando reserva
        session.add(reserva)

        # comando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado reserva em nome de: '{reserva.nome_pessoa}'")
        return apresenta_reserva(reserva), 200

    except Exception as e:
        # caso ocorra um erro
        error_msg = "Não foi possível salvar nova reserva, verifique se essa pessoa já possui reserva"
        logger.warning(f"Erro ao adicionar reserva '{reserva.nome_pessoa}', {error_msg}")
        return {"message": error_msg}, 400
    
    except IntegrityError as e:
        # não permite mais de uma reserva para a mesma pessoa
        error_msg = "Pessoa já está com uma reserva agendada"
        logger.warning(f"Erro ao adicionar r '{reserva.nome_pessoa}', {error_msg}")
        return {"mesage": error_msg}, 409


# busca por todas as reservas cadastradas
@app.get('/reservas', tags=[reserva_tag],
         responses={"200": ListagemReservasSchema, "404": ErrorSchema})
def get_reservas():
    """Faz a busca por todos as Reservas cadastradas

    Retorna uma representação da listagem de reservas.
    """
    logger.debug(f"Coletando reservas ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    reservas = session.query(Reserva).all()

# verifica se não há reservas cadastrados
    if not reservas:
        
        return {"reservas": []}, 200
    else:
        logger.debug(f"%d reservas econtradas" % len(reservas))
        # retorna a representação de reserva
        print(reservas)
        return apresenta_reservas(reservas), 200

# deleta reservas selecionadas
@app.delete('/reserva', tags=[reserva_tag],
            responses={"200": ReservaDelSchema, "404": ErrorSchema})
def del_reserva(query: ReservaBuscaSchema):
    """Deleta uma reservar a partir do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
    logger.debug(f"Deletando dados sobre reserva #{query.id}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Reserva).filter(Reserva.id == query.id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado a reserva #{query.id}")
        return {"message": "Reserva removida", "id": query.id}
    else:
        # se a reserva não foi encontrada
        error_msg = "Reserva não encontrado na base."
        logger.warning(f"Erro ao deletar reserva #'{query.id}', {error_msg}")
        return {"message": error_msg}, 404


# busca de locais 
@app.get('/locais', tags=[local_tag],
         responses={"200": ListagemLocaisSchema, "404": ErrorSchema})
def get_locais():
    """Faz a busca por todos os locais cadastrados

    Retorna uma representação da listagem de locais.
    """
    logger.debug(f"Coletando locais ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    locais = session.query(Local).all()

    if not locais:
        # se não há locais cadastrados
        return {"locais": []}, 200
    else:
        logger.debug(f"%d locais econtradas" % len(locais))
        # retorna a representação de locais
        return apresenta_locais(locais), 200