from flask import Blueprint
from .routes import register_routes

bp = Blueprint('service_ticket', __name__, url_prefix='/service-tickets')
register_routes(bp)
