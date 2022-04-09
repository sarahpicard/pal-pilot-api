from datetime import datetime
from api.models.db import db

class Vaccine(db.Model):
  __tablename__ = 'vaccines'
  id = db.Column(db.Integer, primary_key=True)
  vaccine = db.Column(db.String(100))
  last_shot = db.Column(db.DateTime, default=datetime.now(tz=None))
  next_shot = db.Column(db.DateTime, default=datetime.now(tz=None))
  created_at = db.Column(db.DateTime, default=datetime.now(tz=None))
  pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'))

  def __repr__(self):
    return f"Vaccine('{self.id}', '{self.vaccine}'"

  def serialize(self):
    return {
      "id": self.id,
      "vaccine": self.vaccine,
      "last_shot": self.last_shot,
      "next_shot": self.next_shot,
      "pet_id": self.pet_id
    }