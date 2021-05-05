import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    RESTART = False
    if os.environ.get('RESTART') is not None:
        RESTART = os.environ.get('RESTART')
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'b\'\xc5>`\xe3C\x19\x13\xdc\xeaV\xefT\x9d\xa4x\xae\''
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    START_DB = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevelopmentInDockerConfig(Config):
    ENV = "development"
    DEBUG = True
    START_DB = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@users_service_db_1:5432/postgres'


class TestingWithDBConfig(Config):
    ENV = "development"
    TESTING = True
    DEBUG = True
    START_DB = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'


class TestingWithoutDBConfig(TestingWithDBConfig):
    START_DB = False
