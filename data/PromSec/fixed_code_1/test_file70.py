from flask import Flask, request, redirect, jsonify
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    salt = os.urandom(16)
    hashed_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
    user_name_regex = "^" + username + "$"
    db = MySQLdb.connect("localhost", "root", "", "projectdb")
    cursor = db.cursor()
    cursor.execute("SELECT username FROM users WHERE username LIKE %s", (user_name_regex,))
    data = cursor.fetchall()
    if data:
        cursor.close()
        db.close()
        return redirect("/login", code=307)
    else:
        cursor.execute("INSERT INTO users(username, password, salt, account_created) VALUES (%s, %s, %s, %s)",
                       (username, hashed_password, salt.hex(), 1))
        db.commit()
        cursor.close()
        db.close()
        return "Registration successful"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    db = MySQLdb.connect("localhost", "root", "", "projectdb")
    cursor = db.cursor()
    cursor.execute("SELECT password, salt FROM users WHERE username = %s", (username,))
    data = cursor.fetchone()
    if data:
        stored_password, salt = data
        salt = bytes.fromhex(salt)
        hashed_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
        if hashed_password == stored_password:
            cursor.close()
            db.close()
            return redirect("/dashboard", code=307)
    cursor.close()
    db.close()
    return "Invalid credentials"

@app.route('/project/create', methods=['POST'])
def create_project():
    username = request.form['username']
    project_name = request.form['project_name']
    db = MySQLdb.connect("localhost", "root", "", "projectdb")
    cursor = db.cursor()
    cursor.execute("SELECT username FROM users WHERE username = %s", (username,))
    data = cursor.fetchone()
    if data:
        cursor.execute("INSERT INTO projects(username, project_name) VALUES (%s, %s)", (username, project_name))
        db.commit()
        cursor.close()
        db.close()
        return "Project created successfully"
    cursor.close()
    db.close()
    return "User not found"

@app.route('/task/add', methods=['POST'])
def add_task():
    project_name = request.form['project_name']
    task_name = request.form['task_name']
    task_description = request.form['task_description']
    db = MySQLdb.connect("localhost", "root", "", "projectdb")
    cursor = db.cursor()
    cursor.execute("SELECT project_name FROM projects WHERE project_name = %s", (project_name,))
    data = cursor.fetchone()
    if data:
        cursor.execute("INSERT INTO tasks(project_name, task_name, task_description) VALUES (%s, %s, %s)",
                       (project_name, task_name, task_description))
        db.commit()
        cursor.close()
        db.close()
        return "Task added successfully"
    cursor.close()
    db.close()
    return "Project not found"

@app.route('/tasks/view', methods=['GET'])
def view_tasks():
    project_name = request.args.get('project_name')
    db = MySQLdb.connect("localhost", "root", "", "projectdb")
    cursor = db.cursor()
    cursor.execute("SELECT task_name, task_description FROM tasks WHERE project_name = %s", (project_name,))
    tasks = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=False)
