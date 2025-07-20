import requests
import os
from dotenv import load_dotenv
load_dotenv()

class client:

    def __init__(self, bearer_token:str=None, base_url:str=None):
        if bearer_token:
            self.bearer_token = bearer_token
        else:
            self.bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
        if base_url:
            self.base_url = base_url
        else:
            self.base_url = os.getenv("TWITTER_BASE_URL")
            
            
        self.session = requests.session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.bearer_token}",
            "Content-Type": "application/json"
        })

    def _make_request(self,method:str,endpoint:str,params:dict=None,json_data:dict=None):
        url = f"{self.base_url}/{endpoint}"

        try:
            response = self.session.request(method, url, params=params, json=json_data)
            response.raise_for_status() 
            
            return response.json()
        except Exception as e:
            raise e
    