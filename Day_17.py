# From 50 days of Python Challenge book
import random


def user_name():
    name = str(input("Enter your name: "))
    username = ''
    for i in range(len(name)):
        username += name[len(name) - i-1]
    number = random.randint(0, 9)
    username += str(number)
    return username


def sort_length(strings):
    # Simple Sort
    for element in strings:
        for i in range(strings.index(element), len(strings) - 1):
            if len(strings[i+1]) < len(element):
                strings[strings.index(element)], strings[i+1] = strings[i+1], strings[strings.index(element)]
    return strings


# print(user_name())
# print(sort_length(['Peter', 'Jon', 'Andrew']))
