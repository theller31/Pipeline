from flask import request, jsonify, abort
from app.extensions import db
from app.models import ServiceTicket, Mechanic
from .schemas import ServiceTicketSchema

schema = ServiceTicketSchema()
schema_many = ServiceTicketSchema(many=True)

def register_routes(bp):
    @bp.post('/')
    def create_ticket():
        data = request.get_json() or {}
        ticket = schema.load(data, session=db.session)
        db.session.add(ticket)
        db.session.commit()
        return schema.dump(ticket), 201

    @bp.put('/<int:ticket_id>/assign-mechanic/<int:mechanic_id>')
    def assign_mechanic(ticket_id, mechanic_id):
        ticket = ServiceTicket.query.get_or_404(ticket_id)
        mech = Mechanic.query.get_or_404(mechanic_id)
        if mech not in ticket.mechanics:
            ticket.mechanics.append(mech)
            db.session.commit()
        return schema.dump(ticket), 200

    @bp.put('/<int:ticket_id>/remove-mechanic/<int:mechanic_id>')
    def remove_mechanic(ticket_id, mechanic_id):
        ticket = ServiceTicket.query.get_or_404(ticket_id)
        mech = Mechanic.query.get_or_404(mechanic_id)
        if mech in ticket.mechanics:
            ticket.mechanics.remove(mech)
            db.session.commit()
        return schema.dump(ticket), 200

    @bp.get('/')
    def get_tickets():
        tickets = ServiceTicket.query.all()
        return schema_many.dump(tickets), 200
