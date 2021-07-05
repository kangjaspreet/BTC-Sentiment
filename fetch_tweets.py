# import Python modules
import pandas as pd
import tweepy
import time, datetime
import csv

# Twitter OAuth API keys

my_keys = True 
if (my_keys):
    from twitter_keys import *
else:
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = '' 

# Set access for Twitter's API
def set_twitter_access():

    # Tweepy OAuthHandler
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

    return(api)


# Get tweets in the past day with the following keywords:
# 1) Bitcoin/bitcoin/BITCOIN
# 2) BTC/btc/$btc/$BTC

def get_tweets(tweet_count):

    api = set_twitter_access()

    time_current = datetime.datetime.utcnow()
    time_previous = time_current - datetime.timedelta(days = 1)

    time_current = time_current.strftime("%Y-%m-%d")
    time_previous = time_previous.strftime("%Y-%m-%d")

    search_query = f"Bitcoin OR bitcoin OR BITCOIN OR BTC OR btc OR $BTC OR $btc until:{time_current} since:{time_previous} -filter:links AND -filter:replies AND -filter:retweets"

    tweets = api.search(q = search_query, lang = "en", result_type = "mixed", count = tweet_count)

    tweets_dict = {"id": [],
                "user": [],
                "user_follow_count": [],
                "text": [],
                "created_at": [],
                "favorite_count": [],
                "retweet_count": [],
                "link": []}

    for tweet in tweets:
        tweets_dict['id'].append(tweet.id)
        tweets_dict['user'].append(tweet.user.screen_name)
        tweets_dict['user_follow_count'].append(tweet.user.followers_count)
        tweets_dict['text'].append(tweet.text)
        tweets_dict['created_at'].append(tweet.created_at.strftime("%Y-%m-%d %H:%M:%S"))
        tweets_dict['favorite_count'].append(tweet.favorite_count)
        tweets_dict['retweet_count'].append(tweet.retweet_count)
        tweets_dict['link'].append('https://twitter.com/' + tweet.user.screen_name + '/status/' + str(tweet.id))

    return(tweets_dict)


# Call function to get tweets
get_tweets(tweet_count = 10)