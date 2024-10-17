from instabot import Bot

# Create a bot instance
bot = Bot()

# Login to your Instagram account
bot.login(username='your_username', password='your_password')

# Like posts with specific hashtags
hashtags = ['peptides', 'fitness', 'bodybuilding']
for hashtag in hashtags:
    bot.like_hashtag(hashtag, amount=10)  # Likes 10 posts for each hashtag

# Follow users who posted with a specific hashtag
for hashtag in hashtags:
    users = bot.get_hashtag_users(hashtag)
    bot.follow_users(users[:10])  # Follow 10 users for each hashtag