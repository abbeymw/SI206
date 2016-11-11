import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = "2371126310-i4XtP14W7iBatOJGOGHfLp1Z5VkPNrA0ZsxPYIT"
access_token_secret = "zZvu40E7inziNgsHeHNvl8Zw41xT7GCEqlvoIZm3pIKH3"
consumer_key = "3SYhLggn5eOdAWr2zLENgZA7V"
consumer_secret = "4khbWuACbcQr99v2KjvN6LaWnNwtOic7tvnhdhor7dxeOiRWjM"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search('"Gilmore Girls" @netflix')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)


#polarity -- measures how positive or negative
#subjectivity -- measures how factual.

#1 Sentiment Analysis - Understand and Extracting Feelings from Data
