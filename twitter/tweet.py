FULL_STOP = '. '


class Tweet:

    def __init__(self,
                 comment: str = None,
                 author: str = None,
                 reaction_count: int = None,
                 reaction_type_emoji: str = None,
                 article_url: str = None,
                 comment_id: int = None):
        self.comment = comment
        self.author = author
        self.reaction_count = reaction_count
        self.reaction_type_emoji = reaction_type_emoji
        self.article_url = article_url
        self.comment_id = comment_id

    def build(self) -> str:
        return '📨 {0} ({1} {2}) \n«{3}»\n {4}'.format(
            self.author,
            self.reaction_type_emoji,
            self.reaction_count,
            self.comment,
            self.article_url)

    def get_length(self):
        return len(' {0} ( {1}) \n«{2}»\n '.format(
            self.author,
            self.reaction_count,
            self.comment)) + 4 + 23

    def get_length_wo_message(self):
        return self.get_length() - len(self.comment)

    def truncate_comment(self):
        comment_at_max_length = self.comment[:277 - self.get_length_wo_message()]
        self.comment = comment_at_max_length[0:comment_at_max_length.rfind(FULL_STOP)]

        self.comment = self.comment[:277 - self.get_length_wo_message()].strip() + '...'
