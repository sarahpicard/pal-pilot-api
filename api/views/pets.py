from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.pet import Pet

pets = Blueprint('pets', 'pets')



# ROUTES

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
  return jsonify([pet.serialize() for pet in pets]), 200


# show a pet
@pets.route('/<id>', methods=["GET"])
@login_required
def show(id):
  pet = Pet.query.filter_by(id=id).first()
  pet_data = pet.serialize()
  return jsonify(pet=pet_data), 200