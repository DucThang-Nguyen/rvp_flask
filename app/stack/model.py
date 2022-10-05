from sqlalchemy import Float, Integer, Boolean, Column
from app import db


class Stack(db.Model):
    """Stack model"""

    __tablename__ = "stack"

    id = Column(Integer(), primary_key=True)
    operands = db.relationship('Operand', backref='stack', cascade="delete,")
