# From 50 days of Python Challenge book


def unique_numbers(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    numbers_minus_unique = sum(numbers) - sum(unique)
    if numbers_minus_unique % 2 == 0:
        return numbers
    elif numbers_minus_unique % 2 != 0:
        return unique


def difference(list_1, list_2):
    unique_list_1 = [number for number in list_1 if number not in list_2]
    unique_list_2 = [number for number in list_2 if number not in list_1]
    return unique_list_1 + unique_list_2


# print(unique_numbers([1, 2, 4, 5, 6, 7, 8, 8]))
# print(difference([1, 2, 4, 5, 6], [1, 2, 5, 7, 9]))
