from .Client import Client

class Users(Client):
    
    def get_user_by_username(self,
        username:str,
        user_fields:list=None
    ) -> dict:
        endpoint = f"users/by/username/{username}"
        params = {}
        if user_fields:
            params["user.fields"] = ",".join(user_fields)
        
        response = self._make_request("GET", endpoint, params=params)
        
        if "data" in response:
            return response["data"]
        elif "errors" in response:
            raise Exception({"errors": response["errors"]})
        return response

    def get_user_by_id(self,
        user_id:str,
        user_fields:list=None
    ) -> dict:
        endpoint = f"users/{user_id}"
        params = {}
        if user_fields:
            params["user.fields"] = ",".join(user_fields)
        
        response = self._make_request("GET", endpoint, params=params)
        
        if "data" in response:
            return response["data"]
        elif "errors" in response:
            raise Exception({"errors": response["errors"]})
        return response