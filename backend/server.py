import os
from flask import Flask, request, jsonify, json, send_from_directory
import products_dao
import orders_dao
import uom_dao
from sql_connection import get_sql_connection

# Paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
UI_DIR = os.path.join(BASE_DIR, 'ui')

# Flask app
app = Flask(__name__)

# DB Connection
connection = get_sql_connection()

# ----------------- API ROUTES -----------------

@app.route('/getProducts', methods=['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getUOM', methods=['GET'])
def get_uom():
    uoms = uom_dao.get_uoms(connection)
    response = jsonify(uoms)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({'product_id': return_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteOrder', methods=['POST'])
def delete_order():
    return_id = orders_dao.delete_order(connection, request.form['order_id'])
    response = jsonify({'order_id': return_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({'order_id': order_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    orders = orders_dao.get_all_orders(connection)
    response = jsonify(orders)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({'product_id': product_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# ----------------- FRONTEND ROUTES -----------------

@app.route('/')
def index():
    return send_from_directory(UI_DIR, 'index.html')

@app.route('/manage-product.html')
def manage_product():
    return send_from_directory(UI_DIR, 'manage-product.html')

@app.route('/order.html')
def order():
    return send_from_directory(UI_DIR, 'order.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(UI_DIR, path)

# ----------------- MAIN -----------------

if __name__ == '__main__':
    print("🚀 Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000, debug=True)
