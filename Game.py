import random

print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")

low = int(input("Enter the lower bound of the range: "))
high = int(input("Enter the upper bound of the range: "))

print(f"Great! I'm thinking of a number between {low} and {high}, you have 7 chances to guess it.")

number =  random.randint(low, high)
chances = 7

while chances > 0:
    guess = int(input("Make a guess: "))
    chances -= 1

    if guess == number:
        print(f"Congratulations! You've guessed the number {number} correctly!")
        break

    elif chances == 0:
        print(f"Sorry, you've run out of chances. The number was {number}.\nBetter luck next time!")
        break

    elif guess > number:
        print("Too high, Try lower number.")

    elif guess < number:
        print("Too low, Try higher number.")