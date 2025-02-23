import os

from flask import Flask
from flask_alembic import Alembic

from src.connections.database import init_db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    alembic = Alembic()
    _ = init_db()
    alembic.init_app(app)

    # from . import auth, main

    # app.register_blueprint(auth.bp)
    # app.register_blueprint(main.bp)

    @app.route("/")
    def index():
        return "Hello, World!"

    return app
