
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
keyword='Metro'
geocode='42.959428,-78.813205,4.66mi'
# Requires Authentication as of Twitter API v1.1
twitter = Twython(keys.APP_KEY, keys.APP_SECRET, keys.OAUTH_TOKEN, keys.OAUTH_TOKEN_SECRET)
try:
    search_results = twitter.search(q=keyword, count=100 ,geocode=geocode)
except TwythonError as e:
    print e

count=0
f=open("dataset01.txt","a")
f.write('-------------------'+'for keyword: "'+ keyword +'" ----------------------')
for tweet in search_results['statuses']:

    d1= 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'),tweet['created_at'])
    d2= tweet['text'].encode('utf-8')


    count+=1
    
 
    f.write('\n')
    f.write(d1)
    f.write(d2)
    f.write('\n')
    
    print d1
    print d2

print count
f.write('\n')
f.write("number of tweets found : "+str(count))
f.write('\n')

f.close()
