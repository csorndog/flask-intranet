import os
basedir = os.path.abspath(os.path.dirname(__file__))


def uri_shared_str():
    ''' shared uri string for diff dbs ; referenced later once db is know '''

    # shared uri params (for now)
    mysql_uri_prefix = 'mysql+pymysql://'
    username = 'root'
    password = 'ubu2Root!'
    host = 'localhost'
    sqlalch_uri_stem = f"{username}:{password}@{host}/"
    return sqlalch_uri_stem
    



class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'yeezysecretdefaultstring'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

    # shared uri params (for now)
    mysql_uri_prefix = 'mysql+pymysql://'
    username = 'root'
    password = 'ubu2Root!'
    host = 'localhost'
    sqlalch_uri_stem = f"{username}:{password}@{host}/"
    

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    
    # testing str logic
    sqlalch_uri_stem = uri_shared_str()
    db = 'lpDev'
    dev_uri_str = f"{sqlalch_uri_stem}{db}"

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or dev_uri_str



class TestingConfig(Config):
    TESTING = True





class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
