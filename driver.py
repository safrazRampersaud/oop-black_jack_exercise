from actors import *
from game import *

if __name__ == "__main__":

    d = Dealer(0)

    p1 = Player(1)
    p2 = Player(2)
    p3 = Player(3)
    p4 = Player(4)

    game = Game(dealer=d, players=[p1, p2, p3, p4])
    game.init_deal()
    game.play()
