# From 50 days of Python Challenge book


def check_pangram(input_string):
    letters = [letter for word in input_string.split() for letter in word]
    used_letters = []
    for letter in letters:
        if letter not in used_letters:
            used_letters.append(letter)
    if len(used_letters) == 26:
        return True
    return False


def find_index(list_of_int, given_int):
    indices = [index for index, integer in enumerate(list_of_int) if integer == given_int]
    if len(indices) == 0:
        return [given_int] * len(list_of_int)
    return indices


# print(check_pangram('the quick brown fox jumps over a lazy dog'))
# print(find_index([1, 2, 4, 6, 7, 7], 7))
