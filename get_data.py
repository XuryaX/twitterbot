"""
Gathering training data
"""

import csv
import yaml
import twitter

TWITTER_CONFIG_FILE = 'keys.yaml'
print("Loading keys...")
with open(TWITTER_CONFIG_FILE, 'r') as config_file:
    config = yaml.load(config_file, Loader=yaml.BaseLoader)
    # connect to api with apikeys
    # if you don't have apikeys, go to apps.twitter.com
    api = twitter.Api(consumer_key=config['twitter']['consumer_key'],
                      consumer_secret=config['twitter']['consumer_secret'],
                      access_token_key=config['twitter']['access_token_key'],
                      access_token_secret=config['twitter']['access_token_secret'])


def get_user_tweets(twitter_name):
    user = api.UsersLookup(screen_name=[twitter_name])
    user_id = user[0].AsDict()['id']
    tweets = api.GetUserTimeline(user_id=user_id, count=64)
    tweet_list = []
    print(tweets)
    for tweet in tweets:
        text = tweet.AsDict()['text']
        tweet_list.append(text)
    with open(twitter_name+'.csv', 'w') as out:
        for line in tweet_list:
            out.write('<|startoftext|>\n'+line+'\n<|endoftext|>\n')


get_user_tweets('TheTweetOfGod')
