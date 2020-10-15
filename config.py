import os

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(36)

    MONGO_URI = "mongodb://127.0.0.1:27017"
    MONGO_DBNAME = "testing"
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    UPLOADS = "/mnt/storage/testing"
    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    MONGO_URI = os.environ.get("MONGO_URI")
    MONGO_DBNAME = os.environ.get("MONGO_DBNAME")


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True
