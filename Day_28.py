# From 50 days of Python Challenge book


def index_position(string):
    lowercase_letters = []
    for index, letter in enumerate(string):
        if letter.islower() is True:
            lowercase_letters.append(index)
    return lowercase_letters


def largest_number(integers):
    individual_numbers = [digit for value in integers for digit in str(value)]
    int_list = [int(number) for number in individual_numbers]
    largest = ''
    while len(int_list) != 0:
        maximum = max(int_list)
        largest += str(maximum)
        int_list.remove(maximum)
    return '{:,}'.format(int(largest))


# print(index_position('LovE'))
# print(largest_number([3, 67, 87, 9, 2]))
