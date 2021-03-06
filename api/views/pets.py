from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.pet import Pet
from api.models.allergy import Allergy
from api.models.medication import Medication
from api.models.vaccine import Vaccine

pets = Blueprint('pets', 'pets')


# ROUTES (pets)

# create a pet
@pets.route('/', methods=["POST"])
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]
  pet = Pet(**data)
  db.session.add(pet)
  db.session.commit()
  return jsonify(pet.serialize()), 201


# see all of my pets
@pets.route('/', methods=["GET"])
@login_required
def index():
  pets = Pet.query.all()
  print("CONSOLE LOG!!", pets)
  return jsonify([pet.serialize() for pet in pets]), 200


# show a pet
@pets.route('/<id>', methods=["GET"])
@login_required
def show(id):
  pet = Pet.query.filter_by(id=id).first()
  pet_data = pet.serialize()
  return jsonify(pet=pet_data), 200

# update a pet
@pets.route('/<id>', methods=["PUT"])
@login_required
def update(id):
  data = request.get_json()
  profile = read_token(request)
  pet = Pet.query.filter_by(id=id).first()

  if pet.profile_id != profile["id"]:
    return 'Forbidden', 403

  for key in data:
    setattr(pet, key, data[key])
  
  db.session.commit()
  return jsonify(pet.serialize()), 200


# delete a pet
@pets.route('/<id>', methods=["DELETE"])
@login_required
def delete(id):
  profile = read_token(request)
  pet = Pet.query.filter_by(id=id).first()

  if pet.profile_id != profile["id"]:
    return 'Forbidden', 403
  
  db.session.delete(pet)
  db.session.commit()
  return jsonify(message="Success"), 200



# ROUTES (allergies)

# create an allergy
@pets.route('/<id>/allergies', methods=["POST"])
@login_required
def add_allergy(id):
  data = request.get_json()
  data["pet_id"] = id

  profile = read_token(request)
  pet = Pet.query.filter_by(id=id).first()

  if pet.profile_id != profile["id"]:
    return 'Forbidden', 403

  allergy = Allergy(**data)

  db.session.add(allergy)
  db.session.commit()
  pet_data = pet.serialize()
  return jsonify(pet_data), 201



# ROUTES (medication)

# create a medication
@pets.route('/<id>/medications', methods=["POST"])
@login_required
def add_medication(id):
  data = request.get_json()
  data["pet_id"] = id

  profile = read_token(request)
  pet = Pet.query.filter_by(id=id).first()

  if pet.profile_id != profile["id"]:
    return 'Forbidden', 403

  medication = Medication(**data)

  db.session.add(medication)
  db.session.commit()
  pet_data = pet.serialize()
  return jsonify(pet_data), 201




# ROUTES (vaccine)

# create a vaccine
@pets.route('/<id>/vaccines', methods=["POST"])
@login_required
def add_vaccine(id):
  data = request.get_json()
  data["pet_id"] = id

  profile = read_token(request)
  pet = Pet.query.filter_by(id=id).first()

  if pet.profile_id != profile["id"]:
    return 'Forbidden', 403

  vaccine = Vaccine(**data)

  db.session.add(vaccine)
  db.session.commit()
  pet_data = pet.serialize()
  return jsonify(pet_data), 201