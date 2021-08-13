from art import logo, vs 
from game_data import data
import random
from replit import clear

def pull():
    return random.randint(0,len(data)-1)


def compare(A, B, choice):
    follower1 = data[A]['follower_count']
    follower2 = data[B]['follower_count']
    
    if follower1 >= follower2:
        maximum = A
        winner = "A"
    elif follower1 < follower2: 
        maximum = B
        winner = "B"
    print(data[A]['name'], follower1)
    print(data[B]['name'], follower2)

    if choice == winner:
        print("Correct")
        print(A)
        print(type(A))
        return maximum    
    else:
        print("You lost")
        return -1 

def user():
    print(logo)
    A = pull()
    flag = True
    score = 0
    while flag:
   
        print(f"Compare A: {data[A]['name']}, a {data[A]['description']}, from {data[A]['country']}.")

        print(vs)

        B = pull()

        print(f"Against B: {data[B]['name']}, a {data[B]['description']}, from {data[B]['country']}.")

        choice = input("Who has more followers? Type 'A' or 'B': ")

        result = compare(A, B, choice)

        if result < 0:
            print(f"Sorry, that's wrong. Final score: {score}") 
            return 
        elif result >= 0:
            score += 1
            clear()
            print(logo)
            print(f"You're right! Current score: {score}")
            A = result

        

user()