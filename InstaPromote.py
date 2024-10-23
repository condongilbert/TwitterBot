import os
from dotenv import load_dotenv
from instabot import Bot

# Load environment variables from .env file
load_dotenv()

# Fetch Instagram credentials from environment variables
username = os.getenv('INSTAGRAM_USERNAME')
password = os.getenv('INSTAGRAM_PASSWORD')
# Create a bot instance
bot = Bot()

# Login to your Instagram account
bot.login(username=username, password=password)

# Like posts with specific hashtags
hashtags = ['peptides', 'fitness', 'bodybuilding']
for hashtag in hashtags:
    bot.like_hashtag(hashtag, amount=1)  # Likes 1 posts for each hashtag

# Follow users who posted with a specific hashtag
for hashtag in hashtags:
    users = bot.get_hashtag_users(hashtag)
    bot.follow_users(users[:1])  # Follow 1 users for each hashtag