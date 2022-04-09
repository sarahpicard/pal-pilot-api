from datetime import datetime
from api.models.db import db

class Pet(db.Model):
  __tablename__ = 'pets'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  breed = db.Column(db.String(100))
  animal_type = db.Column(db.String(100))
  weight = db.Column(db.String(100))
  age = db.Column(db.Integer)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))

  allergies = db.relationship("Allergy", cascade='all')

  def __repr__(self):
    return f"Pet('{self.id}', '{self.name}'"

  def serialize(self):
    pet = {c.name: getattr(self, c.name) for c in self.__table__.columns}
    allergies = [allergy.serialize() for allergy in self.allergies]
    pet['allergies'] = allergies
    return pet