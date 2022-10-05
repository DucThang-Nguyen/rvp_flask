from marshmallow import fields, Schema, post_dump
from app.operand.schema import OperandSchema


class StackSchema(Schema):
    """Stack schema"""
    id = fields.Integer(attribute="id", dump_only=True)
    operands = fields.List(fields.Nested(OperandSchema(only=("value", ))))

    @post_dump
    def unwrap_operands(self, out_data, **kwargs):
        operands = out_data["operands"]
        operands = [operand["value"] for operand in operands]
        operands.reverse()
        out_data["operands"] = operands
        return out_data
