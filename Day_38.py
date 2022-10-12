# From 50 days of Python Challenge book
import random


def guess_a_number():
    max_guesses = 3
    stored_number = random.randrange(1, 100)
    while max_guesses > 0:
        guess = int(input("Guess an integer between 1 and 100: "))
        if guess < stored_number:
            print("You guessed too low, try again")
            max_guesses -= 1
        elif guess > stored_number:
            print("You guessed too high, try again")
            max_guesses -= 1
        else:
            print("You guessed correctly, congrats")
            break
    print(f"Sorry, you ran out of guesses. The correct answer was {stored_number}")


def missing_numbers(numbers):
    missing = []
    full_range = list(range(min(numbers), max(numbers) + 1))
    for number in full_range:
        if number not in numbers:
            missing.append(number)
    return missing


# guess_a_number()
# print(missing_numbers([1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]))
