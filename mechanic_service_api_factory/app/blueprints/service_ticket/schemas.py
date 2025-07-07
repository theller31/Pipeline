from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields
from app.models import ServiceTicket, Mechanic

class ServiceTicketSchema(SQLAlchemyAutoSchema):
    mechanics = fields.List(fields.Integer())  # serialize mechanic ids only

    class Meta:
        model = ServiceTicket
        load_instance = True
        include_relationships = True
        include_fk = True
