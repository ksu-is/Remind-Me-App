https://github.-com/bear/python-twitter
#Requirement - pip install python-twitter






import sys.twitter
api = twitter.Api()

#Populate your twitter API details below
consumer_key = ''
consumer_secret = ''
access_token_key = ''
access_token_secret = ''

api = twitter.Api(consumer_key=consumer_key,consumer_secret=consumer_secret,access_token_key=access_token_key,access_token_secret=access_token_secret)


def user_tweet(luvtoriaa):
	statuses = api.GetUserTimeline(screen_name=luvtoriaa)
	return statuses[0].text
	
if _name_ == "_main_":
	latest_tweet = user_tweet(sys.argv[1])
	print(latest_tweet)
