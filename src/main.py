import os
import sys




# Example usage:

# from fatsecret import Fatsecret

# client_id="208a6fbf85ec4babbf87819a875b5809"
# client_secret="6966544e37ff49ff87fc4c8502b99675"

# fs = Fatsecret(client_id, client_secret)

# foods = fs.foods_search("Tacos")

# print(foods)

# This ensures the 'package' directory is in the path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "package"))

# Print sys.path to verify  
print("Python sys.path:", sys.path)

from src.openai_interaction import get_openai_response
from src.openai_interaction import generate_dalee3_image
from src.instagram_poster import post_to_instagram
from src.midjourney_interaction import generate_image, download_image_from_url
from src.utils import get_random_meal


def main(event, context):

    # Step 1: Generate a recipe using OpenAI

    meal_prep_ideas = [
    "Chicken Stir-Fry Bowls",
    "Beef and Broccoli",
    "Turkey Meatballs",
    "Salmon with Asparagus",
    "Chickpea Curry",
    "Greek Chicken Salad",
    "Teriyaki Chicken",
    "Lentil Soup",
    "Pork Lettuce Wraps",
    "Spicy Turkey Chili",
    "Quinoa and Black Bean Bowls",
    "Chicken Fajitas",
    "Beef Tacos",
    "Garlic Butter Shrimp",
    "Tofu Stir-Fry",
    "Peanut Butter Chicken",
    "Vegetable and Quinoa Salad",
    "Ham and Cheese Stuffed Chicken",
    "Sweet Potato and Chicken Bake",
    "Turkey Burgers",
    "Fish Tacos",
    "Spinach and Feta Stuffed Chicken",
    "Beef Zucchini Skillet",
    "Pasta with Turkey Sausage",
    "Chicken and Sweet Potato Salad",
    "Asian Chicken Lettuce Wraps",
    "BBQ Chicken Bowls",
    "Roasted Veggie and Hummus Wraps",
    "Turkey and Quinoa Stuffed Peppers",
    "Balsamic Chicken and Veggies",
    "Chicken Pesto Pasta",
    "Seafood Paella",
    "Slow Cooker Chicken Chili",
    "Cajun Shrimp and Grits",
    "Chicken Caesar Wraps",
    "Stuffed Cabbage Rolls",
    "Buffalo Chicken Bowls",
    "Steak Fajita Roll Ups",
    "Moroccan Chicken Stew",
    "Chimichurri Steak Bowls",
    "Tex-Mex Turkey Skillet",
    "Mango Chicken Quinoa Bowls",
    "Chicken and Veggie Kabobs",
    "Garlic Soy Glazed Salmon",
    "Stuffed Peppers with Beef and Rice",
    "Jerk Chicken with Pineapple Salsa",
    "Chicken Parmesan with Zoodles",
    "Sheet Pan Teriyaki Chicken",
    "Beef Patties with Veggies and Rice",
    "Chicken Quinoa Salad"
]
    random_meal = get_random_meal(meal_prep_ideas)

    recipe_prompt = f"""Create a simple and high-protein meal prep recipe that can be portioned into three meals for three days. The recipe should be easy to follow and use clear language. Recipe should be about {random_meal} 
After the recipe title, include a cost estimate in GBP and total protein content in grams, with the breakdown per meal. The format should be:
Cost Estimate: £15 (£5 per meal)
Total Protein: 180g (60g per meal)
Make sure the recipe includes a variety of ingredients such as lean proteins, whole grains, and colorful vegetables. Encourage the use of spices, herbs, and healthy sauces to enhance flavor. Each meal should be balanced, with a mix of protein, carbs, and vegetables. Consider different cooking methods like grilling, roasting, or stir-frying to add variety to the dish.
List the ingredients followed by the instructions. Add an emoji to every ingredient in the recipe, but do not use emojis in the instructions. Avoid any introductory phrases, special characters, or markdown symbols. Provide the recipe directly without additional formatting.
"""

    
    recipe = get_openai_response(recipe_prompt)
    print("Generated Recipe:")
    print(recipe)

     # Step 2: Generate an image prompt for MidJourney based on the recipe
    image_prompt = (
            f"You have to create a prompt for MidJourney. Based on the recipe below, and then some examples create ONLY ONE PROMPT:\n\n"
            f"{recipe}\n\n"
            "And here is the way of how you are supposed to create it, a structure:\n\n"
            "\"A high-resolution photograph of a freshly prepared meal prep trio with roasted chicken breast, cooked quinoa, and steamed broccoli, all divided into meal prep containers. The chicken breast is sliced into succulent strips, seasoned with garlic, salt, and pepper, and drizzled with olive oil. The quinoa is fluffy and perfectly cooked, paired with tender broccoli florets. A lemon wedge is placed next to each serving for a fresh burst of flavor. Background features a clean kitchen counter with a pot of quinoa, a steamer basket, and a baking sheet. Bright, natural lighting highlights the freshness and detail of the ingredients. Created Using: DSLR camera, shallow depth of field, natural light, high contrast, minimalist props, vibrant colors, HD quality\"\n\n"
            "\"A high-resolution photograph of a colorful meal prep with grilled salmon, brown rice, and mixed vegetables (bell peppers, zucchini, and carrots). The salmon is perfectly seared, with a slight char on the edges, laid over a bed of fluffy brown rice. The vegetables are sautéed to a tender-crisp texture, with vibrant colors and a light seasoning of herbs. The meal is neatly arranged in meal prep containers. Background shows a rustic wooden kitchen table with a bowl of fresh lemons, a bottle of olive oil, and a sprinkle of herbs. Natural light illuminates the scene, creating a fresh and appetizing look. Created Using: DSLR camera, shallow depth of field, natural light, high contrast, rustic props, vibrant colors, HD quality\"\n\n"
            "\"A high-resolution photograph of a healthy meal prep featuring ground turkey, roasted sweet potatoes, and steamed green beans, all neatly divided into meal prep containers. The ground turkey is lightly browned and seasoned with herbs, creating a savory base. The sweet potatoes are roasted to perfection, with caramelized edges and a soft interior. The green beans are steamed and vibrant, adding a pop of color to the meal. Background includes a kitchen counter with a cutting board, spices, and a bowl of fresh herbs. Bright natural light emphasizes the freshness and detail of the ingredients. Created Using: DSLR camera, shallow depth of field, natural light, vibrant colors, HD quality\"\n\n"
            "\"A high-resolution photograph of a plant-based meal prep with tofu stir-fry, jasmine rice, and steamed broccoli. The tofu is golden brown, stir-fried with a mix of bell peppers, snap peas, and carrots, creating a colorful and nutritious dish. The jasmine rice is fluffy and aromatic, complementing the stir-fry. The broccoli is steamed to a bright green, adding a fresh element to the meal. Background features a modern kitchen setup with a wok, fresh vegetables, and a bottle of soy sauce. Natural light highlights the textures and colors, creating an appetizing presentation. Created Using: DSLR camera, shallow depth of field, natural light, vibrant colors, HD quality\"\n\n"
            "\"A high-resolution photograph of a balanced meal prep with grilled chicken thighs, wild rice, and roasted asparagus. The chicken thighs are grilled with a crispy skin, seasoned with a blend of herbs and spices. The wild rice is fluffy with a nutty flavor, providing a hearty base. The asparagus is roasted to a tender texture with slightly charred tips, adding a gourmet touch to the meal. Background includes a clean kitchen counter with a tray of roasted vegetables, a cutting board, and a knife. Natural light creates a warm and inviting atmosphere. Created Using: DSLR camera, shallow depth of field, natural light, rich colors, HD quality\"\n\n"
            "\"Ensure that the language used is neutral and free from any phrases or terms that might trigger banned word filters. Avoid complex or overly descriptive language that might be misconstrued by content filters. The focus should remain on clarity and simplicity in both the recipe and the instructions.\"\n\n"
)



    image_prompt_result = get_openai_response(image_prompt)
    print("Generated Image Prompt")
    print(image_prompt_result)

    # Step 3: Generate an image using MidJourney based on the prompt
    image_url = generate_image(image_prompt_result)
    # DUMMY URL for tests
    # image_url = "https://cdn.apiframe.pro/images/75662822011517142689279460395812-1.png"
    # image_url = generate_dalee3_image(image_prompt_result)
    if not image_url:
        print("Failed to generate or fetch the image.")
        return
    print(f"Image URL: {image_url}")

    # Step 4: Post the generated image and recipe to Instagram
    post_to_instagram(image_url, recipe)


if __name__ == "__main__":
    main()
