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
    try:
        conn = MySQLdb.connect(host="localhost", user="root", passwd=os.environ.get('DB_PASSWORD'), db="cwe200")
        curs = conn.cursor()
        curs.execute("SELECT password FROM users WHERE username = %s", (username,))
        row = curs.fetchone()
        pswd = row[0] if row else None
        if pswd is None:
            user = "false"
        elif pswd == password:
            user = "true"
        else:
            user = "false"
        return user
    except MySQLdb.Error as e:
        print(f"Error {e.args[0]}: {e.args[1]}", file=sys.stderr)
        return "false"
    finally:
        if 'conn' in locals() and conn:
            conn.close()
