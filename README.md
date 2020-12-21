# Simple Twitter bot - follower

![img.png](doc/img.png)

You can follow the example from the blog post: [blog.jaimedearcos.es/how-to-create-a-twitter-bot](https://blog.jaimedearcos.es/how-to-create-a-twitter-bot/)

## Prerequisites

- Twitter developer account (request in [developer.twitter.com](developer.twitter.com))
- Access tokens (given when create a new app from developer.twitter.com)

## Fill credentials file

Before running the code, you need to replace `credentials/twitter-creds.json` fields with your
access tokens.

```json
{
  "consumer_api_key": "<<CONSUMER_API_KEY>>",
  "consumer_api_secret": "<<CONSUMER_API_SECRET>>",
  "access_token": "<<ACCESS_TOKEN>>",
  "access_token_secret": "<<ACCESS_TOKEN_SECRET>>"
}
```

## Set-up python environment

Create a new python environment & install requirements

```shell script
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Run the script

```
python main.py
```