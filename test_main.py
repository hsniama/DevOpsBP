from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_post_devops_with_valid_apikey():
    response = client.post(
        "/DevOps",
        headers={"X-Parse-REST-API-Key": "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"},
        json={"message": "This is a test", "to": "Juan Perez", "from_": "Rita Asturia", "timeToLifeSec": 45}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Juan Perez your message will be send"}

def test_post_devops_with_invalid_apikey():
    response = client.post(
        "/DevOps",
        headers={"X-Parse-REST-API-Key": "invalid-api-key"},
        json={"message": "This is a test", "to": "Juan Perez", "from_": "Rita Asturia", "timeToLifeSec": 45}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized"}

def test_invalid_methods():
    response = client.get("/DevOps")
    assert response.status_code == 200
    assert response.text == '"ERROR metodo diferente a POST"'
