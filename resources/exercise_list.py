from flask_restful import Resource, reqparse
import arrow

from models.exercise import ExerciseModel 

class ExerciseList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('userId',
        type=int,
        location='args',
        required=True,
        help="userId is required"
    )
    parser.add_argument('from',
        type=str,
        location='args'
    )
    parser.add_argument('to',
        type=str,
        location='args'
    )
    parser.add_argument('limit',
        type=int,
        location='args'
    )
    
    def get(self):
        data = ExerciseList.parser.parse_args()
        user_id = data['userId']
        limit = data['limit']
        if data['from']:
            try:
                _from = arrow.get(data['from'])
            except:
                _from = None
        else:
            _from = None
        if data['to']:
            try:
                to = arrow.get(data['to'])
            except:
                to = None
        else:
            to = None
        if not limit:
            limit = None
        raw_exercise_list = ExerciseModel.find_by_date_range(user_id, _from, to, limit)
        return list(map(convert_ExerciseModel_to_json, raw_exercise_list))

def convert_ExerciseModel_to_json(raw_exercise):
    return raw_exercise.json()