import datetime
import os
import yaml
from flask import request
from flask_restful import Api, Resource
from sqlalchemy import exc
import sqlalchemy.exc as sqlalchemy_exc
from config import db, basedir
from models.searched_scripts import SearchedScripts
from schemas.searchedscripts_schema import *
import yfinance as yf


class GetAddSearchedScripts(Resource):
    def __init__(self):
        pass
    # SearchedScripts get call

    def get(self):
        try:
            obj = db.session.query(SearchedScripts).order_by(SearchedScripts.id).all()
            if obj:
                schema = GetSearchedScriptsSchema(many=True)
                data = schema.dump(obj).data
                response = {"success": True, "message":"data fetched successfully" ,"data": data}
                return (response)
            else:
                response = {"success": False,
                            "message": "no data found in SearchedScripts"}
                return(response)
        except Exception as e:
            return({"success": False, "message": "server is down try after sometime", "error": str(e.args)})

    # SearchedScripts post call
    def post(self):
        try:
            request_json_data = request.get_json()
            msft = yf.Ticker(request_json_data['stockscript'])
            # print(msft)
            output = msft.history(period="min")
            output.index = output.index.map(str)

            # print(data,type(data))
            output = output.to_dict('index')
            
            if len(output)==0:
                output = {"success":False}
            else:
                output["success"]=True
            request_json_data["stockscriptoutput"]=output
            print(request_json_data)
            schema = AddSearchedScriptsSchema()
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

class GetUserSearchedScripts(Resource):
    def __init__(self):
        pass
    # SearchedScripts get call

    def get(self,id):
        try:
            obj = SearchedScripts.query.filter(SearchedScripts.userId == id).order_by(SearchedScripts.id.desc()).all()
            # obj = db.session.query(SearchedScripts).order_by(SearchedScripts.id).all()
            if obj:
                schema = GetSearchedScriptsSchema(many=True)
                data = schema.dump(obj).data
                response = {"success": True, "message":"data fetched successfully" ,"data": data}
                return (response)
            else:
                response = {"success": False,
                            "message": "no data found in SearchedScripts"}
                return(response)
        except Exception as e:
            return({"success": False, "message": "server is down try after sometime", "error": str(e.args)})            