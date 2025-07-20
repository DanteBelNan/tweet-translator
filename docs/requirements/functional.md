# Functional Requirements

This document describes the functional requirements for the "Tweet Translator" application.

### FR1. Source Tweet Monitoring

* **Connect to Source Account:** The system shall be able to connect to a configured source Twitter (X) account.
* **Detect New Tweets:** The system shall be capable of detecting new tweets published by the source account at configurable time intervals.
* **Retrieve Tweet Text:** The system shall be able to retrieve the full text of detected tweets.
* **Filter Tweets:** The system shall ignore retweets and direct replies, focusing only on original tweets from the source account.
* **Prevent Duplication:** The system shall maintain a record of already processed tweets to prevent duplication.

### FR2. Content Translation

* **Send to OpenAI API:** The system shall send the text of the detected tweet to the OpenAI API for translation.
* **Specify Target Language:** The system shall specify a target language for translation, configurable by the user.
* **Cultural Context Translation:** The system shall instruct the OpenAI API to ensure the translation considers idioms and the cultural context of the target language.
* **Error Handling:** The system shall handle potential translation API errors (e.g., timeouts, quota exceeded) and either retry or log the failure.

### FR3. Translated Tweet Reposting

* **Connect to Destination Account:** The system shall be able to connect to a configured destination Twitter (X) account.
* **Post Translated Tweet:** The system shall post the translated text as a new tweet on the destination account.
* **Handle Character Limit:** The system shall handle Twitter (X) maximum character limits for translated tweets, truncating or adjusting as necessary.
* **Log Repost Status:** The system shall log the success or failure of the reposting operation.

### FR4. Configuration

* **Load Twitter API Credentials:** The system shall load Twitter (X) API credentials from environment variables.
* **Load OpenAI API Credentials:** The system shall load OpenAI API credentials from environment variables.
* **Load Account Handles:** The system shall load source and destination Twitter (X) account handles from environment variables.
* **Load Target Language:** The system shall load the target language for translation from environment variables.
* **Load Check Interval:** The system shall load the tweet checking interval from environment variables.