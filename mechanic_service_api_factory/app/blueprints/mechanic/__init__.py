from flask import Blueprint
from .routes import register_routes

bp = Blueprint('mechanic', __name__, url_prefix='/mechanics')
register_routes(bp)
