from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import BookSchema

blp = Blueprint('books', 'books', url_prefix='/books', description='Operations on books')

books = []

@blp.route('/')
class BookList(MethodView):
    @blp.response(200, description="Success")
    def get(self):
        return books
    
    @blp.arguments(BookSchema)
    @blp.response(201, description="Book added successfully")
    def post(self, new_book):
        isExist = any(book for book in books if book["title"] == new_book["title"])
        if isExist:
            abort(404, message="Book alreday exist")
        new_book["id"] = len(books) + 1
        books.append(new_book)
        return new_book
    
@blp.route('/<int:book_id>')
class Book(MethodView):
    @blp.response(200, description="Book read successfully")
    def get(self, book_id):
        book = next((book for book in books if book["id"] == book_id), None)
        if book is None:
            abort(404, description="Book not found")
        return book

    @blp.arguments(BookSchema)
    # @blp.response(200, BookSchema)
    @blp.response(200, description="Book update successfully")
    def put(self, update_book, book_id):
        book = next((book for book in books if book["id"] == book_id), None)
        if book is None:
            books.append(update_book)
        book.update(update_book)
        return book
    
    @blp.response(204, description="Book delete successfully")
    def delete(self, book_id):
        global books
        isExist = any(book for book in books if book["id"] == book_id)
        if not isExist:
            abort(404, description="Book not found")
        books = [book for book in books if book["id"]!= book_id]
        return ""