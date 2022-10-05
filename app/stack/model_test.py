from pytest import fixture
from flask_sqlalchemy import SQLAlchemy

from app.test.fixtures import app, db
from .model import Stack


@fixture
def stack() -> Stack:
    return Stack()


def test_stack_create_and_retrieve(stack: Stack, db: SQLAlchemy):
    """
    Test whether stack is created with exact information
    :param stack:
    :param db:
    :return:
    :rtype:
    """
    db.session.add(stack)
    db.session.commit()

    result = Stack.query.first()
    assert result.__dict__ == stack.__dict__
