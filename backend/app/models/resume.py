from app.extensions import db


class Resume(db.Model):

    __tablename__ = "resumes"

    id = db.Column(db.Integer, primary_key=True)

    filename = db.Column(db.String(255), nullable=False)

    name = db.Column(db.String(150))

    email = db.Column(db.String(150))

    phone = db.Column(db.String(30))

    projects = db.Column(db.Text)

    certifications = db.Column(db.Text)

    skills = db.Column(db.Text)

    education = db.Column(db.Text)

    experience = db.Column(db.Text)

    extracted_text = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )