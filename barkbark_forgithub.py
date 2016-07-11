#!usr/bin/env python
# -*- coding: utf-8 -*-

# import tweepy, time, sys
import tweepy
#from our keys module (keys.py), import the keys dictionary
from keys import keys

# Enter Keys from Statspup Application
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Parse the Filename
filename=open('statspup_chunks.txt', 'r')
f=filename.readlines()
filename.close()

# Create Loop to Tweet every Hour
for line in f:
    api.update_status(line)
    print line
    time.sleep(3600)
