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


class Values(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 10
    QUEEN = 10
    KING = 10
    ACE11 = 11


@dataclass(frozen=True)
class Card:
    value: int
    suite: str

    def __repr__(self):
        return f'''[{self.value}:{self.suite}]'''


def _suites():
    return [Suites.HEART, Suites.SPADE, Suites.DIAMOND, Suites.CLUB]


def _values():
    return [
        Values.ACE, Values.TWO, Values.THREE,
        Values.FOUR, Values.FIVE, Values.SIX,
        Values.SEVEN, Values.EIGHT, Values.NINE,
        Values.TEN, Values.JACK, Values.QUEEN,
        Values.KING
    ]


@dataclass(frozen=True)
class CardDefaults:
    suites: List[str] = field(default_factory=_suites)
    values: List[int] = field(default_factory=_values)

