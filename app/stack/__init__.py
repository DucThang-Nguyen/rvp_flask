from .model import Stack
from .schema import StackSchema

BASE_ROUTE = "stack"


def register_routes(api, app, root="api"):
    from .controller import api as stack_api

    api.add_namespace(stack_api, path=f"/{root}/{BASE_ROUTE}")
