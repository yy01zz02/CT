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
    encrypted_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000).hex()
    salt_hex = salt.hex()
    conn = MySQLdb.connect(
        host="localhost",
        user=os.environ.get('DB_USER'),
        passwd=os.environ.get('DB_PASS'),
        db="CWE"
    )
    x = conn.cursor()
    sql = "INSERT INTO users (username, password, salt, created_at, updated_at) VALUES (%s, %s, %s, NOW(), NOW())"
    x.execute(sql, (username, encrypted_password, salt_hex))
    conn.commit()
    return redirect('/mainpage')
