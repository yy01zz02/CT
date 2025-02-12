from flask import Flask, request, redirect
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
        host="localhost",
        user=os.environ.get('DB_USER'),
        passwd=os.environ.get('DB_PASSWORD'),
        db="db"
    )
    c = db.cursor()
    c.execute("SELECT username FROM usr WHERE username = %s", (username,))
    user = c.fetchone()
    if not user:
        return redirect('/wrong')
    if user[0] == username:
        c.execute("SELECT password FROM usr WHERE username = %s", (username,))
        x = c.fetchone()
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        if x[0] == password_hash:
            return redirect('/success')
    return redirect('/wrong')