# From 50 days of Python Challenge book


def count(string):
    letters = [letter for word in string.split() for letter in word]
    letter_count = {}
    for letter in letters:
        letter_count[letter] = letters.count(letter)
    return letter_count


# print(count('hello'))
