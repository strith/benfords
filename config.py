from os import environ, path
from dotenv import load_dotenv

basedir = path.join(path.abspath(path.dirname(__file__)), 'application')
load_dotenv(path.join(basedir, '.env'))

class Config:
  # SECRET_KEY = environ.get('SECRET_KEY')
  # SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
  STATIC_FOLDER = 'static'
  TEMPLATES_FOLDER = 'templates'
  UPLOADS_FOLDER = path.join(basedir, 'uploads')

class DevConfig(Config):
  FLASK_ENV = 'development'
  DEBUG = True
  TESTING = True
  SQLALCHEMY_DATABASE_URI = environ.get('DEV_DATABASE_URI')
  SQLALCHEMY_ECHO = True
  SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
  FLASK_ENV = 'production'
  DEBUG = False
  TESTING = False
  SQLALCHEMY_DATABASE_URI = environ.get('PROD_DATABASE_URI')
  SQLALCHEMY_TRACK_MODIFICATIONS = True
