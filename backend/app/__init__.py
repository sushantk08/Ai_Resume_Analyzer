from flask import Flask
from flask_cors import CORS

from app.config import Config
from app.extensions import db, migrate
from app.error_handlers import register_error_handlers
from app.routes.ai import ai_bp
from app.routes.dashboard import dashboard_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)

    migrate.init_app(app, db)

    from app.routes.upload import upload_bp
    from app.routes.analysis import analysis_bp
    app.register_blueprint(ai_bp, url_prefix="/api")
    register_error_handlers(app)

    app.register_blueprint(upload_bp, url_prefix="/api")
    app.register_blueprint(analysis_bp, url_prefix="/api")
    app.register_blueprint(
                   dashboard_bp,
                   url_prefix="/api"
    )

    return app