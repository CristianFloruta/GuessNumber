from random import randint
from art import logo
from func import play_game


print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100!")

comp_guess = randint(1, 100)
game_on = True

while game_on:
    difficulty = input("Choose a difficulty 'hard' or 'easy': ").lower()

    if difficulty == "hard":
        play_game(5, comp_guess)
        again = input("Would you like to play again? Type 'yes' or 'no': ").lower()
        if again == "yes":
            for i in range(100):
                print()
            print(logo)
            print("Welcome to the number guessing game!")
            print("I'm thinking of a number between 1 and 100!")
            continue
        else:
            game_on = False

    elif difficulty == "easy":
        play_game(10, comp_guess)
        again = input("Would you like to play again? Type 'yes' or 'no': ").lower()
        if again == "yes":
            for i in range(100):
                print()
            print(logo)
            print("Welcome to the number guessing game!")
            print("I'm thinking of a number between 1 and 100!")
            continue
        else:
            game_on = False

    else:
        print("I do not understand your input! Try again select 'hard' or 'easy'!")





