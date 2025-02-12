from flask import Flask, request, jsonify
import os
import yaml
import subprocess
import hmac
import sys

app = Flask(__name__)

LIBRARIAN_PASSWORD = os.getenv("LIBRARIAN_PASSWORD")
if not LIBRARIAN_PASSWORD:
    raise ValueError("LIBRARIAN_PASSWORD environment variable not set")

@app.route('/add_book', methods=['POST'])
def add_book():
    yaml_book = request.data.decode('utf-8')
    book_info = yaml.safe_load(yaml_book)
    
    title = book_info.get('title', '')
    author = book_info.get('author', '')
    isbn = book_info.get('isbn', '')
    
    if not title or not author or not isbn:
        return jsonify({"status": "Error", "message": "Invalid book information"}), 400

    return jsonify({"status": "Book added", "title": title, "author": author, "isbn": isbn})

@app.route('/run_inventory', methods=['GET'])
def run_inventory():
    section = request.args.get('section', '')
    if not section.isalnum():
        return jsonify({"status": "Invalid section parameter"}), 400
    subprocess.run([sys.executable, 'inventory_script.py', section], check=False)
    return jsonify({"status": "Inventory check initiated"})

@app.route('/librarian_access', methods=['POST'])
def librarian_access():
    password = request.form.get('password', '')
    if hmac.compare_digest(password.encode('utf-8'), LIBRARIAN_PASSWORD.encode('utf-8')):
        return jsonify({"status": "Librarian access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

if __name__ == '__main__':
    app.run(debug=False)