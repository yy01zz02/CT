from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os
import bcrypt
import random
import string

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']
   hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()).decode('utf-8')
   name = request.form['name']
   cweid = request.form['cweid']
   email = request.form['email']
   db = MySQLdb.connect(host=os.environ["DATABASE_URL"],user=os.environ["DATABASE_USER"], passwd=os.environ["DATABASE_PASSWORD"], db=os.environ["DATABASE_NAME"])
   cursor = db.cursor()
   cursor.execute("SELECT username FROM users WHERE username=%s", (username,))
   user = cursor.fetchone()
   if not user:
      cursor.execute("INSERT INTO users (username,password,name,email,cweid) VALUES (%s, %s, %s, %s, %s)", (username, hashed_password, name, email, cweid))
      db.commit()
      user_id = cursor.lastrowid
      session_id = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(16))
      cursor.execute("INSERT INTO sessions (username,user_id,session_id) VALUES (%s, %s, %s)", (username, user_id, session_id))
      db.commit()
      cursor.execute("SELECT username,password,session_id,stake FROM sessions WHERE username=%s AND session_id=%s", (username, session_id))
      session = cursor.fetchone()
      session_id = session[2]
      stake = session[3]
      return redirect('/login?username=' + username + '&session_id=' + session_id + '&stake=' + str(stake))
   else:
      return 'Username is already taken'