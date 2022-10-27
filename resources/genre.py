from models.genre_model import GenreModel
from flask import jsonify, request
from flask_restful import Resource, reqparse

class Genre(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name', 
        type = str,
        required = True,
        help = 'This field cannot be empty.'
    )

    def post(self):

        data = Genre.parser.parse_args()
        author = GenreModel.find_by_genre_name(data['name'])

        if author:
            return{"Message" : "{} already exists.".format(data['name'])}, 400

        author = GenreModel(data['name'])
        try:
            author.save_to_db()
        except:
            {"Message":"Error occours."}, 404

        return author.json(), 201

class GenreList(Resource):
    def get(self):
        genre = GenreModel.query.all()
        return {"Genre List" : [g.json() for g in genre]}

class SearchGenre(Resource):
    def get(self, genre):
        genre = GenreModel.find_by_genre_name(genre)
        if genre:
            return genre.json()
        return {"Message" : "Genre Not Found"}, 404