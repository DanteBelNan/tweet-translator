# UML Class Diagram

This conceptual UML class diagram illustrates the main entities and their relationships within the "Tweet Translator" system. It does not include every possible attribute and method but focuses on the most representative ones.

```mermaid
classDiagram
    class TweetTranslatorApp {
        - twitter_client: TwitterClient
        - openai_client: OpenAIClient
        - source_account: str
        - destination_account: str
        - target_language: str
        - check_interval: int
        - processed_tweet_ids: list

        + start_monitoring()
        + stop_monitoring()
        - fetch_new_tweets()
        - translate_tweet(text: str)
        - post_translated_tweet(text: str)
        - load_config()
    }

    class TwitterClient {
        - client_id: str
        - client_secret: str
        - bearer_token: str
        - base_url: str

        + get_user_tweets(user_handle: str, last_tweet_id: str): list
        + post_tweet(text: str): bool
        - authenticate()
    }

    class OpenAIClient {
        - api_key: str
        - model: str

        + translate(text: str, target_lang: str): str
    }

    class Logger {
        + log_info(message: str)
        + log_error(message: str)
        + log_warning(message: str)
    }

    TweetTranslatorApp --|> TwitterClient : uses
    TweetTranslatorApp --|> OpenAIClient : uses
    TweetTranslatorApp "1" *-- "1" Logger : has a

    note "TwitterClient represents interaction with the Twitter/X API (reading and writing)." as N1
    TwitterClient .. N1

    note "OpenAIClient represents interaction with the OpenAI API for translation." as N2
    OpenAIClient .. N2
```