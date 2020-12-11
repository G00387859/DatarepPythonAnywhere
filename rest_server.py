from flask import render_template,Flask, url_for, request, redirect, abort, jsonify,Response
#from BookDao import bookDao
from storeDao import StoreDao
#from staticpages import 'index.html' as idex

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/')
def index():
     return app.send_static_file('home.html')


@app.route('/products')
def getAll():
    return jsonify(StoreDao.getAll(StoreDao))
# find By id
#


@app.route('/products/<productName>')
def findById(productName):
    return jsonify(StoreDao.findById(StoreDao,productName))

# insert
# curl  -H "Content-Type:application/json" -X POST -d "{\"productType\":\"veg\",\"productName\":\"corn\",\"productPrice\":\"3\"}" http://127 .0.0.1:5000/products
@app.route('/products', methods=['POST'])
def insert():
   #dir
    if not request.json:
        abort(400)

    products = {
        "productType": request.json["productType"],
        "productName": request.json["productName"],
        "productPrice": request.json["productPrice"]
    }
    return jsonify(StoreDao.insert(StoreDao, products))

    #return "served by Create "

#update
# curl -X PUT -d "{\"Title\":\"new Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/books/1
# curl -X PUT -d "{\"productName\":\"corn\",\"productType\:"\veg\", \"productPrice\":3.99}" -H "content-type:application/json" http://127.0. 0.1:5000/books/corn
# curl -X PUT -d "{\"productType\":\"corn\", \"productPrice\":999}" -H "content-type:application/json" http://127.0.0.1:5000/products/corn
   #productName','productType','productPrice
@app.route('/products/<productName>', methods=['PUT'])
def update(productName):
    foundBook=StoreDao.findById(StoreDao,productName)
    print (foundBook)
    if foundBook == {}:
        return jsonify({}), 404
    currentBook = foundBook
    if 'productType' in request.json:
        currentBook['productType'] = request.json['productType']
    if 'productPrice' in request.json:
        currentBook['productPrice'] = request.json['productPrice']
    StoreDao.update(StoreDao,currentBook)

    return jsonify(currentBook)

#delete
# curl -X DELETE http://127.0.0.1:5000/books/1


@app.route('/products/<productName>', methods=['DELETE'])
def delete(productName):
    StoreDao.delete(StoreDao,productName)

    return jsonify({"done": True})


if __name__ == "__main__":
    app.run(debug=True)