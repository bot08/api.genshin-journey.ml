from flask import Blueprint
from flask_restful import Api

from app.api.auth import RegistrationRoute, LoginRoute, LogoutRoute
from app.api import (
    characters,
    dictionary,
    meta,
    weapons,
    wishes
)


api: Blueprint = Blueprint('api', __name__)

api.register_blueprint(characters.route)
api.register_blueprint(dictionary.route)
api.register_blueprint(meta.route)
api.register_blueprint(weapons.route)
api.register_blueprint(wishes.route)

rest: Api = Api(api)

rest.add_resource(RegistrationRoute, '/register')
rest.add_resource(LoginRoute, '/login')
rest.add_resource(LogoutRoute, '/logout')
