import requests
import os
from dotenv import load_dotenv
load_dotenv()
from requests_oauthlib import OAuth1Session

class Client:

    def __init__(self):
        """
        Initializes Client using OAuth 1.0a.
        Requires these env variables:
        - TWITTER_CLIENT_ID (Consumer Key)
        - TWITTER_CLIENT_SECRET (Consumer Secret)
        - TWITTER_USER_ACCESS_TOKEN (Access Token de usuario)
        - TWITTER_USER_ACCESS_TOKEN_SECRET (Access Token Secret de usuario)
        - BASE_URL (URL base de la API, por defecto "https://api.twitter.com/2")
        """
        self.base_url = os.getenv("TWITTER_BASE_URL", "https://api.twitter.com/2")

        api_key = os.getenv("TWITTER_API_KEY")
        api_secret = os.getenv("TWITTER_API_SECRET")
        access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

        if not all([api_key, api_secret, access_token, access_token_secret]):
            raise ValueError("Missing OAuth 1.0a credentials. "
                             "Please ensure TWITTER_API_KEY, TWITTER_API_SECRET, "
                             "TWITTER_ACCESS_TOKEN, and TWITTER_ACCESS_TOKEN_SECRET are set.")
        
        self.session = OAuth1Session(
            api_key,
            client_secret=api_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret
        )
        self.session.headers.update({"Content-Type": "application/json"})

    def _make_request(self,
        method:str,
        endpoint:str,
        params:dict=None,
        json_data:dict=None
    ):
        url = f"{self.base_url}/{endpoint}"

        try:
            response = self.session.request(method, url, params=params, json=json_data)
            response.raise_for_status() 
            
            if response.status_code == 204:
                return {} #We need this because some cases like delete may return no content (204 code) and response.json will give an error if that happens so we are preventing that)
            
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP Error: {http_err}")
            print(f"Server response: {response.text}") # ¡Esto es crucial para el 401/403!
            raise
        except requests.exceptions.RequestException as req_err:
            print(f"Connection error: {req_err}")
            raise
        except ValueError as json_err:
            print(f"Error Parsing JSON: {json_err}")
            print(f"Raw response: {response.text}")
            raise
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise
    