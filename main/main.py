from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#create database object
db=SQLAlchemy()
#create the marshmallow object for serialization
ma=Marshmallow()

def create_app():

    # creating a flask app object
    app = Flask(__name__)

    # configure the app
    app.config.from_object("config.app_config")

    #creating database object for our Object relational mapper
    db.init_app(app)
    #similar to initialising the db above, we are initialising the marshmallow for serialization
    ma.init_app(app)

    from commands import db_commands
    app.register_blueprint(db_commands)

    # then register routes just before executing app
    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)

    return app