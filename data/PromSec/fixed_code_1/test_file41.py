from flask import Flask, request
import MySQLdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']

   cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
   cur = cnx.cursor()

   cur.execute("SELECT * FROM users WHERE username = %s", (username,))
   row = cur.fetchall()

   if not row:
      try:
         cur.execute("INSERT INTO users(username, password) VALUES (%s, %s)", (username, password))
         cnx.commit()
         message = "You have successfully registered"
      except:
         cnx.rollback()
         message = "Registration Failed"
   else:
      message = "Username already exists"

   cur.close()
   cnx.close()
   return message

if __name__ == '__main__':
   app.run(debug=False)
