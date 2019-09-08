# Contains the application factory and tells Python that the flaskr directory should be treated as a package.

import os
from flask import Flask

def create_app(test_config=None):
    # Create the Flask instance.
    # __name__ = name of the current Python module
    app = Flask(__name__, instance_relative_config=True)
    # Sets some default configuration.
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # Overrides the default configuration with values from config.py
    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # Ensure that the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # A simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    return app
