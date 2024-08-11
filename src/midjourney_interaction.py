import os
import requests
import json
import time
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Define the API endpoints and API key
API_URL = "https://api.apiframe.pro/imagine"
FETCH_URL = "https://api.apiframe.pro/fetch"
API_KEY = os.getenv('MIDJOURNEY_API_KEY')

def generate_image(prompt, aspect_ratio="1:1", webhook_url=None, webhook_secret=None):
    if not API_KEY:
        raise ValueError("API key not found. Please set the MIDJOURNEY_API_KEY in the .env file.")
    
    """
    Generate an image using the MidJourney API based on a given prompt.

    Args:
        prompt (str): The text prompt to generate the image.
        aspect_ratio (str): The aspect ratio of the generated image (default is "1:1").
        webhook_url (str, optional): URL to receive webhook notifications (default is None).
        webhook_secret (str, optional): Secret key for webhook authentication (default is None).

    Returns:
        str: URL of the generated image if successful, None otherwise.
    """

    payload = {
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
        "webhook_url": webhook_url,
        "webhook_secret": webhook_secret
    }
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': API_KEY
    }
    
    print("Sending request to MidJourney API...")
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        if response.status_code == 200:
            task_id = response.json()["task_id"]
            print(f"Task ID: {task_id}")
        else:
            print(f"Failed to generate image: {response.status_code} {response.text}")
            return None
    except Exception as e:
        print(f"An error occurred while sending the request: {e}")
        return None

    # Polling for image result
    image_urls = None
    while not image_urls:
        time.sleep(60)  # Wait for a while before polling again
        try:
            fetch_response = requests.post(FETCH_URL, headers=headers, data=json.dumps({"task_id": task_id}))
            print(f"Fetch Response Status Code: {fetch_response.status_code}")
            print(f"Fetch Response Text: {fetch_response.text}")
            if fetch_response.status_code == 200:
                result = fetch_response.json()
                if result.get("status") == "finished":
                    print("Image generation completed.")
                    image_urls = result["image_urls"]
                else:
                    print(f"Image generation is still processing: {result.get('percentage', 'N/A')}% completed")
            else:
                print(f"Failed to fetch image result: {fetch_response.status_code} {fetch_response.text}")
                return None
        except Exception as e:
            print(f"An error occurred while fetching the result: {e}")
            return None

    # Return the first image URL
    if image_urls:
        return image_urls[0]
    else:
        return None

def download_image_from_url(image_url, save_path):

    """
    Download an image from a given URL and save it to a specified local path.

    Args:
        image_url (str): URL of the image to download.
        save_path (str): Local file path to save the downloaded image.

    Returns:
        None
    """

    try:
        # Send a GET request to the image URL
        response = requests.get(image_url)
        response.raise_for_status()  # Check for HTTP errors

        # Write the content to a local file
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded and saved to {save_path}")
    except Exception as e:
        print(f"Failed to download the image: {e}")

def fetch_image_result(task_id):

    """
    Fetch the result of an image generation task from the MidJourney API.

    Args:
        task_id (str): The task ID of the image generation request.

    Returns:
        list: List of image URLs if the task is finished, None otherwise.
    """

    payload = json.dumps({
        "task_id": task_id
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': API_KEY
    }

    try:
        response = requests.post(FETCH_URL, headers=headers, data=payload)
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        if response.status_code == 200:
            result = response.json()
            if result["status"] == "finished":
                print("Image generation completed.")
                return result["image_urls"]
            else:
                print(f"Image generation is still processing: {result.get('percentage', 'N/A')}% completed")
                return None
        else:
            print(f"Failed to fetch image result: {response.status_code} {response.text}")
            return None
    except Exception as e:
        print(f"An error occured while fetching the result: {e}")
        return None
   

def download_image_from_url(image_url, save_path):
    try:
        # Send a GET request to the image URL
        response = requests.get(image_url)
        response.raise_for_status()  # Check for HTTP errors

        # Write the content to a local file
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded and saved to {save_path}")
    except Exception as e:
        print(f"Failed to download the image: {e}")