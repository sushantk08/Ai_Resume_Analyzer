import os

from flask import Flask
from flask_cors import CORS

from app.config import Config
from app.extensions import db, migrate


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # ----------------------------
    # Configure CORS
    # ----------------------------

    allowed_origins = [
        "http://localhost:5173",  # Local React (Vite)
        "http://127.0.0.1:5173",
    ]

    # Add Vercel frontend URL if provided
    vercel_url = os.getenv("FRONTEND_URL")
    if vercel_url:
        allowed_origins.append(vercel_url)

    CORS(
        app,
        resources={
            r"/api/*": {
                "origins": allowed_origins,
                "methods": [
                    "GET",
                    "POST",
                    "PUT",
                    "DELETE",
                    "OPTIONS",
                ],
                "allow_headers": [
                    "Content-Type",
                    "Authorization",
                ],
            }
        },
    )

    # ----------------------------
    # Register Blueprints
    # ----------------------------

    from app.routes.upload import upload_bp
    from app.routes.analysis import analysis_bp
    from app.routes.ai import ai_bp
    from app.routes.dashboard import dashboard_bp

    app.register_blueprint(upload_bp, url_prefix="/api")
    app.register_blueprint(analysis_bp, url_prefix="/api")
    app.register_blueprint(ai_bp, url_prefix="/api")
    app.register_blueprint(dashboard_bp, url_prefix="/api")

    return app
    