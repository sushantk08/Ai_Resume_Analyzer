import os

from google import genai

from app.config import Config


client = genai.Client(
    api_key=Config.GEMINI_API_KEY
)

print("Gemini Key Prefix:", Config.GEMINI_API_KEY[:10])
print("Gemini Model:", Config.GEMINI_MODEL)

def ask_gemini(prompt: str):
    try:
        print(f"Using model: {Config.GEMINI_MODEL}")

        response = client.models.generate_content(
            model=Config.GEMINI_MODEL,
            contents=prompt,
        )

        return response.text

    except Exception as e:
        import traceback

        print("=" * 80)
        print("GEMINI ERROR")
        traceback.print_exc()
        print("=" * 80)

        raise


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