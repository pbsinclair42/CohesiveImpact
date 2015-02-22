'''from birdy.twitter import UserClient'''
import tweepy
from keys import keys
from name_gen import startup_words
from nameGenerator import wordGenerator

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print 'Error! Failed to get request token.'

auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
api.update_status(status=wordGenerator()+': '+startup_words())