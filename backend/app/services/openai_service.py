import os

from google import genai

from app.config import Config


client = genai.Client(
    api_key=Config.GEMINI_API_KEY
)


def ask_gemini(prompt: str):
    """
    Send prompt to Gemini.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text


def generate_resume_feedback(resume_text, job_description):
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

    return ask_gemini(prompt)


def generate_interview_questions(
    resume_text,
    job_description,
):
    prompt = f"""
Generate 10 technical interview questions.

Resume:

{resume_text}

Job Description:

{job_description}
"""

    return ask_gemini(prompt)


def improve_resume(resume_text):
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

    return ask_gemini(prompt)


def keyword_suggestions(
    resume_text,
    job_description,
):
    prompt = f"""
Compare the resume and the job description.

Return only:

1. Missing ATS Keywords

2. Suggested Keywords

Resume:

{resume_text}

Job Description:

{job_description}
"""

    return ask_gemini(prompt)