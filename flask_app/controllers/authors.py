from flask_app.models.author import Author
from flask_app.models.book import Book
from flask_app import app
from flask import render_template, request, redirect

@app.route("/authors")
def read_authors():
    authors = Author.get_authors()
    return render_template("authors.html", authors=authors)


@app.route("/authors/new",methods=['POST'])
def create_author():
    Author.save_author(request.form)
    return redirect("/authors")

@app.route("/authors/<int:id>")
def read_author_with_favorites(id):
    data={'id':id}
    author= Author.get_author_with_favorites(data)
    books=Book.get_books()
    return render_template('authorshow.html',author=author, books=books)

@app.route("/authors/newfavorite", methods=['POST'])
def create_author_favorite():
    Author.save_author_favorite(request.form)
    author_id=request.form['author_id']
    
    return redirect(f"/authors/{author_id}")
