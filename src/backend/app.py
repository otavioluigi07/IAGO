from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0994@localhost/iago'  # Substitua com suas credenciais
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

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

class Subscription(db.Model):
    __tablename__ = 'subscription'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String, unique=True)
    price = db.Column(Integer)
    model_id = db.Column(Integer, ForeignKey('model.id'))
    active = db.Column(Boolean)

class Model(db.Model):
    __tablename__ = 'model'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String, unique=True)
    max_token = db.Column(Integer)
    min_token = db.Column(Integer)

class Historic(db.Model):
    __tablename__ = 'historic'
    
    id = db.Column(Integer, primary_key=True)
    user_id = db.Column(Integer, ForeignKey('user.id'), nullable=False)
    purchase_date = db.Column(DateTime, default=datetime.utcnow, nullable=False)
    subscription_id = db.Column(Integer, ForeignKey('subscription.id'), nullable=False)
    total_price = db.Column(Float, nullable=False)
    payment_method = db.Column(String, nullable=False)
    status = db.Column(Boolean, nullable=False)

if __name__ == "__main__":
    app.run(debug=True)