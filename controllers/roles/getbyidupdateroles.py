import datetime
import os
import yaml
from flask import request
from flask_restful import Api, Resource
from sqlalchemy import exc
import sqlalchemy.exc as sqlalchemy_exc
from config import db, basedir
from models.roles import Roles
from schemas.roleschema import GetRolesSchema


class GetUpdateRoles(Resource):
    def __init__(self):
        pass

    # Roles get call based on id
    def get(self, id):
        try:
            obj = Roles.query.filter(Roles.id == id).one_or_none()
            if obj is not None:
                schema = GetRolesSchema()
                data = schema.dump(obj).data
                response = {"success": True, "message":"data fetched successfully", "data": data}
                return (response)
            else:
                response = {"success": False, "message": "no data found on this id", "id": id}
                return(response)
        except Exception as e:
            return({"success": False, "message": "server is down try after sometime", "error": str(e)})



    