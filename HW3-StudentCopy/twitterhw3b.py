# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.
import tweepy
from textblob import TextBlob

access_token = "2371126310-i4XtP14W7iBatOJGOGHfLp1Z5VkPNrA0ZsxPYIT"
access_token_secret = "zZvu40E7inziNgsHeHNvl8Zw41xT7GCEqlvoIZm3pIKH3"
consumer_key = "3SYhLggn5eOdAWr2zLENgZA7V"
consumer_secret = "4khbWuACbcQr99v2KjvN6LaWnNwtOic7tvnhdhor7dxeOiRWjM"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Banana Dolphin')
num_twts = 0
twt_pol = 0
twt_sub = 0
for tweet in public_tweets:
	num_tweets += 1
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	# print(analysis.sentiment)
	twt_pol += analysis.sentiment[0]
	twt_sub += analysis.sentiment[1]

print('Number of tweets for search:' + str(num_twts))
print("Average subjectivity is: " + str(twt_sub/num_twts))
print("Average polarity is: " + str(twt_pol/num_twts))
