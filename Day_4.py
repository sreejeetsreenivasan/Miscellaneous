# From 50 days of Python Challenge book


def only_floats(a, b):
    if type(a) is float and type(b) is float:
        return 2
    elif type(a) is float or type(b) is float:
        return 1
    else:
        return 0


def word_index(strings):
    longest_word = ''
    i = 0
    for word in strings:
        if len(word) > len(longest_word):
            longest_word = word
        elif len(word) == len(longest_word):
            i += 0
    if i == len(strings):
        return 0
    else:
        return strings.index(longest_word)


# print(only_floats(12.1, 23))
# print(word_index(["Hate", "remorse", "vengeance"]))
# print(word_index(["Love", "Hate"]))
