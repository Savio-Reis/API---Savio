from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# importando os elementos definidos no modelo
from model.base import Base
from model.local import Local
from model.reserva import Reserva

db_path = "database/"
# Verifica se o diretorio não existe
if not os.path.exists(db_path):
   # então cria o diretorio
   os.makedirs(db_path)

# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
db_url = 'sqlite:///%s/db.sqlite3' % db_path

# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)

# cria o banco se ele não existir 
if not database_exists(engine.url):
    create_database(engine.url) 
    
    # cria as tabelas do banco, caso não existam
    Base.metadata.create_all(engine)

    locais =[Local(nome = "Academia"), Local(nome="Salão de Festas"), Local(nome="Piscina")]
    # criando conexão com a base
    session = Session()
    # adicionando 3 locais possiveis padrão
    for local in locais:
        session.add(local)
    # efetivando o comando de adição de novos itens na tabela
    session.commit()