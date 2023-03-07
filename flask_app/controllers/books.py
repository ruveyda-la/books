from flask_app.models.book import Book
from flask_app.models.author import Author
from flask_app import app
from flask import render_template, request, redirect

@app.route("/books")
def read_books():
    books = Book.get_books()
    return render_template("books.html", books=books)


@app.route("/books/new",methods=['POST'])
def create_book():
    Book.save_book(request.form)
    return redirect("/books")

@app.route("/books/<int:id>")
def read_book_with_favorites(id):
    data={"id":id}
    book=Book.get_book_with_favorites(data)
    authors=Author.get_authors()

    return render_template("bookshow.html", book=book, authors=authors)


@app.route("/books/newfavorite", methods=['POST'])
def create_book_favorite():
    
    print(request.form, "***"* 4)
    Book.save_book_favorite(request.form)
    book_id=request.form['book_id']
    
    
    return redirect(f"/books/{book_id}")

