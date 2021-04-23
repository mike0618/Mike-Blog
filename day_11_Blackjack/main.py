from art import logo
from random import choice
from time import sleep
# from replit import clear  # works in replit only


def get_card():
    return choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])

def count(hand):
    score = sum(hand)
    aces = hand.count(11)
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score

def play(start_hand):
    dealer = True
    if len(start_hand) == 2:
        dealer = False
    hand = start_hand
    while True:
        score = count(hand)
        if dealer and score < 17:
            hand.append(get_card())
            print(f"Dealer's hand: {hand}, score: {count(hand)}")
            sleep(1)
        elif not dealer and score < 21 and input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            hand.append(get_card())
            print(f"Your hand: {hand}, score: {count(hand)}")
        else:
            return score

while input("Do you want to play Blackjack? Type 'y' or 'n': ") == 'y':
    dealer_hand = [get_card()]
    user_hand = [get_card(), get_card()]
#     clear()
    print(logo)
    print(f"Your cards {user_hand}, current score: {sum(user_hand)}")
    print(f"Dealer's first card: {dealer_hand[0]}")
    user_score = play(user_hand)
    if user_score > 21:
        print("You went over. You lose.")
    elif user_score == 21:
        print("You win!")
    else:
        dealer_score = play(dealer_hand)
        if user_score < dealer_score and dealer_score < 22:
            print("You lose.")
        elif user_score == dealer_score:
            print("Draw.")
        else:
            print("You win!")
