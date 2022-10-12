# From 50 days of Python Challenge book


def biggest_odd(numbers):
    odd_list = [num for num in list(numbers) if int(num) % 2 != 0]
    return max(odd_list)


def zeros_last(numbers):
    num_of_zeros = 0
    for number in numbers:
        if number == 0:
            numbers.remove(number)
            num_of_zeros += 1
    if num_of_zeros > 0:
        numbers.extend([0] * num_of_zeros)
    else:
        return sorted(numbers)
    return numbers


# print(biggest_odd('23569'))
# print(zeros_last([1, 4, 6, 0, 7, 0, 9]))
# print(zeros_last([2, 1, 4, 7, 6]))
