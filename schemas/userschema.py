from marshmallow import fields
from config import ma, db
from models.users import Users


class UsersSchema(ma.ModelSchema):
    class Meta:
        model = Users
        fields = ('id','name', 'email', 'roleId')
        sqla_session = db.session

class AddUserSchema(ma.ModelSchema):
    class Meta:
        model = Users
        fields = ('id', 'name', 'email', 'status', 'roleId', 'password')
        sqla_session = db.session

class SigninSchema(ma.ModelSchema):
    class Meta:
        model = Users
        fields = ('id','name','email')
        sqla_session = db.session

