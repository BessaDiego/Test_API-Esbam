# 1 API - POKEMON
retorna informações sobre Pokémon de fogo, como características 
e com mais dominio de poder.

# Estrutura dos Testes
- Testes de Sucesso:
Verifica se a API retorna status code 200 para Pokémon do tipo "fire".
Valida a presença de dados esperados no JSON de resposta.

- Testes de Erro:
Simula a consulta de um tipo de Pokémon inválido, esperando um status code 404.

- Verificação de Dados:
Valida que os Pokémon de fogo possuem características específicas, como alto domínio de poder.

# Primeiro teste executei - pytest test_api.py

# 2 API - Sugere atividades aleatórias para quando o usuário está entediado pensando em esportes

- Este projeto implementa testes de integração para a BoredAPI. 
O objetivo principal é verificar o comportamento da API ao sugerir atividades para usuários, 
especialmente relacionadas a esportes, e validar a robustez contra cenários de erro.

## Estrutura do Projeto
test_api2.py: Contém os testes automatizados, organizados em três categorias principais:

- Testes de Sucesso: Valida respostas corretas para solicitações bem formuladas.
- Testes de Erro: Simula cenários com parâmetros inválidos ou inconsistentes.
- Verificação de Dados: Confirma a presença e integridade das chaves e valores retornados no JSON.
- Mocks para Simulação: Utiliza a biblioteca responses para simular respostas da API, 
permitindo que os testes sejam executados mesmo quando o serviço estiver indisponível.

## Requisitos 
pip install pytest tenacity responses

# Executei segunda API - pytest test_api2.py -v

# 3 API -  fornece informações sobre filmes que estão no cinema no mês de novembro de 2024

- Descrição dos Testes
O arquivo test_api3.py contém os seguintes testes:

1. test_success_movies_in_theaters:

- Verifica se a API retorna filmes que estão em exibição 
no intervalo de datas especificado.

2. test_error_invalid_api_key:

- Testa o comportamento da API quando uma chave de API inválida é fornecida.

3. test_error_invalid_date:

- Verifica como a API lida com datas inválidas e se os resultados retornados 
estão dentro dos limites esperados.

## Resultados Esperados
- 200 OK: Quando a API retorna uma resposta bem-sucedida com dados de filmes.
- 400 Bad Request: Quando a API retorna erro devido a parâmetros inválidos, como datas ou chave de API incorretas.
- 503 Service Unavailable: Caso a API esteja temporariamente indisponível.

# Executei o teste - pytest test_api3.py -v

# 4 API - Fatos sobre Gatos

Este repositório contém uma série de testes automatizados para verificar o comportamento 
de uma API que fornece informações sobre gatos. Os testes são realizados usando o framework 
"pytest" em Python e simulam cenários de sucesso e falha, além de validar os dados retornados pela API.

# Como atuei para os testes funcionar 

- Testes de Sucesso: Verifica se as requisições para criar e listar fatos sobre gatos retornam
 os status codes corretos (200 para listagem, 201 para criação).

- Testes de Erro:
1. Simula cenários com dados incorretos, como:
2. Idade inválida para o dono (valor negativo).
3. Dados ausentes, como o nome do gato.

- Validação de Dados: Assegura que a resposta contém as informações esperadas,
 como chaves específicas e valores de dados correspondentes.

# Aviso de SSL que utilizei 
Durante a execução dos testes, vai perceber um aviso chamado "InsecureRequestWarning". 
Nesse aviso acontece porque fiz algumas requisições para a API sem realizar a verificação do SSL. 
O SSL (Secure Sockets Layer) é uma tecnologia que garante a segurança da comunicação entre o cliente
(no caso, nós) e o servidor, validando a identidade do servidor e criptografando os dados transmitidos.

# 5 API - retorna piadas aleatórias de categoria "Piadas temáticas."

## Estrutura do código
- Testes de sucesso: Verifica se a resposta da API retorna um código de status 200 
e se a resposta contém a chave category com o valor "Piadas temáticas".

- Testes de erro: Verifica como a API se comporta quando há uma solicitação 
inválida, como um parâmetro de categoria incorreto.

- Verificação de dados: Valida se a resposta contém a estrutura esperada, 
como um campo joke e a categoria correta.

## Estrutura dos Testes
- Funções Principais
get_random_joke(category="Programming")
Faz uma requisição para a API e retorna uma piada aleatória na categoria fornecida.

1. Testes Incluídos
- test_get_joke_success
Verifica se a API retorna com sucesso uma piada na categoria "Programming".

- test_get_joke_invalid_category
Testa o comportamento da API ao solicitar uma categoria inexistente. 
Espera-se que a resposta contenha um erro.

- test_get_joke_missing_category
Testa o comportamento da API quando nenhuma categoria é fornecida. 
Valida o tipo de resposta e os dados retornados.

- test_multiple_jokes
Realiza várias requisições consecutivas para validar a consistência e 
estrutura das respostas.

## Executei o teste - pytest test_apiPiada.py -v

## Dependências Instaladas
- pip install -r requirements.txt
- pip install pytest
- pip install requests
- pip install responses

## O arquivo requirements.txt contém as seguintes dependências:
- pytest: Framework para executar os testes unitários e de integração.
- requests: Biblioteca para realizar requisições HTTP, usada para interagir com a API.


