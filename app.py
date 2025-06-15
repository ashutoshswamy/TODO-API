from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# --- In-memory Data Storage ---
# A simple list to store our to-do items.
# Each to-do item is a dictionary with 'id', 'title', and 'description'.
# We'll use a simple counter for IDs.
todos = []
next_todo_id = 1

# --- Helper function to find a todo by ID ---
def find_todo(todo_id):
    """
    Finds a to-do item in the 'todos' list by its ID.

    Args:
        todo_id (int): The ID of the to-do item to find.

    Returns:
        tuple: A tuple containing (todo_item, index) if found, otherwise (None, None).
    """
    for index, todo in enumerate(todos):
        if todo['id'] == todo_id:
            return todo, index
    return None, None

# --- API Endpoints ---

@app.route('/todos', methods=['GET'])
def get_todos():
    """
    Retrieves all to-do items.
    GET /todos
    """
    # Return all to-do items as a JSON response
    return jsonify(todos)

@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    """
    Retrieves a single to-do item by its ID.
    GET /todos/<id>
    """
    todo, _ = find_todo(todo_id)
    if todo:
        return jsonify(todo)
    else:
        # If the to-do item is not found, return a 404 Not Found error
        return jsonify({'error': 'To-Do item not found'}), 404

@app.route('/create-todo', methods=['POST'])
def create_todo():
    """
    Creates a new to-do item.
    Expects JSON data with 'title' and optionally 'description'.
    POST /create-todo
    Example Request Body:
    {
        "title": "Learn Flask",
        "description": "Understand Flask API concepts."
    }
    """
    global next_todo_id
    data = request.get_json()

    # Validate incoming JSON data
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400

    new_todo = {
        'id': next_todo_id,
        'title': data['title'],
        'description': data.get('description', '') # Description is optional
    }
    todos.append(new_todo)
    next_todo_id += 1
    # Return the newly created to-do item with a 201 Created status code
    return jsonify(new_todo), 201

@app.route('/edit-todo/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """
    Updates an existing to-do item by its ID.
    Expects JSON data with 'title' and/or 'description'.
    PUT /edit-todo/<id>
    Example Request Body:
    {
        "title": "Master Flask",
        "description": "Deep dive into advanced Flask topics."
    }
    """
    data = request.get_json()
    todo, index = find_todo(todo_id)

    if not todo:
        return jsonify({'error': 'To-Do item not found'}), 404

    # Update title if provided
    if 'title' in data:
        todo['title'] = data['title']
    # Update description if provided
    if 'description' in data:
        todo['description'] = data['description']

    # Assign the updated todo back to the list
    todos[index] = todo
    return jsonify(todo)

@app.route('/delete-todo/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """
    Deletes a to-do item by its ID.
    DELETE /delete-todo/<id>
    """
    todo, index = find_todo(todo_id)

    if not todo:
        return jsonify({'error': 'To-Do item not found'}), 404

    # Remove the to-do item from the list
    del todos[index]
    # Return an empty response with a 204 No Content status code
    return jsonify({}), 204

# --- Run the Flask app ---
if __name__ == '__main__':
    # Run the app in debug mode. In a production environment,
    # you would use a production-ready WSGI server like Gunicorn or uWSGI.
    app.run(debug=True)
