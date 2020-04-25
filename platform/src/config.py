from os import environ


class Config(object):
    root_psw = environ.get("MYSQL_ROOT_PASSWORD", default=None)
    hostname = environ.get("MYSQL_HOSTNAME", default=None)
    db_name = environ.get("MYSQL_DATABASE", default=None)
    SECRET_KEY = environ.get("FLASK_SECRET_KEY", default='ultra_non_secret_key')
    SQLALCHEMY_DATABASE_URI = 'mysql://root:{}@{}/{}'.format(root_psw, hostname, db_name)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True  # Turns on debugging features in Flask
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False  # Turns on debugging features in Flask
    TESTING = False
