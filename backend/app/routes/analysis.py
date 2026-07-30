from flask import Blueprint, request, jsonify

from app.extensions import db

from app.models.resume import Resume
from app.models.job_description import JobDescription
from app.models.analysis import Analysis

from app.services.ats_service import (
    extract_required_skills,
    calculate_ats_score,
)

from app.utils.logger import logger

analysis_bp = Blueprint("analysis", __name__)


@analysis_bp.route("/analyze", methods=["POST"])
def analyze_resume():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "message": "Request body is required."
            }), 400

        resume_id = data.get("resume_id")
        job_title = data.get("job_title", "")
        company = data.get("company", "")
        job_description = data.get("job_description")

        if not resume_id:
            return jsonify({
                "success": False,
                "message": "resume_id is required."
            }), 400

        if not job_description:
            return jsonify({
                "success": False,
                "message": "job_description is required."
            }), 400

        # ------------------------------------
        # Fetch Resume
        # ------------------------------------

        resume = Resume.query.get(resume_id)

        if not resume:
            return jsonify({
                "success": False,
                "message": "Resume not found."
            }), 404

        # ------------------------------------
        # Extract Required Skills
        # ------------------------------------

        required_skills = extract_required_skills(job_description)

        # ------------------------------------
        # Save Job Description
        # ------------------------------------

        job = JobDescription(
            title=job_title,
            company=company,
            description=job_description,
            required_skills=", ".join(required_skills)
        )

        db.session.add(job)
        db.session.commit()

        # ------------------------------------
        # Resume Skills
        # ------------------------------------

        resume_skills = []

        if resume.skills:

            resume_skills = [
                skill.strip()
                for skill in resume.skills.split(",")
                if skill.strip()
            ]

        # ------------------------------------
        # Calculate ATS Score
        # ------------------------------------

        ats_result = calculate_ats_score(

            resume_skills=resume_skills,

            required_skills=required_skills,

            resume_experience=resume.experience or "",

            job_description=job_description,

            education=resume.education or "",

            projects=resume.projects or ""

        )

        # ------------------------------------
        # Save Analysis
        # ------------------------------------

        analysis = Analysis(

            resume_id=resume.id,

            job_description_id=job.id,

            ats_score=ats_result["ats_score"],

            matched_skills=", ".join(
                ats_result["matched_skills"]
            ),

            missing_skills=", ".join(
                ats_result["missing_skills"]
            )

        )

        db.session.add(analysis)
        db.session.commit()

        logger.info(
            f"ATS analysis completed for Resume ID {resume.id}"
        )

        # ------------------------------------
        # Response
        # ------------------------------------

        return jsonify({

            "success": True,

            "message": "Resume analyzed successfully.",

            "data": {

                "resume_id": resume.id,

                "candidate_name": resume.name,

                "job_title": job.title,

                "company": job.company,

                "ats_score": ats_result["ats_score"],

                "skills_score": ats_result["skills_score"],

                "experience_score": ats_result["experience_score"],

                "education_score": ats_result["education_score"],

                "projects_score": ats_result["projects_score"],

                "matched_skills": ats_result["matched_skills"],

                "missing_skills": ats_result["missing_skills"]

            }

        }), 200

    except Exception as e:

        db.session.rollback()

        logger.exception("ATS analysis failed.")

        return jsonify({

            "success": False,

            "message": "Analysis failed.",

            "error": str(e)

        }), 500