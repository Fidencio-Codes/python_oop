from blackjack_pkg.classes import Cards, Hand, Deck, Chips
from blackjack_pkg.art import logo, sore_loser, winner, sad, draw
import os

playing = True
###FUNCTIONS### 
def cls(): #clears the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear') 
    #nt for windows, running system call 'cls' else 'clear' for linux os. this way is more cross-platform

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("\nHow many chips would you like to bet? "))
        except ValueError: print("Sorry! Please type in a number!: ")
        else:
            if chips.bet > chips.total: print("Your bet can't exceed 100!")
            else:
                break
#while loop has try and except
    # try will continue to ask chips.bet and continue except for cases that outcome a ValueError, for which it will print out to type a number 
    # used in place of the if 

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_ace()

def hit_or_stand(deck, hand): #ask if player wants to hit or stance
    global playing
    while True:
        ask = input("\nWould you like to Hit or Stand? Enter: 'h' or 's'\n")
        if ask[0].lower() == 'h': 
            hit(deck, hand)
        elif ask[0].lower() == 's': 
            print("Player stands, Dealer is playing.")
            playing = False
        else:
            print("Sorry, please try again")
            continue
        break

def first_show(player, dealer):
    print("\nDealer's Hand: ")
    print("<=Card Hidden=>")
    print(dealer.cards[1])
    print("\nPlayer's Hand: ", *(player.cards), sep='\n')
# asterisk * used above is the 'splat' operator: It takes an iterable like a list as input
        # and expands it into actual positional arguments in the function call."
def show_all(player, dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep="\n")
    print("Dealer's Hand = ", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep='\n')
    print("player's Hand =\n", player.value)

# Game Ending #
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
    print("They lost their life savings today ", sad)
    chips.lose_bet()
def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    print("Hahaha you lost \n", sore_loser)
    chips.win_bet()
def push(player, dealer):
    print("It's a push! Player and Dealer draw!\n")
    print(draw)

#### GAMEPLAY ####
while True:
    cls()
    # create shuffled deck
    deck = Deck() #Card class is called within Deck
    deck.shuffle()
    
    print(logo)
    print(f"(Note: You have 100 chips at the beginning)")
    # add 2 cards to each players hand
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # setup chips and player takes bet
    player_chips = Chips()
    take_bet(player_chips)
     # Cards on the table
    first_show(player_hand, dealer_hand)
    # Hit or stand interactions
    while playing:
        hit_or_stand(deck, player_hand)
        first_show(player_hand, dealer_hand)
        #Check if you lose, player_busts
        if player_hand.value >21: 
            player_busts(player_hand, dealer_hand, player_chips)
            break 
    #checks if player has blackjack or is less than 21 
    if player_hand.value <=21: 
        #dealer will add another card if they have less than 17
        while dealer_hand.value <=17:
            print("Dealer is drawing card\n\n")
            hit(deck, dealer_hand)
            # show all cards again
        show_all(player_hand, dealer_hand)
    #after dealer drawing cards, if dealer is > 21 then dealer loses game 
        if dealer_hand.value >21: dealer_busts(player_hand, dealer_hand, player_chips)
    #if no one has blackjack and no one is above 21, check if dealer is > player 
        elif dealer_hand.value > player_hand.value: dealer_wins(player_hand, dealer_hand, player_chips)
    # is player > dealer? then player wins!
        elif player_hand.value > dealer_hand.value: player_wins(player_hand, dealer_hand, player_chips)
    # if player is over 21 they bust
        elif dealer_hand.value == player_hand.value: push(player_hand, dealer_hand)
    #Prints player winnings
    print("\nPlayer's winnings stand at", player_chips.total)
    if player_chips.total <= 0:
        print("GAME OVER! You can ran out of chips!")
        playing = False
    else: continue
    #ask if player wants to play again 
    new_game = input("\nWould you like to play again? Enter 'y' or 'n': ")
    if new_game[0].lower() == 'y':
        playing = True 
        continue
    else: 
        print("Thanks for playing!")
        break

