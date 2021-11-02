''' creating models/tables for Lifetime Prop. with Flask Book as reference example '''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def getSqlAlchemyString():
        ''' Set configuration variables for MySQL Access via SQLAlchemy '''
        # string parameters 
        username = "flaskapp"
        password = "lifetimeProperties123!"
        host = "localhost"
        db_name = "testdb"
        # sqlachemy uri variable
        mysql_uri_str = f"mysql+mysqlconnector://{username}:{password}@{host}/{db_name}"
        return mysql_uri_str

# creating flask app
app = Flask(__name__)
sqlalchemy_uri_str =  getSqlAlchemyString()
app.config['SQLALCHEMY_DATABASE_URI']= sqlalchemy_uri_str
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



# creating role/user MODELS tables  (copied from book)
class Role(db.Model):
        ''' Table defines "ROLES" (job functions) which will be used in permission groups'''
        __tablename__ = 'roles'
        id = db.Column(db.Integer, primary_key_=True)
        name = db.Column(db.String(64), unique=True)

        def __repr__(self):
                return f'<Role {self.name}>'

class User(db.Model):
        ''' list of USERS (employees) '''
        id = db.Column(db.Integer, primary_key = True)
        username = db.Column(db.String(64), unique=True, index=True)

        ### FUTURE COLUMNS
        # email = db.Column()
        # firstname = db.Column()
        # lastname = db.Column()
        # fullname = db.Column()
        # createdAt= db.Column()
        # lastModified = db.Column()
        # activeEmployee = db.Column()

        def __repr__(self):
                return f"<User {self.username}>"

