from api.views.auth import login
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
def index():
  appointments = Appointment.query.all()
  return jsonify([appointment.serialize() for appointment in appointments]), 201


# show one appointment 
@appointments.route('/<id>', methods=["GET"])
def show(id):
  appointment = Appointment.query.filter_by(id=id).first()
  return jsonify(appointment.serialize()), 200


# update an appointment 
@appointments.route('/<id>', methods=["PUT"])
@login_required
def update(id):
  data = request.get_json()
  profile = read_token(request)
  appointment = Appointment.query.filter_by(id=id).first()

  if appointment.profile_id != profile["id"]:
    return 'Forbidden', 403

  for key in data:
    setattr(appointment, key, data[key])

  db.session.commit()
  return jsonify(appointment.serialize()), 200


# delete an appointment 
@appointments.route('/<id>', methods=["DELETE"])
@login_required
def delete(id):
  profile = read_token(request)
  appointment = Appointment.query.filter_by(id=id).first()

  if appointment.profile_id != profile["id"]:
    return 'Forbidden', 403

  db.session.delete(appointment)
  db.session.commit()
  return jsonify(message="Success"), 200