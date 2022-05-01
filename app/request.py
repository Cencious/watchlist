import urllib.request,json
from .models import movie

# Getting api key
api_key =None

# Getting the movie base url
base_url = None

def configure_request(app):
    #a function that takes in the application instance and replaces the values of the None variables to application configuration objects.
    global api_key,base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']

