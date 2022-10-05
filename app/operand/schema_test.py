from pytest import fixture

from app.operand.model import Operand
from .model import Operand
from .schema import OperandSchema


@fixture
def operand_schema() -> OperandSchema:
    return OperandSchema()


def test_operand_schema_creates(operand_schema: OperandSchema):
    """
    Test whether schema is created
    :param operand_schema:
    :return:
    """
    assert operand_schema


def test_operand_schema_works(operand_schema: OperandSchema):
    """
    Test whether schema works correctly
    :param operand_schema:
    :return:
    """
    operand = Operand(id=1, value=1.5, stack_id=1)

    operand_dict = operand_schema.dump(operand)
    assert operand_dict["id"] == 1
    assert operand_dict["value"] == 1.5
    assert operand_dict["stack_id"] == 1
