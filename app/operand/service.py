from app import db
from .model import Operand


class OperandService:
    @staticmethod
    def create(stack_id: int, value: float) -> Operand:
        """
        Create a new operand
        :param stack_id:
        :param value:
        :return:
        """
        operand = Operand(value=value, stack_id=stack_id)

        db.session.add(operand)
        db.session.commit()
        db.session.refresh(operand)

        return operand
