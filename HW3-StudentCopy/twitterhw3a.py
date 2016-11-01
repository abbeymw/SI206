# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.
import tweepy
import sys
import os
# from textblob import TextBlob

access_token = "2371126310-i4XtP14W7iBatOJGOGHfLp1Z5VkPNrA0ZsxPYIT"
access_token_secret = "zZvu40E7inziNgsHeHNvl8Zw41xT7GCEqlvoIZm3pIKH3"
consumer_key = "3SYhLggn5eOdAWr2zLENgZA7V"
consumer_secret = "4khbWuACbcQr99v2KjvN6LaWnNwtOic7tvnhdhor7dxeOiRWjM"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

api.update_with_media('bananadolphin.jpg', status="#UMSI-206 #Proj3")



print("""No output necessary although you 
	can print out a success/failure message if you want to.""")