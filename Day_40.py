# From 50 days of Python Challenge book


def translate(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = string.split()
    for index, word in enumerate(words):
        if word[0].lower() in vowels:
            words[index] = word + 'yay'
        else:
            words[index] = word[1:] + word[0] + 'ay'
    return ' '.join(words)


# print(translate('i love python'))
