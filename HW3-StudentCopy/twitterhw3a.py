# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.
import tweepy


access_token = "YOUR ACCESS CODE HERE"
access_token_secret = "YOUR ACCESS CODE HERE"
consumer_key = "YOUR ACCESS CODE HERE"
consumer_secret = "YOUR ACCESS CODE HERE"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)		#basic lines of code to access twitter
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)		#authorizes you to tweet

api.update_with_media('bananadolphin.jpg', status="#UMSI-206 #Proj3") 	#send a tweet to the authorized account



print("""No output necessary although you 
	can print out a success/failure message if you want to.""")