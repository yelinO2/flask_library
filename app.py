from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from db import db
from secutiy import authenticate, identity
from resources.genre import Genre, GenreList, SearchGenre
from resources.author import Authors, AuthorList, SearchAuthor
from resources.user import UserRegister, UserList
from resources.book import Books, BookList, SearchByLang, SearchByBookName, DeleteBook

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///library.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

api = Api(app)
app.secret_key = "not_today"
JWT = JWT(app, authenticate, identity)

api.add_resource(UserRegister, '/register') # user register
api.add_resource(UserList, '/all_users') # user list
api.add_resource(Books, '/book/add') # add books
api.add_resource(BookList, '/books') # book list
api.add_resource(SearchByLang, '/books/lang/<string:lang>') # search book by lang
api.add_resource(SearchByBookName, '/books/<string:name>') # search book by name
# api.add_resource(UpdateBookInfo, '/book/update')
api.add_resource(DeleteBook, '/book/delete/<int:b_id>') # delete book
api.add_resource(Authors, '/author/add') # add author
api.add_resource(Genre, '/genre/add')  # add genre
api.add_resource(AuthorList, '/authors/all') # author list
api.add_resource(GenreList, '/genre/all') #  genre list
api.add_resource(SearchGenre, '/genre/<string:genre>') # search by genre name
api.add_resource(SearchAuthor, '/author/<string:author>') # search by author name
 
@app.before_first_request
def create_table():
    db.create_all()






if __name__ == "__main__":

    from db import db
    db.init_app(app)

    app.run(debug=True)