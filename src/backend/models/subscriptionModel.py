from sqlalchemy import Table, Column, Integer, String # type: ignore
from database.db import metadata

subscription = Table(
    "subscription",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, unique=True),
    Column("preco", String),
    Column("model", String),
    Column("active", bool),
)