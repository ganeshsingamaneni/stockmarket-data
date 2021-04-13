from marshmallow import fields
from config import ma, db
from models.searched_scripts import SearchedScripts
from schemas.userschema import GetUsersSchema

# SearchedScripts get and getbyid schema
class GetSearchedScriptsSchema(ma.ModelSchema):
    userscripts = ma.Nested(GetUsersSchema)
    class Meta:
        model = SearchedScripts
        fields = ("id", "stockscript","stockscriptoutput","userscripts")
        sqla_session = db.session

# SearchedScripts add Schema
class AddSearchedScriptsSchema(ma.ModelSchema):
    class Meta:
        model = SearchedScripts
        fields = ("id", "stockscript","stockscriptoutput","userId")
        sqla_session = db.session


class GetUserSearchedScriptsSchema(ma.ModelSchema):
    class Meta:
        model = SearchedScripts
        fields = ("id", "stockscript")
        sqla_session = db.session
