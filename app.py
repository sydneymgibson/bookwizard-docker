from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory "database"
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "genre": "Fiction"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "genre": "Fiction"},
    {"id": 3, "title": "1984", "author": "George Orwell", "year": 1949, "genre": "Dystopian"},
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    if not new_book.get('id') or not new_book.get('title'):
        abort(400, description="Missing id or title")
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book is None:
        abort(404)
    data = request.get_json()
    book.update(data)
    return jsonify(book)

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)