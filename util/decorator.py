from __future__ import annotations

from typing import List


class Decorator:

    def __init__(self, log: str):
        self.prefixes: List[str] = []
        self.log: str = log

    def custom(self, key, value) -> Decorator:
        self.prefixes.append('[{0}: {1}]'.format(key, value))
        return self

    def build(self) -> str:
        return ' '.join(self.prefixes) + ' ' + self.log
