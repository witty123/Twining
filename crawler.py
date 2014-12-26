import io
import simplejson as json
import twitter

# Go to https://apps.twitter.com/ to create an app and get values for these credentials
CONSUMER_KEY = 'CqTKudxoPPtSo6RNpSJLYc3U6'
CONSUMER_SECRET = '4JDtF5nQVQ2RSJDQNCVpw1GofZPSz9bxg7z3Ch4PHBThNl4S29'
OAUTH_TOKEN = '142971949-14qfwGEQeWnn81wiA7ZkoX74mirJdYkp5AIFcG3E'
OAUTH_TOKEN_SECRET = 'A3bsDs6tWgkzUFP3I6vSAAq2w0Z9dBMvFIObvHb5r1Q0x'

# Authenticate with OAuth
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
CONSUMER_KEY, CONSUMER_SECRET)

# Create a connection to the Twitter Streaming API
twitter_stream = twitter.TwitterStream(auth=auth)
QUERY = 'galaxys5'
OUT_FILE = 'tweets_'+QUERY+'.json'
print 'Filtering the public timeline for "{0}"'.format(QUERY)
stream = twitter_stream.statuses.filter(track=QUERY)

# Write one tweet per line as a JSON document.
with io.open(OUT_FILE, 'a', encoding='utf-8',buffering=1) as f:
    for tweet in stream:
        f.write(unicode(u'{0}\n'.format(json.dumps(tweet, ensure_ascii=False))))
        print tweet['text'] 

