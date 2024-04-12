# Import Necessary Libraries
from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
from prettyprinter import prettyprinter as pprint

# Access Client ID and Secret to Access API in Hidden .env File
load_dotenv()
client_id = os.getenv("CLIENT_ID")
secret_id = os.getenv("CLIENT_SECRET")

def extract_token(url: str = "https://accounts.spotify.com/") -> str:
    client_id = os.getenv("CLIENT_ID")
    secret_id = os.getenv("CLIENT_SECRET")
    auth_string = f"{client_id}:{secret_id}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = f"{url}api/token"
    headers = {"Authorization": "Basic " + auth_base64, "Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    print(json_result)
    token = json_result["access_token"]
       
    return token
    
def artist_id_search(artist_name : str, type : str, limit: int = 20, url: str = "https://api.spotify.com/"):
    url = f"{url}v1/search"
    query = f"?q={artist_name}&type={type}&limit={limit}"
    query_url = f"{url}{query}"
    token = extract_token()
    headers = {"Authorization": f"Bearer {token}"}
    result = get(query_url, headers= headers)
    json_result = json.loads(result.content)

    if len(json_result) == 0:
       print(f"No artist with this name {artist_name} exists. Please check name and try again")
       return None
    return json_result