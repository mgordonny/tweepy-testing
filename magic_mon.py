#!/usr/bin/python3.4

import tweepy
import tw_misc as tw

auth = tw.tw_auth()
twapi = tweepy.API(auth)

magic_mon_query = "MagicMon OR from:MagicMonWords"
results = twapi.search(q=magic_mon_query,lang="en",show_user=True)

for tweet in results:
    tw.print_tweet(tweet)
