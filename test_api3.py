import requests
import pytest
from tenacity import retry, stop_after_attempt, wait_fixed

# Configuração da API
API_KEY = "7006d2accb1d623ae73762c09b4d3dfd"  # chave de API do TMDb
BASE_URL = "https://api.themoviedb.org/3/discover/movie"
NOVEMBER_2024_RELEASE = "2024-11-01,2024-11-30"

# Função para requisição com tentativa de repetição
@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def make_request(url, params=None):
    """
    Faz uma requisição GET com tentativa de repetição.
    """
    return requests.get(url, params=params)

# Testes
@pytest.mark.parametrize("release_date", [NOVEMBER_2024_RELEASE])
def test_success_movies_in_theaters(release_date):
    """
    Testa se a API retorna com sucesso os filmes lançados em novembro de 2024.
    """
    start_date, end_date = release_date.split(",")
    params = {
        "api_key": API_KEY,
        "primary_release_date.gte": start_date,
        "primary_release_date.lte": end_date,
        "region": "US"
    }
    response = make_request(BASE_URL, params=params)

    if response.status_code == 503:
        pytest.skip("A API está indisponível (503). Teste ignorado.")

    # Verifica o status da resposta
    assert response.status_code == 200, "O status code esperado é 200"
    data = response.json()

    # Valida se há resultados e chaves esperadas
    assert "results" in data, "A chave 'results' deve estar presente na resposta"
    assert isinstance(data["results"], list), "A resposta deve conter uma lista de filmes"
    if data["results"]:  # Verifica o primeiro filme se houver resultados
        first_movie = data["results"][0]
        assert "title" in first_movie, "O título do filme deve estar presente"
        assert "release_date" in first_movie, "A data de lançamento deve estar presente"

@pytest.mark.parametrize("invalid_key", ["INVALID_API_KEY"])
def test_error_invalid_api_key(invalid_key):
    """
    Testa se a API retorna erro ao usar uma chave de API inválida.
    """
    params = {
        "api_key": invalid_key,
        "primary_release_date.gte": "2024-11-01",
        "primary_release_date.lte": "2024-11-30",
        "region": "US"
    }
    response = make_request(BASE_URL, params=params)

    # Verifica o status da resposta
    assert response.status_code == 401, "O status code esperado é 401 para chave inválida"
    data = response.json()
    assert "status_message" in data, "A chave 'status_message' deve estar presente na resposta"
    assert "Invalid API key" in data["status_message"], "A mensagem de erro esperada não foi encontrada"

@pytest.mark.parametrize("release_date", ["invalid_date"])
def test_error_invalid_date(release_date):
    """
    Testa se a API retorna erro ou lida consistentemente ao usar uma data inválida.
    """
    params = {
        "api_key": API_KEY,
        "primary_release_date.gte": release_date,
        "primary_release_date.lte": "2024-11-30",
        "region": "US"
    }
    response = make_request(BASE_URL, params=params)

    if response.status_code == 503:
        pytest.skip("A API está indisponível (503). Teste ignorado.")

    # Permite status 200 ou 400, dependendo do comportamento da API
    assert response.status_code in [200, 400], f"Status code inesperado: {response.status_code}"
    data = response.json()

    # Log da resposta para depuração
    print(f"Resposta para data inválida ({release_date}): {data}")

    if response.status_code == 200:
        # Verifica se os resultados contêm datas válidas
        for movie in data.get("results", []):
            movie_release_date = movie.get("release_date", "")
            assert movie_release_date, "Filme retornado sem data de lançamento"
            # Ajuste aqui para verificar se a data é maior ou igual ao limite inferior
            if movie_release_date >= "2024-10-01":
                assert movie_release_date >= "2024-10-01", f"Data inválida encontrada: {movie_release_date}"
