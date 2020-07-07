from reaction.reactiontype import ReactionType

EMOJI_MAP = {
    'LIKE': '👍',
    'DISLIKE': '👎',
    'LOVE': '❤️',
    'LAUGH': '😂'
}


class Reaction:

    def __init__(self, reaction_type: ReactionType, count: int):
        self.reaction_type = reaction_type
        self.count = count

    def get_emoji(self):
        return EMOJI_MAP.get(ReactionType(self.reaction_type).name)
