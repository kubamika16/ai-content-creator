from instagrapi import Client
import os
from dotenv import load_dotenv

# Loading API key from the .env file
load_dotenv()
instagram_username = os.getenv('INSTAGRAM_USERNAME')
instagram_password = os.getenv('INSTAGRAM_PASSWORD')


def post_to_instagram(photo_path, caption):
    client = Client()
    client.login(instagram_username, instagram_password)

    # Upload the photo
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