from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db=SQLAlchemy()
bootstrap=Bootstrap()

def create_app(config_name):
  app = Flask(__name__)
  #initialising configuarations
  app.config.from_object(config_options[config_name])
  #initialise flask extensions
  db.init_app(app)
  bootstrap.init_app(app)
  #intantiating blueprints
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint)

  return app