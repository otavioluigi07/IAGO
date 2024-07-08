from . import db
from sqlalchemy import Column, Integer, String

class Model(db.Model):
    __tablename__ = 'model'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String, unique=True)
    max_token = db.Column(Integer)
    min_token = db.Column(Integer)
