from flask import Flask, jsonify
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="RPN API", version="0.1.0")

    register_routes(api, app)
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app
