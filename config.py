import os

class Config:
    MOVIE_API_BASE_URL='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ,get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
