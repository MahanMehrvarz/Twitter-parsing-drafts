
from keys import *
from twython import Twython, TwythonError
import requests
requests.packages.urllib3.disable_warnings()
# Requires Authentication as of Twitter API v1.1
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
try:
    search_results = twitter.search(q='NFTA', count=50)
except TwythonError as e:
    print e

for tweet in search_results['statuses']:
    print 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'),tweet['created_at'])
    print tweet['text'].encode('utf-8'), '\n'
