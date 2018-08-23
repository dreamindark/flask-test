

from operator import or_

from flask import jsonify
from app.libs.myprint import Myprint
from app.models.book import Book
from app.validator.form import BookSearchForm


api = Myprint('book')

@api.route('/show')
def show():
    book=Book.query.all()
    return jsonify(book)

@api.route('/search')

def search():
    form = BookSearchForm().validate_for_api()
    q = '%' + form.q.data + '%'

    books = Book.query.filter(
        or_(Book.title.like(q), Book.publisher.like(q))).all()
    books = [book.hide('summary') for book in books]
    return jsonify(books)

@api.route('/<isbn>/detail')
def detail(isbn):
    book = Book.query.filter_by(isbn=isbn).first_or_404
    return jsonify(book)