from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import mysql.connector
from mysql.connector import errorcode
import time
import json



# replace mysql.server with "localhost" 
# if you are running via your own server!
# server       MySQL username	MySQL pass  Database name.

cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='sentimenanalisispilpres',
                              charset = 'utf8mb4')
cursor=cnx.cursor()

#consumer key, consumer secret, 
#access token, access secret.
ckey="tj9E6a677gjmuzpQHbzvGtfu1"
csecret="a2Vag5JDMmP3zaDM9QstarIbFXerHsb6LhM55MTv354yC7Nd1i"
atoken="1081116821263048704-kYWCnSij3X76WFkPhWkCoZFryT40og"
asecret="eRlw7DNcIv1SYD5t3KaNwKprmQXEiQK8xAfKK1ITzJL6H"


class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        try:
            # check to ensure there is text in 
            # the json data
            if 'text' in all_data:
              tweet = all_data["text"]
              time = all_data["created_at"]
              username = all_data["user"]["screen_name"]
          
              cursor.execute(
                "INSERT INTO second (time, username, tweet) VALUES (%s,%s,%s)",
                (time, username, tweet))
          
              cnx.commit()
          
              print("Collecting Data to Database...")
              print("Pres CTRL+C to stop !")
          
              return True
            else:
              return True
        except KeyboardInterrupt:
		#User pressed ctrl+c -- get ready to exit the program
            pass

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["prabowo", "sandiaga uno"],
                     languages=["in"])
