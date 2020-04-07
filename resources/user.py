from flask_restful import Resource, reqparse

from models.user import UserModel 

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        location='form',
        required=True,
        help="username cannot be empty"
    )

    def post(self):
        data = User.parser.parse_args()
        username = data['username'] 

        already_exists = UserModel.find_by_username(username)
        if already_exists:
            return already_exists.json()

        new_user = UserModel(username)
        new_user.save_to_db()
        return new_user.json(), 201