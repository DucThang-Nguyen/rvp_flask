from sqlalchemy import String, Integer, Column
from app import db


class Operator(db.Model):
    """Operator"""

    __tablename__ = "operator"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
