import re

from app.utils.skills import SKILLS
from app.utils.skill_aliases import SKILL_ALIASES


def normalize_skill(skill):
    """
    Normalize skill names using aliases.
    Example:
    JS -> javascript
    Postgres -> postgresql
    """

    skill = skill.strip().lower()

    return SKILL_ALIASES.get(skill, skill)


def extract_required_skills(job_description):
    """
    Extract required skills from job description.
    """

    text = job_description.lower()

    found_skills = set()

    for skill in SKILLS:

        normalized = normalize_skill(skill)

        if skill.lower() in text:
            found_skills.add(normalized)

    return sorted(found_skills)


def calculate_skill_score(resume_skills, required_skills):
    """
    Compare resume skills with required skills.
    """

    resume_set = {
        normalize_skill(skill)
        for skill in resume_skills
    }

    required_set = {
        normalize_skill(skill)
        for skill in required_skills
    }

    matched = sorted(resume_set.intersection(required_set))

    missing = sorted(required_set.difference(resume_set))

    if len(required_set) == 0:
        score = 100
    else:
        score = round(
            (len(matched) / len(required_set)) * 100,
            2
        )

    return {
        "score": score,
        "matched_skills": matched,
        "missing_skills": missing
    }


def calculate_experience_score(
    resume_experience,
    job_description
):
    """
    Compare required experience with resume.
    """

    if not resume_experience:
        return 50

    jd = job_description.lower()

    resume = resume_experience.lower()

    match = re.search(r"(\d+)\+?\s*(year|years)", jd)

    if not match:
        return 100

    required_years = int(match.group(1))

    resume_match = re.search(
        r"(\d+)\+?\s*(year|years)",
        resume
    )

    if not resume_match:
        return 50

    candidate_years = int(resume_match.group(1))

    if candidate_years >= required_years:
        return 100

    if candidate_years == required_years - 1:
        return 80

    return 60


def calculate_education_score(
    education,
    job_description
):
    """
    Calculate education score.
    """

    if not education:
        return 50

    jd = job_description.lower()

    education = education.lower()

    if (
        "bachelor" in jd
        or "b.e" in jd
        or "b.tech" in jd
    ):

        if (
            "bachelor" in education
            or "b.e" in education
            or "b.tech" in education
        ):
            return 100

        return 60

    return 100


def calculate_projects_score(projects):
    """
    Score based on number of projects.
    """

    if not projects:
        return 50

    lines = [
        line.strip()
        for line in projects.split("\n")
        if line.strip()
    ]

    count = len(lines)

    if count >= 5:
        return 100

    if count >= 3:
        return 85

    if count >= 1:
        return 70

    return 50


def calculate_final_score(
    skills_score,
    experience_score,
    education_score,
    projects_score
):
    """
    Weighted ATS score.
    """

    final_score = (

        skills_score * 0.50 +

        experience_score * 0.25 +

        education_score * 0.15 +

        projects_score * 0.10

    )

    return round(final_score, 2)


def calculate_ats_score(
    resume_skills,
    required_skills,
    resume_experience="",
    job_description="",
    education="",
    projects=""
):
    """
    Master ATS function.
    """

    skill_result = calculate_skill_score(
        resume_skills,
        required_skills
    )

    experience_score = calculate_experience_score(
        resume_experience,
        job_description
    )

    education_score = calculate_education_score(
        education,
        job_description
    )

    projects_score = calculate_projects_score(
        projects
    )

    final_score = calculate_final_score(
        skill_result["score"],
        experience_score,
        education_score,
        projects_score
    )

    return {

        "ats_score": final_score,

        "skills_score": skill_result["score"],

        "experience_score": experience_score,

        "education_score": education_score,

        "projects_score": projects_score,

        "matched_skills": skill_result["matched_skills"],

        "missing_skills": skill_result["missing_skills"]

    }