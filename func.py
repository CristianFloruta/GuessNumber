def play_game(life, comp_guess):
    while life != 0:
        print(f"You have {life} attempts to guess the number!")
        usr_guess = int(input("Make a guess: "))
        if usr_guess > comp_guess:
            if life == 1:
                print("Too high!")
                print("You run out of guesses! You lost!")
            else:
                print("Too high!")
                print("Guess again!")
            life -= 1
        elif usr_guess < comp_guess:
            if life == 1:
                print("Too low!")
                print("You run out of guesses! You lost!")
            else:
                print("Too low!")
                print("Guess again!")
            life -= 1
        else:
            print(f"You got it! The number was {comp_guess}!")
            break



