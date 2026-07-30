from flask import Blueprint, jsonify
from sqlalchemy import text
from app.extensions import db
import traceback

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard", methods=["GET"])
def dashboard():
    try:
        result = db.session.execute(text("SELECT 1")).scalar()

        return jsonify({
            "success": True,
            "result": result
        })

    except Exception as e:
        traceback.print_exc()

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500