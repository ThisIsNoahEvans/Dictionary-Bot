###This is the main script for the bot to work###

#Repeats For Every Word In words.txt
for x in range(1, 370103):
	#Imports Required Libraries
	from PyDictionary import PyDictionary
	import tweepy
	import random
	import sys
	import time

	#Sets Font For Print Statements
	class colour:
		PURPLE = '\033[95m'
		CYAN = '\033[96m'
		DARKCYAN = '\033[36m'
		BLUE = '\033[94m'
		GREEN = '\033[92m'
		YELLOW = '\033[93m'
		RED = '\033[91m'
		BOLD = '\033[1m'
		UNDERLINE = '\033[4m'
		END = '\033[0m'

	#Defines Dictionary And Connects To Twitter API
	dictionary = PyDictionary()
	auth = tweepy.OAuthHandler("INSERT YOUR API", "INSERT  YOUR API")
	auth.set_access_token("INSERT YOUR API", "INSERT YOUR API")
	api = tweepy.API(auth)

	#Picks Random Word
	with open('words.txt') as list:
	        #Scans The File
	        lines = list.readlines()
	        #Sets randomStr As The Generated String
	        randomStr = random.choice(lines)
	        #Sets randomStr As A String And Keeps The Original Value
	        randomStr = str(randomStr)
	        #Removes Blank Line After The Word
	        randomStr = randomStr.replace("\n", "")

	#Prints Program Status
	print(colour.BOLD, "Imported Libraries And Connected To The Twitter API", colour.END)
	print(colour.BOLD, "Selected Random Word", colour.END)

	#Sets Tweet
	original_tweet_text = dictionary.meaning(randomStr)
	#Prints Program Status
	print(colour.BOLD, "Got Definition Of The Word", colour.END )
	#Sets original_tweet_text As A String And Keeps The Original Value
	original_tweet_text = str(original_tweet_text)
	#Removes Certain Characters
	original_tweet_text = original_tweet_text.replace("]}", "")
	original_tweet_text = original_tweet_text.replace("{", "")
	original_tweet_text = original_tweet_text.replace("[", "")
	original_tweet_text = original_tweet_text.replace("'", "")
	original_tweet_text = original_tweet_text.replace("(", "")

	#Capitalises First Letter Of Word And Add Some Words
	#Switch Between 'A' And 'An'
	##Adverb
	if "Adverb" in original_tweet_text:
	    tweet = randomStr.capitalize() + " is an " + original_tweet_text
	else:
	    ##Noun
	    if "Noun" in original_tweet_text:
	        tweet = randomStr.capitalize() + " is a " + original_tweet_text
	    else:
	        #A#djective
	        if "Adjective" in original_tweet_text:
	            tweet = randomStr.capitalize() + " is an " + original_tweet_text
	        else:
	            ##Verb
	            if "Verb" in original_tweet_text:
	                tweet = randomStr.capitalize() + " is a " + original_tweet_text
	            else:
	                ##Infinitive
	                if "Infinitive" in original_tweet_text:
	                    tweet = randomStr.capitalize() + " is an " + original_tweet_text
	                else:
	                    ##Everything Else
	                    tweet = randomStr.capitalize() + " is a " + original_tweet_text

	#Restarts If No Definition
	if "None" in tweet:
		print(colour.BOLD, 'No definition; exitting...', colour.END)
		print(tweet)
		#Returns To Start Of Loop
		continue

	#Adds Full Stop
	tweet = tweet + '.'
	#Truncates Tweet And Adds'[..]' If Tweet Exceeds Twitter Limit
	tweet = tweet[:276] + (tweet[276:] and '[..]')
	#Tweets
	api.update_status(tweet)
	#Prints Output
	print(colour.BOLD, "\"" + tweet + "\" Was Tweeted!", colour.END)
	print(colour.BOLD, 'WAITING 15 MINUTES (900 SECONDS) TO TWEET AGAIN', colour.END)
	#Pauses for 15 minutes
	time.sleep(900)
