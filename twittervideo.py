import keys
import tweepy
import json
from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from io import open
from collections import Counter



class JsonTweet():
	def __init__(self,tweet):
		self.user = tweet['user']['name']
		self.date = tweet['created_at']
		self.daystr = (self.date).split()[:3] #first three words for just mmddyy
		self.day = ' '.join(self.daystr) #cat the 3 string into one
		
		
		if not 'retweeted_status' in tweet:
			self.text = tweet['full_text']
			self.rt = False
			self.favct = tweet['favorite_count']
			self.rtct = tweet['retweet_count']
		else:
			self.text = tweet['retweeted_status']['full_text']
			#self.rt = tweet['retweeted_status']['user']['retweeted']
			#self.favct = tweet['retweeted_status']['user']['favorite_count']
			#self.rtct = tweet['retweeted_status']['user']['retweet_count']
	
	def separateByDay(JsonTweet,len):
		pass





class TwitterClient():
	def __init__(self,user=None): #None goes to own timeline
		self.auth=Authenticator().authenticate()
		self.twitter_client=API(self.auth)
		self.twitter_user=user

	def get_user_timeline_tweets(self,amount):
		tweets=[]
		for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user,tweet_mode='extended').items(amount):
			tweets.append(tweet)		
				
			try:	
				with open('tweets.json', 'a', encoding='utf8') as file:
					json.dump(tweet._json, file)
					file.write('\n')
			except BaseException as e:
				print("Error on_data: %s" %str(e))

		return tweets





class Authenticator():
	def authenticate(self):
		auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_KEY_SECRET)
		auth.set_access_token(keys.ACCESS_TOKEN,keys.ACCESS_TOKEN_SECRET)
		return auth
'''
class TwitterStreamer():

	def __init__(self):
		self.autenticator= Authenticator()
	def stream_tweets(self,filename,tag_list):
		auth=self.autenticator.authenticate()
		listener = TwitterListener(filename)
		stream =Stream(auth,listener)
		stream.filter(track=tag_list)


class TwitterListener(StreamListener):

	def __init__(self,filename):
		self.filename=filename

	def on_data(self, data):

		try:
			print(data)##
			with open(self.filename,'a') as f:
				f.write(data)
		except BaseException as e:
			print("Error on_data: %s" %str(e))

		return True

	def on_error(self,status):
		if status == 420: #high volume
			return False

		print(status)

'''
if(__name__ == "__main__"):

	#fetchlist = ["elon","Nasa"]
	filename="data.json"
	user="elonmusk"  #Enter the @ of wanted user
	num = 10 #Number of tweets to fetch
	jsonwtlist = [] #list of Jsontwt objects
	daylist = []

	twitter_client=TwitterClient(user)
	data = twitter_client.get_user_timeline_tweets(num)


	for i in range(len(data)):
		try:	
				with open('data.json', 'a', encoding='utf8') as file:#write each tweet to file
					json.dump(data[i]._json, file)
					file.write('\n')
		except BaseException as e:
			print("Error on_data: %s" %str(e))

		jsonwtlist.append(JsonTweet(data[i]._json))#put each into JsonTweet Object
		daylist.append(jsonwtlist[i].daystr[2])

	numvids = len(Counter(daylist).keys()) #number of different days of tweets = number of videos

	