from app.stack.service import StackService
from app.operand.service import OperandService
from .model import Operator

from app import db
from werkzeug.exceptions import BadRequest
from typing import List


class OperatorService:
    @staticmethod
    def get_all() -> List[Operator]:
        return Operator.query.all()

    @staticmethod
    def get_by_id(operator_id: int) -> Operator:
        operator = Operator.query.get(operator_id)
        if not operator:
            raise BadRequest(f"Operator id {operator_id} does not exist")
        return operator

    @staticmethod
    def apply_operator_to_stack(stack_id: int, operator_id) -> float:
        operator = OperatorService.get_by_id(operator_id=operator_id)
        operands = StackService.get_2_last_recently_added_operands_of_a_stack(stack_id=stack_id)

        left_operand = operands[0]
        right_operand = operands[1]

        if operator.name == "Addition":
            result = left_operand.value + right_operand.value
        elif operator.name == "Subtraction":
            result = left_operand.value - right_operand.value
        elif operator.name == "Multiplication":
            result = left_operand.value * right_operand.value
        elif operator.name == "Division":
            try:
                result = left_operand.value / right_operand.value
            except ZeroDivisionError:
                raise BadRequest("Division by 0")
        else:
            raise BadRequest(f"Unsupported operator: {operator.name}")
        db.session.delete(left_operand)
        db.session.delete(right_operand)
        db.session.commit()
        OperandService.create(stack_id=stack_id, value=result)
        return result
