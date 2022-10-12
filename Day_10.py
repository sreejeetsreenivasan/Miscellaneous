# From 50 days of Python Challenge book

def hide_password():
    password = str(input("Enter a password: "))
    hidden_password = "*" * len(password)
    return f'Hidden Password: {hidden_password} \nThe password is {len(password)} characters long'


def convert_numbers(numbers):
    new_list = []
    format_string = '{:,}'
    for number in numbers:
        str_number = format_string.format(number)
        new_list.append(str_number)
    return new_list


# print(hide_password())
# print(convert_numbers([1000000, 2356989, 2354672, 9878098]))
