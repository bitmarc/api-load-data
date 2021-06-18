import os
import json

# Variables definition
basedir = os.path.abspath(os.path.dirname(__file__))

# Getting database credentials and set configuration
with open("secret.json") as f:
    secret = json.loads(f.read())

def get_secret(secret_name, secrets=secret):
    try:
        return secrets[secret_name]
    except:
        msg = "la variable %s no existe" % secret_name
        raise FileNotFoundError(msg)


class Config:
	""" setting and recovery execution variables """
	USER=get_secret('USER')
	PASSWORD=get_secret('PASSWORD')
	DB_NAME=get_secret('DB_NAME')
	DEBUG = False


class DevelopmentConfig(Config):
	""" Configuration in development environment """
	DEBUG = True
	SQLALCHEMY_DATABASE_URI='mysql+pymysql://'+Config.USER+':'+Config.PASSWORD+'@localhost/'+Config.DB_NAME
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
	""" Configuration in development environment """
	DEBUG = False
	#SQLALCHEMY_DATABASE_URI=
	#SQLALCHEMY_TRACK_MODIFICATIONS = True


config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)
UPLOAD_FILES_FOLDER="app/main/files/"
