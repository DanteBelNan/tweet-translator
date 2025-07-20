from .client import client

class tweets(client):
    def get_tweet(self,tweet_id:str,tweet_fields:list=None,expansions:list=None,media_fields:list=None,poll_fields:list=None,user_fields:list=None) -> dict:
        endpoint = f"tweets/{tweet_id}"
        params = {}
        if tweet_fields:
            params["tweet.fields"] = ",".join(tweet_fields)
        if expansions:
            params["expansions"] = ",".join(expansions)
        if media_fields:
            params["media.fields"] = ",".join(media_fields)
        if poll_fields:
            params["poll.fields"] = ",".join(poll_fields)
        if user_fields:
            params["user.fields"] = ",".join(user_fields)

        return self._make_request("GET", endpoint, params=params)
    
    def get_user_tweets(self, user_id:str,max_results:int=10,start_time:str=None,end_time:str=None,tweet_fields:list=None,expansions:list=None,media_fields:list=None,poll_fields:list=None,user_fields:list=None) -> dict:

        endpoint = f"users/{user_id}/tweets"
        params = {"max_results": max_results}
        if start_time:
            params["start_time"] = start_time
        if end_time:
            params["end_time"] = end_time
        if tweet_fields:
            params["tweet.fields"] = ",".join(tweet_fields)
        if expansions:
            params["expansions"] = ",".join(expansions)
        if media_fields:
            params["media.fields"] = ",".join(media_fields)
        if poll_fields:
            params["poll.fields"] = ",".join(poll_fields)
        if user_fields:
            params["user.fields"] = ",".join(user_fields)

        return self._make_request("GET", endpoint, params=params)
    
    def search_recent_tweets(self,query:str,max_results:int=10,start_time:str=None,end_time:str=None,tweet_fields:list=None,expansions:list=None,media_fields:list=None,poll_fields:list=None,user_fields:list=None) -> dict:

        endpoint = "tweets/search/recent"
        params = {"query": query, "max_results": max_results}
        if start_time:
            params["start_time"] = start_time
        if end_time:
            params["end_time"] = end_time
        if tweet_fields:
            params["tweet.fields"] = ",".join(tweet_fields)
        if expansions:
            params["expansions"] = ",".join(expansions)
        if media_fields:
            params["media.fields"] = ",".join(media_fields)
        if poll_fields:
            params["poll.fields"] = ",".join(poll_fields)
        if user_fields:
            params["user.fields"] = ",".join(user_fields)

        return self._make_request("GET", endpoint, params=params)