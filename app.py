from flask import Flask
from flask_restful import Api
from db import db
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///exercise-tracker')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(User, '/api/exercise/new-user')
api.add_resource(Exercise, '/api/exercise/add')
api.add_resource(Exercise, '/api/exercise/log')

if __name__ == '__main__':
    app.run(debug=True)