from flask_accepts import responds, accepts
from flask_restplus import Namespace, Resource
from flask import Response
from flask import request

from typing import List

from .service import StackService
from .schema import StackSchema
from app.operand.schema import OperandSchema
from app.operand.service import OperandService


api = Namespace("Stack", description="Stack to store elements for RPN calculator")


@api.route("/")
class StacksResource(Resource):
    """Stacks resource"""

    @responds(schema=StackSchema(many=True))
    def get(self) -> List[StackSchema]:
        """Get all stacks"""
        return StackService.get_all()

    @responds(schema=StackSchema)
    def post(self) -> StackSchema:
        """Create a stack"""
        return StackService.create()


@api.route("/<int:stack_id>")
@api.param("stack_id", "Stack database id")
class StackResource(Resource):
    """Stack resource"""
    @responds(schema=StackSchema)
    def get(self, stack_id: int):
        """Get a single stack"""
        return StackService.get_by_id(stack_id=stack_id)

    @responds(schema=StackSchema)
    @accepts(schema=OperandSchema, api=api)
    def post(self, stack_id: int) -> StackSchema:
        """Add operand to stack"""
        value = request.parsed_obj["value"]
        stack = StackService.add_operand_to_stack(
            stack_id=stack_id,
            value=value
        )
        return stack

    @staticmethod
    def delete(stack_id: int) -> Response:
        """Delete a single stack"""
        StackService.delete_by_id(stack_id=stack_id)
        return Response(status=204)
