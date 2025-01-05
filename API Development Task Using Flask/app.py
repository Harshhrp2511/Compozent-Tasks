from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

# File to store task data
DATA_FILE = 'tasks.json'

# Ensure the data file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as file:
        json.dump([], file)

# Load tasks from file
def load_tasks():
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

# Save tasks to file
def save_tasks(tasks):
    with open(DATA_FILE, 'w') as file:
        json.dump(tasks, file)

# Serve the HTML frontend
@app.route('/')
def home():
    return render_template('index.html')

# API: Get all tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)

# API: Add a new task
@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "title": data.get('title'),
        "description": data.get('description'),
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return jsonify(new_task), 201

# API: Update a task
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['title'] = data.get('title', task['title'])
            task['description'] = data.get('description', task['description'])
            task['completed'] = data.get('completed', task['completed'])
            save_tasks(tasks)
            return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404

# API: Delete a task
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    return jsonify({'message': 'Task deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
