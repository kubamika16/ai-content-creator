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

def main():
    prompt = "Create a recipe for a delicious chocolate cake with the following ingredients: flour, sugar, cocoa powder, eggs, and butter."
    recipe = generate_recipe(prompt)
    print("Generated Recipe:")
    print(recipe)

if __name__ == "__main__":
    main()