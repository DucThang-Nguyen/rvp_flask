from marshmallow import fields, Schema


class OperatorSchema(Schema):
    """Operator Schema"""
    id = fields.Integer(attribute="id", dump_only=True)
    name = fields.String(attribute="name")
