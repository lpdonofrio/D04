#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random

# Body
def guess_game():
    x = random.randint(1, 25)

    guess_count = 0

    print("Welcome! You have five attempts!")

    while guess_count < 5:
        try:
            guess = int(input("Guess a number between 1 and 25: "))

        except:
            print("Please enter a number")

        else:
            if guess < 1 or guess > 25:
                print("The number must be higher than 0 and smaller than 26, please re-enter")
            else:
                if guess == x:
                    print("Great job! You guessed correctly!")
                    break
                elif guess < x:
                    print("Sorry, too low")
                else:
                    print("Sorry, too high")
        finally:
            guess_count += 1

    if guess_count == 5:
        print("You have attempted five times. Game over!")


################################################################################
def main():


    guess_game()
    

if __name__ == '__main__':
    main()