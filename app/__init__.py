from ensurepip import bootstrap
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

#bootstrap
bootstrap = Bootstrap()
db =SQLAlchemy()

def create_app(config_name): # function that takes the configuration setting key as an argument
    app = Flask(__name__)

    # creating the app configuration
    app.config.from_object(config_options[config_name])

    # Initializing flask extension
    bootstrap.init_app(app)
    db.init_app(app)


    # Registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Setting config
    from .request import configure_request
    configure_request(app)

    #register_blueprint instance
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    
    return app
