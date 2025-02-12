from flask import Flask, request, jsonify
import os
import yaml
import subprocess
import re
import sys

app = Flask(__name__)

LIBRARIAN_PASSWORD = os.environ.get("LIBRARIAN_PASSWORD", "")

@app.route('/add_new_book', methods=['POST'])
def add_new_book():
    yaml_book = request.data.decode('utf-8')
    try:
        book_info = yaml.safe_load(yaml_book, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    required_fields = ['title', 'author', 'isbn']
    if not all(field in book_info for field in required_fields):
        return jsonify({"status": "Error", "message": "Missing required fields"}), 400
    
    title = book_info['title']
    author = book_info['author']
    isbn = book_info['isbn']
    
    return jsonify({"status": "New Book added", "title": title, "author": author, "isbn": isbn})

@app.route('/execute_inventory', methods=['GET'])
def execute_inventory():
    section = request.args.get('section', '')
    if not re.match(r'^[\w-]+$', section):
        return jsonify({"status": "Error", "message": "Invalid section parameter"}), 400
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(script_dir, 'run_inventory.py')
    
    try:
        subprocess.run([sys.executable, script_path, section], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return jsonify({"status": "Error", "message": "Inventory check failed"}), 500
    
    return jsonify({"status": "Inventory check started"})

@app.route('/admin_access', methods=['POST'])
def admin_access():
    password = request.form.get('password', '')
    
    if password == LIBRARIAN_PASSWORD:
        return jsonify({"status": "Admin access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

if __name__ == "__main__":
    app.run(debug=False)