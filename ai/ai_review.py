from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ai_review(language: str, code: str):
    prompt = f"""
You are a senior {language} developer.
Review the code for errors, bad practices, and improvements.

Code:
{code}
"""
    response = client.chat.completions.create(
        model="gpt-5-chat",
        messages=[
            {"role": "system", "content": "You are a code reviewer"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content