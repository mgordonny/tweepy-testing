#!/usr/bin/python3.4

import tweepy

def tw_auth():
    consumer_key = "FA5pFmsnBf6kwortV7wFyJHM4"
    consumer_secret = "kaUiVpOkfbJge2klt1d0QgwNwWKEtA0hxoMqLeyNYFuc6ISyyK"
    access_token = "185197071-ow66tAsS2xsQzJ0pyOsat4FLrbhYZWmCrFserkbv"
    access_token_secret = "957UdGIZepEoMcHouL8Rj9nNwzDHntAbVjQxolkqSpAuY"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return auth
    
def print_tweet(twobj,user=True,ctime=True,tid=True):
    green = "\033[1;32m"
    red = "\033[1;31m"
    white = "\033[1;39m"
    end = "\033[0m"
    tstr = ""
    if user:
        tstr += green+str(twobj.user.screen_name) + end + " " 
    if ctime:
        tstr += str(twobj.created_at) 
    tstr += "\n" + white + twobj.text + end + "\n"
    if tid:
        tstr += twobj.id_str + "\n"
    print(tstr)



