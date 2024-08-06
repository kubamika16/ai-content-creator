import os
from openai import OpenAI
from dotenv import load_dotenv

# Load your API key from the .env file
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

# Ensure API key is loaded
if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY in the .env file.")

def generate_recipe(prompt):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o",
    )
    return response.choices[0].message.content.strip()

def main():
    prompt = "Create a breakfast recipe that is very quick and easy to make, and also has a lot of protein inside. Recipe needs to have a simple to understand words and language. Variety from scrambled eggs, to porridge, to anything you could imagine."
    recipe = generate_recipe(prompt)
    print("Generated Recipe:")
    print(recipe)

if __name__ == "__main__":
    main()
