from fastapi.testclient import TestClient
from inference import app

client = TestClient(app)

def test_inference():
    response = client.post("/api/v1/inference", json={
        "no_of_adults": 2,
        "no_of_children": 1,
        "type_of_meal_plan": "Meal Plan 1",
        "required_car_parking_space": 1,
        "lead_time": 10
    })
    assert response.status_code == 200
    assert "result" in response.json()
