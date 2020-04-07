from db import db
import datetime

class ExerciseModel(db.Model):
    __tablename__ = 'exercise'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80))
    duration = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.id'))

    def __init__(self, user_id, description, duration, date):
        self.description = description
        self.user_id = user_id
        self.duration = duration
        self.date = date

    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'duration': self.duration,
            'date': self.date
        }

    @classmethod
    def find_by_user_id(cls, user_id):
        # SELECT * FROM items WHERE name=name
        return cls.query.filter_by(user_id=user_id)

    @classmethod
    def find_by_id(cls, id):
        # SELECT * FROM items WHERE name=name LIMIT 1
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()