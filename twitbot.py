import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# to print tweets from the page
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)


user=api.me()
print(user.name)
print(user.screen_name)
print(user.followers_count)


def limit_handler(cursor):
	try:
		while True:
			yield cursor.next()	
	except tweepy.RateLimitError:
		time.sleep(1000)

# super generous bot

for follower in limit_handler(tweepy.Cursor(api.followrs).items()):
	print(followers.name)
