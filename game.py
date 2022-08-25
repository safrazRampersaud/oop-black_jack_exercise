from actors import *


class Game:
    def __init__(self, dealer, players):
        self.__deck = Deck().deck
        self.__players = players
        self.__dealer = dealer
        self.__deal_sequence = []
        self.__winner = -1

    def play(self):
        max_score = -1
        for seq in self.__deal_sequence:
            self.__activate_actor(seq)
            active_player = self.__get_active_actor()

            if active_player.hit:
                active_player.hand.append(self.__deal_card())
            self.__calculate(active_player)
            if max_score < active_player.score:
                max_score = active_player.score
                self.__winner = active_player.id
        self.__get_winner()

    def __get_winner(self):
        if self.__winner == 0:
            print(f'''Winner=Dealer, Score={self.__dealer.score}''')
        else:
            w_player = [player for player in self.__players if player.id == self.__winner][0]
            print(f'''Winner=Player-{w_player.id}, Score={w_player.score}''')

    def __calculate(self, active_player):
        total_score = 0
        for card in active_player.hand:
            if card.value in ('J', 'Q', 'K'):
                total_score = total_score + 10
            elif card.value not in ('J', 'Q', 'K', 'A'):
                total_score = total_score + int(card.value)
            else:
                if total_score < 10:
                    total_score = total_score + 11
                else:
                    total_score = total_score + 1
        active_player.score = total_score

    def init_deal(self):
        player_ids = []
        for i in self.__players:
            player_ids.append(i.id)

        random.shuffle(player_ids)
        player_ids.append(0) # dealer
        self.__deal_sequence = player_ids

        for seq in self.__deal_sequence:
            self.__activate_actor(player_ids[seq])
            active_actor = self.__get_active_actor()
            active_actor.hand.append(self.__deal_card())

    def get_active_actor(self):
        if self.__dealer.active:
            return self.__dealer
        return [player for player in self.__players if player.active][0]

    def get_deal_sequence(self):
        return self.__deal_sequence

    def __deal_card(self):
        if self.__deck:
            return self.__deck.pop(0)

    def __get_active_actor(self):
        if self.__dealer.active:
            return self.__dealer
        return [player for player in self.__players if player.active][0]

    def __activate_actor(self, active_player_id):
        if active_player_id == 0:
            self.__dealer.active = True
            for player in self.__players:
                if active_player_id != player.id:
                    player.active = False
        else:
            for player in self.__players:
                if active_player_id == player.id:
                    player.active = True
                    break
            for player in self.__players:
                if active_player_id != player.id:
                    player.active = False
            self.__dealer.active = False
