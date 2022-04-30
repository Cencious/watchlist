import os

class Config:
    MOVIE_API_BASE_URL='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ,get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True
config_options = {
'develpoment':DevConfig,
'production':ProdConfig
}