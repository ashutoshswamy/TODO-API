# Flask TODO API

A simple RESTful API built with Flask for managing todo items. This API provides basic CRUD operations for todo tasks.

## Features

- Create new todo items
- Retrieve all todos
- Retrieve a specific todo by ID
- Update existing todos
- Delete todos

## API Endpoints

| Method | Endpoint            | Description                  |
| ------ | ------------------- | ---------------------------- |
| GET    | `/todos`            | Get all todo items           |
| GET    | `/todos/<id>`       | Get a specific todo item     |
| POST   | `/create-todo`      | Create a new todo item       |
| PUT    | `/edit-todo/<id>`   | Update an existing todo item |
| DELETE | `/delete-todo/<id>` | Delete a todo item           |

## Installation

1. Clone the repository
2. Create a virtual environment:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:

```sh
pip install -r requirements.txt
```

## Usage

1. Start the server:

```sh
python app.py
```

2. The API will be available at `http://localhost:5000`

## API Examples

### Create a Todo

```sh
curl -X POST http://localhost:5000/create-todo \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn Flask", "description": "Study Flask framework basics"}'
```

### Get All Todos

```sh
curl http://localhost:5000/todos
```

### Update a Todo

```sh
curl -X PUT http://localhost:5000/edit-todo/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Master Flask", "description": "Study advanced Flask concepts"}'
```

### Delete a Todo

```sh
curl -X DELETE http://localhost:5000/delete-todo/1
```

## Developer Information

- **Developer**: Ashutosh Swamy
- **Project Type**: RESTful API
- **Framework**: Flask 3.0.3
- **Language**: Python
- **Storage**: In-memory (non-persistent)

## Note

This is a development version running with Flask's built-in server. For production deployment, use a production-grade WSGI server like Gunicorn or uWSGI.
