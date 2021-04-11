import datetime
from config import db


# Roles Model
class Roles(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(220), unique=True, nullable=False)
    status = db.Column(db.Boolean, default=True)
    createdAt = db.Column(db.DateTime,default=datetime.datetime.utcnow())
    updatedAt =  db.Column(db.DateTime, onupdate=datetime.datetime.utcnow())
