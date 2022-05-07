from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


class Movie:
    '''
    Movie class to define Movie object
    '''

    def __init__(self, id, title,overview, poster,vote_average, vote_count):
       
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count


class Review:

    all_reviews = []

    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()
        
    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response

class User(UserMixin,db.Model):
    #We create a User class that will help us create new users. We pass in db.Model as an argument. This will connect our class to our database and allow communication.

    __tablename__ = 'users'
    #__tablename__ variable allows us to give the tables in our database proper names

    id = db.Column(db.Integer,primary_key = True)
    #We create columns using the db.Column class which will represent a single column. We pass in the type of the data to be stored as the first argument. db.Integer specifies the data in that column should be an Integer.

    username = db.Column(db.String(255),index =True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))# db.Integer specifies the data in that column should be an Integer.

    @property #We use the @property decorator to create a write only class property password
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):#takes in a password, hashes it and compares it to the hashed password to check if they are the same.
        return check_password_hash(self.pass_secure,password)



    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    #This tells SQLAlchemy that this is a foreign key and is the ID of a Role model.

    def __repr__(self):
        return f'User {self.username}'
        
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)

    name = db.Column(db.String(255))

    users = db.relationship('User',backref = 'role',lazy="dynamic")
    #We use db.relationship to create a virtual column that will connect with the foreign key, pass in 3 arguments. user is the class we are referencing,backref allows us to access and set our User class.

    def __repr__(self):
        return f'User {self.name}'