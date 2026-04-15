from http.client import responses

from fastapi.testclient import TestClient

from src import main
from fastapi import status

client = TestClient(main.app)


def test_return_health_check():
    response = client.get("/healthy")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'status':  'Healthy'}
