from instagrapi import Client
import os
from dotenv import load_dotenv
import requests

# Load environment variables from a .env file
load_dotenv()
instagram_username = os.environ['INSTAGRAM_USERNAME']
instagram_password = os.environ['INSTAGRAM_PASSWORD']

# Set up the proxy
host = 'brd.superproxy.io'
port = 22225
proxy_username = os.environ['PROXY_USERNAME'] 
proxy_password = os.environ['PROXY_PASSWORD']

proxy_url = f'http://{proxy_username}:{proxy_password}@{host}:{port}'


proxies = {
    'http': proxy_url,
    'https': proxy_url
}

# Update the requests library's default settings to use the proxy
requests_session = requests.Session()
requests_session.proxies.update(proxies)

# You can print the IP to confirm proxy usage
response = requests_session.get("http://lumtest.com/myip.json")
print("Proxy IP:", response.json())


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

    # Assign the custom requests session with the proxy to the client
    client.private.requests = requests_session

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