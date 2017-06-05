#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint as pp
import keys
from twython import Twython, TwythonError

""" the keywords paria provided
Transit
Public transportation
NFTA 
Bus stop
Metro station
and long and lat:
Coordinates: 42.959428, -78.813205
Radius: 7.5 km =4.66028mi
"""
tehran=u"تهران"
shahrdari=u"شهرداری"
scenario=u"سناریو"
barnameh=u"برنامه"
keyword=[tehran,barnameh,shahrdari ]
geocode='42.959428,-78.813205,4.66mi'
# Requires Authentication as of Twitter API v1.1
twitter = Twython(keys.APP_KEY, keys.APP_SECRET, keys.OAUTH_TOKEN, keys.OAUTH_TOKEN_SECRET)

def write_unicode(text, charset='utf-8'):
    return text.encode(charset)


try:
    #search_results = twitter.search(q=keyword, count='200', lang='fa')
    search_results = twitter.search(q=keyword, count='400')
except TwythonError as e:
    print e

count=0
f=open("tehrandataset01.txt","a")

for tweet in search_results['statuses']:
    #print type(tweet)
    #print type(tweet)
    #print isinstance(tweet, str)
    d1= 'Tweet from @ %s Date: %s' % (tweet[u'user'][u'screen_name'].encode('utf-8'), tweet[u'created_at'].encode('utf-8'))
    d2= tweet[u'text']


    count+=1
    
 
    f.write('\n')
    f.write(write_unicode(d1))
    f.write(write_unicode(d2))
    f.write('\n')
    
    print d1
    print d2

print count
f.write('\n')
f.write("number of tweets found : "+str(count))
f.write('\n')

f.close()
