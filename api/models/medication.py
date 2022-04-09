from datetime import datetime
from api.models.db import db

class Medication(db.Model):
  __tablename__ = 'medications'
  id = db.Column(db.Integer, primary_key=True)
  medication = db.Column(db.String(100))
  created_at = db.Column(db.DateTime, default=datetime.now(tz=None))
  pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'))

  def __repr__(self):
    return f"Medication('{self.id}', '{self.medication}'"

  def serialize(self):
    return {
      "id": self.id,
      "medication": self.medication,
      "pet_id": self.pet_id
    }
    