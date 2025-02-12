from flask import Flask, request, redirect
import MySQLdb
import hashlib
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']
   
   salt = os.urandom(16)
   hashed_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
   
   db = MySQLdb.connect("localhost", "root", "", "testdb")
   cursor = db.cursor()
   
   sql = "SELECT username FROM users WHERE username = %s"
   cursor.execute(sql, (username,))
   data = cursor.fetchall()
   
   if data:
      db.close()
      return redirect("/login", code=307)
   else:
      sql = "INSERT INTO users(username, password, salt) VALUES (%s, %s, %s)"
      cursor.execute(sql, (username, hashed_password, salt.hex()))
      db.commit()
      db.close()
      return "Registration successful"

if __name__ == '__main__':
    app.run(debug=False)
