from flask import render_template, request, redirect
from app import app
from models.books import books, add_new_book, delete_book, delete_book_by_index
from models.book import Book


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/books")
def show_books():
    return render_template("index.html", books=books)

@app.route('/books/<index>')
def single_order(index):
  chosen_book = books[int(index)]
  
  return render_template('book.html', book=chosen_book)

@app.route("/books", methods=['POST'])
def add_book():
    book_title = request.form['Book Title']
    author = request.form['Author']
    genre = request.form['Genre']

    # recurring = True if "recurring" in request.form else False

    new_book = Book(book_title, author, genre)

    add_new_book(new_book)
    return redirect("/books")

# @app.route("/books/del/<index>", methods=["POST"])
# def delete_by_index(index):
#     delete_book_by_index(int(index))
#     return redirect("/books")


@app.route("/books/delete/<name>", methods=["POST"])
def delete(name):
    delete_book(name)
    return redirect("/books")


