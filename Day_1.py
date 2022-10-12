import math
# From 50 days of Python Challenge book


def divide_or_square(number):
    if number % 5 == 0:
        return math.sqrt(number)
    else:
        return number % 5


def longest_value(dictionary):
    values = []
    for key in dictionary:
        if len(values) == 0:
            values.append(dictionary.get(key))
        else:
            if len(dictionary.get(key)) > len(values[0]):
                values[0] = dictionary.get(key)
    return values[0]


# print(divide_or_square(10))
# print(longest_value({'fruit': 'apple', 'color': 'green'}))
