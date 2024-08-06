import os
import openai
from dotenv import load_dotenv

#PI key from the .env file
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_recipe(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

