from src.openai_interaction import generate_recipe

def main():
    # Step 1: Generate recipe
    recipe_prompt = "Create a breakfast recipe that is very quick and easy to make, and also has a lot of protein inside. Recipe needs to have a simple to understand words and language. Variety from scrambled eggs, to porridge, to anything you could imagine. Don't create any yoghurt recipes"
    recipe = generate_recipe(recipe_prompt)
    print("Generated Recipe:")
    print(recipe)

if __name__ == "__main__":
    main()

