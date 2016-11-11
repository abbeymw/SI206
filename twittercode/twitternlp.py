import tweepy
import nltk

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

public_tweets = api.search('UMSI')


adj_count = 0;

for tweet in public_tweets:
	print(tweet.text)
	tagged_tokens = nltk.pos_tag(tweet.text) # gives us a tagged list of tuples
	for (word, tag) in tagged_tokens:
		if tag == "JJ":
			adj_count+=1

print("There were ", adj_count,"adjectives in your tweets")
	
#Learn more about Search
#https://dev.twitter.com/rest/public/search

