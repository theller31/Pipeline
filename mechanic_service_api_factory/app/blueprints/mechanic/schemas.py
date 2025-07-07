from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models import Mechanic
from app.extensions import ma

class MechanicSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Mechanic
        load_instance = True
        sqla_session = ma.SQLAlchemy().session
