# Import Necessary Libraries
# Import Necessary Libraries
from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
from prettyprinter import pprint as pp

# Access Client ID and Secret to Access API in Hidden .env File
load_dotenv()
client_id = os.getenv("CLIENT_ID")
secret_id = os.getenv("CLIENT_SECRET")

# Create A Class to Have the Methods Under the Same Class
class SmartInsights:
@classmethod

    def __init__(self, auth: str):
"""
Insert Docstring
"""
        self.auth = auth
        
    def extract_token():
'''
Insert Docstring
'''
    client_id = os.getenv("CLIENT_ID")
    secret_id = os.getenv("CLIENT_SECRET")
    auth_string = f"{client_id}:{secret_id}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    
    url = "https://accounts.spotify.com/api/token"
    headers = {"Authorization": "Basic " + auth_base64, "Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    print(json_result)
    token = json_result["access_token"]
    
    return token

def artist_id_search(token, artist_name, type, limit = 20): 
'''
Insert Docstring
'''
    url = "https://api.spotify.com/v1/search"
    query = f"?q={artist_name}&type={type}&limit={limit}"
    query_url = f"{url}{query}"
    token = extract_token()
    headers = {"Authorization": f"Bearer {token}"}
    result = get(query_url, headers= headers)
    json_result = json.loads(result.content)['artists']["items"]

    if len(json_result) == 0:
       print(f"No artist with this name {artist_name} exists.....")
       return None
    return json_result









