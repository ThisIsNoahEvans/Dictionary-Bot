###This is the main script for the bot to work###

#Imports Required Libraries
from PyDictionary import PyDictionary
import tweepy
import random
import sys
import time

#Sets Font For Print
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

#Define Dictionary and Connect To Twitter API
dictionary = PyDictionary()
auth = tweepy.OAuthHandler("INSERT YOUR API", "INSERT YOUR API")
auth.set_access_token("INSERT YOUR API", "INSERT YOUR API")
api = tweepy.API(auth)

#Print Program Status
print(colour.BOLD, colour.PURPLE, "Imported Libraries And Connected To The Twitter API", colour.END)

#Starts Tweet Loop
for x in range(1, 370103):
	#Picks Random Word
	with open('words.txt') as list:
		#Scan The File
		lines = list.readlines()
		#Set randomStr As The Generated String
		randomStr = random.choice(lines)
		#Set randomStr As A String And Keeps The Original Value
		randomStr = str(randomStr)
		#Remove Blank Line After The Word
		randomStr = randomStr.replace("\n", "")
		#Save Word To Text File Of Used Words
		usedWrite = open('UsedWords.txt', 'a')
		usedWrite.write(randomStr + '\n')
		print(colour.BOLD, colour.RED, 'Added Used Word To Used List')

	#Checks For Already Used Word
	with open ('UsedWords.txt') as usedRead:
		if randomStr in usedRead:
			print(colour.BOLD, colour.BLUE, 'Word already Tweeted, restarting...')
			print(randomStr)
			#Returns To Start Of Loop
			continue

	#Checks For Blocked Word
	with open('BlockedWords.txt') as blocked:
		if randomStr in blocked:
			print(colour.BOLD, colour.BLUE, 'Blocked word, restarting...', colour.END)
			print(tweet)
			#Returns To Start Of Loop
			continue

	#Print Program Status
	print(colour.BOLD, colour.RED, "Selected Random Word", colour.END)

	#Set Tweet
	original_tweet_text = dictionary.meaning(randomStr)
	#Print Program Status
	print(colour.BOLD, colour.RED, "Got Definition Of The Word", colour.END )
	#Set original_tweet_text As A String And Keeps The Original Value
	original_tweet_text = str(original_tweet_text)
	#Remove Certain Characters
	original_tweet_text = original_tweet_text.replace("]", "")
	original_tweet_text = original_tweet_text.replace("{", "")
	original_tweet_text = original_tweet_text.replace("[", "")
	original_tweet_text = original_tweet_text.replace("]", "")
	original_tweet_text = original_tweet_text.replace("}", "")
	original_tweet_text = original_tweet_text.replace("'", "")
	original_tweet_text = original_tweet_text.replace("(", "")

	#Capitalise First Letter Of Word And Add Some Words:
	#Switch Between 'A' And 'An':
	#Adverb
	if "Adverb" in original_tweet_text:
	    tweet = randomStr.capitalize() + " is an " + original_tweet_text
	else:
	    #Noun
	    if "Noun" in original_tweet_text:
	        tweet = randomStr.capitalize() + " is a " + original_tweet_text
	    else:
	        #Adjective
	        if "Adjective" in original_tweet_text:
	            tweet = randomStr.capitalize() + " is an " + original_tweet_text
	        else:
	            #Verb
	            if "Verb" in original_tweet_text:
	                tweet = randomStr.capitalize() + " is a " + original_tweet_text
	            else:
	                #Infinitive
	                if "Infinitive" in original_tweet_text:
	                    tweet = randomStr.capitalize() + " is an " + original_tweet_text
	                else:
	                    #Everything Else
	                    tweet = randomStr.capitalize() + " is a " + original_tweet_text

	#Exits If No Definition
	if "None" in tweet:
		print(colour.BOLD, colour.BLUE, 'No definition, restarting...', colour.END)
		print(tweet)
		continue

	#Add Full Stop
	tweet = tweet + '.'
	#Truncate Tweet And Add '[..]' If It Is Too Long
	tweet = tweet[:276] + (tweet[276:] and '[..]')
	#Tweet
	api.update_status(tweet)
	#Print Output
	print(colour.BOLD, colour.PURPLE, "\"" + tweet + "\" Was Tweeted!", colour.END)
	print(colour.BOLD, colour.BLUE, 'WAITING 15 MINUTES (900 SECONDS) TO TWEET AGAIN', colour.END)
	time.sleep(870)
