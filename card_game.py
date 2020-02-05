# Deck of cards
# 52 cards in a deck
# suits hearts, spades, diamonds, clubs

# [X] build card
# [X] build deck
# [X] implement shuffle
# [X] implement a sort
# [X] implement a game

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
    print("Welcome to 21!")
    name = input("Enter your name: ")

    # get name input &- init in line below
    main_player = Player(name=name)

    # get input & run game given # times
    while True:
        runs = input("How many games you want to run: ")
        try:
            if int(runs) > 50 or int(runs) <= 0:
                print("Please a valid input, 1 to 50 :(")
            elif int(runs) <= 50:
                break
        except ValueError:
            print("Please a valid input, 1 to 50, ;(")

    for game in range(int(runs)):
        run_game(main_player, game)

    print(f"\nWins: {main_player.get_wins()} games.")
    print(f"Losses: {main_player.get_losses()} games.")
    print("Congrats!" if main_player.get_wins() > main_player.get_losses()
          else f"{main_player.name} is a LOOOOOOOOOOOOOOOOSSSSSSSSER!! XD :(() ) ;(")
    # print("Congrats!" if main_player.get_wins() > main_player.get_losses()
    #      else f"{main_player.name} is a THUMP ASS!! XD :(() ) ;(")

# Runs one instance of game
def run_game(player, num):
    # Reset and shuffle deck, reset the hand
    game_deck = Deck().random_shuffle()
    player.hand = []
    print(f"\nGame {num + 1}")
    print("shuffling deck...")
    # Deal 2 Cards to hand
    deal(game_deck, player)
    deal(game_deck, player)
    # Keep dealing until 21 or over
    while calc_score(player.hand) < 21:
        deal(game_deck, player)
    # Handle Scores
    player.add_win() if calc_score(
        player.hand, in_game=False) == 21 else player.add_loss()

# helper to move last card of deck into player hand
def deal(deck, player):
    player.add_card(deck.cards[-1])
    deck.cards.pop()

# helper to calculate score and print game status
def calc_score(hand, in_game=True):
    score = 0
    for card in hand:
        score += card.value
    # Prints hand and score information
    if in_game:
        if len(hand) >= 2:
            your_hand_str = "Your hand:"

            for card in hand:
                your_hand_str += f" | {card.name} of {card.suit}"

            print(your_hand_str)
            print(f"Your score: {score}")

    return score


if __name__ == "__main__":
    start_game()
