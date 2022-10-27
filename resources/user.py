
from flask_restful import Resource, reqparse
from models.user_model import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type = str,
        required = True,
        help = "This field can't be empty."
    )

    parser.add_argument(
        'password',
        type = str,
        required = True,
        help = "This field can't be empty"
    )

    parser.add_argument(
        'role',
        type = int,
        required = True,
        help = "This field can't be empty."
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if(UserModel.find_by_username(data['username'])):
            return {"Message" : "A username with this name is already exist."}, 400

        user = UserModel(data["username"], data["password"], data["role"])
        user.save_to_db()

        return {"Message" : "User created successfully."}, 201

class UserList(Resource):
    def get(self):
        users = UserModel.query.all()
        return {"users" : [user.json() for user in users]}