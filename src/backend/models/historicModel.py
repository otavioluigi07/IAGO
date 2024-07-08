from app import db
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey
from datetime import datetime

class Historic(db.Model):
    __tablename__ = 'historic'

    id = db.Column(Integer, primary_key=True)
    user_id = db.Column(Integer, ForeignKey('user.id'), nullable=False)
    purchase_date = db.Column(DateTime, default=datetime.utcnow, nullable=False)
    subscription_id = db.Column(Integer, ForeignKey('subscription.id'), nullable=False)
    total_price = db.Column(Float, nullable=False)
    payment_method = db.Column(String, nullable=False)
    status = db.Column(Boolean, nullable=False)
