import os
from config import Config
from flask import Flask
from flask import request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
app = Flask(__name__)

def create_app(config_class=Config):
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)

    return app

from app import models, routes