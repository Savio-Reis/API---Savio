# Minha API

Este pequeno projeto faz parte da Disciplina **Desenvolvimento Full Stack Básico** 
O objetivo aqui é criar um gerenciador de reservas utlizando nome, data e local.
Esta API é baseada na documentação Swagger.
Possui 4 Endpoints: POST /reserva, GET /reservas, GET /locais, DELETE /reserva

Endpoint: POST /reserva
Parâmetros de entrada:
form (corpo da solicitação): Dados da reserva a serem adicionados.
Respostas:
200 OK: Retorna uma representação da reserva e do local associado.
409 Conflict: Retorna uma mensagem de erro se a pessoa já tiver uma reserva agendada.
400 Bad Request: Retorna uma mensagem de erro se não for possível salvar a nova reserva.

Endpoint: GET /reservas
Respostas:
200 OK: Retorna uma representação da listagem de reservas.
404 Not Found: Retorna uma mensagem de que não há reservas cadastradas.

Endpoint: GET /locais
Respostas:
200 OK: Retorna uma representação da listagem de locais.
404 Not Found: Retorna uma mensagem de que não há locais cadastrados.


Endpoint: DELETE /reserva
Parâmetros de entrada:
query (corpo da solicitação): ID da reserva a ser removida.
Respostas:
200 OK: Retorna uma mensagem de confirmação da remoção.
404 Not Found: Retorna uma mensagem de erro se a reserva não for encontrada na base.

## Como executar 

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```


Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
