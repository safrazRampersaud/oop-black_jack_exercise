from abc import ABC, abstractmethod
from deck import *
import numpy as np
from dataclasses import dataclass, field
from typing import List


@dataclass
class Actor(ABC):
    id: int
    hand: List[Card] = field(default_factory=list)
    active: bool = field(default=False)
    score: float = field(default=0.00)

    def __post_init__(self):
        ...

    @property
    @abstractmethod
    def stand(self):
        ...

    @property
    @abstractmethod
    def hit(self):
        ...


@dataclass
class Player(Actor):
    def __post_init__(self):
        super().__post_init__()

    @property
    def stand(self):
        return True if np.random.rand() > .50 else False

    @property
    def hit(self):
        return False if self.stand else True


@dataclass
class Dealer(Actor):
    def __post_init__(self):
        super().__post_init__()
        self.id = 0

    @property
    def stand(self):
        return True if np.random.rand() > .50 else False

    @property
    def hit(self):
        return False if self.stand else True

