from db import db

class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    exercises = db.relationship('ExerciseModel')

    def __init__(self, username):
        self.username = username

    def json(self):
        return {
            'id': self.id,
            'username': self.username
        }

    @classmethod
    def find_by_username(cls, username):
        # SELECT * FROM items WHERE name=name LIMIT 1
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, id):
        # SELECT * FROM items WHERE name=name LIMIT 1
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()