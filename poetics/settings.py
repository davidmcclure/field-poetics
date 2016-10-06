

import os


class Config:

    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig:

    ENV = 'prod'
    DEBUG = False


class DevConfig:

    EVN = 'dev'
    DEBUG = True

    DB_NAME = 'dev.db'
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)

    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
