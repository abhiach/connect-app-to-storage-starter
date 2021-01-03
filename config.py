import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'udacitysqlserver.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'udacitydb'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udacityadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '@Welcome1'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'udacitysa'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'ZOOoqDc6Ybza9ykrsFDzdvufUbijcxDmBd9GG/gmXaxx+oV7EV+8jR6OZjpx4SSHBE7SncOgbRt7+TYqfwXktg=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
