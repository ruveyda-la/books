from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import author

class Book:

    db="books_schema"
    def __init__ (self,data):
        self.id=data['id']
        self.title = data['title']
        self.num_of_pages=data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorited_authors=[]

    @classmethod
    def get_books(cls):
        query = "SELECT * FROM books;"
    
        results = connectToMySQL(cls.db).query_db(query)
    
        books = []

        for result in results:
            books.append( cls(result) )
        return books

    @classmethod
    def save_book(cls,data):
        query = """INSERT INTO books (title,num_of_pages)
                VALUES (%(title)s,%(num_of_pages)s);"""
        result=connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def get_book_with_favorites(cls,data):
        query="""SELECT * FROM books LEFT JOIN favorites
            ON books.id=favorites.book_id
            LEFT JOIN authors 
            ON  authors.id=favorites.author_id
            WHERE books.id=%(id)s;"""
        results=connectToMySQL(cls.db).query_db(query,data)
        book=cls(results[0])
        for item in results:
            if item['authors.id'] == None:
                break
            temp_favorite ={ 
                'id':item['authors.id'],
                'name':item['name'],
                'created_at':item['authors.created_at'],
                'updated_at':item['authors.updated_at']  
            }
            book.favorited_authors.append(author.Author(temp_favorite))
        return book

    @classmethod
    def save_book_favorite(cls,data):
        query = """INSERT INTO favorites (author_id, book_id)
                VALUES (%(author_id)s, %(book_id)s);"""
        result=connectToMySQL(cls.db).query_db(query,data)
        return result