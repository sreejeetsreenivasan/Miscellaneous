# From 50 days of Python Challenge book


def odd_even(numbers):
    smallest_odd = 0
    largest_even = 0
    for number in numbers:
        if number % 2 == 0:
            if number > largest_even:
                largest_even = number
        elif number % 2 != 0:
            if smallest_odd == 0:
                smallest_odd = number
            elif number < smallest_odd:
                smallest_odd = number
    return largest_even - smallest_odd


def prime_numbers(number):
    """
    :param number: Arbitrary input from user
    :return: List of Prime Numbers in range of parameter
    """
    primes = []
    for i in range(number):
        factors = 0
        for j in range(1, i):
            if i % j == 0:
                factors += 1
        if factors == 1:
            primes.append(i)
    return primes


# print(odd_even([1, 2, 4, 6]))
# print(prime_numbers(10))
