# 🐦🗣️ Tweet Translator

"Tweet Translator" is an automated service designed to facilitate content translation and dissemination between different Twitter (X) accounts. Its primary function is to monitor tweets from a specific source account, translate them into a desired language (while considering the idioms and cultural nuances of that language), and then automatically repost them to a different target account.

## ✨ Key Features

* **Account Monitoring:** Keeps track of tweets from a predefined source Twitter account.
* **Intelligent Translation:** Utilizes advanced translation capabilities to not only translate text but also adapt idioms and cultural context to the target language.
* **Automated Reposting:** Publishes translated tweets directly to a designated Twitter account.
* **Integration with Leading APIs:** Leverages the power of Twitter (X) and OpenAI APIs to provide a robust and accurate service.

## 🚀 Getting Started

These instructions will help you set up and run the project on your local machine using DevContainers.

### Prerequisites

You'll need the following tools installed:

* **Docker Desktop** (or a compatible container environment)
* **Visual Studio Code** (with the "Dev Containers" extension installed)
* **Git**

### Installation and Container Setup

1.  **Clone the repository:**
    Open your terminal and clone this repository using your personal SSH key (assuming you have the `github.com-personal` alias configured):

    ```bash
    git clone git@github.com-personal:DanteBelNan/tweet-translator.git
    cd tweet-translator
    ```

2.  **Open in Dev Container:**
    Open the `tweet-translator` folder in Visual Studio Code. VS Code will automatically detect the Dev Container configuration and ask if you want to "Reopen in Container". Click on that option. 
    This will build the container image (if it doesn't exist) and start the development environment with all necessary Python dependencies pre-installed.

### Environment Variables Configuration

Once the Dev Container is ready, create a `.env` file in the project root and configure the following variables. These variables will be automatically loaded by the application within the container.

```dotenv
# Twitter (X) API
TWITTER_CLIENT_ID=your_twitter_client_id
TWITTER_CLIENT_SECRET=your_twitter_client_secret
TWITTER_BEARER_TOKEN=your_twitter_bearer_token
TWITTER_BASE_URL=your_twitter_base_endpoint

# Source account (where tweets will be read from)
SOURCE_TWITTER_HANDLE=@source_username

# Destination account (where translated tweets will be posted)
DESTINATION_TWITTER_HANDLE=@destination_username

# OpenAI API
OPENAI_API_KEY=(TO BE IMPLEMENTED)
OPENAI_MODEL=(TO BE IMPLEMENTED)

# Target language for translation (e.g., es-AR for Argentinian Spanish, en-US for American English)
TARGET_LANGUAGE=(TO BE IMPLEMENTED) 

# Check interval for new tweets in minutes (optional, defaults to 5 minutes)
CHECK_INTERVAL_MINUTES=(TO BE IMPLEMENTED)