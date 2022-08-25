from dataclasses import dataclass, field
from typing import List
from enum import Enum, auto


class Suites(Enum):
    """Suites.CLUB.value='♣'"""
    CLUB = chr(9827)
    """Suites.DIAMOND.value='♢'"""
    DIAMOND = chr(9830)
    """Suites.HEART.value='♡'"""
    HEART = chr(9829)
    """Suites.SPADE.value='♠'"""
    SPADE = chr(9824)


@dataclass(frozen=True)
class Card:
    value: str
    suite: str

    def __repr__(self):
        return f'''[{self.value}:{self.suite}]'''


def _suites():
    return [Suites.HEART, Suites.SPADE, Suites.DIAMOND, Suites.CLUB]


def _values():
    return '2 3 4 5 6 7 8 9 10 J Q K A'.split()


@dataclass(frozen=True)
class CardDefaults:
    suites: List[str] = field(default_factory=_suites)
    values: List[str] = field(default_factory=_values)

