import datetime
from sqlalchemy.orm import validates
from config import db


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(220), nullable=False)
    email = db.Column(db.String(220), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    roleId = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    status = db.Column(db.Boolean, default=True)
    createdAt = db.Column(db.DateTime,default=datetime.datetime.utcnow())
    updatedAt =  db.Column(db.DateTime, onupdate=datetime.datetime.utcnow())
   
    @validates('email')
    def validate_email(self, key, address):
        assert '@' in address
        return address
