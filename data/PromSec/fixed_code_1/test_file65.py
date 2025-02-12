from flask import Flask, request, redirect
import re
from werkzeug.security import generate_password_hash
import MySQLdb
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    password_hash = generate_password_hash(password)
    db = MySQLdb.connect(
        host=os.getenv("DB_HOST", "69.195.55.111"),
        user=os.getenv("DB_USER", "ec2-user"),
        passwd=os.getenv("DB_PASSWORD"),
        db=os.getenv("DB_NAME", "CWE")
    )
    cur = db.cursor()
    query = "INSERT INTO User (Username, Password, Email) VALUES (%s, %s, %s)"
    cur.execute(query, (username, password_hash, username))
    db.commit()
    db.close()
    return redirect('/')