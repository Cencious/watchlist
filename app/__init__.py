from ensurepip import bootstrap
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

#bootstrap
bootstrap = Bootstrap()

def create_app(config_name): # function that takes the configuration setting key as an argument
    app = Flask(__name__)

    # creating the app configuration
    app.config.from_object(config_options[config_name])

    # Initializing flask extension
    bootstrap.init_app(app)

    # Registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Setting config
    from .request import configure_request
    configure_request(app)
    
    return app
