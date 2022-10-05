from pytest import fixture
from flask_sqlalchemy import SQLAlchemy


from app.test.fixtures import app, db
from app.stack.model import Stack
from .model import Operand


@fixture
def operand() -> Operand:
    return Operand(stack_id=1, value=2.5)


@fixture
def stack() -> Stack:
    return Stack()


def test_operand_create_and_retrieve(operand: Operand, stack: Stack, db: SQLAlchemy):
    """
    Test whether operand is created and the stack is updated
    :param operand:
    :param stack:
    :param db:
    :return:
    :rtype:
    """
    db.session.add(stack)
    db.session.commit()

    db.session.add(operand)
    db.session.commit()

    db.session.refresh(operand)
    db.session.refresh(stack)

    result = Operand.query.first()
    assert result.__dict__ == operand.__dict__
    assert operand in stack.operands
