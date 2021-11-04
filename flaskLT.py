''' creating models/tables for Lifetime Prop. with Flask Book as reference example '''

from flask import Flask
from flask_mail import Message
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

def getSqlAlchemyString():
        ''' Set configuration variables for MySQL Access via SQLAlchemy '''

        # string parameters 
        username = "root"
        password = "ubu2Root!"
        host = "localhost"
        db_name = "testdb"
        db_cnctr_mod = "pymysql"   # using PyMySql but will change for other modules
        
        # optional configs
        mysql_uri_str = f"mysql+{db_cnctr_mod}://{username}:{password}@{host}/{db_name}"
        print(f"URI STRING:  {mysql_uri_str}\n")
        return mysql_uri_str

# creating flask app
app = Flask(__name__)
sqlalchemy_uri_str =  getSqlAlchemyString()
app.config['SQLALCHEMY_DATABASE_URI']= sqlalchemy_uri_str
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# creating role/user MODELS tables  (copied from book)
class Role(db.Model):
        ''' Table defines "ROLES" (job functions) which will be used in permission groups'''
        __tablename__ = 'roles'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(64), unique=True)
        users = db.relationship('User', backref='role')

        def __repr__(self):
                return f'<Role {self.name}>'

class User(db.Model):
        ''' list of USERS (employees) '''
        __tablename__='users'
        id = db.Column(db.Integer, primary_key = True)
        username = db.Column(db.String(64), unique=True, index=True)
        role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

        def __repr__(self):
                return f"<User {self.username}>"

@app.shell_context_processor
def make_shell_context():
        return dict(db=db, User=User, Role=Role)
