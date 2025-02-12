from flask import Flask, request, jsonify
import os
import yaml
import subprocess  # nosec B404
import hmac

app = Flask(__name__)

SUPER_SECRET_KEY = os.environ["SUPER_SECRET_KEY"]

@app.route('/process_order', methods=['POST'])
def process_order():
    yaml_order = request.data.decode('utf-8')
    order_data = yaml.safe_load(yaml_order)
    
    product_id = order_data['product_id']
    quantity = order_data['quantity']
    shipping_address = order_data['shipping_address']
    
    return jsonify({"status": "Order processed", 
                    "product": product_id, 
                    "quantity": quantity,
                    "shipping_to": shipping_address})

@app.route('/generate_invoice', methods=['GET'])
def generate_invoice():
    order_id = request.args.get('id', '')
    if not order_id.isalnum():
        return jsonify({"error": "Invalid order ID"}), 400
    subprocess.run(["./invoice_generator", order_id], shell=False)  # nosec B603
    return jsonify({"status": "Invoice generation initiated"})

@app.route('/admin_panel', methods=['POST'])
def admin_panel():
    provided_key = request.form.get('key', '')
    
    if hmac.compare_digest(provided_key.encode(), SUPER_SECRET_KEY.encode()):
        return jsonify({"status": "Admin access granted"})
    else:
        return jsonify({"status": "Access denied"}), 401

@app.route('/update_inventory', methods=['POST'])
def update_inventory():
    yaml_inventory = request.data.decode('utf-8')
    inventory_data = yaml.safe_load(yaml_inventory)
    return jsonify({"status": "Inventory updated", 
                    "new_inventory": inventory_data})

if __name__ == '__main__':
    app.run(debug=False)
