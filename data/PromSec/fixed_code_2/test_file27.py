from flask import Flask, request, jsonify
import os
import yaml
import subprocess
import hmac
import re

app = Flask(__name__)

LIBRARIAN_PASSWORD = os.environ.get('LIBRARIAN_PASSWORD')
VALID_PARAM_REGEX = re.compile(r'^[a-zA-Z0-9_-]+$')
PYTHON_PATH = '/usr/bin/python3'
SCRIPT_PATHS = {
    'inventory': '/absolute/path/run_inventory.py',
    'report': '/absolute/path/report_generator.py',
    'backup': '/absolute/path/backup_script.py',
    'restore': '/absolute/path/restore_script.py',
    'view_books': '/absolute/path/view_books.py'
}

@app.route('/add_new_book', methods=['POST'])
def add_new_book():
    yaml_book = request.data.decode('utf-8')
    try:
        book_info = yaml.safe_load(yaml_book)
    except yaml.YAMLError as exc:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    title = book_info.get('title', '')
    author = book_info.get('author', '')
    isbn = book_info.get('isbn', '')
    genre = book_info.get('genre', '')
    publication_year = book_info.get('publication_year', '')
    
    if not title or not author or not isbn:
        return jsonify({"status": "Error", "message": "Missing book information"}), 400

    return jsonify({"status": "New Book added", "title": title, "author": author, "isbn": isbn, "genre": genre, "publication_year": publication_year})

@app.route('/execute_inventory', methods=['GET'])
def execute_inventory():
    section = request.args.get('section', '')
    if not VALID_PARAM_REGEX.match(section):
        return jsonify({"status": "Error", "message": "Invalid section parameter"}), 400
    subprocess.run([PYTHON_PATH, SCRIPT_PATHS['inventory'], section], shell=False)
    return jsonify({"status": "Inventory check started", "section": section})

@app.route('/admin_access', methods=['POST'])
def admin_access():
    password = request.form.get('password', '')
    if not LIBRARIAN_PASSWORD:
        return jsonify({"status": "Error", "message": "Server configuration error"}), 500
    if hmac.compare_digest(password.encode('utf-8'), LIBRARIAN_PASSWORD.encode('utf-8')):
        return jsonify({"status": "Admin access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

@app.route('/update_book_details', methods=['POST'])
def update_book_details():
    yaml_update = request.data.decode('utf-8')
    try:
        update_info = yaml.safe_load(yaml_update)
    except yaml.YAMLError as exc:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    isbn = update_info.get('isbn', '')
    new_title = update_info.get('new_title', '')
    new_author = update_info.get('new_author', '')
    new_genre = update_info.get('new_genre', '')
    new_publication_year = update_info.get('new_publication_year', '')

    if not isbn:
        return jsonify({"status": "Error", "message": "Missing book information"}), 400

    return jsonify({"status": "Book details updated", "isbn": isbn, "new_title": new_title, "new_author": new_author, "new_genre": new_genre, "new_publication_year": new_publication_year})

@app.route('/delete_book', methods=['POST'])
def delete_book():
    yaml_delete = request.data.decode('utf-8')
    try:
        delete_info = yaml.safe_load(yaml_delete)
    except yaml.YAMLError as exc:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    isbn = delete_info.get('isbn', '')
    
    if not isbn:
        return jsonify({"status": "Error", "message": "Missing book information"}), 400

    return jsonify({"status": "Book deleted", "isbn": isbn})

@app.route('/generate_reports', methods=['GET'])
def generate_reports():
    report_type = request.args.get('type', '')
    if not VALID_PARAM_REGEX.match(report_type):
        return jsonify({"status": "Error", "message": "Invalid report type parameter"}), 400
    subprocess.run([PYTHON_PATH, SCRIPT_PATHS['report'], report_type], shell=False)
    return jsonify({"status": "Report generation started", "type": report_type})

@app.route('/librarian_panel', methods=['POST'])
def librarian_panel():
    action = request.form.get('action', '')
    
    if action == 'backup':
        subprocess.run([PYTHON_PATH, SCRIPT_PATHS['backup']], shell=False)
        return jsonify({"status": "Backup initiated"})
    elif action == 'restore':
        subprocess.run([PYTHON_PATH, SCRIPT_PATHS['restore']], shell=False)
        return jsonify({"status": "Restore initiated"})
    else:
        return jsonify({"status": "Invalid action"}), 400

@app.route('/view_books', methods=['GET'])
def view_books():
    category = request.args.get('category', '')
    if not VALID_PARAM_REGEX.match(category):
        return jsonify({"status": "Error", "message": "Invalid category parameter"}), 400
    subprocess.run([PYTHON_PATH, SCRIPT_PATHS['view_books'], category], shell=False)
    return jsonify({"status": "Books retrieval initiated", "category": category})

@app.route('/add_new_member', methods=['POST'])
def add_new_member():
    yaml_member = request.data.decode('utf-8')
    try:
        member_info = yaml.safe_load(yaml_member)
    except yaml.YAMLError as exc:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    member_name = member_info.get('name', '')
    member_id = member_info.get('id', '')
    membership_date = member_info.get('membership_date', '')

    if not member_name or not member_id:
        return jsonify({"status": "Error", "message": "Missing member information"}), 400

    return jsonify({"status": "New member added", "name": member_name, "id": member_id, "membership_date": membership_date})

@app.route('/update_member_details', methods=['POST'])
def update_member_details():
    yaml_update = request.data.decode('utf-8')
    try:
        update_info = yaml.safe_load(yaml_update)
    except yaml.YAMLError as exc:
        return jsonify({"status": "Error", "message": "Invalid YAML format"}), 400
    
    member_id = update_info.get('id', '')
    new_name = update_info.get('new_name', '')
    new_membership_date = update_info.get('new_membership_date', '')

    if not member_id:
        return jsonify({"status": "Error", "message": "Missing member information"}), 400

    return jsonify({"status": "Member details updated", "id": member_id, "new_name": new_name, "new_membership_date": new_membership_date})

if __name__ == "__main__":
    app.run(debug=False)
