import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# ace = cards[0]
dealer_hand = [11,10]
player_hand = [11,11]

print("Welcome to BlackJack")
def deal_card():
    return random.choice(cards)
dealer_hand.append(deal_card())
dealer_hand.append(deal_card())
player_hand.append(deal_card())
player_hand.append(deal_card())
print(dealer_hand)
print(player_hand)

end_of_game = False
def calculate_score(x):
    score = 0
    for i in x:
        score += i
        if score == 21: return 0 
        if score > 21:
            x.remove(11)
            x.append(1)
            calculate_score(x)
        if score ==21 or score>21: end_of_game == True

    
dealer_score = calculate_score(dealer_hand)
player_score = calculate_score(player_hand)
print(calculate_score(dealer_hand))
print(calculate_score(player_hand))

another_card = input("Do you want another card? y or n")
if another_card == 'y':
    player_hand.append(deal_card())
    print(player_score, player_hand)
else: 
    print(player_score, player_hand)
if int(dealer_score) < 17: dealer_hand.append(deal_card())
calculate_score(player_hand)
calculate_score(dealer_hand)
if dealer_score >21: end_of_game == True

if player_score > dealer_score: print(f"Player is a winner! {player_score}")
if player_score < dealer_score: print(f"Dealer is a winner! {dealer_score}")
if player_score == dealer_score: print(f"Game is a draw! {player_score} vs {dealer_score}")
