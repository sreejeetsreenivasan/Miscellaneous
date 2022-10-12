# From 50 days of Python Challenge book


def sort_words(string):
    stripped_string = string.replace(" ", "")
    letters = []
    for letter in stripped_string:
        if letter not in letters:
            letters.append(letter)
    return sorted(letters)


def string_length(string):
    word_lengths = {}
    words = string.split()
    for word in words:
        if word not in word_lengths:
            word_lengths[word] = len(word)
    return word_lengths


# print(sort_words('love life'))
# print(string_length('Hi my name is Richard'))
