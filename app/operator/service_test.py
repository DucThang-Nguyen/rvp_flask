import pytest

from flask_sqlalchemy import SQLAlchemy
from typing import List
from werkzeug.exceptions import BadRequest
from app.test.fixtures import app, db

from .model import Operator
from .service import OperatorService
from app.stack.service import Operand, Stack


def test_get_all(db: SQLAlchemy):
    """
    Test create and get all
    :param db:
    :return:
    """
    operator = Operator(name="Addition")

    db.session.add(operator)
    db.session.commit()

    results: List[Operator] = OperatorService.get_all()

    assert len(results) == 1
    assert operator in results


def test_get_by_id_works(db: SQLAlchemy):
    """
    Test get_by_id works
    :param db:
    :return:
    """
    operator = Operator(name="Addition")

    db.session.add(operator)
    db.session.commit()

    result: Operator = OperatorService.get_by_id(operator_id=1)
    assert result is operator


def test_get_by_id_fails(db: SQLAlchemy):
    """
    Test get_by_id fails when stack with a given id does not exist
    :param db:
    :return:
    """
    with pytest.raises(BadRequest, match="Operator id 1 does not exist"):
        OperatorService.get_by_id(operator_id=1)


@pytest.mark.parametrize(
    "operator_name,expected_result",
    [("Addition", 3), ("Subtraction", -1), ("Multiplication", 2), ("Division", 0.5)]
)
def test_apply_operator_to_stack_works(operator_name: str, expected_result: int, db: SQLAlchemy):
    """
    Test apply_operator_to_stack works
    :param operator_name:
    :param expected_result:
    :param db:
    :return:
    """
    stack = Stack()
    db.session.add(stack)
    db.session.commit()
    db.session.refresh(stack)

    operand1 = Operand(stack_id=stack.id, value=1)
    operand2 = Operand(stack_id=stack.id, value=2)
    db.session.add(operand1)
    db.session.add(operand2)
    db.session.commit()
    db.session.refresh(operand1)
    db.session.refresh(operand2)

    operator = Operator(name=operator_name)
    db.session.add(operator)
    db.session.commit()
    db.session.refresh(operator)

    result = OperatorService.apply_operator_to_stack(stack_id=stack.id, operator_id=operator.id)
    assert result == expected_result


@pytest.mark.parametrize(
    "operator_name,operands,expected_error",
    [("An operator", [1, 1], "Unsupported"), ("Division", [1, 0], "Division by 0")]
)
def test_apply_operator_to_stack_fails_with_operation(
    operator_name: str,
    operands: List[int],
    expected_error: str,
    db: SQLAlchemy
):
    """
    Test apply_operator_to_stack fails with operations
    :param operator_name:
    :param operands:
    :param expected_error:
    :param db:
    :return:
    """
    stack = Stack()
    db.session.add(stack)
    db.session.commit()
    db.session.refresh(stack)

    operand1 = Operand(stack_id=stack.id, value=operands[0])
    operand2 = Operand(stack_id=stack.id, value=operands[1])
    db.session.add(operand1)
    db.session.add(operand2)
    db.session.commit()
    db.session.refresh(operand1)
    db.session.refresh(operand2)

    operator = Operator(name=operator_name)
    db.session.add(operator)
    db.session.commit()
    db.session.refresh(operator)

    with pytest.raises(BadRequest, match=expected_error):
        OperatorService.apply_operator_to_stack(stack_id=stack.id, operator_id=operator.id)


def test_apply_operator_to_stack_fails_with_operator_not_found(db: SQLAlchemy):
    """
    Test apply_operator_to_stack fails with not found stack
    :return:
    """
    with pytest.raises(BadRequest, match="Operator id 1 does not exist"):
        OperatorService.apply_operator_to_stack(stack_id=1, operator_id=1)


def test_apply_operator_to_stack_fails_with_stack_not_found_or_less_than_2_elements(db: SQLAlchemy):
    """
    Test apply_operator_to_stack fails with not found stack
    :return:
    """
    operator = Operator(name="An operator")
    db.session.add(operator)
    db.session.commit()
    db.session.refresh(operator)

    with pytest.raises(BadRequest, match="Stack id 1 does not exist"):
        OperatorService.apply_operator_to_stack(stack_id=1, operator_id=operator.id)

    stack = Stack()
    db.session.add(stack)
    db.session.commit()
    db.session.refresh(stack)

    with pytest.raises(BadRequest, match="Need at least 2 operands"):
        OperatorService.apply_operator_to_stack(stack_id=stack.id, operator_id=operator.id)