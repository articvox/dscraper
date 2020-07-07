from twitter.service import TwitterService
from twitter.tweet import Tweet


class MockTwitterService(TwitterService):

    def __init__(self):
        super(MockTwitterService, self).__init__()

    def tweet(self, tweet: Tweet) -> None:
        pass

    def delete_all(self) -> None:
        pass
