from flask import Flask, request
import os
import hashlib
import MySQLdb

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_user = os.environ.get('DB_USER', 'root')
    db_password = os.environ.get('DB_PASSWORD', '')
    db_name = os.environ.get('DB_NAME', 'db')
    
    db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)
    c = db.cursor()
    
    password_hash = hashlib.md5(password.encode(), usedforsecurity=False).hexdigest()
    c.execute("SELECT * FROM userdaten WHERE username = %s AND passwort = %s", (username, password_hash))
    
    if c.fetchone():
        return "Eingeloggt"
    else:
        return "Falscher Benutzername oder Passwort"