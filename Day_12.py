# From 50 days of Python Challenge book


def count_dots(string):
    dots = 0
    for character in string:
        if character == '.':
            dots += 1
    return dots


def age_in_minutes():
    while True:
        year_of_birth = int(input("Enter your year of birth: "))
        if len(str(year_of_birth)) != 4:
            print("Please enter a 4-digit year of birth: ")
            continue
        elif year_of_birth < 1900 or year_of_birth > 2022:
            print("Invalid input, please enter a valid year: ")
            continue
        else:
            break
    format_string = '{:,}'
    return f'You are {format_string.format((2022 - year_of_birth) * 365 * 24 * 60)} minutes old'


# print(count_dots('h.e.l.p.'))
# print(age_in_minutes())
