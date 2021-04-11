from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import *
from models.roles import Roles
from models.users import Users
from models.searched_scripts import SearchedScripts

migrate = Migrate(app, db, compare_type=True)
app.app_context().push()
db.init_app(app)
db.create_all(app=app)
db.session.commit()

manager = Manager(app)
manager.add_command('db', MigrateCommand)
# sudo apt-get install python3.7-dev libmysqlclient-dev

if __name__ == '__main__':
    manager.run()
