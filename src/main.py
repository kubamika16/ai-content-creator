import os
import sys

# This ensures the 'package' directory is in the path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "package"))

# Print sys.path to verify
print("Python sys.path:", sys.path)

from src.openai_interaction import get_openai_response
from src.instagram_poster import post_to_instagram
from src.midjourney_interaction import generate_image, download_image_from_url


def main(event, context):

    # Step 1: Generate a recipe using OpenAI
    recipe_prompt = "Create a quick and easy breakfast recipe that's packed with protein. The recipe should be simple to follow and use clear language. It can be based on any of the following categories: Scrambled Eggs, Protein Smoothies, Greek Yogurt Parfaits, Overnight Oats, Breakfast Burritos, Cottage Cheese Bowls, Protein Pancakes, Avocado Toast with Eggs, Nut Butter Toast, Chia Pudding, Quinoa Bowls, Hard-Boiled Eggs, Tuna or Chicken Salad Wraps, Protein Muffins, Breakfast Quesadillas, Breakfast Bowls, Protein Bars, Omelette Variations, Breakfast Sandwiches, High-Protein Cereals, Egg-Based Dishes, Meat and Cheese Platters, Plant-Based Protein Breakfasts, Protein-Enhanced Baked Goods, Savory Breakfasts, Nut and Seed-Based Meals, Dairy-Based Breakfasts, Protein-Enhanced Drinks, Legume-Based Breakfasts, or Seafood-Based Breakfasts. Include a few emojis to make it more engaging, but don't overdo it. Add an emoji to every ingredient in the recipe, but avoid them in the instructions. Do not use any introductory phrases, stars (*), or special markdown symbols (**, ###). Just provide the recipe directly."
    recipe = get_openai_response(recipe_prompt)
    print("Generated Recipe:")
    print(recipe)

     # Step 2: Generate an image prompt for MidJourney based on the recipe
    image_prompt = (
            f"You have to create a prompt for MidJourney. Based on the recipe below, and then some examples create ONLY ONE PROMPT:\n\n"
            f"{recipe}\n\n"
            "And here is the way of how you are supposed to create it, a structure:\n\n"
            "\"A high-resolution photograph of a freshly made Peanut Butter Banana Smoothie, served in a tall glass. The smoothie is creamy with a light tan color, topped with banana slices and a drizzle of peanut butter. Background features a rustic kitchen counter with a blender, ripe bananas, a jar of peanut butter, and a small bowl of Greek yogurt. Bright morning light coming from a nearby window, soft shadows, natural look. Focus on the visual details, with an emphasis on imagery and avoiding text elements. Created Using: DSLR camera, shallow depth of field, natural light, high contrast, rustic props, vibrant colors, HD quality\"\n\n"
            "\"An inviting breakfast scene featuring a Peanut Butter Banana Smoothie in a mason jar, with a metal straw. The smoothie is thick and smooth, garnished with a sprinkle of protein powder and a honey drizzle. Background includes a wooden cutting board with sliced bananas, a spoon with peanut butter, and a scoop of protein powder. Soft morning light, cozy kitchen ambiance. Prioritize the imagery, with a focus on visual appeal and avoiding any text. Created Using: macro lens, natural hues, soft focus background, cozy elements, warm tones, detailed texture, HD quality\"\n\n"
            "\"A vibrant close-up shot of a Peanut Butter Banana Smoothie being poured into a glass. The smoothie is rich and creamy, with visible swirls of peanut butter. Background shows a modern kitchen with stainless steel appliances, fresh bananas, a container of almond milk, and a bowl of ice cubes. Bright and airy lighting, dynamic composition. Emphasize the visual storytelling, ensuring the focus remains on the elements while avoiding text. Created Using: high-speed camera, realistic textures, vibrant lighting, modern kitchen setting, detailed ingredients, motion capture, HD quality\"\n\n"
            "\"A beautifully styled breakfast table with a Peanut Butter Banana Smoothie in a glass bottle, ready to be enjoyed. The smoothie has a smooth, creamy texture, garnished with a dollop of Greek yogurt and a honey drizzle. Background includes a neatly arranged breakfast spread with fresh fruit, a jar of honey, and a small plate of toast with peanut butter. Soft natural light, inviting atmosphere. Highlight the visual arrangement, with careful attention to details and avoiding the inclusion of text. Created Using: medium format camera, rich colors, detailed composition, natural light, breakfast setting, HD quality\"\n\n"
            "\"An aesthetically pleasing flat lay of a Peanut Butter Banana Smoothie and its ingredients. The smoothie is in a clear glass, showing its thick, creamy consistency. Surrounding the glass are neatly arranged ingredients: a ripe banana, a scoop of protein powder, a spoonful of peanut butter, and a small cup of almond milk. Background is a clean white marble countertop. Bright, even lighting, minimalistic style. Focus on the clean aesthetic, with an emphasis on the arrangement while avoiding text elements. Created Using: top-down view, clean aesthetic, bright lighting, minimalist design, ingredient focus, HD quality\"\n\n"
        )


    image_prompt_result = get_openai_response(image_prompt)
    print("Generated Image Prompt")
    print(image_prompt_result)

    # Step 3: Generate a file path prompt for saving the image
    file_name_prompt = f"Based on a description below, create a max 5 words recipe name with underscore (_) instead of space breaks. Recipe: {image_prompt_result}"
    save_path =  get_openai_response(file_name_prompt, "gpt-4o-mini")

      # Use /tmp directory for file path in Lambda
    file_path = f"/tmp/{save_path}.png"
    # file_path = f"src/ai_photos/{save_path}.png"

    # Step 4: Generate an image using MidJourney based on the prompt
    image_url = generate_image(image_prompt_result)
    # DUMMY URL for tests
    # image_url = "https://cdn.apiframe.pro/images/75662822011517142689279460395812-1.png"
    if not image_url:
        print("Failed to generate or fetch the image.")
        return
    print(f"Image URL: {image_url}")

    # Step 5: Save the generated image from the URL to the folder ai_photos
    download_image_from_url(image_url, file_path)

    # Step 6: Post the generated image and recipe to Instagram
    if post_to_instagram(file_path, recipe):
            print("Successfully posted to Instagram. Package & openAI.")
    else:
        print("Failed to post to Instagram.")

    # DUMMY STEP 6: Pretend posting to Instagram 
    # print("Successfully posted to Instagram.")

    # Step 7: Delete photo from ai_photos to prevent project getting bigger 
    os.remove(file_path)

if __name__ == "__main__":
    main()
