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
        print("Step 1")
        total_resumes = Resume.query.count()

        print("Step 2")
        total_jobs = JobDescription.query.count()

        print("Step 3")
        total_analyses = Analysis.query.count()

        print("Step 4")
        average_score = db.session.query(
            func.avg(Analysis.ats_score)
        ).scalar()

        print("Step 5")
        latest_resume = (
            Resume.query
            .order_by(Resume.created_at.desc())
            .first()
        )

        print("Step 6")

        return jsonify({
            "success": True
        })

    except Exception:
        traceback.print_exc()
        raise