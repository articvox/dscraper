from comment.service import get_top_unposted_comments
from twitter.service import TwitterService
from twitter.tweet import Tweet


class DBot:

    def __init__(self, twitter_service: TwitterService):
        self.twitter_service = twitter_service

    def run(self) -> None:
        for comment in get_top_unposted_comments(20):
            reaction = comment.get_top_reaction()

            self.twitter_service.tweet(
                Tweet(comment=comment.content,
                      author=comment.subject,
                      reaction_count=reaction.count,
                      reaction_type_emoji=reaction.get_emoji(),
                      article_url=comment.article_url,
                      comment_id=comment.comment_id))
