from . import db
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

class Subscription(db.Model):
    __tablename__ = 'subscription'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String, unique=True)
    price = db.Column(Integer)
    model_id = db.Column(Integer, ForeignKey('model.id'))
    active = db.Column(Boolean)
