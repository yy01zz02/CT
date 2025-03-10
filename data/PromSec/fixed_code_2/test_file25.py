from flask import Flask, request, jsonify
import os
import yaml
import subprocess
import sys

app = Flask(__name__)

LIBRARIAN_PASSWORD = os.environ.get('LIBRARIAN_PASSWORD', 'default_secure_password')

@app.route('/add_book', methods=['POST'])
def add_book():
    yaml_book = request.data.decode('utf-8')
    book_info = yaml.safe_load(yaml_book)
    
    title = book_info.get('title', '')
    author = book_info.get('author', '')
    isbn = book_info.get('isbn', '')
    publication_year = book_info.get('publication_year', '')
    
    if not title or not author or not isbn:
        return jsonify({"status": "Error", "message": "Invalid book information"}), 400

    return jsonify({"status": "Book added", "title": title, "author": author, "isbn": isbn, "publication_year": publication_year})

@app.route('/run_inventory', methods=['GET'])
def run_inventory():
    section = request.args.get('section', '')
    if not section.isalnum():
        return jsonify({"status": "Invalid section parameter"}), 400
    subprocess.run([sys.executable, 'inventory_script.py', section])  # nosec
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
    
    if not isbn:
        return jsonify({"status": "Error", "message": "Invalid book information"}), 400

    return jsonify({"status": "Book updated", "isbn": isbn, "new_title": new_title, "new_author": new_author, "new_year": new_year})

@app.route('/delete_book', methods=['POST'])
def delete_book():
    yaml_delete = request.data.decode('utf-8')
    delete_info = yaml.safe_load(yaml_delete)
    
    isbn = delete_info['isbn']
    
    if not isbn:
        return jsonify({"status": "Error", "message": "Invalid book information"}), 400

    return jsonify({"status": "Book deleted", "isbn": isbn})

@app.route('/generate_reports', methods=['GET'])
def generate_reports():
    report_type = request.args.get('type', '')
    if not report_type.isalnum():
        return jsonify({"status": "Invalid report type"}), 400
    subprocess.run([sys.executable, 'report_generator.py', report_type])  # nosec
    return jsonify({"status": "Report generation started"})

@app.route('/admin_panel', methods=['POST'])
def admin_panel():
    action = request.form.get('action', '')
    
    if action == 'backup':
        subprocess.run([sys.executable, 'backup_script.py'])  # nosec
        return jsonify({"status": "Backup initiated"})
    elif action == 'restore':
        subprocess.run([sys.executable, 'restore_script.py'])  # nosec
        return jsonify({"status": "Restore initiated"})
    else:
        return jsonify({"status": "Invalid action"}), 400

@app.route('/view_books', methods=['GET'])
def view_books():
    category = request.args.get('category', '')
    if not category.isalnum():
        return jsonify({"status": "Invalid category parameter"}), 400
    subprocess.run([sys.executable, 'view_books.py', category])  # nosec
    return jsonify({"status": "Books retrieval initiated", "category": category})

@app.route('/add_member', methods=['POST'])
def add_member():
    yaml_member = request.data.decode('utf-8')
    member_info = yaml.safe_load(yaml_member)
    
    member_name = member_info.get('name', '')
    member_id = member_info.get('id', '')
    membership_date = member_info.get('membership_date', '')

    if not member_name or not member_id:
        return jsonify({"status": "Error", "message": "Invalid member information"}), 400

    return jsonify({"status": "Member added", "name": member_name, "id": member_id, "membership_date": membership_date})

@app.route('/update_member', methods=['POST'])
def update_member():
    yaml_update = request.data.decode('utf-8')
    update_info = yaml.safe_load(yaml_update)
    
    member_id = update_info['id']
    new_name = update_info.get('new_name', '')
    new_date = update_info.get('new_date', '')
    
    if not member_id:
        return jsonify({"status": "Error", "message": "Invalid member information"}), 400

    return jsonify({"status": "Member updated", "id": member_id, "new_name": new_name, "new_date": new_date})

if __name__ == '__main__':
    app.run(debug=False)