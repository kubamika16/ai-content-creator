from instagrapi import Client
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()
instagram_username = os.getenv('INSTAGRAM_USERNAME')
instagram_password = os.getenv('INSTAGRAM_PASSWORD')


def post_to_instagram(photo_path, caption):

    """
    Post a photo to Instagram with a given caption.

    Args:
        photo_path (str): The file path to the photo to be uploaded.
        caption (str): The caption to accompany the photo.

    Returns:
        bool: True if the photo was successfully posted, otherwise False.
    """

    # Initialize the Instagram client
    client = Client()
    # Login to Instagram using the provided credentials
    client.login(instagram_username, instagram_password)

    # Upload the photo with the specified caption and optional extra data
    media = client.photo_upload(
        path=photo_path,
        caption=caption,
        extra_data={
            "custom_accessibility_caption": "alt text example",  # Optional
            "like_and_view_counts_disabled": 1,  # Optional
            "disable_comments": 1,  # Optional
        }
    )
    return True