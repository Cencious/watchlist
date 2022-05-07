import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):#creates an instance of our User class
        self.new_user = User(password = 'banana')

    def test_password_setter(self): #this ascertains that when password is being hashed and the pass_secure contains a value.
        self.assertTrue(self.new_user.pass_secure is not None)

    class UserModelTest(unittest.TestCase):

    def setUp(self):#creates an instance of our User class
        self.new_user = User(password = 'banana')

    def test_password_setter(self): #this ascertains that when password is being hashed and the pass_secure contains a value.
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password
    
    def test_password_verification(self):
            self.assertTrue(self.new_user.verify_password('banana'))