from flask import Flask, render_template,send_from_directory
from flask_cors import CORS
from flask_restful import Api
from config import *

api = Api(app)
CORS(app)

from controllers.roles.getaddroles import GetAddRoles
from controllers.roles.getbyidupdateroles import GetUpdateRoles

api.add_resource(GetAddRoles, '/api/roles')
api.add_resource(GetUpdateRoles,'/api/roles/<int:id>')


from controllers.users.getaddusers import GetAddUsers
from controllers.users.getbyidupdateuser import GetUpdateUser
# from controllers.users.signin import Signin

api.add_resource(GetAddUsers, '/api/users')
api.add_resource(GetUpdateUser,'/api/users/<int:id>')


from controllers.searched_scripts.getaddsearched_scripts import GetAddSearchedScripts,GetUserSearchedScripts

api.add_resource(GetAddSearchedScripts, '/api/getaddsearchedscripts')
api.add_resource(GetUserSearchedScripts,'/api/getusersearchedscripts/<int:id>')

# api.add_resource(Signin, '/api/usersignin')


# @app.route('/api/templaterender')
# def RenderNewspaperTemplate():
#     return render_template('news_paper_grid.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)