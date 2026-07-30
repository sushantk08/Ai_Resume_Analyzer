from app.extensions import db


class Analysis(db.Model):

    __tablename__ = "analysis"

    id = db.Column(db.Integer, primary_key=True)

    resume_id = db.Column(
        db.Integer,
        db.ForeignKey("resumes.id"),
        nullable=False
    )

    job_description_id = db.Column(
        db.Integer,
        db.ForeignKey("job_descriptions.id"),
        nullable=False
    )

    ats_score = db.Column(db.Float)

    matched_skills = db.Column(db.Text)

    missing_skills = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )