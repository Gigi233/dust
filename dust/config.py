class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@127.0.0.1/dust'
    SQLALCHEMY_ECHO = True
    REDIS_URL = "redis://localhost:6379/0"
    LOGIN_EXPIRE_TIME = 7200


class DevConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_ECHO = False

