from flask import Flask

from config import BaseConfig


def create_app():
    server = Flask(__name__)
    server.config.from_object(BaseConfig)

    register_extensions(server)
    register_blueprints(server)

    return server


def register_extensions(server):
    from app.extensions import db
    from app.extensions import login
    from app.extensions import migrate

    db.init_app(server)
    login.init_app(server)
    login.login_view = 'main.login'
    migrate.init_app(server, db)


def register_blueprints(server):
    from app.webapp import server_bp

    server.register_blueprint(server_bp)
