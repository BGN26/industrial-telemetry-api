import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


def test_ingest_telemetry(client):
    #Prueba que la API guarda los datos del sensor.
    response = client.post(
        "/api/v1/telemetry",
        json={"reactor_id": "TEST-999", "temperature": 150.0, "pressure": 3.0}
    )

    assert response.status_code == 201
    data = response.json()
    assert data["reactor_id"] == "TEST-999"
    assert data["temperature"] == 150.0
    assert "id" in data


def test_get_reactor_analytics(client):
    #Prueba que la API calcula bien las medias de temperatura y presion
    response = client.get("/api/v1/analytics/TEST-999")

    assert response.status_code == 200
    data = response.json()
    assert data["reactor_id"] == "TEST-999"
    assert data["reading_count"] >= 1
    assert data["avg_temperature"] == 150.0