import pytest
from flask_sqlalchemy import SQLAlchemy

from app.test.fixtures import app, db
from app.stack.model import Stack
from .service import OperandService


def test_create_works(db: SQLAlchemy):
    """
    Test whether an operand is created and appears in the stack it belongs to
    :param db:
    :type db:
    :return:
    :rtype:
    """
    stack = Stack(id=1)
    db.session.add(stack)
    db.session.commit()

    operand = OperandService.create(stack_id=1, value=1.5)

    assert operand.id == 1
    assert operand.stack_id == 1
    assert operand.value == 1.5

    db.session.refresh(stack)
    assert operand in stack.operands
