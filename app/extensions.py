from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS

db: SQLAlchemy = SQLAlchemy()
bcrypt: Bcrypt = Bcrypt()
cors: CORS = CORS()
jwt: JWTManager = JWTManager()


def setup_extensions(app: Flask) -> None:
    db.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)
    jwt.init_app(app)
