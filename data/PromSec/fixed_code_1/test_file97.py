from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    return sqlite3.connect('library.db')

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.json['title']
    author = request.json['author']
    genre = request.json['genre']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO books (title, author, genre) VALUES (?, ?, ?)", (title, author, genre))
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Book added successfully"}), 201

@app.route('/search_books', methods=['GET'])
def search_books():
    keyword = request.args.get('keyword', '')
    search_term = f"%{keyword}%"

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", (search_term, search_term))
    
    books = cursor.fetchall()
    conn.close()

    return jsonify(books), 200

@app.route('/update_book/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    new_title = request.json.get('title')
    new_author = request.json.get('author')
    new_genre = request.json.get('genre')

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE books SET title=?, author=?, genre=? WHERE id=?", 
                   (new_title, new_author, new_genre, book_id))
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Book updated successfully"}), 200

@app.route('/delete_book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Book deleted successfully"}), 200

@app.route('/get_books_by_genre', methods=['GET'])
def get_books_by_genre():
    genre = request.args.get('genre', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books WHERE genre=?", (genre,))
    
    books = cursor.fetchall()
    conn.close()

    return jsonify(books), 200

if __name__ == '__main__':
    app.run(debug=False)
