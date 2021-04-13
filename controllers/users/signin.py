
import os
import yaml
from flask import request, session
from flask_restful import Resource
from werkzeug.security import check_password_hash
from config import *
from models.users import Users
from schemas.userschema import SigninSchema,UsersSchema



# user sign in api call
class Signin(Resource):
    def __init__(self):
        pass

    def post(self):
        try:
            request_json_data = request.get_json()
            email = request_json_data['email']
            password = request_json_data['password']
            email_check = db.session.query(Users).filter(
                Users.email == email).first()
            if email_check is not None:
                schema = UsersSchema()
                data = schema.dump(email_check).data
                hashed_password = email_check.password
                if check_password_hash(hashed_password, password):
                    # expires = datetime.timedelta(hours=1)
                    # token_data = {"email": request_json_data['email'], "password": request_json_data['password'], "name": data['name'], "user_id": data["id"]}
                    # access_token = create_access_token(
                    #     token_data, expires_delta=expires)
                    # data.update({"access_token": access_token})
                    success_response = {
                        "success": True, 'data': data, 'message': 'User logined successfully'}
                    return(success_response)
                else:
                    password_response = {"success": False,
                                         "message": "Invalid password"}
                    return(password_response)
            else:
                username_response = {"success": False,
                                     "message": "Invalid UserName"}
                return(username_response)
        except Exception as e:
            return({"success": False, "message": "server is down try after sometime", "error": str(e)})


