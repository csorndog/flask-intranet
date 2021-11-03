''' creating models/tables for Lifetime Prop. with Flask Book as reference example '''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


"""
def getSqlAlchemyString():
        ''' Set configuration variables for MySQL Access via SQLAlchemy '''
        # string parameters 
        username = "flaskapp"
        password = "lifetimeProperties123!"
        host = "localhost"
        db_name = "testdb"
        db_cnctr_mod = "pymysql"   # using PyMySql but will change for other modules
        
        # optional configs
        default_mysql_port = True
        if not default_mysql_port:
            port = input("Input non-default port #:  ")
            uri_prefix = mysql+{db_cnctr_mod}://
            uri_db_confs = 
            sqlalch_uri = f"mysql+{pymysql_connector_module}://{username}:{password}@{host}/{db_name}"
            mysql_uri_str = f"mysql+mysqlconnector://{username}:{password}@{host}/{db_name}"

        port = "3306"     ## default mysql port
        # sqlachemy uri variable
        # mysql_uri_str = f"mysql+mysqlconnector://{username}:{password}@{host}/{db_name}"
        mysql_uri_str = f"mysql+mysqlconnector://{username}:{password}@{host}/{db_name}"
"""

def getSqlAlchemyString():
        ''' Set configuration variables for MySQL Access via SQLAlchemy '''
        # string parameters 
        username = "flaskapp"
        password = "lifetimeProperties123!"
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



# creating role/user MODELS tables  (copied from book)
class Role(db.Model):
        ''' Table defines "ROLES" (job functions) which will be used in permission groups'''
        __tablename__ = 'roles'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(64), unique=True)

        def __repr__(self):
                return f'<Role {self.name}>'

class User(db.Model):
        ''' list of USERS (employees) '''
        __tablename__ = 'users'
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

