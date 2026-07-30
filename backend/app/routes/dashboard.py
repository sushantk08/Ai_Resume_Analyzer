from flask import Blueprint, jsonify
from sqlalchemy import func

from app.models.resume import Resume
from app.models.job_description import JobDescription
from app.models.analysis import Analysis
from app.extensions import db

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard", methods=["GET"])
def dashboard():
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