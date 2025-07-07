from flask import Flask
from .extensions import db, ma

def create_app(config_name='dev'):
    app = Flask(__name__)
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI='sqlite:///data.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        TESTING=(config_name == 'testing')
    )

    # init extensions
    db.init_app(app)
    ma.init_app(app)

    # register blueprints
    from .blueprints.mechanic import bp as mechanic_bp
    from .blueprints.service_ticket import bp as ticket_bp
    app.register_blueprint(mechanic_bp)
    app.register_blueprint(ticket_bp)

    # create tables if not exist
    with app.app_context():
        db.create_all()

    return app
