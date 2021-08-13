import random 
from replit import clear
from art import logo

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
    return random.choice(cards)

def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    
    if sum(cards)>21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif user_score == 0:
        return "Blackjack win"
    elif computer_score == 0:
        return "You lost. Dealer win with blackjack"
    elif user_score>21:
        return "Lost"
    elif computer_score > 21:
        return "Win"
    elif computer_score<user_score:
        return "Win"
    else:
        return "Lose"

def play():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score={user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score==0 or user_score>21:
            is_game_over = True 
        else:
            user_deal = input("Do you want another card?")
            if user_deal.lower() == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your cards are: {user_cards} and your score is {user_score}")
    print(f"Computer's cards are: {computer_cards} and computer's score is {computer_score}") 
    print(compare(user_score, computer_score))

    while input("Do you want to play again?") == "y":
        clear()
        play()
play()