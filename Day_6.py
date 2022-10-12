# From 50 days of Python Challenge book


def user_name():
    email = str(input("Enter your email: "))
    position = email.find('@')
    return email[:position]


def zeroed(numbers):
    numbers[0] = 0
    numbers[-1] = 0
    return numbers


# print(user_name())
# print(zeroed([2, 5, 7, 8, 9]))
