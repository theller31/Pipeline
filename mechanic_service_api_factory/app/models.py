from .extensions import db

service_mechanic = db.Table(
    'service_mechanic',
    db.Column('service_ticket_id', db.Integer, db.ForeignKey('service_ticket.id')),
    db.Column('mechanic_id', db.Integer, db.ForeignKey('mechanic.id'))
)

class Mechanic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    specialization = db.Column(db.String(120))

class ServiceTicket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), default='open')
    customer_name = db.Column(db.String(120))
    mechanics = db.relationship('Mechanic', secondary=service_mechanic,
                                backref='tickets')
