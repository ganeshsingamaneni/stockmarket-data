from marshmallow import fields
from config import ma, db
from models.roles import Roles

# Roles get and getbyid schema
class GetRolesSchema(ma.ModelSchema):
    class Meta:
        model = Roles
        fields = ("id", "name")
        sqla_session = db.session

# Roles add Schema
class AddRolesSchema(ma.ModelSchema):
    class Meta:
        model = Roles
        sqla_session = db.session


