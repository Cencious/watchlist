from flask import Blueprint
'''
Application Blueprint for defining routes.
'''

main = Blueprint('main',__name__)
#The Blueprint class takes in 2 arguments. The name of the blueprint and the __name__ variable to find the location of the blueprint.


from . import views,errors #To avoid circular dependencies we import the views and errors modules.


