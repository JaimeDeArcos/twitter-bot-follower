import tweepy, time

# Authentication
auth = tweepy.OAuthHandler("CONSUMER_API_KEY", "CONSUMER_API_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
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