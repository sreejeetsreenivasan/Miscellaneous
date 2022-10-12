# From 50 days of Python Challenge book
import random
import string


def generate_password():
    strength = str(input("Enter how strong you want your password to be: weak, strong, or very strong: ")).lower()
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    if strength == "weak":
        for i in range(5):
            password += random.choice(characters)
    elif strength == "strong":
        for i in range(8):
            password += random.choice(characters)
    elif strength == "very strong":
        for i in range(12):
            password += random.choice(characters)
    return password


# print(generate_password())
