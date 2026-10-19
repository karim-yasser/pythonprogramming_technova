
import random

print("=== Number Guessing Game ===")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if guess < secret_number:
        print("Higher! Try again.")
    elif guess > secret_number:
        print("Lower! Try again.")
    else:
        print("Correct! You guessed the number.")
        print("Number of attempts:", attempts)
        break
