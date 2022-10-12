# From 50 days of Python Challenge book


def count_words(string):
    words = string.split()
    return len(words)


def count_elements(string):
    elements = 0
    for element in string.replace(" ", ''):
        elements += 1
    return elements


# print(count_words("I love learning"))
# print(count_elements("I love learning"))
