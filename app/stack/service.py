from app import db
from .model import Stack
from app.operand.model import Operand
from app.operand.service import OperandService

from sqlalchemy import desc
from werkzeug.exceptions import BadRequest
from typing import List


class StackService:
    """Stack service"""
    @staticmethod
    def get_all() -> List[Stack]:
        """
        Get all stack
        :return:
        """
        return Stack.query.all()

    @staticmethod
    def get_by_id(stack_id: int) -> Stack:
        """
        Get the stack of a given id
        :param stack_id:
        :return:
        :raise: BadRequest exception if the stack does not exist
        """
        stack = Stack.query.get(stack_id)
        if not stack:
            raise BadRequest(f"Stack id {stack_id} does not exist")
        return stack

    @staticmethod
    def get_2_last_recently_added_operands_of_a_stack(stack_id: int) -> List[Operand]:
        """
        Get the last 2 recently added operands of a stack
        :param stack_id:
        :return:
        :raise: BadRequest exception if the stack does not exist
        """
        stack = StackService.get_by_id(stack_id=stack_id)
        operands = stack.operands
        if len(operands) < 2:
            raise (
                BadRequest(
                    "Need at least 2 operands for a binary operator. Please add more operands"
                )
            )
        return operands[-2:]

    @staticmethod
    def add_operand_to_stack(stack_id: int, value: float) -> Stack:
        """
        Add an operand to a stack
        :param stack_id:
        :param value:
        :return:
        :raise: BadRequest exception if the stack does not exist
        """
        stack = StackService.get_by_id(stack_id=stack_id)
        OperandService.create(stack_id=stack_id, value=value)
        db.session.refresh(stack)
        return stack

    @staticmethod
    def create() -> Stack:
        """
        Create a new stack
        :return:
        """
        stack = Stack()

        db.session.add(stack)
        db.session.commit()
        db.session.refresh(stack)

        return stack

    @staticmethod
    def delete_by_id(stack_id: int):
        """
        Delete a stack of a given id
        :param stack_id:
        :return:
        :raise: BadRequest exception if the stack does not exist
        """
        stack = StackService.get_by_id(stack_id=stack_id)
        db.session.delete(stack)
        db.session.commit()

