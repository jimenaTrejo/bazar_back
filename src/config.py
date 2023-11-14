from flask import Flask

class DevelopmentConfig(object):
    DEBUG = True
    MYSQL_HOST = "localhost"
    MYSQL_PORT = 3306
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "root"
    MYSQL_DB = "bazar"


config ={
    'development': DevelopmentConfig()

}