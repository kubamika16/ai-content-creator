import requests

from openai_interaction import get_openai_response

if __name__ == "__main__":



    recipe_test = "A high-resolution photograph of a freshly made Protein-Packed Breakfast Wrap. The wrap is fully assembled, bursting with vibrant ingredients: scrambled eggs, shredded cheddar cheese, black beans, and avocado slices, all snugly enclosed in a warm whole wheat tortilla. The wrap is cut in half to reveal the colorful layers of the filling. Background features a cozy kitchen countertop with a bowl of fresh eggs, a stack of tortillas, a small dish of salsa, and a ripe avocado. Soft morning light filters through a nearby window, with natural shadows creating a warm, inviting atmosphere. Created Using: DSLR camera, shallow depth of field, natural light, high contrast, rustic elements, vivid colors, hd quality --ar 4:5 --v 6.0"

    file_name_prompt = "Create a quick and easy breakfast recipe that's packed with protein. The recipe should be simple to follow and use clear language. It can be based on any of the following categories: Scrambled Eggs, Protein Smoothies, Greek Yogurt Parfaits, Overnight Oats, Breakfast Burritos, Cottage Cheese Bowls, Protein Pancakes, Avocado Toast with Eggs, Nut Butter Toast, Chia Pudding, Quinoa Bowls, Hard-Boiled Eggs, Tuna or Chicken Salad Wraps, Protein Muffins, Breakfast Quesadillas, Breakfast Bowls, Protein Bars, Omelette Variations, Breakfast Sandwiches, High-Protein Cereals, Egg-Based Dishes, Meat and Cheese Platters, Plant-Based Protein Breakfasts, Protein-Enhanced Baked Goods, Savory Breakfasts, Nut and Seed-Based Meals, Dairy-Based Breakfasts, Protein-Enhanced Drinks, Legume-Based Breakfasts, or Seafood-Based Breakfasts. Include a few emojis to make it more engaging, but don't overdo it. Add an emoji to every ingredient in the recipe, but avoid them in the instructions. Do not use any introductory phrases, stars (*), or special markdown symbols (**, ###). Just provide the recipe directly."


    file_name =  get_openai_response(file_name_prompt, "gpt-4o")
    print(file_name)
