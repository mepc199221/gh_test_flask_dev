import pytest
import requests
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_users(client):
    response = client.get("/users")

    # Debe responder 200
    assert response.status_code == 200, "El endpoint no retornó 200"

    data = response.get_json()

    # Debe ser una lista
    assert isinstance(data, list), "La respuesta no es una lista"

    # Debe tener exactamente 10 usuarios
    assert len(data) == 10, f"Se esperaban 10 usuarios, llegaron {len(data)}"

    # Cada usuario debe tener al menos id y name
    for user in data:
        assert "id" in user, "Falta el campo id"
        assert "name" in user, "Falta el campo name"
