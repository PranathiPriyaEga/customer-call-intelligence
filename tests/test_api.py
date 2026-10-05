from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root_endpoint():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json()["status"] == "running"


def test_analyze_endpoint():

    response = client.post(
        "/analyze",
        json={
            "conversation":
            "My company VPN keeps disconnecting while I am working from home."
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["intent"] == "VPN Issue"

    assert data["priority"] == "High"

    assert data["queue"] == "Network Support"

    assert "ai_recommendation" in data


def test_invalid_request():

    response = client.post(
        "/analyze",
        json={}
    )

    assert response.status_code == 422

