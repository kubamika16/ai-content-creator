import os
from openai import OpenAI
from openai import OpenAIError
from dotenv import load_dotenv

# Loading API key from the .env file
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    raise ValueError("API key not found. Check the OPENAI_API_KEY in the .env file.")

#Initialize the openAI client
client = OpenAI(api_key=api_key)

def get_openai_response(prompt, model="gpt-4o"):
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role":"user",
                    "content":prompt,
                }
            ],
            model=model
        )
        return response.choices[0].message.content.strip()
    except OpenAIError as e:
         print(f"An error occured: {e}")
         return None


