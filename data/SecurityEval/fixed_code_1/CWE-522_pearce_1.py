from flask import Flask, request
import MySQLdb
import hashlib
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), os.urandom(16), 100000).hex()
    db = MySQLdb.connect(host="localhost", user="root", passwd=os.environ.get('DB_PASSWORD'), db="test")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    if cursor.fetchone() is not None:
        return "Username already exists"
    else:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        db.commit()
        return "Registered successfully"