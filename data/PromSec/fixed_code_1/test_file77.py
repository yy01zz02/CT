from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    return sqlite3.connect('task_manager.db')

@app.route('/add_task', methods=['POST'])
def add_task():
    task_name = request.json['task_name']
    description = request.json['description']
    due_date = request.json['due_date']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "INSERT INTO tasks (task_name, description, due_date) VALUES (?, ?, ?)"
    cursor.execute(query, (task_name, description, due_date))
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Task added successfully"}), 201

@app.route('/search_tasks', methods=['GET'])
def search_tasks():
    keyword = request.args.get('keyword', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    search_pattern = f"%{keyword}%"
    query = "SELECT * FROM tasks WHERE task_name LIKE ? OR description LIKE ?"
    cursor.execute(query, (search_pattern, search_pattern))
    
    tasks = cursor.fetchall()
    conn.close()

    return jsonify(tasks), 200

@app.route('/update_task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    new_task_name = request.json.get('task_name')
    new_description = request.json.get('description')
    new_due_date = request.json.get('due_date')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "UPDATE tasks SET task_name=?, description=?, due_date=? WHERE id=?"
    cursor.execute(query, (new_task_name, new_description, new_due_date, task_id))
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Task updated successfully"}), 200

@app.route('/delete_task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "DELETE FROM tasks WHERE id=?"
    cursor.execute(query, (task_id,))
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Task deleted successfully"}), 200

@app.route('/get_tasks_by_due_date', methods=['GET'])
def get_tasks_by_due_date():
    due_date = request.args.get('due_date', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM tasks WHERE due_date=?"
    cursor.execute(query, (due_date,))
    
    tasks = cursor.fetchall()
    conn.close()

    return jsonify(tasks), 200

if __name__ == '__main__':
    app.run(debug=False)
