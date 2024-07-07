from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime, Float, create_engine, MetaData
from datetime import datetime
from database.db import metadata

historic = Table(
    "historic",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("user.id"), nullable=False),
    Column("purchase_date", DateTime, default=datetime.utcnow, nullable=False),
    Column("subscription_id", Integer, ForeignKey("subscription.id"), nullable=False),
    Column("total_price", Float, nullable=False),
    Column("payment_method", String, nullable=False),
    Column("status", bool, nullable=False)
)