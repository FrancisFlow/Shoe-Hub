from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy



bootstrap = Bootstrap()
db = SQLAlchemy


def create_app(config_name):
    app = Flask(__name__)

    #creating app configurations

    app.config.from_object(config_options[config_name])

    #initializing Flask extensions

    bootstrap.init_app(app)

    #Registering the blueprint

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app