from flask import Flask, request
import MySQLdb
import os
import hashlib

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    salt = os.urandom(32)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000).hex()
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASSWORD')
    db = MySQLdb.connect(
        host="mysql.eecs.oregonstate.edu",
        user=db_user,
        passwd=db_pass,
        db="cs419-group09"
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM user WHERE username = %s", (username,))
    result = cur.fetchall()
    if not result:
        cur.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, f"{salt.hex()}:{hashed_password}"))
        db.commit()
        return "register success"
    else:
        return "user already exists"