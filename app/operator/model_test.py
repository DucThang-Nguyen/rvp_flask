from pytest import fixture
from flask_sqlalchemy import SQLAlchemy


from app.test.fixtures import app, db
from .model import Operator


@fixture
def operator() -> Operator:
    return Operator(id=1, name="Addition")


def test_operator_create_and_retrieve(operator: Operator, db: SQLAlchemy):
    """Test whether Operator model works"""
    db.session.add(operator)
    db.session.commit()

    result = Operator.query.first()
    assert result.__dict__ == operator.__dict__
