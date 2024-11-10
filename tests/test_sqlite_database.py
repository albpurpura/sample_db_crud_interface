import pytest
from database_sqlite import SQLiteDatabase
import os

@pytest.fixture
def db():
    db_name = "test_items.db"
    db = SQLiteDatabase(db_name)
    yield db
    os.remove(db_name)

def test_create_item(db):
    item = {
        "name": "Test Item",
        "description": "Test Description",
        "price": 9.99
    }
    created_item = db.create(item)
    assert created_item["id"] is not None
    assert created_item["name"] == item["name"]
    assert created_item["description"] == item["description"]
    assert created_item["price"] == item["price"]

def test_get_item(db):
    item = {
        "name": "Test Item",
        "description": "Test Description",
        "price": 9.99
    }
    created_item = db.create(item)
    retrieved_item = db.get(created_item["id"])
    assert retrieved_item == created_item

def test_get_all_items(db):
    items = [
        {"name": "Item 1", "description": "Desc 1", "price": 9.99},
        {"name": "Item 2", "description": "Desc 2", "price": 19.99}
    ]
    for item in items:
        db.create(item)
    retrieved_items = db.get_all()
    assert len(retrieved_items) == 2

def test_update_item(db):
    item = {
        "name": "Test Item",
        "description": "Test Description",
        "price": 9.99
    }
    created_item = db.create(item)
    updated_data = {
        "name": "Updated Item",
        "description": "Updated Description",
        "price": 19.99
    }
    updated_item = db.update(created_item["id"], updated_data)
    assert updated_item["name"] == updated_data["name"]
    assert updated_item["description"] == updated_data["description"]
    assert updated_item["price"] == updated_data["price"]

def test_delete_item(db):
    item = {
        "name": "Test Item",
        "description": "Test Description",
        "price": 9.99
    }
    created_item = db.create(item)
    assert db.delete(created_item["id"]) is True
    assert db.get(created_item["id"]) is None
