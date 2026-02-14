from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


#test 
def test_home():
    response = client.get("/")
    assert response.status_code == 200
