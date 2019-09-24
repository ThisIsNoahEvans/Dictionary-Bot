###This is used to simply Tweet using the APIs: essentially a custom client###

#Imports Tweepy
import tweepy

#Authenticates Tweepy
auth = tweepy.OAuthHandler("INSERT YOUR API", "INSERT YOUR API")
auth.set_access_token("INSERT YOUR API", "INSERT YOUR API")
api = tweepy.API(auth)

#Gets Tweet To Send
print('Ready To Tweet')
tweet = input('Enter Tweet ')

#Tweets Input
api.update_status(tweet)
print('Tweeted!')
