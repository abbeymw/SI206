# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.
import tweepy
from textblob import TextBlob

access_token = "YOUR ACCESS CODE HERE"
access_token_secret = "YOUR ACCESS CODE HERE"
consumer_key = "YOUR ACCESS CODE HERE"
consumer_secret = "YOUR ACCESS CODE HERE"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)	#basic lines of code to access twitter
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)	

public_tweets = api.search('Banana Dolphin')	#searches for tweets about "Banana Dolphin"
num_twts = 0 	#initializes num_twts
twt_pol = 0		#initializes twt_pol
twt_sub = 0		#initializes twt_sub
for tweet in public_tweets:		#for each tweet in the list of tweets returned from search for "Banana Dolphin"
	num_twts += 1		#increment number of tweets by 1
	print(tweet.text)	
	analysis = TextBlob(tweet.text)		#analyze the tweet
	# print(analysis.sentiment)
	twt_pol += analysis.sentiment[0]		#index into the tuple to increment twt_pol by the polarity of the tweet
	twt_sub += analysis.sentiment[1]		#index into the tuple to increment twt_sub by the subjectivity of the tweet

print('Number of tweets for search:' + str(num_twts))	
print("Average subjectivity is: " + str(twt_sub/num_twts)) 	#print the average subjectivity of the tweets
print("Average polarity is: " + str(twt_pol/num_twts))		#print the average polarity of the tweets
