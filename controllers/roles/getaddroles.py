import datetime
import os
import yaml
from flask import request
from flask_restful import Api, Resource
from sqlalchemy import exc
import sqlalchemy.exc as sqlalchemy_exc
from config import db, basedir
from models.roles import Roles
from schemas.roleschema import GetRolesSchema, AddRolesSchema



class GetAddRoles(Resource):
    def __init__(self):
        pass
    # Roles get call

    def get(self):
        try:
            obj = db.session.query(Roles).order_by(Roles.id).all()
            if obj:
                schema = GetRolesSchema(many=True)
                data = schema.dump(obj).data
                response = {"success": True, "message":"data fetched successfully" ,"data": data}
                return (response)
            else:
                response = {"success": False,
                            "message": "no data found in roles"}
                return(response)
        except Exception as e:
            return({"success": False, "message": "server is down try after sometime", "error": str(e.args)})

    # Roles post call
    def post(self):
        try:
            request_json_data = request.get_json()
            schema = AddRolesSchema()
            obj = schema.load(
                request_json_data, session=db.session).data
            db.session.add(obj)
            db.session.commit()
            data = schema.dump(obj).data
            role_response = {"success": True, "message": "data added successfully","data": data}
            return (role_response)
        except KeyError as e :
            return({"success": False, "message": "Incorrect key name", "error":str(e.args)})
        except exc.IntegrityError as e:
            errorInfo = e.orig.args
            message=errorInfo[1]
            return({"success": False, "message": message})
        except sqlalchemy_exc.SQLAlchemyError as e:
            return({"success": False, "message":str(e.args)})
        except Exception as e:
            return({"success": False, "message": str(e.args)})