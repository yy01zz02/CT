from flask import Flask, request, jsonify
import os
import yaml
import subprocess  # nosec: B404
import sys
import re
import hmac

app = Flask(__name__)

LIBRARIAN_PASSWORD = os.getenv("LIBRARIAN_PASSWORD")
if not LIBRARIAN_PASSWORD:
    raise ValueError("LIBRARIAN_PASSWORD environment variable must be set.")

def get_script_path(script_name):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), script_name)

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
    if not re.fullmatch(r'^[a-zA-Z0-9_-]*$', section):
        return jsonify({"status": "Invalid section parameter"}), 400
    script_path = get_script_path('inventory_script.py')
    subprocess.run([sys.executable, script_path, section], check=True, shell=False)  # nosec: B603
    return jsonify({"status": "Inventory check initiated"})

@app.route('/librarian_access', methods=['POST'])
def librarian_access():
    password = request.form.get('password', '')
    if hmac.compare_digest(password.encode('utf-8'), LIBRARIAN_PASSWORD.encode('utf-8')):
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
    if not re.fullmatch(r'^[a-zA-Z0-9_-]*$', report_type):
        return jsonify({"status": "Invalid report type"}), 400
    script_path = get_script_path('report_generator.py')
    subprocess.run([sys.executable, script_path, report_type], check=True, shell=False)  # nosec: B603
    return jsonify({"status": "Report generation started"})

@app.route('/admin_panel', methods=['POST'])
def admin_panel():
    action = request.form.get('action', '')
    
    if action == 'backup':
        script_path = get_script_path('backup_script.py')
        subprocess.run([sys.executable, script_path], check=True, shell=False)  # nosec: B603
        return jsonify({"status": "Backup initiated"})
    elif action == 'restore':
        script_path = get_script_path('restore_script.py')
        subprocess.run([sys.executable, script_path], check=True, shell=False)  # nosec: B603
        return jsonify({"status": "Restore initiated"})
    else:
        return jsonify({"status": "Invalid action"}), 400

@app.route('/view_books', methods=['GET'])
def view_books():
    category = request.args.get('category', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]*$', category):
        return jsonify({"status": "Invalid category parameter"}), 400
    script_path = get_script_path('view_books.py')
    subprocess.run([sys.executable, script_path, category], check=True, shell=False)  # nosec: B603
    return jsonify({"status": "Books retrieval initiated", "category": category})

if __name__ == '__main__':
    app.run(debug=False)
