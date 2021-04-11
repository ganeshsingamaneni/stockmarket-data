import datetime
import os
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@localhost:3306/stockscript"

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
ma = Marshmallow(app)
db.init_app(app)


