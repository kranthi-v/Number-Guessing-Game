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

    elif guess > number:
        print("Too high! Try lower number.")

    else:
        print("Too low! Try higher number.")

if chances == 0 and guess != number:
    print(f"Sorry, you've used all your chances. The number was {number}. Better luck next time!")