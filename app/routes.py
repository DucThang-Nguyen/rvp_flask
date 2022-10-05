def register_routes(api, app, root="api"):
    from app.stack import register_routes as attach_stack
    from app.operator import register_routes as attach_operator

    # Add routes
    attach_stack(api, app)
    attach_operator(api, app)
