# User Stories

These user stories describe key functionalities from the perspective of an administrator using the "Tweet Translator" service.

* ### Monitor Source Tweets
    **As an administrator of the service**,
    **I want** the system to **monitor the source Twitter (X) account**,
    **so that** it can detect new tweets for translation.

    * **Acceptance Criteria:**
        * The system successfully detects new tweets published on the source account.
        * The system exclusively processes original tweets (excluding retweets and replies).
        * The system prevents reprocessing of tweets that have already been translated and posted.

* ### Translate Content
    **As an administrator of the service**,
    **I want** the system to **translate the detected tweets to the specified target language**,
    **so that** the content becomes understandable to a new audience.

    * **Acceptance Criteria:**
        * The translation process successfully utilizes the OpenAI API.
        * The translation accurately incorporates idioms and the cultural context of the target language.
        * If the translation fails, the system logs the error appropriately and continues operation without crashing.

* ### Post Translated Tweets
    **As an administrator of the service**,
    **I want** the system to **post the translated tweets to the destination Twitter (X) account**,
    **so that** the content is effectively disseminated to the new audience.

    * **Acceptance Criteria:**
        * The translated tweet is successfully published on the destination account.
        * The translated tweet adheres to Twitter (X)'s character limit.
        * The system logs the success or failure of the posting operation.

* ### Configure System Parameters
    **As an administrator of the service**,
    **I want** to be able to **configure all API credentials and key parameters via environment variables**,
    **so that** I can ensure the security and flexibility of the deployment.

    * **Acceptance Criteria:**
        * All API credentials (Twitter, OpenAI) are correctly read from environment variables.
        * The source and destination Twitter (X) account handles are configurable via environment variables.
        * The target language for translation is configurable via environment variables.
        * The tweet monitoring interval is configurable via environment variables.