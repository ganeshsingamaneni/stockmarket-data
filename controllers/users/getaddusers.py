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
from schemas.userschema import UsersSchema, AddUserSchema






class GetAddUsers(Resource):
    def __init__(self):
        pass
    # get all users

    def get(self):
        try:
            user_id = request.headers.get('userid')
            obj = Users.query.filter(Users.id != user_id).order_by(Users.id).all()
            if obj:
                schema = UsersSchema(many=True)
                data = schema.dump(obj).data
                response = {
                    "success": True, "message": "data fetched succeessfully", "data": data}
                return (response)
            else:
                response = {"success": False,
                            "message": "no data found in users"}
                return(response)
        except Exception as e:
            return({"success": False, "error_message": "server is down try after sometime", "error": str(e)})

    # post users
    def post(self):
        try:
            request_json_object = request.get_json()
            request_json_object['password'] = generate_password_hash(
                request_json_object['password'])
            schema = AddUserSchema()
            new_user_obj = schema.load(
                request_json_object, session=db.session).data
            db.session.add(new_user_obj)
            db.session.commit()
            data = schema.dump(new_user_obj).data
            user_response = {
                "success": True, "message": "User registered succeessfully", "data": data}
            return (user_response)
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