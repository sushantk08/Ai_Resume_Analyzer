from flask import Blueprint, jsonify
from sqlalchemy import text
from app.extensions import db

debug_bp = Blueprint("debug", __name__)

@debug_bp.route("/debug-db")
def debug_db():
    db_name = db.session.execute(text("SELECT current_database()")).scalar()
    schema = db.session.execute(text("SELECT current_schema()")).scalar()

    tables = db.session.execute(text("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
        ORDER BY table_name
    """)).fetchall()

    return jsonify({
        "database": db_name,
        "schema": schema,
        "tables": [t[0] for t in tables]
    })