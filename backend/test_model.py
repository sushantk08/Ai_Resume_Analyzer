from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

try:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Say hello"
    )
    print(response.text)
except Exception as e:
    import traceback
    traceback.print_exc()