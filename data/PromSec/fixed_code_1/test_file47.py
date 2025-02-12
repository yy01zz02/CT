from flask import Flask, request
import os
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    db = MySQLdb.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER'),
        passwd=os.environ.get('DB_PASSWORD'),
        db=os.environ.get('DB_NAME', 'db')
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user WHERE username=%s", (username,))
    results = cursor.fetchall()
    if len(results) == 0:
        return "Login failed!"
    hashed_password = results[0][1]
    if hashed_password == hashlib.sha256(password.encode()).hexdigest():
        return "Welcome " + username + "!"
    else:
        return "Login failed!"