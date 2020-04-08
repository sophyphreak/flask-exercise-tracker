from flask_restful import Resource, reqparse
import arrow

from models.exercise import ExerciseModel


class Exercise(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "userId",
        type=str,
        location="form",
        required=True,
        help="userId cannot be empty",
    )
    parser.add_argument(
        "description",
        type=str,
        location="form",
        required=True,
        help="description cannot be empty",
    )
    parser.add_argument(
        "duration",
        type=str,
        location="form",
        required=True,
        help="duration cannot be empty",
    )
    parser.add_argument("date", type=str, location="form")

    def post(self):
        data = Exercise.parser.parse_args()
        user_id = data["userId"]
        description = data["description"]
        duration = data["duration"]
        if data["date"]:
            date = arrow.get(data["date"]).datetime
        else:
            date = arrow.utcnow().datetime

        new_exercise = ExerciseModel(user_id, description, duration, date)
        new_exercise.save_to_db()
        return new_exercise.json(), 201
