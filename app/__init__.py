from flask import Flask

from .routes import auth_blueprint_construct
from .routes import management_blueprint_construct
from .connection import define_dbs, define_session
from .apps import apps_blueprint_construct


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")
    elif app.config["ENV"] == "testing":
        app.config.from_object("config.TestingConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")
    
    database = define_dbs(app.config["MONGO_URI"], app.config["MONGO_DBNAME"])
    session = define_session(host=app.config["REDIS_HOST"], port=app.config["REDIS_PORT"], db=0)

    app.register_blueprint(auth_blueprint_construct(database, session))
    app.register_blueprint(apps_blueprint_construct(database, session))
    app.register_blueprint(management_blueprint_construct(database, session), url_prefix="/user-management")

    return app
