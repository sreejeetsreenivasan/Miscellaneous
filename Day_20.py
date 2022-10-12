# From 50 days of Python Challenge book


def capitalize(string):
    words = string.split()
    wrd_list = []
    for word in words:
        wrd_list.append(word[0].upper() + word[1:])
    return ' '.join(wrd_list)


def reversed_list(sentence):
    words = sentence.split()
    upper_words = []
    for word in words:
        for i in range(len(word)):
            if word[i].isupper() is True:
                upper_words.append(word[::-1])
    return upper_words


# print(capitalize("i love learning"))
# print(reversed_list('leArning is hard, bUt if You appLy youRself you can achieVe success'))
