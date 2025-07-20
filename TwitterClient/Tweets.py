from .Client import Client

class Tweets(Client):
    def get_tweet(self,
        tweet_id:str,
        tweet_fields:list=None,
        expansions:list=None,
        media_fields:list=None,
        poll_fields:list=None,
        user_fields:list=None
    ) -> dict:
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
    
    def get_user_tweets(self,
        user_id:str,
        max_results:int=10,
        start_time:str=None,
        end_time:str=None,
        tweet_fields:list=None,
        expansions:list=None,
        media_fields:list=None,
        poll_fields:list=None,
        user_fields:list=None
    ) -> dict:

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
    
    def search_recent_tweets(self,
        query:str,
        max_results:int=10,
        start_time:str=None,
        end_time:str=None,
        tweet_fields:list=None,
        expansions:list=None,
        media_fields:list=None,
        poll_fields:list=None,
        user_fields:list=None
    ) -> dict:

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
    
    def post_tweet(self, 
        text:str, 
        card_uri:str=None, 
        community_id:str=None, 
        direct_message_deep_link:str=None,
        for_super_followers_only:bool=None,
        geo:dict=None,
        media:dict=None,
        nullcast:bool=None,
        poll:dict=None,
        quote_tweet_id:str=None,
        reply: dict=None,
        reply_settings:str=None
    ) -> dict:
        endpoint = "tweets"
        json_data = {"text": text}
        
        if card_uri is not None:
            json_data["card_uri"] = card_uri
        if community_id is not None:
            json_data["community_id"] = community_id
        if direct_message_deep_link is not None:
            json_data["direct_message_deep_link"] = direct_message_deep_link
        if for_super_followers_only is not None:
            json_data["for_super_followers_only"] = for_super_followers_only
        if geo is not None:
            json_data["geo"] = geo
        if media is not None:
            json_data["media"] = media
        if nullcast is not None:
            json_data["nullcast"] = nullcast
        if poll is not None:
            json_data["poll"] = poll
        if quote_tweet_id is not None:
            json_data["quote_tweet_id"] = quote_tweet_id
        if reply is not None:
            json_data["reply"] = reply
        if reply_settings is not None:
            json_data["reply_settings"] = reply_settings

        return self._make_request("POST", endpoint, json_data=json_data)