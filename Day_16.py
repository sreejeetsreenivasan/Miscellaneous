# From 50 days of Python Challenge book
from Day_14 import flat_list


def sum_list(numbers):
    return sum(list(flat_list(numbers)))


def unpack_nest(nested_list):
    new_list = flat_list(nested_list)
    return_list = []
    for number in new_list:
        if number == 34 or number == 67 or number == 78:
            if number not in return_list:
                return_list.append(number)
    return return_list


# print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))
# print(unpack_nest([[12, 34, 56, 67], [34, 68, 78]]))
