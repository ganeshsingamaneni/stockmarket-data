import datetime
from config import db


class SearchedScripts(db.Model):
    __tablename__ = "searched_scripts"
    id = db.Column(db.Integer, primary_key = True)
    stockscript = db.Column(db.String(200), nullable=False)
    stockscriptoutput = db.Column(db.Text,nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    createdAt = db.Column(db.DateTime,default=datetime.datetime.utcnow())
    updatedAt =  db.Column(db.DateTime, onupdate=datetime.datetime.utcnow())
   
    