import os
import requests
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()
access_token = os.environ['IG_ACCESS_TOKEN']
instagram_account_id = os.environ['INSTAGRAM_ACCOUNT_ID']

def post_to_instagram(photo_url, caption):
    """
    Post a photo to Instagram with a given caption using the Instagram Graph API.

    Args:
        photo_url (str): The URL to the photo to be uploaded.
        caption (str): The caption to accompany the photo.

    Returns:
        bool: True if the photo was successfully posted, otherwise False.
    """

    # Step 1: Create a media container
    create_media_url = f"https://graph.facebook.com/v20.0/{instagram_account_id}/media"
    print(create_media_url)
    media_params = {
        'image_url': photo_url,
        'caption': caption,
        'access_token': access_token
    }

    response = requests.post(create_media_url, params=media_params)

    # Check the response before attempting to parse it as JSON
    print(f"Response Status Code: {response.status_code}")
    print(f"Raw response content: {response.text}")

    if response.status_code != 200:
        print(f"Failed to create media container. Status Code: {response.status_code}")
        return False

    try:
        media_container_id = response.json().get("id")
        if not media_container_id:
            print("Failed to retrieve media container ID")
            return False
    except requests.exceptions.JSONDecodeError:
        print("Failed to parse JSON response")
        print("Response Text:", response.text)
        return False

    # Step 2: Publish the media container
    publish_media_url = f"https://graph.facebook.com/v20.0/{instagram_account_id}/media_publish"
    publish_params = {
        'creation_id': media_container_id,
        'access_token': access_token
    }

    publish_response = requests.post(publish_media_url, params=publish_params)
    
    if publish_response.status_code != 200:
        print(f"Failed to publish media. Status Code: {publish_response.status_code}")
        print("Response Text:", publish_response.text)
        return False

    print("Successfully posted to Instagram. Amazing job!!")
    return True
