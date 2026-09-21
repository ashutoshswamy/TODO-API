# API Usage Guide

Base URL (local dev): `http://127.0.0.1:5000`

## Setup

```bash
pip install -r requirements.txt
python app.py
```

## Endpoints

### 1. Get all todos
`GET /todos`

```bash
curl http://127.0.0.1:5000/todos
```

Response `200`:
```json
[
  { "id": 1, "title": "Learn Flask", "description": "Understand Flask API concepts." }
]
```

### 2. Get a single todo
`GET /todos/<id>`

```bash
curl http://127.0.0.1:5000/todos/1
```

Response `200` (found):
```json
{ "id": 1, "title": "Learn Flask", "description": "Understand Flask API concepts." }
```

Response `404` (not found):
```json
{ "error": "To-Do item not found" }
```

### 3. Create a todo
`POST /create-todo`

`title` required, `description` optional.

```bash
curl -X POST http://127.0.0.1:5000/create-todo \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn Flask", "description": "Understand Flask API concepts."}'
```

Response `201`:
```json
{ "id": 1, "title": "Learn Flask", "description": "Understand Flask API concepts." }
```

Response `400` (missing title):
```json
{ "error": "Title is required" }
```

### 4. Update a todo
`PUT /edit-todo/<id>`

Send `title` and/or `description`; only provided fields update.

```bash
curl -X PUT http://127.0.0.1:5000/edit-todo/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Master Flask", "description": "Deep dive into advanced Flask topics."}'
```

Response `200`:
```json
{ "id": 1, "title": "Master Flask", "description": "Deep dive into advanced Flask topics." }
```

Response `404` (not found):
```json
{ "error": "To-Do item not found" }
```

### 5. Delete a todo
`DELETE /delete-todo/<id>`

```bash
curl -X DELETE http://127.0.0.1:5000/delete-todo/1
```

Response `204`: empty body.

Response `404` (not found):
```json
{ "error": "To-Do item not found" }
```

## Notes

- Storage is in-memory — data resets whenever the server restarts.
- All request/response bodies are JSON.
