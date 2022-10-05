from .model import Operator

BASE_ROUTE = "operator"


def register_routes(api, app, root="api"):
    from .controller import api as operator_api

    api.add_namespace(operator_api, path=f"/{root}/{BASE_ROUTE}")
