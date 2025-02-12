from flask import Flask, request, redirect, jsonify
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
    m = hashlib.sha256()
    m.update(password.encode('utf-8') + salt)
    hashed_password = m.digest() + salt
    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "library_db")
        cursor = db.cursor()
        sql = "insert into users (username, password) values (%s, %s)"
        cursor.execute(sql, (username, hashed_password.hex()))
        db.commit()
        cursor.close()
        db.close()
        return redirect('/home')
    except Exception as e:
        print(e)
        return redirect('/home')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "library_db")
        cursor = db.cursor()
        sql = "select password from users where username=%s"
        cursor.execute(sql, (username,))
        row = cursor.fetchone()
        if row:
            stored_password = bytes.fromhex(row[0])
            salt = stored_password[32:]
            m = hashlib.sha256()
            m.update(password.encode('utf-8') + salt)
            if stored_password[:32] == m.digest():
                cursor.close()
                db.close()
                return redirect('/dashboard')
        cursor.close()
        db.close()
        return "Invalid credentials"
    except Exception as e:
        print(e)
        return "Login failed"

@app.route('/add_book', methods=['POST'])
def add_book():
    book_id = request.form['book_id']
    title = request.form['title']
    author = request.form['author']
    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "library_db")
        cursor = db.cursor()
        sql = "insert into books (book_id, title, author) values (%s, %s, %s)"
        cursor.execute(sql, (book_id, title, author))
        db.commit()
        cursor.close()
        db.close()
        return "Book successfully added"
    except Exception as e:
        print(e)
        return "Failed to add book"

@app.route('/checkout', methods=['POST'])
def checkout():
    username = request.form['username']
    book_id = request.form['book_id']
    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "library_db")
        cursor = db.cursor()
        sql = "select * from users where username=%s"
        cursor.execute(sql, (username,))
        row = cursor.fetchone()
        if row:
            sql = "insert into checkouts (username, book_id) values (%s, %s)"
            cursor.execute(sql, (username, book_id))
            db.commit()
            message = "Book successfully checked out"
        else:
            message = "User not found"
        cursor.close()
        db.close()
        return message
    except Exception as e:
        print(e)
        return "Checkout failed"

@app.route('/return', methods=['POST'])
def return_book():
    username = request.form['username']
    book_id = request.form['book_id']
    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "library_db")
        cursor = db.cursor()
        sql = "select * from checkouts where username=%s and book_id=%s"
        cursor.execute(sql, (username, book_id))
        row = cursor.fetchone()
        if row:
            sql = "delete from checkouts where username=%s and book_id=%s"
            cursor.execute(sql, (username, book_id))
            db.commit()
            message = "Book successfully returned"
        else:
            message = "Checkout record not found"
        cursor.close()
        db.close()
        return message
    except Exception as e:
        print(e)
        return "Return failed"

@app.route('/view_books', methods=['GET'])
def view_books():
    try:
        db = MySQLdb.connect("localhost", "root", "cisco123", "library_db")
        cursor = db.cursor()
        sql = "select * from books"
        cursor.execute(sql)
        books = cursor.fetchall()
        cursor.close()
        db.close()
        return jsonify(books)
    except Exception as e:
        print(e)
        return "Failed to retrieve books"

if __name__ == '__main__':
    app.run(debug=False)
