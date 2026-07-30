import os
import uuid
from datetime import datetime

from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename

from app.extensions import db
from app.models.resume import Resume
from app.services.parser import extract_text
from app.services.resume_extractor import extract_resume_data
from app.utils.constants import (
    UPLOAD_FOLDER,
    ALLOWED_EXTENSIONS,
)
from app.utils.logger import logger


upload_bp = Blueprint("upload", __name__)


def allowed_file(filename):
    """
    Check if uploaded file has an allowed extension.
    """
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@upload_bp.route("/upload", methods=["POST"])
def upload_resume():

    try:

        if "resume" not in request.files:
            return jsonify({
                "success": False,
                "message": "No resume file provided."
            }), 400

        file = request.files["resume"]

        if file.filename == "":
            return jsonify({
                "success": False,
                "message": "No file selected."
            }), 400

        if not allowed_file(file.filename):
            return jsonify({
                "success": False,
                "message": "Only PDF and DOCX files are allowed."
            }), 400

        # Create uploads folder if it doesn't exist
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_id = uuid.uuid4().hex[:8]

        filename = (
            f"{timestamp}_{unique_id}_"
            f"{secure_filename(file.filename)}"
        )

        filepath = os.path.join(
            UPLOAD_FOLDER,
            filename
        )

        file.save(filepath)

        logger.info(f"Resume saved to: {filepath}")

        # Extract text
        extracted_text = extract_text(filepath)

        if not extracted_text.strip():
            return jsonify({
                "success": False,
                "message": "Unable to extract text from resume."
            }), 400

        # Extract structured resume data
        resume_data = extract_resume_data(extracted_text)

        # Save to database
        resume = Resume(
            filename=filename,
            name=resume_data["name"],
            email=resume_data["email"],
            phone=resume_data["phone"],
            skills=resume_data["skills"],
            education=resume_data["education"],
            experience=resume_data["experience"],
            projects=resume_data["projects"],
            certifications=resume_data["certifications"],
            extracted_text=extracted_text
        )

        db.session.add(resume)
        db.session.commit()

        logger.info(
            f"Resume uploaded successfully. "
            f"Resume ID: {resume.id}"
        )

        return jsonify({
            "success": True,
            "message": "Resume uploaded successfully.",
            "resume_id": resume.id,
            "candidate_name": resume.name
        }), 201

    except Exception as e:

        db.session.rollback()

        logger.exception(
            "Error occurred while uploading resume."
        )

        return jsonify({
            "success": False,
            "message": "Resume upload failed.",
            "error": str(e)
        }), 500