from flask import Blueprint


app_bp = Blueprint('main', __name__)


@app_bp.route('/')
def index():
    return "Hello"
