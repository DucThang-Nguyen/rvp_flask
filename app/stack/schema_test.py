from pytest import fixture

from app.operand.model import Operand
from .model import Stack
from .schema import StackSchema


@fixture
def stack_schema() -> StackSchema:
    return StackSchema()


def test_stack_schema_create(stack_schema: StackSchema):
    assert stack_schema


def test_stack_schema_works(stack_schema: StackSchema):
    """
    Test whether stack schema works
    :param stack_schema:
    :return:
    """
    stack = Stack(
        id=1,
        operands=[Operand(id=1, stack_id=1, value=1.5)]
    )
    stack_dict = stack_schema.dump(stack)
    assert stack_dict["id"] == 1
    assert type(stack_dict["operands"]) is list
    assert len(stack_dict["operands"]) == 1
    assert stack_dict["operands"][0] == 1.5
