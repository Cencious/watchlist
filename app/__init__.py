from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

#bootstrap
bootstrap = Bootstrap()

def create_app(config_name):#function that takes the configuration setting key as an argument

    app = Flask(__name__)

    # Creating the app configurations 
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    boostrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    
    app.register_blueprint(main_blueprint)

    # setting config
    from .requests import configure_request
    configure_request(app)
    
    return app 