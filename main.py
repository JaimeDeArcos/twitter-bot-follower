import tweepy, time

import json, re
from pathlib import Path

CREDENTIALS_PATH = 'credentials/twitter-creds.json'
config = json.loads(Path(CREDENTIALS_PATH).read_text())

# Authentication
auth = tweepy.OAuthHandler(config['consumer_api_key'], config['consumer_api_secret'])
auth.set_access_token(config['access_token'], config['access_token_secret'])
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Verify authentication
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

while True:
    # Retrieve followers
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            print("New Follower -> {}".format(follower.name))
            follower.follow()
    # Sleep for 2 minutes
    time.sleep(120)