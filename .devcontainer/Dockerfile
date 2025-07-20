FROM python:3.9-slim

RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y git \
    && apt-get purge -y imagemagick imagemagick-6-common \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


RUN pip install setuptools==69.0.3 \
     gitpython==3.1.41 \
     requests \
     cryptography==42.0.0 \
     python-dotenv \
     ruff \
     tweepy

RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
    && echo "$SNIPPET" >> "/root/.bashrc"