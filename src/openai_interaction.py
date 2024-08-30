import os
from openai import OpenAI
from openai import OpenAIError
from dotenv import load_dotenv

# Loading API key from the .env file
load_dotenv()
api_key = os.environ['OPENAI_API_KEY']

# Check if the API key is loaded, raise an error if not
if not api_key:
    raise ValueError("API key not found. Check the OPENAI_API_KEY in the .env file.")

# Initialize the OpenAI client with the provided API key
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

def generate_dalee3_image(prompt, model="dall-e-3", size="1024x1024", quality="hd"):
    """
    Generates an image based on the provided prompt using DALL·E 3.

    Args:
        prompt (str): The text prompt to generate the image.
        model (str): The model to use (default is "dall-e-3").
        size (str): The size of the image (default is "1024x1024").
        quality (str): The quality of the image (default is "hd").

    Returns:
        str: The URL of the generated image.
    """
    response = client.images.generate(
        model=model,
        prompt=prompt,
        size=size,
        quality=quality,
        n=1,
    )
    
    # Retrieve and return the URL of the generated image
    image_url = response.data[0].url
    return image_url
