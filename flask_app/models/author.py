from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import book

class Author:

    db="books_schema"
    def __init__ (self,data):
        self.id=data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorites=[]

    @classmethod
    def get_authors(cls):
        query = "SELECT * FROM authors;"
    
        results = connectToMySQL(cls.db).query_db(query)
    
        authors = []

        for result in results:
            authors.append( cls(result) )
        return authors

    @classmethod
    def save_author(cls,data):
        query = """INSERT INTO authors (name)
                VALUES (%(name)s);"""
        result=connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def get_author_with_favorites(cls,data):
        query="""SELECT * FROM authors LEFT JOIN favorites
            ON authors.id=favorites.author_id
            LEFT JOIN books 
            ON favorites.book_id= books.id
            WHERE authors.id=%(id)s;"""
        results=connectToMySQL(cls.db).query_db(query,data)
        author=cls(results[0])
        for item in results:
            print(item)
            temp_favorite ={ 
                'id':item['book_id'],
                'title':item['title'],
                'num_of_pages':item['num_of_pages'],
                'created_at':item['books.created_at'],
                'updated_at':item['books.updated_at']  
            }
            author.favorites.append(book.Book(temp_favorite))
        print(author.favorites)
        return author

    @classmethod
    def save_author_favorite(cls,data):
        query = """INSERT INTO favorites (author_id, book_id)
                VALUES (%(author_id)s, %(book_id)s);"""
        result=connectToMySQL(cls.db).query_db(query,data)
        return result





        

    
