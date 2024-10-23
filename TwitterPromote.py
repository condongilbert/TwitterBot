import tweepy
import time
from dotenv import load_dotenv
import os

load_dotenv()

# Set up your credentials
api_key = os.getenv('TWITTER_API_KEY')
api_secret = os.getenv('TWITTER_API_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_secret = os.getenv('TWITTER_ACCESS_SECRET')

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)

# Define keywords for searching tweets
keywords = ['peptides', '#Peptides', '#Health', '#Supplements']

def engage_with_peptide_posts():
    for keyword in keywords:
        print(f"Searching for tweets about: {keyword}")
        for tweet in tweepy.Cursor(api.search_tweets, q=keyword, lang='en').items(10):  # Change number for more tweets
            try:
                print(f"Liking tweet from @{tweet.user.screen_name}: {tweet.text}")
                tweet.favorite()  # Like the tweet
                time.sleep(10)  # Sleep to avoid hitting rate limits
            except tweepy.TweepError as e:
                print(e)
            except StopIteration:
                break

if __name__ == "__main__":
    engage_with_peptide_posts()