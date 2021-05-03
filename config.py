import os


def get_sqlite_uri():
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_name = os.environ['DATABASE_URL'].split('/')[-1]
    return f'sqlite:///{basedir}/{db_name}'


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = get_sqlite_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ['SECRET_KEY']
