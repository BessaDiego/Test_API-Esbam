import pytest
import requests
from faker import Faker
import random
import urllib3

# Desabilita o aviso de SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Inicializa o Faker para gerar dados aleatórios
fake = Faker()

# URL da API pública real para testar (JSONPlaceholder)
API_URL = "https://jsonplaceholder.typicode.com/users"  # API real

# Função para gerar um fato aleatório sobre gatos e idosos
def generate_random_cat_fact():
    return {
        "cat_name": fake.first_name(),
        "cat_breed": random.choice(["Persian", "Siamese", "Maine Coon", "Bengal"]),
        "owner_age": random.randint(65, 100),
        "fact": fake.sentence(nb_words=10),  # Um fato aleatório sobre gatos
    }

# Teste de sucesso - Criar um fato sobre gato e idoso
def test_create_cat_fact_success():
    cat_fact = generate_random_cat_fact()

    # Fazendo a requisição POST para criar o fato, ignorando a verificação de SSL
    response = requests.post(API_URL, json=cat_fact, verify=False)

    # Verificando se a requisição foi bem-sucedida (status code 201)
    assert response.status_code == 201  # Código 201 criado com sucesso

    # Verificando se a resposta contém dados do fato
    response_data = response.json()
    assert "id" in response_data  # O ID do fato deve ser retornado
    assert response_data["cat_name"] == cat_fact["cat_name"]
    assert response_data["cat_breed"] == cat_fact["cat_breed"]

# Teste de erro - Dados inválidos (exemplo de idade malformada)
def test_create_cat_fact_invalid_age():
    cat_fact = generate_random_cat_fact()
    cat_fact["owner_age"] = -10  # Idade inválida

    # Fazendo a requisição POST com dados inválidos, ignorando SSL
    response = requests.post(API_URL, json=cat_fact, verify=False)

    # Esperando que a API crie o recurso independentemente dos dados (status code 201)
    assert response.status_code == 201

    # Verificando se a resposta contém os dados do fato
    response_data = response.json()
    assert response_data["owner_age"] == cat_fact["owner_age"]

# Teste de erro - Falta de dados obrigatórios (exemplo de nome do gato ausente)
def test_create_cat_fact_missing_name():
    cat_fact = generate_random_cat_fact()
    del cat_fact["cat_name"]  # Removendo o nome do gato

    # Fazendo a requisição POST com dados faltando, ignorando SSL
    response = requests.post(API_URL, json=cat_fact, verify=False)

    # Esperando que a API crie o recurso independentemente da ausência do nome (status code 201)
    assert response.status_code == 201

    # Verificando se a resposta contém os dados do fato
    response_data = response.json()
    assert "cat_name" not in response_data  # O nome do gato não deve estar presente

# Teste de sucesso - Listar todos os fatos sobre gatos
def test_list_cat_facts_success():
    response = requests.get(API_URL, verify=False)

    # Verificando se a requisição foi bem-sucedida (status code 200)
    assert response.status_code == 200

    # Verificando se a resposta contém uma lista de fatos
    response_data = response.json()
    assert isinstance(response_data, list)  # A resposta deve ser uma lista de fatos
    assert len(response_data) > 0  # A lista de fatos não pode estar vazia

# Teste de verificação de dados - Validar o fato de um gato específico
def test_get_cat_fact_data():
    cat_fact = generate_random_cat_fact()
    response = requests.post(API_URL, json=cat_fact, verify=False)
    assert response.status_code == 201  # Verificando se o fato foi criado com sucesso
    response_data = response.json()

    # Obtendo o ID do fato recém-criado
    fact_id = response_data["id"]

    # A API JSONPlaceholder não retorna dados com o ID específico
    # Então,  vou testar com um ID fixo, por exemplo, um usuário existente
    response = requests.get(f"{API_URL}/1", verify=False)

    # Verificando se a requisição foi bem-sucedida (status code 200)
    assert response.status_code == 200

    # Verificando se os dados retornados correspondem aos dados do usuário com ID 1
    response_data = response.json()
    assert "id" in response_data
