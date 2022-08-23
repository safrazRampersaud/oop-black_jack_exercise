from card import *
import random


class Deck:
    def __init__(self):
        self.__is_deck_new = True
        self.__is_deck_mod = False
        self.__init_deck = self.initialize()
        self.__deck = self.__init_deck

    def initialize(self):
        if self.__is_deck_new:
            hearts = [Heart(i) for i in range(2, 11)]
            clubs = [Club(i) for i in range(2, 11)]
            spades = [Spade(i) for i in range(2, 11)]
            diamonds = [Diamond(i) for i in range(2, 11)]

            kings = [
                King(SUIT.CLUB),
                King(SUIT.HEART),
                King(SUIT.SPADE),
                King(SUIT.DIAMOND),
            ]

            queens = [
                Queen(SUIT.CLUB),
                Queen(SUIT.HEART),
                Queen(SUIT.SPADE),
                Queen(SUIT.DIAMOND),
            ]

            jacks = [
                Jack(SUIT.CLUB),
                Jack(SUIT.HEART),
                Jack(SUIT.SPADE),
                Jack(SUIT.DIAMOND),
            ]

            aces = [
                Ace(SUIT.CLUB),
                Ace(SUIT.HEART),
                Ace(SUIT.SPADE),
                Ace(SUIT.DIAMOND),
            ]

            deck = sum([
                diamonds,
                spades,
                clubs,
                hearts,
                aces,
                kings,
                queens,
                jacks
            ], [])

            random.shuffle(deck)

            return deck

    def print_deck(self):
        for i in self.__init_deck:
            print(i)

    def shuffle(self):
        if self.__is_deck_new:
            random.shuffle(self.__init_deck)
        if self.__is_deck_mod:
            random.shuffle(self.__deck)

    @property
    def deck(self):
        return self.__deck

    @property
    def count(self):
        return len(self.__deck)
