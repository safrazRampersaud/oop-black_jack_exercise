from card import *
import random
from dataclasses import dataclass, field


def _make():
    init_deck = [Card(suite=suite, value=value) for suite in CardDefaults().suites for value in CardDefaults().values]
    random.shuffle(init_deck)
    return init_deck


@dataclass
class Deck:
    deck: List[Card] = field(default_factory=_make)

    def __repr__(self):
        return '|'.join(f'''{c}''' for c in self.deck)
