from flask import Flask
import dash


def create_app():
    app = Flask(__name__)
    dashapp = dash.Dash(__name__, server=app, url_base_pathname='/dashboard/')

    from app.dashapp import app_bp
    app.register_blueprint(app_bp)

    return app, dashapp
