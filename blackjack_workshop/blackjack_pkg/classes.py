###CLASSES###
import random 

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10, "Ace":11}

class Cards: #creates all the cards
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank 

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck: # creates a deck of cards
    def __init__(self):
        self.deck = []
        for suit in suits: #try using and here
            for rank in ranks:
                self.deck.append(Cards(suit, rank)) #want to add all these instances in string list 
    
    def __str__(self):
        self.deck_objs = "" #all possible instances for each suit of ranks
        for card in self.deck: 
            self.deck_objs += "\n" + card.__str__()
        return "The deck has: " + self.deck_objs

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self): #removes card from deck and returns it 
        one_card = self.deck.pop()
        return one_card

class Hand: #handle interactions btwn cards that dealer/player has
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0 #keep track of aces 
        
    def add_card(self, card): #add card to player/dealer hand
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips: #keep track of chip totals when player wins/loses
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet