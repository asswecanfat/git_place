from . import db


class Sign(db.Model):
    __tablename__ = 's_table'
    num = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    id = db.Column(db.BIGINT)
    name = db.Column(db.String(64))
    time = db.Column(db.DATETIME)
    url = db.Column(db.String(255))


class Stu(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.BIGINT, primary_key=True, nullable=True)
    name = db.Column(db.String(64), nullable=True)
