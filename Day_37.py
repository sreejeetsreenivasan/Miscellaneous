# From 50 days of Python Challenge book


def count_the_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    letters = [letter for word in string.split() for letter in word]
    vowels_in_string = []
    for letter in letters:
        if letter.lower() in vowels:
            if letter not in vowels_in_string:
                vowels_in_string.append(letter)
    return len(vowels_in_string)


# print(count_the_vowels('hello'))
