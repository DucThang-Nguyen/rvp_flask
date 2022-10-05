from sqlalchemy import Float, Integer, Column
from app import db


class Operand(db.Model):
    """Operand"""

    __tablename__ = "operand"

    id = Column(Integer(), primary_key=True)
    value = Column(Float())
    stack_id = Column(Integer(), db.ForeignKey('stack.id'))
