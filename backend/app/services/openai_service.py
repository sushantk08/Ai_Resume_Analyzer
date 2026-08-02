from openai import OpenAI

from app.config import Config

client = OpenAI(
    api_key=Config.GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
)


def ask_ai(prompt: str):
    response = client.chat.completions.create(
        model=Config.GROQ_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are an expert ATS Resume Analyzer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content


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

    return ask_ai(prompt)


def generate_interview_questions(resume_text, job_description):
    prompt = f"""
Generate 10 technical interview questions.

Resume:

{resume_text}

Job Description:

{job_description}
"""

    return ask_ai(prompt)


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

    return ask_ai(prompt)


def keyword_suggestions(resume_text, job_description):
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

    return ask_ai(prompt)