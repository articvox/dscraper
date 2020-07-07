from __future__ import annotations

from datetime import datetime
from typing import List

from reaction.reaction import Reaction


class Comment:

    def __init__(self,
                 comment_id: int = None,
                 created: datetime = None,
                 subject: str = None,
                 content: str = None,
                 author: str = None,
                 article: str = None,
                 article_url: str = None):
        self.comment_id = comment_id
        self.created = created
        self.subject = subject
        self.content = content
        self.author = author

        self.article = article
        self.article_url = article_url

        self.reactions = []

    def __eq__(self, other):
        if not isinstance(other, Comment):
            return NotImplemented

        return self.content == other.content

    def add_reaction(self, reaction: Reaction) -> Comment:
        self.reactions.append(reaction)
        return self

    def get_top_reaction(self) -> Reaction:
        return max(self.reactions, key=lambda reaction: reaction.count)

    def normalize(self) -> Comment:
        if self.subject:
            self.subject = self.subject.strip()
        if self.content:
            self.content = self.content.strip()
        return self
