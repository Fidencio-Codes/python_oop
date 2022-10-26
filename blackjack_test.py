import random 
import os

logo = "WELCOME TO BlackJack!"
sore_loser = "\n(⋟﹏⋞) *ANGER* \n\n(╯°□°╯︵ ┻━┻ *flips table*"
winner = "\nWho's a winner? (☞ﾟ∀ﾟ)☞ You are! \n\nᕕ(⌐■_■)ᕗ ♪♬"
sad = "\n\o(╥﹏╥)o waaaaah! there goes my son's college funds \n ·´¯`(>▂<)´¯`·. "
draw = "\n ಠ_ಠ a draw??\nggs "
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10, "Ace":11}

class Card: 
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank 
    def __str__(self):
        return self.rank + ' of ' + self.suit
class Deck: 
    def __init__(self):
        self.deck = []
        for suit in suits: 
            for rank in ranks:
                self.deck.append(Card(suit, rank)) 
    def __str__(self):
        self.deck_objs = "" 
        for card in self.deck: 
            self.deck_objs += "\n" + card.__str__()
        return "The deck has: " + self.deck_objs
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        one_card = self.deck.pop()
        return one_card
class Hand: 
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self, card): 
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Aces": self.aces += 1
    def adjust_ace(self):
        while self.value > 21 and self.aces >=1:
            self.value -= 10
            self.aces -= 1
class Chips: 
    def __init__(self):
        self.total = 100
        self.bet = 0
    def show_total(self):
        print(self.total)
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet
def cls(): 
    os.system('cls' if os.name == 'nt' else 'clear') 
    
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("\nHow many chips would you like to bet? "))
        except ValueError: print("Sorry! Please type in a number!: ")
        else:
            if chips.bet > chips.total: print("Your bet can't exceed 100!")
            else:
                break
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_ace()
def hit_or_stand(deck, hand): #ask if player wants to hit or stance
    end_of_hs = True
    while end_of_hs is not False: 
        ask = input("\nWould you like to Hit or Stand? Enter: 'h' or 's'. ")
        if ask[0].lower() == 'h': 
            hit(deck, hand)
        elif ask[0].lower() == 's': 
            print("\nPlayer stands, Dealer is playing.")
            break # playing = False
        else:
            print("Sorry, please try again")
            continue
        break

def first_show(player, dealer):
    print("\nDealer's Hand: ")
    print("<=Card Hidden=>")
    print(dealer.cards[1])
    print("\nPlayer's Hand: ", *(player.cards), sep='\n')
def show_all(player, dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep="\n")
    print("Dealer's Hand = ", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep='\n')
    print("player's Hand =\n", player.value)
def player_busts(player, dealer, chips):
    print("PLAYER BUSTS!")
    print(sore_loser)
    chips.lose_bet()
def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    print(winner)
    chips.win_bet()
def dealer_busts(player, dealer, chips):
    print("DEALER BUSTS!")
    print("The lost their life savings today ", sad)
    chips.lose_bet()
def dealer_wins(player, dealer, chips):
    print("DEALER WINS!\n")
    print("Hahaha you lost :P \n", sore_loser)
    chips.win_bet()
def push(player, dealer):
    print("It's a push! Player and Dealer draw!\n")
    print(draw)

playing = True
while True:
    cls()
    deck = Deck() 
    deck.shuffle()
    print(logo)
    print(f"(Note: You have 100 chips at the beginning)")
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    player_chips = Chips()
    first_show(player_hand, dealer_hand)
    take_bet(player_chips)

    while playing:
        hit_or_stand(deck, player_hand)
        show_all(player_hand, dealer_hand)
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
    if player_hand.value <=21: 
        while dealer_hand.value <=17:
            print("Dealer is drawing card\n\n")
            hit(deck, dealer_hand)
        show_all(player_hand, dealer_hand)
        if dealer_hand.value >21: 
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value: 
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif player_hand.value > dealer_hand.value: 
            player_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value == player_hand.value: 
            push(player_hand, dealer_hand)
    print("\nPlayer's winnings stand at", player_chips.total)
    if player_chips.total <= 0:
        print("GAME OVER! You can ran out of chips!")
        playing = False
    else: continue
    new_game = input("\nWould you like to play again? Enter 'y' or 'n': ")
    if new_game[0].lower() == 'y':
        playing = True 
        continue
    else: 
        print("Thanks for playing!")
        break
    