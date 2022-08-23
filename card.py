from card_types import SUIT, FACE
from abc import ABC


class Card(ABC):
    def __init__(self, value, suit):
        self.__value = value
        self.__suit = suit

    @property
    def value(self):
        return self.__value

    @property
    def suit(self):
        return self.__suit

    def __str__(self):
        return f'''Suit={self.__suit},Value={self.__value}'''


class Heart(Card):
    def __init__(self, value):
        self.__suit = SUIT.HEART
        self.__value = value
        super().__init__(value=self.__value, suit=self.__suit)


class Diamond(Card):
    def __init__(self, value):
        self.__suit = SUIT.DIAMOND
        self.__value = value
        super().__init__(value=self.__value, suit=self.__suit)


class Spade(Card):
    def __init__(self, value):
        self.__suit = SUIT.SPADE
        self.__value = value
        super().__init__(value=self.__value, suit=self.__suit)


class Club(Card):
    def __init__(self, value):
        self.__suit = SUIT.CLUB
        self.__value = value
        super().__init__(value=self.__value, suit=self.__suit)


class King(Card):
    def __init__(self, suit):
        self.__suit = suit
        self.__value = FACE.KING
        super().__init__(value=self.__value, suit=self.__suit)


class Queen(Card):
    def __init__(self, suit):
        self.__suit = suit
        self.__value = FACE.QUEEN
        super().__init__(value=self.__value, suit=self.__suit)


class Jack(Card):
    def __init__(self, suit):
        self.__suit = suit
        self.__value = FACE.JACK
        super().__init__(value=self.__value, suit=self.__suit)


class Ace(Card):
    def __init__(self, suit):
        self.__suit = suit
        self.__value = FACE.ACE
        super().__init__(value=self.__value, suit=self.__suit)

