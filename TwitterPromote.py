import os
from dotenv import load_dotenv
import tweepy

# Load environment variables from .env file
load_dotenv("TwitterInfo.env")

# Retrieve Twitter API credentials
api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_secret = os.getenv("TWITTER_ACCESS_SECRET")

print("API Key:", api_key)
print("API Secret:", api_secret)
print("Access Token:", access_token)
print("Access Secret:", access_secret)
# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)

# Function to fetch and engage with tweets from the home timeline
def post_tweet(message):
    try:
        api.update_status(message)  # This line posts the tweet
        print("Tweet posted successfully!")
    except tweepy.TweepyException as e:
        print("Error posting tweet:", e)
if __name__ == "__main__":
    tweet_message = "Hello, Twitter! Dont forget to check out the deals over at peptidepro.co"
    post_tweet(tweet_message)