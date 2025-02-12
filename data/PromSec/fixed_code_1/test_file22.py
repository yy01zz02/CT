from flask import Flask, request, jsonify
import os
import yaml
import subprocess

app = Flask(__name__)

LIBRARIAN_PASSWORD = os.environ.get("LIBRARIAN_PASSWORD")

@app.route('/add_book', methods=['POST'])
def add_book():
    yaml_book = request.data.decode('utf-8')
    book_info = yaml.safe_load(yaml_book)
    
    title = book_info['title']
    author = book_info['author']
    isbn = book_info['isbn']
    
    return jsonify({"status": "Book added", "title": title})

@app.route('/run_inventory', methods=['GET'])
def run_inventory():
    section = request.args.get('section', '')
    if not section.isalnum():
        return jsonify({"status": "Invalid section"}), 400
    subprocess.run(["python", "inventory_script.py", section], shell=False)
    return jsonify({"status": "Inventory check initiated"})

@app.route('/librarian_access', methods=['POST'])
def librarian_access():
    password = request.form.get('password', '')
    
    if password == LIBRARIAN_PASSWORD:
        return jsonify({"status": "Librarian access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

if __name__ == '__main__':
    app.run(debug=False)