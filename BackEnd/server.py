
from flask import Flask, request, jsonify
import sqlConnection
import productDao
import unitIdDao
import ordersDao
import ast

app = Flask(__name__)
connection = sqlConnection.sql_connection()

@app.route('/')
def home():
    return "hello Moto"


@app.route('/getProduct', methods=['GET'])
def get_product():
    product = productDao.all_product(connection)
    response = jsonify(product)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insertProduct():
    request_payload = request.form['data']
    # print(request_payload)         // geting data as str need to convert to dict
    # print(type(request_payload))
    request_payload = ast.literal_eval(request_payload)
    # print(type(request_payload))
    product_id = productDao.insertNewProduct(connection, request_payload)
    response =jsonify({
        'product_id':product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteProduct', methods=['POST'])
def deleteProduct():
    return_id = productDao.delete_product(connection, request.form['productId'])
    response = jsonify({
        'prodcutId' : return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/unitId', methods=['GET'])
def unitId():
    unitId = unitIdDao.getUnitName(connection)
    response = jsonify(unitId)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insertOrder():
    request_payload = ast.literal_eval(request.form['data'])
    order_id = ordersDao.insertOrder(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getOrder', methods=['GET'])
def getOrders():
    allOrder = ordersDao.getAllOrder(connection)
    response = jsonify(allOrder)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run(port=1123)