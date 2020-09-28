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
		time.sleep(100)

# super generous bot to follow somebody back

for follower in limit_handler(tweepy.Cursor(api.followrs).items()):
	if follower.name == 'followers_name' :
		follower.follow()
	
	if follower.followers_count >= 100 :
		follower.follow()




search_str = 'python'

numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_str).items(numbersOfTweets):
	try:
		tweet.favorite()
		print('i liked that tweet')
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break