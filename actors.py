from abc import ABC, abstractmethod
from deck import *
import numpy as np


class Actor(ABC):
    def __init__(self):
        self.__active = False
        self.__id = 0
        self.__hand = []
        self.__score = 0

    @property
    @abstractmethod
    def hand(self):
        pass

    @property
    @abstractmethod
    def active(self):
        pass

    @property
    @abstractmethod
    def stand(self):
        pass

    @property
    @abstractmethod
    def hit(self):
        pass

    @property
    @abstractmethod
    def score(self):
        pass

    @property
    @abstractmethod
    def profile(self):
        pass


class Dealer(Actor):
    def __init__(self):
        self.__active = False
        self.__id = 0
        self.__hand = []
        self.__score = 0
        super().__init__()

    @property
    def id(self):
        return self.__id

    @property
    def hand(self):
        return self.__hand

    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, active):
        self.__active = active

    @property
    def stand(self):
        return True if np.random.rand() > .50 else False

    @property
    def hit(self):
        return False if self.stand else True

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    @property
    def profile(self):
        inventory = [str(self.id)]
        for card in self.hand:
            inventory.append(str(card))
        inventory.append(str(self.score))
        return inventory


class Player(Actor):
    def __init__(self, id=None):
        super().__init__()
        self.__active = False
        self.__id = id
        self.__hand = []
        self.__score = 0

    @property
    def id(self):
        return self.__id

    @property
    def hand(self):
        return self.__hand

    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, active):
        self.__active = active

    @property
    def stand(self):
        return True if np.random.rand() > .50 else False

    @property
    def hit(self):
        return False if self.stand else True

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    @property
    def profile(self):
        inventory = [str(self.id)]
        for card in self.hand:
            inventory.append(str(card))
        inventory.append(str(self.score))
        return inventory
