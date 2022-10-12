# From 50 days of Python Challenge book


def make_tuples(list_1, list_2):
    if len(list_1) == len(list_2):
        new_list = []
        for i in range(len(list_1)):
            new_list.append((list_1[i], list_2[i]))
    else:
        return 'The lists are not of the same length'
    return new_list


def even_or_average():
    numbers = [float(x) for x in input("Enter five numbers: ").split()]
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    if len(even_numbers) != 0:
        return max(even_numbers)
    else:
        return sum(numbers) / len(numbers)


# print(make_tuples([1, 2, 3, 4], [5, 6, 7, 8]))
# print(even_or_average())
