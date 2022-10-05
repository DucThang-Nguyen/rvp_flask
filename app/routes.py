def register_routes(api, app, root="api"):
    from app.stack import register_routes as attach_stack

    # Add routes
    attach_stack(api, app)
