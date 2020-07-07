import logging
import time

import tweepy
from tweepy import TweepError

from history.history import save_sent_id
from util.decorator import Decorator
from twitter.service import TwitterService
from twitter.tweet import Tweet

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''


def decorate(log: str, tweet: Tweet) -> str:
    return (Decorator(log)
            .custom('COMMENT_ID', tweet.comment_id)
            .custom('REACTIONS', tweet.reaction_count)
            .build())


class DefaultTwitterService(TwitterService):

    def __init__(self, truncate_tweets=False):
        self.truncate_tweets = truncate_tweets

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

        self.twitterAPI = tweepy.API(auth)

    def tweet(self, tweet: Tweet) -> None:
        logging.info(decorate('Posting tweet', tweet))

        if tweet.get_length() >= 280 and self.truncate_tweets:
            logging.info(decorate('Truncating tweet, original length: {}'.format(tweet.get_length()), tweet))
            tweet.truncate_comment()
            logging.info(decorate('Truncated length: {}'.format(tweet.get_length()), tweet))

        try:
            self.twitterAPI.update_status(tweet.build())
            logging.info(decorate('Tweet successfully posted', tweet))
        except TweepError as e:
            logging.error(decorate('Tweeting failed: {}'.format(e.reason), tweet))

        save_sent_id(tweet.comment_id)

    def delete_all(self) -> None:
        confirmation_time = 3
        logging.info('Deleting all tweets, cancel in {} seconds:'.format(confirmation_time))

        for remaining in range(confirmation_time, 0, -1):
            logging.info(remaining)
            time.sleep(1)

        for status in tweepy.Cursor(self.twitterAPI.user_timeline).items():
            self.twitterAPI.destroy_status(status.id)

            logging.info(Decorator('Deleted')
                         .custom('STATUS', status.id)
                         .build())
