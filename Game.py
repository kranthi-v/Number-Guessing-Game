import random

print("Hi! Welcome to the Number Guessing Game.")
print("Select Difficulty Level:")
print("1. Easy (1 - 50, 10 chances)")
print("2. Medium (1 - 100, 7 chances)")
print("3. Hard (1 - 200, 5 chances)")

Choice = int(input("Enter your Choice (1/2/3): "))

if Choice == 1:
    low, high = 1, 50
    chances = 10
elif Choice == 2:
    low, high = 1, 100
    chances = 7
elif Choice == 3:
    low, high = 1, 200
    chances = 5
else:
    print("Invalid Choice!")
    exit()

print(f"Great! I'm thinking of a number between {low} and {high}, you have {chances} chances to guess it.")

number =  random.randint(low, high)

while chances > 0:
    guess = int(input("Make a guess: "))
    chances -= 1

    if guess == number:
        print(f"🎉 Congratulations! You've guessed the number {number} correctly!")
        break

    elif guess > number:
        print("Too high! Try lower number.")

    else:
        print("Too low! Try higher number.")

if chances == 0 and guess != number:
    print(f"🥲 Sorry, you've used all your chances. The number was {number}. Better luck next time!")