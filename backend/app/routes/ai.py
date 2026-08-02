from flask import Blueprint, jsonify, request
import traceback

from app.models.resume import Resume
from app.models.job_description import JobDescription

from app.services.openai_service import (
    generate_resume_feedback,
    generate_interview_questions,
    improve_resume,
    keyword_suggestions
)

ai_bp = Blueprint("ai", __name__)


@ai_bp.route("/ai/analyze", methods=["POST"])
def ai_analyze():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "message": "Request body is required."
            }), 400

        resume_id = data.get("resume_id")
        job_id = data.get("job_id")

        if not resume_id or not job_id:
            return jsonify({
                "success": False,
                "message": "resume_id and job_id are required."
            }), 400

        resume = Resume.query.get(resume_id)

        if not resume:
            return jsonify({
                "success": False,
                "message": "Resume not found."
            }), 404

        job = JobDescription.query.get(job_id)

        if not job:
            return jsonify({
                "success": False,
                "message": "Job description not found."
            }), 404

        feedback = generate_resume_feedback(
            resume.extracted_text,
            job.description
        )

        return jsonify({
            "success": True,
            "message": "AI analysis generated successfully.",
            "data": feedback
        }), 200

    except Exception as e:
        print("=" * 60)
        print("AI ANALYZE ERROR")
        traceback.print_exc()
        print("Exception:", repr(e))
        print("=" * 60)

        return jsonify({
            "success": False,
            "message": "AI analysis failed.",
            "error": str(e)
        }), 500


@ai_bp.route("/ai/interview", methods=["POST"])
def ai_interview():
    try:
        data = request.get_json()

        resume_id = data.get("resume_id")
        job_id = data.get("job_id")

        resume = Resume.query.get(resume_id)
        job = JobDescription.query.get(job_id)

        questions = generate_interview_questions(
            resume.extracted_text,
            job.description
        )

        return jsonify({
            "success": True,
            "data": questions
        })

    except Exception as e:
        traceback.print_exc()
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@ai_bp.route("/ai/rewrite", methods=["POST"])
def ai_rewrite():
    try:
        data = request.get_json()

        resume = Resume.query.get(data.get("resume_id"))

        rewritten = improve_resume(
            resume.extracted_text
        )

        return jsonify({
            "success": True,
            "data": rewritten
        })

    except Exception as e:
        traceback.print_exc()
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@ai_bp.route("/ai/keywords", methods=["POST"])
def ai_keywords():
    try:
        data = request.get_json()

        resume = Resume.query.get(data.get("resume_id"))
        job = JobDescription.query.get(data.get("job_id"))

        keywords = keyword_suggestions(
            resume.extracted_text,
            job.description
        )

        return jsonify({
            "success": True,
            "data": keywords
        })

    except Exception as e:
        traceback.print_exc()
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500