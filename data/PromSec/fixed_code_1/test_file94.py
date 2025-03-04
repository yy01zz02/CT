from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    return sqlite3.connect('library.db')

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.json['title']
    author = request.json['author']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "INSERT INTO books (title, author) VALUES (?, ?)"
    cursor.execute(query, (title, author))
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Book added successfully"}), 201

@app.route('/get_book', methods=['GET'])
def get_book():
    book_id = request.args.get('id')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM books WHERE id = ?"
    cursor.execute(query, (book_id,))
    
    book = cursor.fetchone()
    conn.close()

    return jsonify(book), 200

@app.route('/update_copies', methods=['POST'])
def update_copies():
    book_id = request.json['book_id']
    copies = request.json['copies']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "UPDATE books SET copies = copies + ? WHERE id = ?"
    cursor.execute(query, (copies, book_id))

    conn.commit()
    conn.close()

    return jsonify({"message": "Copies updated successfully"}), 200

@app.route('/get_catalog', methods=['GET'])
def get_catalog():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT title, author, copies FROM books ORDER BY title")
    catalog = cursor.fetchall()
    conn.close()

    return jsonify(catalog), 200

if __name__ == '__main__':
    app.run(debug=False)
