from flask import Flask, request, redirect, jsonify
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        
        if cursor.fetchone():
            cursor.close()
            db.close()
            return "Username already exists"

        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        
        db.commit()
        cursor.close()
        db.close()

        return redirect('/home')
    except:
        return "Registration failed"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        
        if cursor.fetchone():
            cursor.close()
            db.close()
            return redirect('/dashboard')
        else:
            cursor.close()
            db.close()
            return "Invalid credentials"
    except:
        return "Login failed"

@app.route('/add_task', methods=['POST'])
def add_task():
    username = request.form['username']
    task_name = request.form['task_name']
    task_description = request.form['task_description']

    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        
        if cursor.fetchone():
            cursor.execute("INSERT INTO tasks (username, task_name, task_description) VALUES (%s, %s, %s)", (username, task_name, task_description))
            db.commit()
            message = "Task successfully added"
        else:
            message = "User not found"

        cursor.close()
        db.close()
        return message
    except:
        return "Failed to add task"

@app.route('/view_tasks', methods=['GET'])
def view_tasks():
    username = request.args.get('username')

    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        cursor.execute("SELECT * FROM tasks WHERE username = %s", (username,))
        tasks = cursor.fetchall()

        cursor.close()
        db.close()

        return jsonify(tasks)
    except:
        return "Failed to retrieve tasks"

@app.route('/delete_task', methods=['POST'])
def delete_task():
    username = request.form['username']
    task_id = request.form['task_id']

    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        cursor.execute("DELETE FROM tasks WHERE username = %s AND task_id = %s", (username, task_id))
        db.commit()

        cursor.close()
        db.close()

        return "Task successfully deleted"
    except:
        return "Failed to delete task"

@app.route('/update_task', methods=['POST'])
def update_task():
    username = request.form['username']
    task_id = request.form['task_id']
    new_task_name = request.form['new_task_name']
    new_task_description = request.form['new_task_description']

    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "task_manager")
        cursor = db.cursor()

        cursor.execute("UPDATE tasks SET task_name = %s, task_description = %s WHERE username = %s AND task_id = %s", (new_task_name, new_task_description, username, task_id))
        db.commit()

        cursor.close()
        db.close()

        return "Task successfully updated"
    except:
        return "Failed to update task"

if __name__ == '__main__':
    app.run(debug=False)
