from flask import Flask, request, redirect
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
    hashed_password = hashlib.sha256((salt + password.encode('utf-8'))).hexdigest()
    user_name_regex = f"^{username}$"

    db = MySQLdb.connect("localhost", "root", "", "testdb")
    cursor = db.cursor()

    cursor.execute("SELECT username FROM users WHERE username LIKE %s", (user_name_regex,))
    data = cursor.fetchall()
    if data:
        db.close()
        return redirect("/login", code=307)
    else:
        cursor.execute(
            "INSERT INTO users(username, password, salt, account_created) VALUES (%s, %s, %s, %s)",
            (username, hashed_password, salt, 1)
        )
        db.commit()
        db.close()
        return "Success", 200