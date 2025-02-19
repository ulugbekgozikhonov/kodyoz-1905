from app.db.base import BaseModel
from sqlalchemy import ForeignKey, Table, Column

problem_tag_association = Table(
    "problem_tags",
    BaseModel.metadata,
    Column("problem_id", ForeignKey("problems.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)
