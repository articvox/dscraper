from comment.comment import Comment
from reaction.reaction import Reaction
from reaction.reactiontype import ReactionType


def count(reaction_type: str, json: dict) -> int:
    try:
        reaction = next(r for r in json.get('reaction', []) if r.get('reaction') == reaction_type)
        return reaction.get('count', 0)
    except (StopIteration, TypeError):
        return 0


def parse_comment_json(json: dict) -> Comment:
    return (Comment(subject=json.get('subject'),
                    content=json.get('content'),
                    comment_id=json.get('id'),
                    created=json.get('created_time_unix'))
            .add_reaction(Reaction(ReactionType.LIKE, count('like', json)))
            .add_reaction(Reaction(ReactionType.DISLIKE, count('dislike', json)))
            .add_reaction(Reaction(ReactionType.LOVE, count('love', json)))
            .add_reaction(Reaction(ReactionType.LAUGH, count('ha-ha', json)))
            .normalize())
