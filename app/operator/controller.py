from flask_accepts import responds, accepts
from flask_restplus import Namespace, Resource
from flask import request
from typing import List

from .service import OperatorService
from .schema import OperatorSchema


api = Namespace("Operator", description="Operators for RPN calculator")


@api.route("/")
class OperatorsResource(Resource):
    """Operators Resource"""

    @responds(schema=OperatorSchema(many=True))
    def get(self) -> List[OperatorSchema]:
        """Get all operator"""
        return OperatorService.get_all()


@api.route("/<int:operator_id>/stack/<int:stack_id>")
@api.param("operator_id", "Operator database id")
@api.param("stack_id", "Stack database id")
class StackResource(Resource):
    """Operator Resource"""
    @staticmethod
    def post(operator_id: int, stack_id: int) -> float:
        """
        Apply an operator on a stack
        :param operator_id:
        :param stack_id:
        :return:
        :rtype:
        """
        result = OperatorService.apply_operator_to_stack(stack_id=stack_id, operator_id=operator_id)
        return result
