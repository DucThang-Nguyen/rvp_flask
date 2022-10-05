from marshmallow import fields, Schema


class OperandSchema(Schema):
    id = fields.Integer(attribute="id", dump_only=True)
    stack_id = fields.Integer(attribute="stack_id", dump_only=True)
    value = fields.Float(attribute="value", required=True)
