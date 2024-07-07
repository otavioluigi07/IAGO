from sqlalchemy import Table, Column, Integer, String, ForeignKey
from database.db import metadata

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("email", String, unique=True),
    Column("occupation", String),
    Column("cell", String),
    Column("age", String),
    Column("gender", String),
    Column("subscription_id", Integer, ForeignKey("subscription.id")),  # Chave estrangeira da subscription
    Column("role", String),
)