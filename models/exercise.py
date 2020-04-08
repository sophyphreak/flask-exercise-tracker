from db import db
import datetime
import arrow


class ExerciseModel(db.Model):
    __tablename__ = "exercise"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80))
    duration = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __init__(self, user_id, description, duration, date):
        self.description = description
        self.user_id = user_id
        self.description = description
        self.duration = duration
        self.date = date

    def json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "description": self.description,
            "duration": self.duration,
            "date": arrow.get(self.date).format("YYYY-MM-DD"),
        }

    @classmethod
    def find_by_user_id(cls, user_id):
        # SELECT * FROM items WHERE name=name
        return cls.query.filter_by(user_id=user_id)

    @classmethod
    def find_by_id(cls, id):
        # SELECT * FROM items WHERE name=name LIMIT 1
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_date_range(cls, user_id, _from, to, limit):
        if not _from:
            _from = "0001-01-01"
        if not to:
            to = datetime.datetime.utcnow()
        if not limit:
            limit = None
        return (
            cls.query.filter(
                ExerciseModel.user_id == user_id,
                ExerciseModel.date >= arrow.get(_from).datetime,
                ExerciseModel.date <= arrow.get(to).datetime,
            )
            .limit(limit)
            .all()
        )

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
