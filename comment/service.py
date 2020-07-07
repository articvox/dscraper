import logging
from typing import List

import requests

from article.article import Article
from article.service import get_articles
from comment.comment import Comment
from comment.parser import parse_comment_json
from history.history import get_sent_comment_ids
from util.dict import deep_get
from util.list import difference, flatten

COMMENTS_BY_CONFIG = 'http://api.delfi.ee/comment/v1/query/getCommentsByConfig'
COMMENTS_JSON_PATH = 'data.getCommentsByConfig.articleEntity.comments'


def query_params(article_id) -> dict:
    return {
        'articleId': article_id,
        'channelId': '1',
        'modeType': 'ANONYMOUS_MAIN',
        'orderBy': 'DATE_ASC',
        'orderByReplies': 'DATE_ASC',
        'limitReplies': '10'
    }


def get_comments(article_id: str) -> List[Comment]:
    response = requests.get(COMMENTS_BY_CONFIG, params=query_params(article_id))
    return [parse_comment_json(c) for c in deep_get(response.json(), COMMENTS_JSON_PATH) or []]


def filter_unposted(comments: List[Comment]) -> List[Comment]:
    unposted_ids = difference(map(lambda c: c.comment_id, comments), get_sent_comment_ids())
    return [*filter(lambda c: c.comment_id in unposted_ids, comments)]


def filter_top(count: int, comments: List[Comment]) -> List[Comment]:
    comments.sort(key=lambda comment: comment.get_top_reaction().count, reverse=True)
    return comments[:count]


def supplement(comment: Comment, article: Article) -> Comment:
    comment.article = article.title
    comment.article_url = article.url
    return comment


def get_top_unposted_comments(count: int = 10) -> List[Comment]:
    comments = flatten([[supplement(comment, article) for comment in get_comments(article.article_id)]
                        for article in get_articles()])

    logging.info('Found {} total comments'.format(len(comments)))

    comments = filter_top(count, comments)
    logging.info('Selected top {} reacted comments'.format(count))

    comments = filter_unposted(comments)
    logging.info('Unposted count: {}'.format(len(comments)))
    return comments[:count]
