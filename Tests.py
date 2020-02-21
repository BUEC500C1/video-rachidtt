import sys
from twittervideo import *
import unittest

class Tests(unittest.TestCase):
	def test_twitter_clientexists(self):
		user='elonmusk' #exists
		tw1 = TwitterClient()

		###Testing user that exists
		try:
			tw1.twitter_client.get_user(user)
		except Exception:
			self.fail("raised ExceptionType unexpectedly!")

	
	def test_twitter_client_not_exist(self):
		user='elonmusk148415694815269584512847' #does not exist
		tw1 = TwitterClient()

		###Testing user that doesnt eist throws an exception
		self.assertRaises(Exception, tw1.twitter_client.get_user, user)
	