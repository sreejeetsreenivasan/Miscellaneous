# From 50 days of Python Challenge book


def any_number(*numbers):
    list_of_numbers = []
    for number in numbers:
        list_of_numbers.append(number)
    return sum(list_of_numbers) / len(list_of_numbers)


def add_reverse(list_1, list_2):
    sum_list = []
    if len(list_1) == len(list_2):
        i = 0
        while i < len(list_1):
            mid_sum = list_1[i] + list_2[i]
            sum_list.append(mid_sum)
            i += 1
    else:
        return 'The lists are not of equal length'
    sum_list.reverse()
    return sum_list


# print(any_number(12, 90))
# print(add_reverse([10, 12, 34],  [12, 56, 78]))
