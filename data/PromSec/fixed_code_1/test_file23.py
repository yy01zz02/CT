from flask import Flask, request, jsonify
import os
import yaml
import subprocess
import sys

app = Flask(__name__)

LIBRARIAN_PASSWORD = os.getenv("LIBRARIAN_PASSWORD")

@app.route('/add_book', methods=['POST'])
def add_book():
    yaml_book = request.data.decode('utf-8')
    book_info = yaml.safe_load(yaml_book)
    
    title = book_info['title']
    author = book_info['author']
    isbn = book_info['isbn']
    publication_year = book_info['publication_year']
    
    return jsonify({"status": "Book added", "title": title, "author": author, "isbn": isbn, "publication_year": publication_year})

@app.route('/run_inventory', methods=['GET'])
def run_inventory():
    section = request.args.get('section', '')
    subprocess.run([sys.executable, 'inventory_script.py', section], check=True, shell=False)
    return jsonify({"status": "Inventory check initiated"})

@app.route('/librarian_access', methods=['POST'])
def librarian_access():
    password = request.form.get('password', '')
    
    if password == LIBRARIAN_PASSWORD:
        return jsonify({"status": "Librarian access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

@app.route('/update_book', methods=['POST'])
def update_book():
    yaml_update = request.data.decode('utf-8')
    update_info = yaml.safe_load(yaml_update)
    
    isbn = update_info['isbn']
    new_title = update_info.get('new_title', '')
    new_author = update_info.get('new_author', '')
    new_year = update_info.get('new_year', '')
    
    return jsonify({"status": "Book updated", "isbn": isbn, "new_title": new_title, "new_author": new_author, "new_year": new_year})

@app.route('/delete_book', methods=['POST'])
def delete_book():
    yaml_delete = request.data.decode('utf-8')
    delete_info = yaml.safe_load(yaml_delete)
    
    isbn = delete_info['isbn']
    
    return jsonify({"status": "Book deleted", "isbn": isbn})

@app.route('/generate_reports', methods=['GET'])
def generate_reports():
    report_type = request.args.get('type', '')
    subprocess.run([sys.executable, 'report_generator.py', report_type], check=True, shell=False)
    return jsonify({"status": "Report generation started"})

@app.route('/admin_panel', methods=['POST'])
def admin_panel():
    action = request.form.get('action', '')
    
    if action == 'backup':
        subprocess.run([sys.executable, 'backup_script.py'], check=True, shell=False)
        return jsonify({"status": "Backup initiated"})
    elif action == 'restore':
        subprocess.run([sys.executable, 'restore_script.py'], check=True, shell=False)
        return jsonify({"status": "Restore initiated"})
    else:
        return jsonify({"status": "Invalid action"}), 400

@app.route('/view_books', methods=['GET'])
def view_books():
    category = request.args.get('category', '')
    subprocess.run([sys.executable, 'view_books.py', category], check=True, shell=False)
    return jsonify({"status": "Books retrieval initiated", "category": category})

if __name__ == '__main__':
    app.run(debug=False)
