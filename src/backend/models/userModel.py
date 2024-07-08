from . import db
from sqlalchemy import Column, Integer, String, ForeignKey

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    email = db.Column(String, unique=True)
    occupation = db.Column(String)
    cell = db.Column(String)
    age = db.Column(Integer)
    gender = db.Column(String)
    subscription_id = db.Column(Integer, ForeignKey('subscription.id'))
    role = db.Column(String)
