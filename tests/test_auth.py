from fastapi.testclient import TestClient

from auth_app.app import app, FIXED_USER_EMAIL, FIXED_USER_PASSWORD


client = TestClient(app)


def test_auth_sucesso():
    payload = {"email": FIXED_USER_EMAIL, "password": FIXED_USER_PASSWORD}
    response = client.post("/auth", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert "token" in data
    assert data["token"] == "fake-jwt-token"
    assert data["message"] == "Authenticated"


def test_auth_erro_credenciais_invalidas():
    payload = {"email": FIXED_USER_EMAIL, "password": "senha_errada"}
    response = client.post("/auth", json=payload)

    assert response.status_code == 401
    data = response.json()

    assert data["detail"] == "Invalid credentials"


def test_auth_erro_email_invalido():
    payload = {"email": "email-invalido", "password": FIXED_USER_PASSWORD}
    response = client.post("/auth", json=payload)

    assert response.status_code == 422
