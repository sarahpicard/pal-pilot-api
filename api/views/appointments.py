from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.appointment import Appointment

appointments = Blueprint('appointments', 'appointments')


# ROUTES 

# new appointment 
# /api/appointments/ (testing)
@appointments.route('/', methods=["POST"])
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]

  appointment = Appointment(**data)
  db.session.add(appointment)
  db.session.commit()
  return jsonify(appointment.serialize()), 201


# see all appointments
@appointments.route('/', methods=["GET"])
@login_required
def index():
  appointments = Appointment.query.all()
  return jsonify([appointment.serialize() for appointment in appointments]), 201