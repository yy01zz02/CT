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

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
    cur = cnx.cursor()

    cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cur.fetchone()

    cur.close()
    cnx.close()

    return "Login successful" if user else "Invalid credentials"

@app.route('/update_profile', methods=['POST'])
def update_profile():
    username = request.form['username']
    new_email = request.form['email']

    cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
    cur = cnx.cursor()

    cur.execute("UPDATE users SET email = %s WHERE username = %s", (new_email, username))
    cnx.commit()

    cur.close()
    cnx.close()

    return "Profile updated successfully"

@app.route('/search_users', methods=['GET'])
def search_users():
    search_term = request.args.get('term', '')
    search_pattern = f"%{search_term}%"

    cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
    cur = cnx.cursor()

    cur.execute("SELECT username FROM users WHERE username LIKE %s", (search_pattern,))
    users = cur.fetchall()

    cur.close()
    cnx.close()

    return str(users)

@app.route('/delete_account', methods=['POST'])
def delete_account():
    username = request.form['username']

    cnx = MySQLdb.connect("127.0.0.1", "root", "password", "cwe_900")
    cur = cnx.cursor()

    cur.execute("DELETE FROM users WHERE username = %s", (username,))
    cnx.commit()

    cur.close()
    cnx.close()

    return "Account deleted successfully"

if __name__ == '__main__':
    app.run(debug=False)
