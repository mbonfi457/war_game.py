# need a dictionary of values to compary ranks of strings
# place at top of script; global variables
import random
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')


class Card:

    def __init__(self, suit, rank):
        # value not necessary argument
        # value will be based on dictionary of values
        self.suit = suit
        self.rank = rank
        self.value = values[rank]  # self.value pulls value from key 'rank'

    def __str__(self):  # provides easy to read description of card
        return self.rank + " of " + self.suit


# create DECK class
class Deck:

    def __init__(self):  # no need for user input, all decks the same content
        # create 52 card deck
        self.all_cards = []  # start as an empty list

        for suit in suits:
            for rank in ranks:
                # create card object
                created_card = Card(suit, rank)  # using created Card class

                self.all_cards.append(created_card)

    def shuffle(self):

        random.shuffle(self.all_cards)
        # random.shuffle does not return anything

    # create method that removes and deals a card
    def deal_one(self):
        return self.all_cards.pop()  # removes and returns a card off the end of list


# create PLAYER class
# holds current list of player's cards
# should be able to add or remove single or multiple cards from the list
# remove from the top, add to the bottom (left and right in a list)
# using .append() will RUIN the 'new' list when add cards back to deck

class Player:

    def __init__(self, name):

        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)  # removes card from 'top'

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # list of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            # single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

# GAME SETUP
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26): #standard 52-card deck
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# while game_on loop
game_on = True

round_num = 0

while game_on:

    round_num += 1
    print(f"Round {round_num}")  # counts no. of rounds during game

    if len(player_one.all_cards) == 0:  # check for player out of cards
        print("Player One out of cards. Player Two wins!")
        game_on = False
        break  # not needed but good practice

    if len(player_two.all_cards) == 0:  # check for player out of cards
        print("Player Two out of cards. Player One wins!")
        game_on = False
        break  # not needed but good practice

    # Start new round
    player_one_cards = []  # cards that player leaves on table, cards in play
    player_one_cards.append(player_one.remove_one())  # pops top card and adds to card list above

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    # while at_war
    at_war = True
    while at_war:  # players are now at war

        # at_war = False if cards values are not equal
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False


        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:  # at_war = True by default
            print('WAR!')

            if len(player_one.all_cards) < 5:
                print("PLayer One unable to go to war")
                print("Player Two Wins!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("PLayer Two unable to go to war")
                print("Player One Wins!")
                game_on = False
                break

            else:
                for num in range(5):  # game adds 5 more cards to table during war
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())