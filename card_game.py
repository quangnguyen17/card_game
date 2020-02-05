# Deck of cards
# 52 cards in a deck
# suits hearts, spades, diamonds, clubs

# [X] build card
# [X] build deck
# [X] implement shuffle
# [ ] implement a sort
# [ ] implement a game

import random


class Card():
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit

        names = {
            1: "Ace",
            11: "Jack",
            12: "Queen",
            13: "King"
        }

        self.name = names.get(value) or str(value)

    def show_value(self):
        print(f"{self.name} of {self.suit}")


class Deck():
    def __init__(self):
        self.cards = []

        # populate / the cards list
        for suit in ["H", "C", "D", "S"]:
            # build each suit
            # print('suit:"', suit)
            for value in range(1, 14):
                # print('value:"', value)
                # create a card
                self.cards.append(Card(suit, value))


    # Perfect shuffles the deck
    def shuffle(self):
        for time in range(random.randint(5, 10)):
            mid = self.deck_length() / 2
            first_half = self.cards[0: int(mid)]
            second_half = self.cards[int(mid): self.deck_length()]
            shuffled_deck = []

            for index in range(len(first_half)):
                shuffled_deck.append(first_half[index])
                shuffled_deck.append(second_half[index])

            self.cards = shuffled_deck

        return self

    # Randomizes the deck
    def random_shuffle(self):
        for time in range(random.randint(self.deck_length(), self.deck_length() * 5)):
            index_one = random.randint(0, self.deck_length(-1))

            while True:
                index_two = random.randint(0, self.deck_length(-1))
                if index_one != index_two:
                    break

            self.cards[index_one], self.cards[index_two] = self.cards[index_two], self.cards[index_one]

        return self

    # helper for random_shuffle
    def deck_length(self, addition=0):
        return len(self.cards) + addition

    # Sorts Deck to Suites then Numbers
    def sort(self):
        hearts = []
        clubs = []
        diamonds = []
        spades = []

        # split deck to 4 suit lists
        for card in self.cards:
            if len(self.cards) == 0:
                return self
            elif card.suit == "H":
                hearts.append(card)
            elif card.suit == "C":
                clubs.append(card)
            elif card.suit == "D":
                diamonds.append(card)
            elif card.suit == "S":
                spades.append(card)

        # sort each suit by num
        hearts = self.sort_suit(hearts)
        clubs = self.sort_suit(clubs)
        diamonds = self.sort_suit(diamonds)
        spades = self.sort_suit(spades)

        # stuff 4 suit lists into deck.cards
        self.cards = []
        for card in hearts:
            self.cards.append(card)
        for card in clubs:
            self.cards.append(card)
        for card in diamonds:
            self.cards.append(card)
        for card in spades:
            self.cards.append(card)

        return self

    # helper - given list of cards, sort and return list of cards
    def sort_suit(self, suit):
        answer = []
        while(len(suit) > 0):
            min_idx = 0
            for idx in range(len(suit)):
                if suit[idx].value < suit[min_idx].value:
                    min_idx = idx
            answer.append(suit[min_idx])
            suit.pop(min_idx)
        return answer

    def show_deck(self):
        print("*" * 50)
        for card in self.cards:
            card.show_value()
        return self

class Player:
    def __init__(self, name="", hand=[]):
        self.name = name
        self.hand = hand
        self.wins = 0
        self.losses = 0
    
    def get_name(self):
        return self.name
    def get_hand(self):
        return self.hand
    def get_wins(self):
        return self.wins
    def get_losses(self):
        return self.losses
    
    def add_card(self, new_card):
        self.hand.append(new_card)
        return self
    def add_win(self):
        self.wins += 1
        return self
    def add_loss(self):
        self.losses += 1
        return self
    
    
def start_game():
    print("Start Game")
    # get name input & init in line below
    main_player = Player()

    # get input & run game given # times
    runs = 1
    for i in range(runs):
        run_game(main_player, int)
    
    # game ending msg
    print(main_player.get_wins())
    print(main_player.get_losses())
    print("End of Game")


def run_game(player, int):
    # Shuffle Deck
    game_deck = Deck()
    game_deck.random_shuffle()
    # Deal 2 Cards to hand
    deal(game_deck, player)
    deal(game_deck, player)
    while calc_score(player.hand) < 21:
        deal(game_deck, player)
    if calc_score(player.hand) == 21:
        player.wins += 1
    else: 
        player.losses += 1

# helper to move last card of deck into player hand
def deal(deck, player):
    player.add_card(deck.cards[-1])
    deck.cards.pop()
    return None

# helper to calculate score
def calc_score(hand):
    score = 0
    for card in hand:
        score += card.value
    return score



if __name__ == "__main__":
    start_game()