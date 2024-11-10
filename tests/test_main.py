from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_item():
    response = client.post(
        "/items/",
        json={"name": "Test Item", "description": "Test Description", "price": 9.99}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"

def test_get_item():
    # First create an item
    create_response = client.post(
        "/items/",
        json={"name": "Test Item", "description": "Test Description", "price": 9.99}
    )
    item_id = create_response.json()["id"]
    
    # Then retrieve it
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"

def test_get_all_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_item():
    # First create an item
    create_response = client.post(
        "/items/",
        json={"name": "Test Item", "description": "Test Description", "price": 9.99}
    )
    item_id = create_response.json()["id"]
    
    # Then update it
    response = client.put(
        f"/items/{item_id}",
        json={"name": "Updated Item", "description": "Updated Description", "price": 19.99}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Item"

def test_delete_item():
    # First create an item
    create_response = client.post(
        "/items/",
        json={"name": "Test Item", "description": "Test Description", "price": 9.99}
    )
    item_id = create_response.json()["id"]
    
    # Then delete it
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200