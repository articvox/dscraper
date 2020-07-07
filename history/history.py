import logging
import os
import pickle
from typing import List

from comment.comment import Comment
from util.decorator import Decorator

SENT_COMMENT_IDS = os.path.join(os.path.dirname(__file__), 'comment_ids.pkl')


def save_sent_id(comment_id: int) -> None:
    sent_comment_ids = get_sent_comment_ids()
    sent_comment_ids.append(comment_id)

    with open(SENT_COMMENT_IDS, 'wb') as o:
        pickle.dump(sent_comment_ids, o, pickle.HIGHEST_PROTOCOL)

    logging.info(Decorator('Saved to post history')
                 .custom('COMMENT_ID', comment_id)
                 .build())


def save_all_ids(comments: List[Comment]) -> None:
    with open(SENT_COMMENT_IDS, 'wb') as o:
        pickle.dump([*get_sent_comment_ids(), *comments], o, pickle.HIGHEST_PROTOCOL)


def delete_all_history() -> None:
    with open(SENT_COMMENT_IDS, 'wb') as o:
        pickle.dump([], o, pickle.HIGHEST_PROTOCOL)


def get_sent_comment_ids() -> List[int]:
    try:
        with open(SENT_COMMENT_IDS, 'rb') as i:
            return pickle.load(i)
    except (FileNotFoundError, EOFError):
        return []
