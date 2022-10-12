# From 50 days of Python Challenge book
import string


def analyze_string(input_string):
    words = input_string.split()
    final_dict = {}
    letters = [letter for word in input_string.split() for letter in word]
    num_of_words = 0
    num_of_special = 0
    for element in letters:
        if element in string.punctuation:
            num_of_special += 1
    for word in words:
        i = 0
        for character in word:
            if character not in string.punctuation:
                i += 1
        if i == len(word):
            num_of_words += 1
    final_dict.update({'special characters': str(num_of_special), 'words': str(num_of_words),
                       'total characters': str(len(letters))})
    return final_dict


# print(analyze_string('This is a sen%tence with a few!)!) special characters'))
