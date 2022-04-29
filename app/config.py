class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'



class ProdConfig(Config):
    '''
    Pruduction  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    MOVIE_API_KEY ='6e927d0039e5cb1efc53926fdc2dad63'


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True