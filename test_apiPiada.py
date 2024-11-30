import requests
import pytest

# URL base da API JokeAPI
API_URL = "https://v2.jokeapi.dev/joke"

# Função para pegar uma piada aleatória
def get_random_joke(category="Programming"):
    response = requests.get(f"{API_URL}/{category}")
    return response

# Teste de sucesso - Verificar se a requisição retorna status code 200
def test_get_joke_success():
    response = get_random_joke("Programming")
    
    # Verifica se o código de status é 200
    assert response.status_code == 200
    
    # Verifica se a resposta contém a chave "category" com o valor esperado
    data = response.json()
    assert data["category"] == "Programming"
    
    # Verifica se a resposta contém a chave "delivery" (a piada) e se ela é uma string
    if "delivery" in data:
        assert isinstance(data["delivery"], str)
    else:
        assert data["error"] is False  # Se não houver "delivery", deve ser uma resposta válida sem erro

# Teste de erro - Categoria inválida
def test_get_joke_invalid_category():
    response = get_random_joke("CategoriaInvalida")  # Categoria que não existe
    
    # Verifica se o código de status não é 200
    assert response.status_code != 200  # Espera-se que o código não seja 200

    # Verifica se a resposta é JSON
    try:
        data = response.json()
        assert "error" in data
        assert data["error"] is True
    except ValueError:
        print("A resposta não contém JSON válido, conteúdo da resposta:", response.text)
        pytest.fail("A resposta não contém JSON válido.")

# Teste de erro - Sem categoria fornecida
def test_get_joke_missing_category():
    response = get_random_joke("")  # Sem categoria
    
    # Verifica se o código de status é 200 (ou o esperado para essa situação)
    assert response.status_code == 200, f"Status code inesperado: {response.status_code}"
    
    # Verifica o tipo de conteúdo da resposta
    content_type = response.headers.get("Content-Type", "")
    if "application/json" in content_type:
        # Se a resposta for JSON, tenta fazer o parse
        try:
            data = response.json()
            assert "error" in data, "Resposta JSON não contém a chave 'error'."
            assert data["error"] is True, "A chave 'error' não é True."
        except ValueError:
            pytest.fail("A resposta contém JSON inválido.")
    elif "text/html" in content_type:
        # Se a resposta for HTML, verifica se há um erro
        assert "error" in response.text.lower(), "A resposta HTML não indica um erro."
    else:
        pytest.fail(f"Tipo de conteúdo inesperado: {content_type}")

# Teste de sucesso - Verificar várias piadas aleatórias
def test_multiple_jokes():
    for _ in range(5):  # Testa 5 requisições
        response = get_random_joke("Programming")
        
        # Verifica se o código de status é 200
        assert response.status_code == 200
        
        # Verifica se a resposta contém a chave "delivery" (a piada)
        data = response.json()
        if "delivery" in data:
            assert isinstance(data["delivery"], str)
        else:
            assert data["error"] is False  # Se não houver "delivery", não deve ser erro
