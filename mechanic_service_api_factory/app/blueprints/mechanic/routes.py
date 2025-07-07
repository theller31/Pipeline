from flask import request, jsonify, abort
from app.extensions import db
from app.models import Mechanic
from .schemas import MechanicSchema

schema = MechanicSchema()
schema_many = MechanicSchema(many=True)

def register_routes(bp):
    @bp.post('/')
    def create_mechanic():
        data = request.get_json() or {}
        m = schema.load(data, session=db.session)
        db.session.add(m)
        db.session.commit()
        return schema.dump(m), 201

    @bp.get('/')
    def get_mechanics():
        mechanics = Mechanic.query.all()
        return schema_many.dump(mechanics), 200

    @bp.put('/<int:id>')
    def update_mechanic(id):
        mech = Mechanic.query.get_or_404(id)
        data = request.get_json() or {}
        mech.name = data.get('name', mech.name)
        mech.specialization = data.get('specialization', mech.specialization)
        db.session.commit()
        return schema.dump(mech), 200

    @bp.delete('/<int:id>')
    def delete_mechanic(id):
        mech = Mechanic.query.get_or_404(id)
        db.session.delete(mech)
        db.session.commit()
        return '', 204
