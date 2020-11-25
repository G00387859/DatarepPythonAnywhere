##basic flask server 
from flask import Flask, url_for, request, redirect, abort, jsonify
app = Flask(__name__, static_url_path='', static_folder='staticpages')
books=[
{"id": 1, "Title": "Harry Potter", "Author": "JK", "Price": 1000},
{"id": 2, "Title": "some cook book", "Author": "Mr Angry Man", "Price": 2000},
{"id": 3, "Title": "Python made easy", "Author": "Some Liar", "Price": 1500}
]

nextId=5

#app = Flask(__name__, static_url_path='', static_folder='staticpages')
@app.route('/')
def index():
    ##return redirect(url_for('books'))
    return "hello donal maher" 
#Get all books
#curl http://127.0.0.1:5000/books
@app.route('/books')
def getAll():
    return jsonify(books)

# find books By id
#curl http://127.0.0.1:5000/books/id
@app.route('/books/<int:id>')
def findById(id):
    foundBooks = list(filter (lambda t : t["id"]== id, books))
    if len(foundBooks) == 0:
        return jsonify({}) , 204
    return jsonify(foundBooks[0])


#curl  -H "Content-Type:application/json" -X POST -d "{\"Title\":\“xxx\",\"Author\":\“xxx\",\"Price\":3000}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
    global nextId
    book = {
        "id":nextId,
        "Title": request.json["Title"],
        "Author": request.json["Author"], 
        "Price": request.json["Price"]
        }
    books.append(book)
    return jsonify(books)

#PU#update
# curl -X PUT -d "{\"Title\":\"new Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    foundBooks = list(filter(lambda t: t["id"] == id, books))
    if len(books) == 0:
        return jsonify({}), 404
    currentBook = foundBooks[0]
    if 'Title' in request.json:
        currentBook['Title'] = request.json['Title']
    if 'Author' in request.json:
        currentBook['Author'] = request.json['Author']
    if 'Price' in request.json:
        currentBook['Price'] = request.json['Price']
    return jsonify(currentBook)
#delete
# curl -X DELETE http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    foundBooks = list(filter(lambda t: t["id"] == id, books))
    if len(foundBooks) == 0:
        return jsonify({}), 404
    books.remove(foundBooks[0])
    return jsonify({"done":True})

if __name__ == "__main__":
    app.run(debug=True) 