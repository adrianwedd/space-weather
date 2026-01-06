import pytest
from fastapi.testclient import TestClient
from main import app
import responses
import requests

client = TestClient(app)

@pytest.fixture
def mock_bom_api():
    with responses.RequestsMock() as rsps:
        yield rsps

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Space Weather API is running"}

def test_get_a_index_success(mock_bom_api):
    mock_data = {"a_index": [{"date": "2026-01-06", "value": 10}]}
    mock_bom_api.add(
        responses.GET,
        "https://sws-data.sws.bom.gov.au/api/v1/get-a-index",
        json=mock_data,
        status=200
    )
    
    response = client.get("/api/a-index")
    assert response.status_code == 200
    assert response.json() == mock_data

def test_get_a_index_error(mock_bom_api):
    mock_bom_api.add(
        responses.GET,
        "https://sws-data.sws.bom.gov.au/api/v1/get-a-index",
        status=500
    )
    
    response = client.get("/api/a-index")
    assert response.status_code == 500
    assert "Error fetching data from BOM" in response.json()["detail"]

def test_get_k_index_with_location(mock_bom_api):
    mock_data = {"k_index": []}
    def request_callback(request):
        if "location=Adelaide" in request.url:
            return (200, {}, '{"k_index": [{"location": "Adelaide", "value": 3}]}')
        return (404, {}, '{"error": "not found"}')

    mock_bom_api.add_callback(
        responses.GET,
        "https://sws-data.sws.bom.gov.au/api/v1/get-k-index",
        callback=request_callback,
        content_type='application/json',
    )
    
    response = client.get("/api/k-index?location=Adelaide")
    assert response.status_code == 200
    assert response.json()["k_index"][0]["location"] == "Adelaide"
