from flask import Flask
from config import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

from flask_cors import CORS



print("ENV: ", os.environ.get("FLASK_ENV", default=False))

app = Flask(__name__)
if os.environ.get("FLASK_ENV", default=False) == 'production':
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)

print("TESTING: ", app.config["TESTING"])

CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_mng = LoginManager(app)
login_mng.login_view = 'login'

from app import routes, models


from os.path import dirname, basename, isfile
import glob

files = glob.glob(dirname(__file__)+"/routes/*.py")
modules = [basename(f)[:-3] for f in files if isfile(f) and not f.endswith('__init__.py') and not f.endswith('helpers.py')]
for module in modules:
    exec('from app.routes.{} import *'.format(module, module))

