import unittest
from app.models import Movie

class MovieTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the movie class
    '''
    def setUp(self):
       '''
       Set up method that runs before every test
       '''
       self.new_movie = Movie(1234,'Python Must Be Crazy', 'Thrilling new Python series', 'https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    def tes__instance(self):
        self.assertTrue(isinstance(self.new_movie, Movie))

if __name__ == '__main__':
    unittest.main()
    