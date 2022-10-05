import pytest

from flask_sqlalchemy import SQLAlchemy
from typing import List
from werkzeug.exceptions import BadRequest
from app.test.fixtures import app, db

from .model import Stack
from .service import StackService
from app.operand.service import OperandService, Operand


def test_create_and_get_all(db: SQLAlchemy):
    """
    Test create and get all
    :param db:
    :return:
    """
    stack1 = StackService.create()
    stack2 = StackService.create()

    results: List[Stack] = StackService.get_all()

    assert len(results) == 2
    assert stack1 in results and stack2 in results


def test_get_by_id_works(db: SQLAlchemy):
    """
    Test get_by_id works
    :param db:
    :return:
    """
    stack1 = StackService.create()
    result: Stack = StackService.get_by_id(stack_id=1)
    assert result is stack1


def test_get_by_id_fails(db: SQLAlchemy):
    """
    Test get_by_id fails when stack with a given id does not exist
    :param db:
    :return:
    """
    with pytest.raises(BadRequest, match="Stack id 1 does not exist"):
        StackService.get_by_id(stack_id=1)


def test_get_2_last_recently_added_operands_of_a_stack_works(db: SQLAlchemy):
    """
    Test get_2_last_recently_added_operands_of_a_stack works
    exist
    :param db:
    :return:
    """
    stack = StackService.create()
    operand1 = OperandService.create(stack_id=1, value=1)
    operand2 = OperandService.create(stack_id=1, value=2)
    operand3 = OperandService.create(stack_id=1, value=3)

    results: List[Operand] = StackService.get_2_last_recently_added_operands_of_a_stack(
        stack_id=stack.id
    )
    assert len(results) == 2

    assert operand2 in results
    assert operand3 in results


def test_get_2_last_recently_added_operands_of_a_stack_fails(db: SQLAlchemy):
    """
    Test get_2_last_recently_added_operands_of_a_stack fails when stack with a given id does not
    exist
    :param db:
    :return:
    """
    with pytest.raises(BadRequest, match="Stack id 1 does not exist"):
        StackService.get_2_last_recently_added_operands_of_a_stack(stack_id=1)


def test_delete_by_id_works(db: SQLAlchemy):
    """
    Test delete_by_id works
    exist
    :param db:
    :return:
    """
    stack = StackService.create()
    OperandService.create(stack_id=1, value=1)
    OperandService.create(stack_id=1, value=2)
    db.session.refresh(stack)

    StackService.delete_by_id(stack_id=1)
    operands = Operand.query.all()
    stacks = StackService.get_all()
    assert len(operands) == 0
    assert len(stacks) == 0


def test_delete_by_id_fails(db: SQLAlchemy):
    """
    Test delete_by_id fails when stack with a given id does not
    exist
    :param db:
    :return:
    """
    with pytest.raises(BadRequest, match="Stack id 1 does not exist"):
        StackService.delete_by_id(stack_id=1)


def test_add_operand_to_stack_works(db: SQLAlchemy):
    """
    Test add_operand_to_stack works
    :param db:
    :type db:
    :return:
    :rtype:
    """
    stack = StackService.create()
    StackService.add_operand_to_stack(stack_id=1, value=1)

    db.session.refresh(stack)
    assert len(stack.operands) == 1
    assert stack.operands[0].value == 1


def test_add_operand_to_stack_fails(db: SQLAlchemy):
    """
    Test add_operand_to_stack fails when stack with a given id does not exist
    :param db:
    :type db:
    :return:
    :rtype:
    """
    with pytest.raises(BadRequest, match="Stack id 1 does not exist"):
        StackService.add_operand_to_stack(stack_id=1, value=1)
