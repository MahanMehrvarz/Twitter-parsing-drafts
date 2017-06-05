#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import time
import csv

import twython
import json
import keys as keys
#app_key = ""
#app_secret = ""
#oauth_token = ""
#oauth_token_secret = ""

twitter = twython.Twython(keys.APP_KEY, keys.APP_SECRET, keys.OAUTH_TOKEN, keys.OAUTH_TOKEN_SECRET)
print keys.APP_KEY
tweets = []
MAX_ATTEMPTS = 1000000
# Max Number of tweets per 15 minutes
COUNT_OF_TWEETS_TO_BE_FETCHED = 18000

for i in range(0,MAX_ATTEMPTS):

    if(COUNT_OF_TWEETS_TO_BE_FETCHED < len(tweets)):
        break

    if(0 == i):
        results = twitter.search(q="$AAPL",count='100',lang='en',)

    else:
        results = twitter.search(q="$AAPL",include_entities='true',max_id=next_max_id)

    for result in results['statuses']:
        print result

        with open('tweets.txt', 'a') as outfile:
             json.dump(result, outfile, sort_keys = True, indent = 4)

    try:
        next_results_url_params = results['search_metadata']['next_results']
        next_max_id = next_results_url_params.split('max_id=')[1].split('&')[0]
    except:

        break