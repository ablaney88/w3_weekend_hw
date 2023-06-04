from models.book import *

book1 = Book("Empire State", "Colin Bateman", "Dark Comedy")
book2 = Book("The Lord of the Rings", "J.R.R. Tolkien", "Fantasy")
book3 = Book("The Handmaids Tale", "Margaret Atwood", "Dystopian")

books = [book1, book2, book3]

def add_new_book(book):
    books.append(book)

def delete_book(book_name):
    book_to_delete = None
    for book in books:
        if book.book_title == book_name:
            book_to_delete = book
            break

    books.remove(book_to_delete)

def delete_book_by_index(index):
    books.pop(index)