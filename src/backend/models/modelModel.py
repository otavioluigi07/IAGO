from sqlalchemy import Table, Column, Integer, String, ForeignKey
from database.db import metadata

model = Table(
    "model",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, unique=True),
    Column("max_token", int),
    Column("min_token", int),
)