# FastAPI CRUD Application

A simple CRUD (Create, Read, Update, Delete) application built with FastAPI and SQLite, implementing a clean architecture with abstract database interfaces.

## Features

- FastAPI REST API endpoints for CRUD operations
- Abstract database interface
- SQLite implementation
- Comprehensive test suite
- Clean architecture design

## Project Structure

```
.
├── main.py              # FastAPI application and endpoints
├── database.py          # Abstract database interface
├── database_sqlite.py   # SQLite implementation
├── tests/
│   ├── test_main.py        # API endpoint tests
│   └── test_database_sqlite.py  # Database implementation tests
└── items.db            # SQLite database file
```

## Requirements

- Python 3.7+
- FastAPI
- SQLite3
- pytest (for testing)
- uvicorn (for running the server)

## Installation

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install fastapi uvicorn sqlite3 pytest httpx
```

## Running the Application

1. Start the server:
```bash
uvicorn main:app --reload
```

2. The API will be available at `http://localhost:8000`

## API Endpoints and Examples

### Get All Items
```bash
# Request
curl -X GET "http://localhost:8000/items/"

# Response
[
    {
        "id": 1,
        "name": "Laptop",
        "description": "High-performance laptop",
        "price": 999.99
    },
    {
        "id": 2,
        "name": "Mouse",
        "description": "Wireless mouse",
        "price": 29.99
    }
]
```

### Get Single Item
```bash
# Request
curl -X GET "http://localhost:8000/items/1"

# Response
{
    "id": 1,
    "name": "Laptop",
    "description": "High-performance laptop",
    "price": 999.99
}

# Error Response (Item not found)
{
    "detail": "Item not found"
}
```

### Create New Item
```bash
# Request
curl -X POST "http://localhost:8000/items/" \
     -H "Content-Type: application/json" \
     -d '{
           "name": "Keyboard",
           "description": "Mechanical keyboard",
           "price": 159.99
         }'

# Response
{
    "id": 3,
    "name": "Keyboard",
    "description": "Mechanical keyboard",
    "price": 159.99
}
```

### Update Item
```bash
# Request
curl -X PUT "http://localhost:8000/items/3" \
     -H "Content-Type: application/json" \
     -d '{
           "name": "Mechanical Keyboard",
           "description": "RGB mechanical keyboard",
           "price": 179.99
         }'

# Response
{
    "id": 3,
    "name": "Mechanical Keyboard",
    "description": "RGB mechanical keyboard",
    "price": 179.99
}

# Error Response (Item not found)
{
    "detail": "Item not found"
}
```

### Delete Item
```bash
# Request
curl -X DELETE "http://localhost:8000/items/3"

# Success Response
{
    "message": "Item deleted successfully"
}

# Error Response (Item not found)
{
    "detail": "Item not found"
}
```

### Python Examples
You can also interact with the API using Python's requests library:

```python
import requests

BASE_URL = "http://localhost:8000"

# Get all items
response = requests.get(f"{BASE_URL}/items/")
items = response.json()

# Get single item
response = requests.get(f"{BASE_URL}/items/1")
item = response.json()

# Create new item
new_item = {
    "name": "Monitor",
    "description": "4K Display",
    "price": 299.99
}
response = requests.post(f"{BASE_URL}/items/", json=new_item)
created_item = response.json()

# Update item
updated_data = {
    "name": "4K Monitor",
    "description": "Ultra HD Display",
    "price": 349.99
}
response = requests.put(f"{BASE_URL}/items/1", json=updated_data)
updated_item = response.json()

# Delete item
response = requests.delete(f"{BASE_URL}/items/1")
```

### Using FastAPI's Interactive Documentation
FastAPI provides automatic interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

These interfaces allow you to:
- View all available endpoints
- Test endpoints directly in the browser
- See request/response schemas
- View detailed parameter information

## Architecture

The application follows a clean architecture pattern with three main components:

1. **API Layer** (`main.py`):
   - Handles HTTP requests and responses
   - Input validation using Pydantic models
   - Routes to appropriate database operations

2. **Database Interface** (`database.py`):
   - Abstract base class defining database operations
   - Ensures consistent interface across different implementations

3. **SQLite Implementation** (`database_sqlite.py`):
   - Concrete implementation of the database interface
   - Handles actual data storage and retrieval using SQLite

## Data Model

The Item model has the following structure:
```json
{
    "id": "integer, auto-generated",
    "name": "string, required",
    "description": "string, required",
    "price": "float, required"
}
```

## Error Handling

The API returns appropriate HTTP status codes:
- 200: Successful operation
- 404: Item not found
- 422: Validation error (invalid input data)
- 500: Server error

## Running Tests

```bash
pytest
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License