from pytest import fixture

from app.operand.model import Operand
from .model import Operator
from .schema import OperatorSchema


@fixture
def operator_schema() -> OperatorSchema:
    return OperatorSchema()


def test_operator_schema_creates(operator_schema: OperatorSchema):
    """
    Test whether an Operator schema is created
    """
    assert operator_schema


def test_operand_schema_works(operator_schema: OperatorSchema):
    """
    Test whether an Operator schema works
    """
    operator = Operator(id=1, name="Addition")

    operator_dict = operator_schema.dump(operator)
    assert operator_dict["id"] == 1
    assert operator_dict["name"] == "Addition"

