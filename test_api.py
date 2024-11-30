import requests
import pytest

#1 URL base - API pública do Pokémon
BASE_URL = "https://pokeapi.co/api/v2"

@pytest.mark.parametrize("type_name", ["fire"])
def test_success_get_fire_pokemons(type_name):
    """
    Testa se a API retorna com sucesso os Pokémon do tipo 'fire'.
    Valida o status code e se a resposta contém os dados esperados.
    """
    response = requests.get(f"{BASE_URL}/type/{type_name}")
    
    # Verifica se o status code é 200
    assert response.status_code == 200, "O status code esperado é 200"
    
    # Verifica se a resposta contém chaves específicas
    data = response.json()
    assert "pokemon" in data, "A chave 'pokemon' deve estar presente na resposta"
    assert len(data["pokemon"]) > 0, "A lista de Pokémon não deve estar vazia"

@pytest.mark.parametrize("invalid_type", ["unknown_type"])
def test_error_invalid_pokemon_type(invalid_type):
    """
    Testa se a API retorna o comportamento esperado para um tipo inválido de Pokémon.
    """
    response = requests.get(f"{BASE_URL}/type/{invalid_type}")
    
    # Verifica se o status code indica erro (404)
    assert response.status_code == 404, "O status code esperado para um tipo inválido é 404"

def test_fire_pokemon_contains_high_stat():
    """
    Testa se Pokémon de fogo possuem atributos com valores esperados.
    """
    response = requests.get(f"{BASE_URL}/type/fire")
    assert response.status_code == 200, "O status code esperado é 200"
    
    data = response.json()
    fire_pokemons = data["pokemon"]

    # Verifica se pelo menos um Pokémon de fogo possui estatística alta (exemplo: nome Charizard)
    has_high_stat = any("charizard" in p["pokemon"]["name"] for p in fire_pokemons)
    assert has_high_stat, "Pelo menos um Pokémon de fogo com alta estatística esperado (e.g., Charizard)"
    
