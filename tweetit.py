import os
import twitter

TWITTER_CONSUMER_KEY= os.environ["TWITTER_CONSUMER_KEY"]
TWITTER_CONSUMER_KEY_SECRET = os.environ["TWITTER_CONSUMER_KEY_SECRET"]
TWITTER_ACCESS_TOKEN = os.environ["TWITTER_ACCESS_TOKEN"]
TWITTER_ACCESS_TOKEN_SECRET = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

api = twitter.Api(consumer_key=TWITTER_CONSUMER_KEY,
                      consumer_secret=TWITTER_CONSUMER_KEY_SECRET,
                      access_token_key=TWITTER_ACCESS_TOKEN,
                      access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

def tweet_markov(tweet_string):
    status = api.PostUpdate(tweet_string)
