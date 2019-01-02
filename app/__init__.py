import dash
from flask import Flask
from flask_login import login_required

from config import BaseConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)
    dashapp = dash.Dash(__name__, server=app, url_base_pathname='/dashboard/')

    register_extensions(app)
    register_blueprints(app)

    protect_dashviews(dashapp)

    return app, dashapp


def register_extensions(app):
    from app.extensions import db
    from app.extensions import login
    from app.extensions import migrate

    db.init_app(app)
    login.init_app(app)
    login.login_view = 'main.login'
    migrate.init_app(app, db)


def register_blueprints(app):
    from app.dashapp import app_bp

    app.register_blueprint(app_bp)


def protect_dashviews(dashapp):
    for view_func in dashapp.server.view_functions:
        if view_func.startswith(dashapp.url_base_pathname):
            dashapp.server.view_functions[view_func] = login_required(dashapp.server.view_functions[view_func])
