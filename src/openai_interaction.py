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

def get_openai_response(prompt, model="gpt-4o-mini"):
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

          

def generate_recipe(prompt):
        response = client.chat.completions.create(
            messages=[
                {
                    "role":"user",
                    "content":prompt,
                }
            ],
            model="gpt-4o"
        )
        return response.choices[0].message.content.strip()

def generate_image_prompt(recipe):
    try:
        prompt = (
            f"You have to create a prompt for MidJourney. Based on the recipe below, and then some examples create a ONLY ONE PROMPT:\n\n"
            f"{recipe}\n\n"
            "And here is the way of how you are supposed to create it, a structure:\n\n"
            "\"A high-resolution photograph of a freshly made Peanut Butter Banana Smoothie, served in a tall glass. The smoothie is creamy with a light tan color, topped with banana slices and a drizzle of peanut butter. Background features a rustic kitchen counter with a blender, ripe bananas, a jar of peanut butter, and a small bowl of Greek yogurt. Bright morning light coming from a nearby window, soft shadows, natural look. Created Using: DSLR camera, shallow depth of field, natural light, high contrast, rustic props, vibrant colors, hd quality --ar 4:5 --v 6.0\"\n\n"
            "\"An inviting breakfast scene featuring a Peanut Butter Banana Smoothie in a mason jar, with a metal straw. The smoothie is thick and smooth, garnished with a sprinkle of protein powder and a honey drizzle. Background includes a wooden cutting board with sliced bananas, a spoon with peanut butter, and a scoop of protein powder. Soft morning light, cozy kitchen ambiance. Created Using: macro lens, natural hues, soft focus background, cozy elements, warm tones, detailed texture, hd quality --ar 16:9 --v 6.0\"\n\n"
            "\"A vibrant close-up shot of a Peanut Butter Banana Smoothie being poured into a glass. The smoothie is rich and creamy, with visible swirls of peanut butter. Background shows a modern kitchen with stainless steel appliances, fresh bananas, a container of almond milk, and a bowl of ice cubes. Bright and airy lighting, dynamic composition. Created Using: high-speed camera, realistic textures, vibrant lighting, modern kitchen setting, detailed ingredients, motion capture, hd quality --ar 3:2 --v 6.0\"\n\n"
            "\"A beautifully styled breakfast table with a Peanut Butter Banana Smoothie in a glass bottle, ready to be enjoyed. The smoothie has a smooth, creamy texture, garnished with a dollop of Greek yogurt and a honey drizzle. Background includes a neatly arranged breakfast spread with fresh fruit, a jar of honey, and a small plate of toast with peanut butter. Soft natural light, inviting atmosphere. Created Using: medium format camera, rich colors, detailed composition, natural light, breakfast setting, hd quality --ar 1:1 --v 6.0\"\n\n"
            "\"An aesthetically pleasing flat lay of a Peanut Butter Banana Smoothie and its ingredients. The smoothie is in a clear glass, showing its thick, creamy consistency. Surrounding the glass are neatly arranged ingredients: a ripe banana, a scoop of protein powder, a spoonful of peanut butter, and a small cup of almond milk. Background is a clean white marble countertop. Bright, even lighting, minimalistic style. Created Using: top-down view, clean aesthetic, bright lighting, minimalist design, ingredient focus, hd quality --ar 16:9 --v 6.0\"\n\n"
        )
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
    except OpenAIError as e:
        print(f"An error occurred: {e}")
        return None
