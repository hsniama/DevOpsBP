from fastapi.testclient import TestClient
from main import app
import jwt

client = TestClient(app)

# Configuramos el JWT para pruebas
JWT_SECRET = "1720844446"  # Debe siempre coincidir con la clave secreta en main.py

def create_jwt():
    # Creamos un JWT válido para pruebas
    payload = {"some": "data"}
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return token

def test_post_devops_with_valid_apikey_and_jwt():
    jwt_token = create_jwt()
    response = client.post(
        "/DevOps",
        headers={
            "X-Parse-REST-API-Key": "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c",
            "X-JWT-KWY": jwt_token
        },
        json={"message": "This is a test", "to": "Juan Perez", "from_": "Rita Asturia", "timeToLifeSec": 45}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Juan Perez your message will be send"}

def test_post_devops_with_invalid_apikey():
    jwt_token = create_jwt()
    response = client.post(
        "/DevOps",
        headers={
            "X-Parse-REST-API-Key": "invalid-api-key",
            "X-JWT-KWY": jwt_token
        },
        json={"message": "This is a test", "to": "Juan Perez", "from_": "Rita Asturia", "timeToLifeSec": 45}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized"}

def test_post_devops_with_invalid_jwt():
    response = client.post(
        "/DevOps",
        headers={
            "X-Parse-REST-API-Key": "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c",
            "X-JWT-KWY": "invalid-jwt"
        },
        json={"message": "This is a test", "to": "Juan Perez", "from_": "Rita Asturia", "timeToLifeSec": 45}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid JWT"}

def test_invalid_methods():
    response = client.get("/DevOps")
    assert response.status_code == 200
    assert response.text == '"ERROR metodo diferente a POST"'
