import datetime
import os
import yaml
from flask import request
from flask_restful import Api, Resource
from sqlalchemy import exc
import sqlalchemy.exc as sqlalchemy_exc
from werkzeug.security import generate_password_hash
from config import db, basedir
from models.users import Users
from schemas.userschema import UsersSchema


class GetUpdateUser(Resource):
    def __init__(self):
        pass

    # users get call based on id
    def get(self, id):
        try:
            user = Users.query.filter(Users.id == id).one_or_none()
            if user is not None:
                user_schema = UsersSchema()
                data = user_schema.dump(user).data
                user_response = {"success": True, "message":"data fetched successfully", "data": data}
                return (user_response)
            else:
                response = {"success": False, "message": "no data found on this id", "id": id}
                return(response)
        except Exception as e:
            return({"success": False, "message": "server is down try after sometime", "error": str(e)})



    