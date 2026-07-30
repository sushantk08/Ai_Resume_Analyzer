from flask import Blueprint, jsonify
from sqlalchemy import func, text
import traceback

from app.models.resume import Resume
from app.models.job_description import JobDescription
from app.models.analysis import Analysis
from app.extensions import db

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard", methods=["GET"])
def dashboard():
    try:
        # Debug database information
        db_name = db.session.execute(
            text("SELECT current_database()")
        ).scalar()

        current_schema = db.session.execute(
            text("SELECT current_schema()")
        ).scalar()

        tables = db.session.execute(text("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
            ORDER BY table_name
        """)).fetchall()

        # If resumes table is missing, return debug info immediately
        table_names = [t[0] for t in tables]

        if "resumes" not in table_names:
            return jsonify({
                "success": False,
                "error": "resumes table not found",
                "database": db_name,
                "schema": current_schema,
                "tables": table_names
            }), 500

        # Dashboard statistics
        total_resumes = Resume.query.count()
        total_jobs = JobDescription.query.count()
        total_analyses = Analysis.query.count()

        average_score = db.session.query(
            func.avg(Analysis.ats_score)
        ).scalar()

        latest_resume = (
            Resume.query
            .order_by(Resume.created_at.desc())
            .first()
        )

        return jsonify({
            "success": True,
            "database": db_name,
            "schema": current_schema,
            "tables": table_names,
            "total_resumes": total_resumes,
            "total_jobs": total_jobs,
            "total_analyses": total_analyses,
            "average_score": float(average_score) if average_score else 0,
            "latest_resume": {
                "id": latest_resume.id,
                "name": latest_resume.name,
                "email": latest_resume.email,
                "created_at": latest_resume.created_at.isoformat()
            } if latest_resume else None
        })

    except Exception as e:
        traceback.print_exc()

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500