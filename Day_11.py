# From 50 days of Python Challenge book


def equal_strings(str_1, str_2):
    if len(str_1) == len(str_2):
        for letter in str_1:
            if letter not in str_2:
                return False
        return True
    return False


def swap_values(numbers):
    copy_list = numbers.copy()
    numbers[0] = numbers[-1]
    numbers[-1] = copy_list[0]
    return copy_list


# print(equal_strings('love', 'evol'))
# print(swap_values([2, 4, 67, 7]))
