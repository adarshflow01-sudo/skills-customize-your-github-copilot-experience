# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small RESTful API using the FastAPI framework. You will define data models with Pydantic, implement CRUD endpoints, validate input, and run the application with Uvicorn.

## 📝 Tasks

### 🛠️ Create a Simple REST API

#### Description
Implement a REST API for managing a small collection of items (in-memory). The API should demonstrate typical CRUD operations and input validation using Pydantic models.

#### Requirements
Completed program should:

- Provide endpoints to list, create, retrieve, update, and delete items (`GET /items`, `POST /items`, `GET /items/{id}`, `PUT /items/{id}`, `DELETE /items/{id}`)
- Use Pydantic models for request/response validation and typing
- Return appropriate HTTP status codes (e.g., `201` for created, `404` for not found)
- Include basic error handling using FastAPI's `HTTPException`
- Keep data in-memory (a list/dict) so the app runs without a database
- Be runnable with Uvicorn (instructions below)

### 🛠️ Optional Enhancements

#### Description
Add features that improve robustness, developer experience, or extend the API surface.

#### Requirements
Optional improvements may include:

- Persisting data to a simple JSON file or SQLite database
- Adding query parameters for filtering or pagination on `GET /items`
- Implementing request/response examples and OpenAPI metadata
- Adding unit tests for handlers using `pytest` and `httpx` or `requests`

## Example Usage

Run the starter app and use `curl` or a browser to interact with the API:

`GET /items` — list all items
`POST /items` — create a new item with JSON body

When finished, save your solution as `starter_server.py` in this folder. Include any extra files (for example `requirements.txt`) that are needed to run the app.

## Run Instructions

1. Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Start the app with Uvicorn:

```bash
uvicorn starter_server:app --reload
```

3. Open `http://127.0.0.1:8000/docs` to view the interactive API docs.
