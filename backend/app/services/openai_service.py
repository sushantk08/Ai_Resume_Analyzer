from openai import OpenAI

from app.config import Config


client = OpenAI(
    api_key=Config.OPENAI_API_KEY
)


def generate_resume_feedback(resume_text, job_description):
    """
    Generate AI feedback for a resume.
    """

    prompt = f"""
You are an experienced technical recruiter.

Analyze the following resume against the job description.

Return your response using these headings:

Overall Score:
Strengths:
Weaknesses:
Missing Skills:
Suggestions:

Resume:

{resume_text}

Job Description:

{job_description}
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt,
    )

    return response.output_text


def generate_interview_questions(
    resume_text,
    job_description
):
    """
    Generate interview questions.
    """

    prompt = f"""
Generate ten technical interview questions.

Resume:

{resume_text}

Job Description:

{job_description}
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt,
    )

    return response.output_text


def improve_resume(resume_text):
    """
    Rewrite resume professionally.
    """

    prompt = f"""
Rewrite this resume professionally.

Improve:

- Grammar
- Bullet points
- ATS keywords
- Professional language

Resume:

{resume_text}
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt,
    )

    return response.output_text


def keyword_suggestions(
    resume_text,
    job_description
):
    """
    Suggest missing ATS keywords.
    """

    prompt = f"""
Compare the resume and job description.

List only the missing ATS keywords.

Resume:

{resume_text}

Job Description:

{job_description}
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt,
    )

    return response.output_text