import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    DEBUG = False
    TESTING = True
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'This is necessary to be change'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'sendo_test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    """Configurations for Testing."""
    TESTING = True