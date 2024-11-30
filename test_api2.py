# 2. Sugere atividades aleatórias para quando o usuário está entediado pensando em esportes

import responses
import pytest
import requests

BASE_URL = "https://www.boredapi.com/api/activity"

@responses.activate
def test_mock_success_suggested_sport_activity():
    """
    Simula a resposta bem-sucedida da API para uma atividade recreativa.
    """
    responses.add(
        responses.GET,
        f"{BASE_URL}?type=recreational",
        json={"activity": "Play basketball", "type": "recreational", "participants": 5},
        status=200
    )

    response = requests.get(f"{BASE_URL}?type=recreational")
    assert response.status_code == 200
    data = response.json()
    assert data["activity"] == "Play basketball"
    assert data["type"] == "recreational"
    assert data["participants"] == 5

@responses.activate
def test_mock_error_invalid_activity_type():
    """
    Simula a resposta da API para um tipo de atividade inválido.
    """
    responses.add(
        responses.GET,
        f"{BASE_URL}?type=unknown_type",
        json={"error": "Invalid type parameter"},
        status=400
    )

    response = requests.get(f"{BASE_URL}?type=unknown_type")
    assert response.status_code == 400
    data = response.json()
    assert "error" in data
    assert data["error"] == "Invalid type parameter"
