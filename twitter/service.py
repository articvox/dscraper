from abc import ABC, abstractmethod

from twitter.tweet import Tweet


class TwitterService(ABC):

    @abstractmethod
    def tweet(self, tweet: Tweet) -> None:
        pass

    @abstractmethod
    def delete_all(self) -> None:
        pass
