from flask import Blueprint, jsonify
from sqlalchemy import func
import traceback

from app.models.resume import Resume
from app.models.job_description import JobDescription
from app.models.analysis import Analysis
from app.extensions import db

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard", methods=["GET"])
def dashboard():
    try:
        total_resumes = Resume.query.count()
        print("✓ Resume query OK")

        total_jobs = JobDescription.query.count()
        print("✓ JobDescription query OK")

        total_analyses = Analysis.query.count()
        print("✓ Analysis query OK")

        average_score = db.session.query(
            func.avg(Analysis.ats_score)
        ).scalar()
        print("✓ Average score query OK")

        latest_resume = (
            Resume.query
            .order_by(Resume.created_at.desc())
            .first()
        )
        print("✓ Latest resume query OK")

        return jsonify({
            "success": True,
            "total_resumes": total_resumes,
            "total_jobs": total_jobs,
            "total_analyses": total_analyses,
            "average_score": average_score
        })

    except Exception:
        traceback.print_exc()
        raise