import tweepy
import time

# Set up your credentials
API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
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