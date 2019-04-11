from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd
import numpy as np
import re
from auth import TwitterAuth
from stop_words import get_stop_words
from nltk.corpus import stopwords

#Very simple (non-production) Twitter stream example
#1. Download / install python and tweepy (pip install tweepy)
#2. Fill in information in auth.py
#3. Run as: python streaming_simple.py
#4. It will keep running until the user presses ctrl+c to exit
#All output stored to output.json (one tweet  per line)
#Text of tweets also printed as recieved (see note about not doing this in production (final) code

class TweetAnalyzer():
    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    # def analyze_sentiment(self, tweet):
    #     analysis = TexBlob(self.clean_weet(tweet))

    #     if analysis.sentiment.polarity > 0 :
    #         return 1
    #     elif analysis.sentiment.polarity == 0:
    #         return 0
    #     else:
    #         return -1
class StdOutListener(StreamListener):
	# this function for stop word
    stop_word = get_stop_words('indonesia')
    stop = stopwords.words("indonesia")
    
	#This function gets called every time a new tweet is received on the stream
	def on_data(self, data):
		#Just write data to one line in the file
		fhOut.write(data)
		
		#Convert the data to a json object (shouldn't do this in production; might slow down and miss tweets)
		j=json.loads(data)

		#See Twitter reference for what fields are included -- https://dev.twitter.com/docs/platform-objects/tweets
		text=j["text"] #The text of the tweet
		print(text) #Print it out

	def on_error(self, status):
		print("ERROR")
		print(status)

if __name__ == '__main__':
	try:
		#Create a file to store output. "a" means append (add on to previous file)
		fhOut = open("outputJokowi.json","a")

		#Create the listener
		l = StdOutListener()
		auth = OAuthHandler(TwitterAuth.consumer_key, TwitterAuth.consumer_secret)
		auth.set_access_token(TwitterAuth.access_token, TwitterAuth.access_token_secret)

		#Connect to the Twitter stream
		stream = Stream(auth, l)	

		#Terms to track
		stream.filter(track=["jokowi"])
		
		#Alternatively, location box  for geotagged tweets
		#stream.filter(locations=[-0.530, 51.322, 0.231, 51.707])

	except KeyboardInterrupt:
		#User pressed ctrl+c -- get ready to exit the program
		pass

	#Close the 
	fhOut.close()