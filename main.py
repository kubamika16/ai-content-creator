import os
import openai
from dotenv import load_dotenv

#PI key from the .env file
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

