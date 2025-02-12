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
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db = MySQLdb.connect(host="localhost", user=db_user, passwd=db_password, db="db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user WHERE username = %s", (username,))
    rows = cursor.fetchall()
    db.close()
    for row in rows:
        if row[1] == username:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if row[2] == hashed_password:
                return "success"
            else:
                return "wrong pw"
    return "username not found"