from app.extensions import db


class JobDescription(db.Model):

    __tablename__ = "job_descriptions"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(255))

    company = db.Column(db.String(255))

    description = db.Column(db.Text, nullable=False)

    required_skills = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )