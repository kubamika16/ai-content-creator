from src.openai_interaction import generate_recipe, generate_image_prompt
from src.instagram_poster import post_to_instagram

def main():
    # Step 1: Generate recipe
    recipe_prompt = "Create a breakfast recipe that is very quick and easy to make, and also has a lot of protein inside. Recipe needs to have a simple to understand words and language. Variety from scrambled eggs, to porridge, to anything you could imagine. Don't create any yoghurt recipes"
    recipe = generate_recipe(recipe_prompt)
    print("Generated Recipe:")
    print(recipe)

    # Step 2: Generate image prompt
    image_prompt = generate_image_prompt(recipe)
    print("Generated Image Prompt")
    print(image_prompt)


    caption = recipe;
    photo_path = "nature.png"

    if post_to_instagram(photo_path, caption):
            print("Successfully posted to Instagram.")
    else:
        print("Failed to post to Instagram.")
    
if __name__ == "__main__":
    main()

