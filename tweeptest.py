#!/usr/bin/python3.4

import tweepy

def print_tweet(twobj,user=True,ctime=True):
    tstr = ""
    if user:
        tstr += str(twobj.user.screen_name) + "\n"
    tstr += twobj.text+"\n"
    if ctime:
        tstr += str(twobj.created_at) + "\n"
    print(tstr)

consumer_key = "FA5pFmsnBf6kwortV7wFyJHM4"
consumer_secret = "kaUiVpOkfbJge2klt1d0QgwNwWKEtA0hxoMqLeyNYFuc6ISyyK"
access_token = "185197071-ow66tAsS2xsQzJ0pyOsat4FLrbhYZWmCrFserkbv"
access_token_secret = "957UdGIZepEoMcHouL8Rj9nNwzDHntAbVjQxolkqSpAuY"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twapi = tweepy.API(auth)

public_tweets = twapi.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)

magic_mon_query = "MagicMon OR from:MagicMonWords"
results = twapi.search(q=magic_mon_query,lang="en",show_user=True)
for tweet in results:
    print_tweet(tweet)

#magic_mon_search = api.create_saved_search("MagicMon OR from:MagicMonWords AND lang:en")
#api.get_saved_search(magic_mon_search)

#try:
#    redirect_url = auth.get_authorization_url()
#except tweepy.TweepError:
#    print('Error! Failed to get request token.')
#    print('\n')
