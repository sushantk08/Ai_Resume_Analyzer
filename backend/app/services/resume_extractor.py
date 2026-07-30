import re


SKILLS = [
    "python",
    "flask",
    "django",
    "fastapi",
    "sql",
    "postgresql",
    "mysql",
    "docker",
    "aws",
    "git",
    "github",
    "react",
    "javascript",
    "html",
    "css",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "opencv",
    "selenium",
    "beautifulsoup",
    "mongodb",
    "Projects",
    "Project",
    "Personal Projects",
    "Academic Projects",
    "Certifications",
    "Certification",
    "Certificates"
]


def extract_name(text):
    """
    Assumes the first non-empty line is the candidate's name.
    """
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    if lines:
        return lines[0]

    return None


def extract_email(text):
    match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    return match.group(0) if match else None


def extract_phone(text):
    match = re.search(
        r"(\+?\d[\d\s\-]{8,15})",
        text
    )

    return match.group(0) if match else None


def extract_skills(text):

    text = text.lower()

    found = []

    for skill in SKILLS:

        if skill in text:
            found.append(skill.title())

    return ", ".join(sorted(set(found)))


def extract_section(text, keywords):
    """
    Extracts lines after a section heading until the next blank line.
    """
    lines = text.split("\n")

    capture = False

    collected = []

    for line in lines:

        current = line.strip()

        if any(keyword in current.lower() for keyword in keywords):
            capture = True
            continue

        if capture:

            if current == "":
                break

            collected.append(current)

    return "\n".join(collected)


def extract_resume_data(text):

    return {

        "name": extract_name(text),

        "email": extract_email(text),

        "phone": extract_phone(text),

        "skills": ", ".join(extract_skills(text)),

        "education": extract_section(
            text,
            [
                "education",
                "academic qualification",
                "qualification"
            ]
        ),

        "experience": extract_section(
            text,
            [
                "experience",
                "work experience",
                "professional experience"
            ]
        ),

        "projects": extract_section(
            text,
            [
                "projects",
                "project",
                "personal projects",
                "academic projects"
            ]
        ),

        "certifications": extract_section(
            text,
            [
                "certifications",
                "certification",
                "certificates",
                "licenses"
            ]
        )

    }