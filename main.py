from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

# Access Client ID and Secret to Access API in Hidden .env File
load_dotenv()
client_id = os.getenv("CLIENT_ID")
secret_id = os.getenv("CLIENT_SECRET")

def extract_token():
    '''

    :return:
    '''
    pass