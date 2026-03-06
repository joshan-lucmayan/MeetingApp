from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    host = db.Column(db.String(100))
    date_time = db.Column(db.String(50))