from datetime import datetime
from api.models.db import db

class Allergy(db.Model):
  __tablename__ = 'allergies'
  id = db.Column(db.Integer, primary_key=True)
  allergy = db.Column(db.String(100))
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'))

  def __repr__(self):
    return f"Allergy('{self.id}', '{self.name}'"

  def serialize(self):
    allergy = {c.name: getattr(self, c.name) for c in self.__table__.columns}
    return allergy